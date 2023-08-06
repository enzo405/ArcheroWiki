import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .function import send_webhook, login_required, send_embed, editor_login,db_maintenance, checkContributor, getCredentialForNonLoginRequired
from .models import UserQueue, Token, user
from django.contrib import messages
from .forms import UserQueueForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse


missing_data = []


## This API will work like that : 
# class UserQueue(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     is_validated = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
# - In order to create a UserQueue, the user need to send a get request (need to secure this views because it send data to a database)
# - Then the owner of the app receive a notification on discord with the url created in the previous step
# - The notification will be send with an existing function send_webhook(msg:Any)
# - When i click on the url, it will check wheter or not i'm logged in as a django superuser
# - if yes then it will add the user to the django User model if not i will be redirected to the admin panel login (which i changed to /luhcaran/ instead of /admin/)
# - after this, the user will need to send a GET request to another views that will redirect the user to the menu of the website at / and in the backend will send a notification with the request, username, password (hashed), token
# - Then once i've got the token, i will search in the admin pannel the user and add it the token in order to get POST access on the API

@db_maintenance
@editor_login
def data(request):
	user_credential = getCredentialForNonLoginRequired(request)['user_credential']
	if checkContributor(user_credential,request):
		status = request.session['status']
		url_query = "?q="
		filter_query = str(request.build_absolute_uri()).split(url_query)
		try:
			with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
				data = json.load(f)
		except (FileNotFoundError, json.JSONDecodeError) as e:
			messages.error(request, f"Error: {e}")
		query_list = filter_query[1].split('.') if len(filter_query) > 1 and filter_query[1] != "" else []
		if request.method == "GET":
			SidebarContent = data['SidebarContent']
			for query in query_list:
				try:
					data = data[query]
					url_query += f"{query}."
				except (KeyError, TypeError) as e:
					messages.error(request, f"Query Error :{e}")
			if not isinstance(data, (int, str, list)):
				keys = list(data.keys()) if len(data) != 1 else data
				result = False
			else:
				keys = data
				result = True
			previous = "/data/?q=" + ".".join(query_list[:-1]) if query_list else "/data/"
			return render(request, "api/api.html", {"keys":keys,"sidebarContent":SidebarContent,"header_msg":"Website Data","url_query":url_query,"result":result,"previous":previous,"status":status})
		elif request.method == "POST":
			if status == "authorized":
				response_data = request.session['response_data']
				old_value = data
				for query in query_list:
					old_value = old_value[query]
				if isinstance(old_value, (int, str, list)):
					avatar_url = f"https://cdn.discordapp.com/avatars/{response_data.get('id','0')}/{response_data.get('avatar','a')}"
					new_value = request.POST.get('new_value',None)
					str_query_list = " -> ".join([i for i in query_list])
					type_old_value = type(old_value)
					try:
						type_old_value(new_value)
					except TypeError as e:
						messages.error(request, f"The type of the old value must be the same for the new value {e}")
						return HttpResponseRedirect(request.build_absolute_uri())
					send_embed(f"{response_data.get('username','a')}","__API Update__",
						f"Change Author : <@{response_data.get('id','a')}> ({response_data.get('locale','a')})",
						f"{str_query_list}",f"```diff\n- {old_value}\n+ {new_value}```","A200FF",request,True,avatar_url=avatar_url)
					data_temp = data
					for key in query_list[:-1]:
						data_temp = data_temp[key]
					data_temp[query_list[-1]] = new_value
					with open('calculator/local_data.json', 'w', encoding="utf-8") as file:
						json.dump(data, file, indent=4)
			return HttpResponseRedirect(request.build_absolute_uri())
	else:
		request.session['error_message'] = f"You're not allowed to access this page"
		return HttpResponseRedirect('/')


class CalculatorAPI(APIView):

	def get(self, request):
		filter_query = request.query_params.get("q")
		try:
			with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
				data = json.load(f)
		except FileNotFoundError:
			return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)
		except json.JSONDecodeError:
			return Response({"error": "Invalid JSON."}, status=status.HTTP_400_BAD_REQUEST)
		query_list = filter_query.split('.') if filter_query else []
		for query in query_list:
			try:
				data = data[query]
			except (KeyError, TypeError):
				return Response({"error": "Invalid query parameter."}, status=status.HTTP_400_BAD_REQUEST)
		return Response(data)


@db_maintenance
@login_required
def create_user_queue(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	if request.method == "POST":
		form = UserQueueForm(request.POST)
		if form.is_valid():
			user_credential = request.session['user_credential']
			user_queue = form.save(commit=False)
			user_queue.save()
			url = request.build_absolute_uri(reverse('validate_user_queue', kwargs={'pk': user_queue.pk}))
			messages.success(request,f"An Admin have been warned and will take care of you demand")
			send_webhook(f'A new user queue was created. Click here to validate: {url}\n{user_credential}')
		else:
			messages.error(request,f"{form.errors.as_text}")
		return HttpResponseRedirect('/')
	else:
		form = UserQueueForm()
	return render(request, 'base/create_user_queue.html', {'form': form,"sidebarContent":SidebarContent})

@db_maintenance
@login_required
def validate_user_queue(request, pk):
	if request.user.is_superuser:
		try:
			user_queue = UserQueue.objects.get(pk=pk)
		except UserQueue.DoesNotExist:
			messages.error(request,f'The user with {pk} as Primary Key doesn\'t exist')
			return HttpResponseRedirect('/')
		user = User.objects.create_user(user_queue.username, user_queue.email, user_queue.password)
		send_webhook(f"{user_queue} Deleted Log :\nUsername : {user_queue.username} | Email : {user_queue.email}")
		user_queue.delete()
		token = Token.objects.create(user=user)
		send_webhook(f'The user "{user.username}" was validated and added to the Django User model. Token: {token.key}')
		messages.info(request,f'The user "{user.username}" was validated and added to the Django User model. Token: {token.key}')
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/luhcaran/login/?next=' + request.build_absolute_uri())
	

def json_payload_profile(request,pbid):
	try:
		user_profile = user.objects.get(public_id=pbid)
	except user.DoesNotExist:
		return HttpResponseRedirect(f"/calculator/index")
	other_model = user_profile.getOtherModels()
	stuff_table_stats = other_model['stuff_table']
	hero_table_stats = other_model['hero_table']
	talent_table_stats = other_model['talent_table']
	skin_table_stats = other_model['skin_table']
	altar_table_stats = other_model['altar_table']
	jewel_type_table_stats = other_model['jewel_type_table']
	jewel_level_table_stats = other_model['jewel_level_table']
	egg_table_stats = other_model['egg_table']
	egg_equipped_table_stats = other_model['egg_equipped_table']
	dragon_table_stats = other_model['dragon_table']
	runes_table_stats = other_model['runes_table']
	reforge_table_stats = other_model['reforge_table']
	refine_table_stats = other_model['refine_table']
	medals_table_stats = other_model['medals_table']
	relics_table_stats = other_model['relics_table']
	weapon_skins_table_stats = other_model['weapon_skins_table']
	data = {
		"user": {
			"public_id": user_profile.public_id,
			"choosen_hero": user_profile.choosen_hero,
			"brave_privileges_level": user_profile.brave_privileges_level,
			"atk_base_stats_hero_choosen": user_profile.atk_base_stats_hero_choosen,
			"health_base_stats_hero_choosen": user_profile.health_base_stats_hero_choosen,
		},
		"stuff_table": {
			"weapon_choosen": stuff_table_stats.weapon_choosen,
			"weapon_level": stuff_table_stats.weapon_level,
			"weapon_rarity": stuff_table_stats.weapon_rarity,
			"armor_choosen": stuff_table_stats.armor_choosen,
			"armor_level": stuff_table_stats.armor_level,
			"armor_rarity": stuff_table_stats.armor_rarity,
			"ring1_choosen": stuff_table_stats.ring1_choosen,
			"ring1_level": stuff_table_stats.ring1_level,
			"ring1_rarity": stuff_table_stats.ring1_rarity,
			"ring2_choosen": stuff_table_stats.ring2_choosen,
			"ring2_level": stuff_table_stats.ring2_level,
			"ring2_rarity": stuff_table_stats.ring2_rarity,
			"pet1_choosen": stuff_table_stats.pet1_choosen,
			"pet1_level": stuff_table_stats.pet1_level,
			"pet1_rarity": stuff_table_stats.pet1_rarity,
			"pet2_choosen": stuff_table_stats.pet2_choosen,
			"pet2_level": stuff_table_stats.pet2_level,
			"pet2_rarity": stuff_table_stats.pet2_rarity,
			"bracelet_choosen": stuff_table_stats.bracelet_choosen,
			"bracelet_level": stuff_table_stats.bracelet_level,
			"bracelet_rarity": stuff_table_stats.bracelet_rarity,
			"locket_choosen": stuff_table_stats.locket_choosen,
			"locket_level": stuff_table_stats.locket_level,
			"locket_rarity": stuff_table_stats.locket_rarity,
			"book_choosen": stuff_table_stats.book_choosen,
			"book_level": stuff_table_stats.book_level,
			"book_rarity": stuff_table_stats.book_rarity
		},
		"hero_table": {
			"atreus_level": hero_table_stats.atreus_level,
			"atreus_star": hero_table_stats.atreus_star,
			"urasil_level": hero_table_stats.urasil_level,
			"urasil_star": hero_table_stats.urasil_star,
			"phoren_level": hero_table_stats.phoren_level,
			"phoren_star": hero_table_stats.phoren_star,
			"taranis_level": hero_table_stats.taranis_level,
			"taranis_star": hero_table_stats.taranis_star,
			"helix_level": hero_table_stats.helix_level,
			"helix_star": hero_table_stats.helix_star,
			"meowgik_level": hero_table_stats.meowgik_level,
			"meowgik_star": hero_table_stats.meowgik_star,
			"shari_level": hero_table_stats.shari_level,
			"shari_star": hero_table_stats.shari_star,
			"ayana_level": hero_table_stats.ayana_level,
			"ayana_star": hero_table_stats.ayana_star,
			"onir_level": hero_table_stats.onir_level,
			"onir_star": hero_table_stats.onir_star,
			"rolla_level": hero_table_stats.rolla_level,
			"rolla_star": hero_table_stats.rolla_star,
			"bonnie_level": hero_table_stats.bonnie_level,
			"bonnie_star": hero_table_stats.bonnie_star,
			"sylvan_level": hero_table_stats.sylvan_level,
			"sylvan_star": hero_table_stats.sylvan_star,
			"shade_level": hero_table_stats.shade_level,
			"shade_star": hero_table_stats.shade_star,
			"ophelia_level": hero_table_stats.ophelia_level,
			"ophelia_star": hero_table_stats.ophelia_star,
			"ryan_level": hero_table_stats.ryan_level,
			"ryan_star": hero_table_stats.ryan_star,
			"lina_level": hero_table_stats.lina_level,
			"lina_star": hero_table_stats.lina_star,
			"aquea_level": hero_table_stats.aquea_level,
			"aquea_star": hero_table_stats.aquea_star,
			"shingen_level": hero_table_stats.shingen_level,
			"shingen_star": hero_table_stats.shingen_star,
			"gugu_level": hero_table_stats.gugu_level,
			"gugu_star": hero_table_stats.gugu_star,
			"iris_level": hero_table_stats.iris_level,
			"iris_star": hero_table_stats.iris_star,
			"blazo_level": hero_table_stats.blazo_level,
			"blazo_star": hero_table_stats.blazo_star,
			"melinda_level": hero_table_stats.melinda_level,
			"melinda_star": hero_table_stats.melinda_star,
			"elaine_level": hero_table_stats.elaine_level,
			"elaine_star": hero_table_stats.elaine_star,
			"bobo_level": hero_table_stats.bobo_level,
			"bobo_star": hero_table_stats.bobo_star,
			"stella_level": hero_table_stats.stella_level,
			"stella_star": hero_table_stats.stella_star
		},
		"talent_table": {
			"strength_level": talent_table_stats.strength_level,
			"power_level": talent_table_stats.power_level,
			"recover_level": talent_table_stats.recover_level,
			"block_level": talent_table_stats.block_level,
			"iron_bulwark_level": talent_table_stats.iron_bulwark_level,
			"enhanced_equipment_level": talent_table_stats.enhanced_equipment_level,
			"hero_power_up_level": talent_table_stats.hero_power_up_level,
			"runes_power_up_level": talent_table_stats.runes_power_up_level
		},
		"skin_table": {
			"skin_health": skin_table_stats.skin_health,
			"skin_attack": skin_table_stats.skin_attack
		},
		"altar_table": {
			"stuff_altar_level": altar_table_stats.stuff_altar_level,
			"stuff_altar_ascension": altar_table_stats.stuff_altar_ascension,
			"heros_altar_level": altar_table_stats.heros_altar_level,
			"heros_altar_ascension": altar_table_stats.heros_altar_ascension
		},
		"jewel_type_table": {
			"weapon_jewel1_type": jewel_type_table_stats.weapon_jewel1_type,
			"weapon_jewel2_type": jewel_type_table_stats.weapon_jewel2_type,
			"weapon_jewel3_type": jewel_type_table_stats.weapon_jewel3_type,
			"weapon_jewel4_type": jewel_type_table_stats.weapon_jewel4_type,
			"armor_jewel1_type": jewel_type_table_stats.armor_jewel1_type,
			"armor_jewel2_type": jewel_type_table_stats.armor_jewel2_type,
			"armor_jewel3_type": jewel_type_table_stats.armor_jewel3_type,
			"armor_jewel4_type": jewel_type_table_stats.armor_jewel4_type,
			"ring1_jewel1_type": jewel_type_table_stats.ring1_jewel1_type,
			"ring1_jewel2_type": jewel_type_table_stats.ring1_jewel2_type,
			"ring1_jewel3_type": jewel_type_table_stats.ring1_jewel3_type,
			"ring1_jewel4_type": jewel_type_table_stats.ring1_jewel4_type,
			"ring2_jewel1_type": jewel_type_table_stats.ring2_jewel1_type,
			"ring2_jewel2_type": jewel_type_table_stats.ring2_jewel2_type,
			"ring2_jewel3_type": jewel_type_table_stats.ring2_jewel3_type,
			"ring2_jewel4_type": jewel_type_table_stats.ring2_jewel4_type,
			"pet1_jewel1_type": jewel_type_table_stats.pet1_jewel1_type,
			"pet1_jewel2_type": jewel_type_table_stats.pet1_jewel2_type,
			"pet1_jewel3_type": jewel_type_table_stats.pet1_jewel3_type,
			"pet1_jewel4_type": jewel_type_table_stats.pet1_jewel4_type,
			"pet2_jewel1_type": jewel_type_table_stats.pet2_jewel1_type,
			"pet2_jewel2_type": jewel_type_table_stats.pet2_jewel2_type,
			"pet2_jewel3_type": jewel_type_table_stats.pet2_jewel3_type,
			"pet2_jewel4_type": jewel_type_table_stats.pet2_jewel4_type,
			"bracelet_jewel1_type": jewel_type_table_stats.bracelet_jewel1_type,
			"bracelet_jewel2_type": jewel_type_table_stats.bracelet_jewel2_type,
			"bracelet_jewel3_type": jewel_type_table_stats.bracelet_jewel3_type,
			"bracelet_jewel4_type": jewel_type_table_stats.bracelet_jewel4_type,
			"locket_jewel1_type": jewel_type_table_stats.locket_jewel1_type,
			"locket_jewel2_type": jewel_type_table_stats.locket_jewel2_type,
			"locket_jewel3_type": jewel_type_table_stats.locket_jewel3_type,
			"locket_jewel4_type": jewel_type_table_stats.locket_jewel4_type,
			"book_jewel1_type": jewel_type_table_stats.book_jewel1_type,
			"book_jewel2_type": jewel_type_table_stats.book_jewel2_type,
			"book_jewel3_type": jewel_type_table_stats.book_jewel3_type,
			"book_jewel4_type": jewel_type_table_stats.book_jewel4_type
		},
		"jewel_level_table": {
			"weapon_jewel1_level": jewel_level_table_stats.weapon_jewel1_level,
			"weapon_jewel2_level": jewel_level_table_stats.weapon_jewel2_level,
			"weapon_jewel3_level": jewel_level_table_stats.weapon_jewel3_level,
			"weapon_jewel4_level": jewel_level_table_stats.weapon_jewel4_level,
			"armor_jewel1_level": jewel_level_table_stats.armor_jewel1_level,
			"armor_jewel2_level": jewel_level_table_stats.armor_jewel2_level,
			"armor_jewel3_level": jewel_level_table_stats.armor_jewel3_level,
			"armor_jewel4_level": jewel_level_table_stats.armor_jewel4_level,
			"ring1_jewel1_level": jewel_level_table_stats.ring1_jewel1_level,
			"ring1_jewel2_level": jewel_level_table_stats.ring1_jewel2_level,
			"ring1_jewel3_level": jewel_level_table_stats.ring1_jewel3_level,
			"ring1_jewel4_level": jewel_level_table_stats.ring1_jewel4_level,
			"ring2_jewel1_level": jewel_level_table_stats.ring2_jewel1_level,
			"ring2_jewel2_level": jewel_level_table_stats.ring2_jewel2_level,
			"ring2_jewel3_level": jewel_level_table_stats.ring2_jewel3_level,
			"ring2_jewel4_level": jewel_level_table_stats.ring2_jewel4_level,
			"pet1_jewel1_level": jewel_level_table_stats.pet1_jewel1_level,
			"pet1_jewel2_level": jewel_level_table_stats.pet1_jewel2_level,
			"pet1_jewel3_level": jewel_level_table_stats.pet1_jewel3_level,
			"pet1_jewel4_level": jewel_level_table_stats.pet1_jewel4_level,
			"pet2_jewel1_level": jewel_level_table_stats.pet2_jewel1_level,
			"pet2_jewel2_level": jewel_level_table_stats.pet2_jewel2_level,
			"pet2_jewel3_level": jewel_level_table_stats.pet2_jewel3_level,
			"pet2_jewel4_level": jewel_level_table_stats.pet2_jewel4_level,
			"bracelet_jewel1_level": jewel_level_table_stats.bracelet_jewel1_level,
			"bracelet_jewel2_level": jewel_level_table_stats.bracelet_jewel2_level,
			"bracelet_jewel3_level": jewel_level_table_stats.bracelet_jewel3_level,
			"bracelet_jewel4_level": jewel_level_table_stats.bracelet_jewel4_level,
			"locket_jewel1_level": jewel_level_table_stats.locket_jewel1_level,
			"locket_jewel2_level": jewel_level_table_stats.locket_jewel2_level,
			"locket_jewel3_level": jewel_level_table_stats.locket_jewel3_level,
			"locket_jewel4_level": jewel_level_table_stats.locket_jewel4_level,
			"book_jewel1_level": jewel_level_table_stats.book_jewel1_level,
			"book_jewel2_level": jewel_level_table_stats.book_jewel2_level,
			"book_jewel3_level": jewel_level_table_stats.book_jewel3_level,
			"book_jewel4_level": jewel_level_table_stats.book_jewel4_level
		},
		"egg_table": {
			"green_bat": egg_table_stats.green_bat,
			"vase": egg_table_stats.vase,
			"bomb_ghost": egg_table_stats.bomb_ghost,
			"rock_puppet": egg_table_stats.rock_puppet,
			"party_tree": egg_table_stats.party_tree,
			"wolfhound": egg_table_stats.wolfhound,
			"skeleton_archer": egg_table_stats.skeleton_archer,
			"skeleton_soldier": egg_table_stats.skeleton_soldier,
			"wasp": egg_table_stats.wasp,
			"fire_mage": egg_table_stats.fire_mage,
			"medusa": egg_table_stats.medusa,
			"ice_mage": egg_table_stats.ice_mage,
			"fire_lizard": egg_table_stats.fire_lizard,
			"flame_ghost": egg_table_stats.flame_ghost,
			"thorny_snake": egg_table_stats.thorny_snake,
			"tornado_demon": egg_table_stats.tornado_demon,
			"piranha": egg_table_stats.piranha,
			"zombie": egg_table_stats.zombie,
			"scarecrow": egg_table_stats.scarecrow,
			"long_dragon": egg_table_stats.long_dragon,
			"skull_wizard": egg_table_stats.skull_wizard,
			"lava_golem": egg_table_stats.lava_golem,
			"ice_golem": egg_table_stats.ice_golem,
			"cactus": egg_table_stats.cactus,
			"crazy_spider": egg_table_stats.crazy_spider,
			"fire_element": egg_table_stats.fire_element,
			"skeleton_swordsman": egg_table_stats.skeleton_swordsman,
			"scythe_mage": egg_table_stats.scythe_mage,
			"pea_shooter": egg_table_stats.pea_shooter,
			"shadow_assassin": egg_table_stats.shadow_assassin,
			"tornado_mage": egg_table_stats.tornado_mage,
			"spitting_mushroom": egg_table_stats.spitting_mushroom,
			"rolling_mushroom": egg_table_stats.rolling_mushroom,
			"fallen_bat": egg_table_stats.fallen_bat,
			"one_eyed_bat": egg_table_stats.one_eyed_bat,
			"scarlet_mage": egg_table_stats.scarlet_mage,
			"icefire_phantom": egg_table_stats.icefire_phantom,
			"purple_phantom": egg_table_stats.purple_phantom,
			"tundra_dragon": egg_table_stats.tundra_dragon,
			"sandian": egg_table_stats.sandian,
			"nether_puppet": egg_table_stats.nether_puppet,
			"psionic_scarecrow": egg_table_stats.psionic_scarecrow,
			"steel_dryad": egg_table_stats.steel_dryad,
			"savage_spider": egg_table_stats.savage_spider,
			"flaming_bug": egg_table_stats.flaming_bug,
			"shark_bro": egg_table_stats.shark_bro,
			"crimson_zombie": egg_table_stats.crimson_zombie,
			"fat_bat": egg_table_stats.fat_bat,
			"plainswolf": egg_table_stats.plainswolf,
			"elite_archer": egg_table_stats.elite_archer,
			"little_dragon": egg_table_stats.little_dragon,
			"arch_leader": egg_table_stats.arch_leader,
			"skeleton_king": egg_table_stats.skeleton_king,
			"crimson_witch": egg_table_stats.crimson_witch,
			"rage_golem": egg_table_stats.rage_golem,
			"queen_bee": egg_table_stats.queen_bee,
			"ice_worm": egg_table_stats.ice_worm,
			"medusa_boss": egg_table_stats.medusa_boss,
			"ice_demon": egg_table_stats.ice_demon,
			"giant_owl": egg_table_stats.giant_owl,
			"fire_demon": egg_table_stats.fire_demon,
			"krab_boss": egg_table_stats.krab_boss,
			"desert_goliath": egg_table_stats.desert_goliath,
			"sinister_touch": egg_table_stats.sinister_touch,
			"scythe_pharoah": egg_table_stats.scythe_pharoah,
			"fireworm_queen": egg_table_stats.fireworm_queen,
			"infernal_demon": egg_table_stats.infernal_demon
		},
		"egg_equipped_table": {
			"egg_equipped1": egg_equipped_table_stats.egg_equipped1,
			"egg_equipped2": egg_equipped_table_stats.egg_equipped2,
			"egg_equipped3": egg_equipped_table_stats.egg_equipped3,
			"egg_equipped4": egg_equipped_table_stats.egg_equipped4,
			"egg_equipped5": egg_equipped_table_stats.egg_equipped5
		},
		"dragon_table": {
			"dragon1_type": dragon_table_stats.dragon1_type,
			"dragon2_type": dragon_table_stats.dragon2_type,
			"dragon3_type": dragon_table_stats.dragon3_type,
			"dragon1_rarity": dragon_table_stats.dragon1_rarity,
			"dragon2_rarity": dragon_table_stats.dragon2_rarity,
			"dragon3_rarity": dragon_table_stats.dragon3_rarity,
			"dragon1_level": dragon_table_stats.dragon1_level,
			"dragon2_level": dragon_table_stats.dragon2_level,
			"dragon3_level": dragon_table_stats.dragon3_level,
			"dragon_1_boost_1": dragon_table_stats.dragon_1_boost_1,
			"dragon_1_boost_2": dragon_table_stats.dragon_1_boost_2,
			"dragon_1_boost_3": dragon_table_stats.dragon_1_boost_3,
			"dragon_1_boost_4": dragon_table_stats.dragon_1_boost_4,
			"dragon_2_boost_1": dragon_table_stats.dragon_2_boost_1,
			"dragon_2_boost_2": dragon_table_stats.dragon_2_boost_2,
			"dragon_2_boost_3": dragon_table_stats.dragon_2_boost_3,
			"dragon_2_boost_4": dragon_table_stats.dragon_2_boost_4,
			"dragon_3_boost_1": dragon_table_stats.dragon_3_boost_1,
			"dragon_3_boost_2": dragon_table_stats.dragon_3_boost_2,
			"dragon_3_boost_3": dragon_table_stats.dragon_3_boost_3,
			"dragon_3_boost_4": dragon_table_stats.dragon_3_boost_4
		},
		"runes_table": {
			"power_line_1": runes_table_stats.power_line_1,
			"power_line_2": runes_table_stats.power_line_2,
			"power_line_3": runes_table_stats.power_line_3,
			"power_line_4": runes_table_stats.power_line_4,
			"power_line_5": runes_table_stats.power_line_5,
			"saviour_line_1": runes_table_stats.saviour_line_1,
			"saviour_line_2": runes_table_stats.saviour_line_2,
			"saviour_line_3": runes_table_stats.saviour_line_3,
			"saviour_line_4": runes_table_stats.saviour_line_4,
			"saviour_line_5": runes_table_stats.saviour_line_5,
			"recovery_line_1": runes_table_stats.recovery_line_1,
			"recovery_line_2": runes_table_stats.recovery_line_2,
			"recovery_line_3": runes_table_stats.recovery_line_3,
			"recovery_line_4": runes_table_stats.recovery_line_4,
			"recovery_line_5": runes_table_stats.recovery_line_5,
			"courage_line_1": runes_table_stats.courage_line_1,
			"courage_line_2": runes_table_stats.courage_line_2,
			"courage_line_3": runes_table_stats.courage_line_3,
			"courage_line_4": runes_table_stats.courage_line_4,
			"courage_line_5": runes_table_stats.courage_line_5,
			"luck_line_1": runes_table_stats.luck_line_1,
			"luck_line_2": runes_table_stats.luck_line_2,
			"luck_line_3": runes_table_stats.luck_line_3,
			"luck_line_4": runes_table_stats.luck_line_4,
			"luck_line_5": runes_table_stats.luck_line_5,
			"value_power_line_1": runes_table_stats.value_power_line_1,
			"value_power_line_2": runes_table_stats.value_power_line_2,
			"value_power_line_3": runes_table_stats.value_power_line_3,
			"value_power_line_4": runes_table_stats.value_power_line_4,
			"value_power_line_5": runes_table_stats.value_power_line_5,
			"value_saviour_line_1": runes_table_stats.value_saviour_line_1,
			"value_saviour_line_2": runes_table_stats.value_saviour_line_2,
			"value_saviour_line_3": runes_table_stats.value_saviour_line_3,
			"value_saviour_line_4": runes_table_stats.value_saviour_line_4,
			"value_saviour_line_5": runes_table_stats.value_saviour_line_5,
			"value_recovery_line_1": runes_table_stats.value_recovery_line_1,
			"value_recovery_line_2": runes_table_stats.value_recovery_line_2,
			"value_recovery_line_3": runes_table_stats.value_recovery_line_3,
			"value_recovery_line_4": runes_table_stats.value_recovery_line_4,
			"value_recovery_line_5": runes_table_stats.value_recovery_line_5,
			"value_courage_line_1": runes_table_stats.value_courage_line_1,
			"value_courage_line_2": runes_table_stats.value_courage_line_2,
			"value_courage_line_3": runes_table_stats.value_courage_line_3,
			"value_courage_line_4": runes_table_stats.value_courage_line_4,
			"value_courage_line_5": runes_table_stats.value_courage_line_5,
			"value_luck_line_1": runes_table_stats.value_luck_line_1,
			"value_luck_line_2": runes_table_stats.value_luck_line_2,
			"value_luck_line_3": runes_table_stats.value_luck_line_3,
			"value_luck_line_4": runes_table_stats.value_luck_line_4,
			"value_luck_line_5": runes_table_stats.value_luck_line_5
		},
		"reforge_table": {
			"reforge_power": reforge_table_stats.reforge_power,
			"reforge_saviour": reforge_table_stats.reforge_saviour,
			"reforge_recovery": reforge_table_stats.reforge_recovery,
			"reforge_courage": reforge_table_stats.reforge_courage,
			"reforge_luck": reforge_table_stats.reforge_luck
		},
		"refine_table": {
			"weapon_refine_atk": refine_table_stats.weapon_refine_atk,
			"weapon_refine_basic_stats": refine_table_stats.weapon_refine_basic_stats,
			"armor_refine_hp": refine_table_stats.armor_refine_hp,
			"armor_refine_basic_stats": refine_table_stats.armor_refine_basic_stats,
			"ring1_refine_atk": refine_table_stats.ring1_refine_atk,
			"ring1_refine_basic_stats": refine_table_stats.ring1_refine_basic_stats,
			"ring2_refine_atk": refine_table_stats.ring2_refine_atk,
			"ring2_refine_basic_stats": refine_table_stats.ring2_refine_basic_stats,
			"bracelet_refine_atk": refine_table_stats.bracelet_refine_atk,
			"bracelet_refine_basic_stats": refine_table_stats.bracelet_refine_basic_stats,
			"locket_refine_hp": refine_table_stats.locket_refine_hp,
			"locket_refine_basic_stats": refine_table_stats.locket_refine_basic_stats,
			"book_refine_hp": refine_table_stats.book_refine_hp,
			"book_refine_basic_stats": refine_table_stats.book_refine_basic_stats
		},
		"medals_table": {
			"medals_1001": medals_table_stats.medals_1001,
			"medals_1002": medals_table_stats.medals_1002,
			"medals_1003": medals_table_stats.medals_1003,
			"medals_1004": medals_table_stats.medals_1004,
			"medals_1005": medals_table_stats.medals_1005,
			"medals_1006": medals_table_stats.medals_1006,
			"medals_1008": medals_table_stats.medals_1008,
			"medals_1009": medals_table_stats.medals_1009,
			"medals_1010": medals_table_stats.medals_1010,
			"medals_1011": medals_table_stats.medals_1011,
			"medals_1012": medals_table_stats.medals_1012,
			"medals_2001": medals_table_stats.medals_2001,
			"medals_2002": medals_table_stats.medals_2002,
			"medals_2003": medals_table_stats.medals_2003,
			"medals_2004": medals_table_stats.medals_2004,
			"medals_2005": medals_table_stats.medals_2005,
			"medals_2006": medals_table_stats.medals_2006,
			"medals_2007": medals_table_stats.medals_2007,
			"medals_2008": medals_table_stats.medals_2008,
			"medals_2009": medals_table_stats.medals_2009,
			"medals_2010": medals_table_stats.medals_2010,
			"medals_2011": medals_table_stats.medals_2011,
			"medals_2012": medals_table_stats.medals_2012,
			"medals_2013": medals_table_stats.medals_2013,
			"medals_2014": medals_table_stats.medals_2014,
			"medals_3001": medals_table_stats.medals_3001,
			"medals_3002": medals_table_stats.medals_3002,
			"medals_3003": medals_table_stats.medals_3003,
			"medals_3004": medals_table_stats.medals_3004,
			"medals_3005": medals_table_stats.medals_3005,
			"medals_3006": medals_table_stats.medals_3006,
			"medals_3007": medals_table_stats.medals_3007,
			"medals_3008": medals_table_stats.medals_3008,
			"medals_3009": medals_table_stats.medals_3009,
			"medals_3010": medals_table_stats.medals_3010,
			"medals_3019": medals_table_stats.medals_3019,
			"medals_3020": medals_table_stats.medals_3020,
			"medals_3021": medals_table_stats.medals_3021,
			"medals_3022": medals_table_stats.medals_3022,
			"medals_3023": medals_table_stats.medals_3023,
			"medals_3024": medals_table_stats.medals_3024,
			"medals_3025": medals_table_stats.medals_3025,
			"medals_3026": medals_table_stats.medals_3026,
			"medals_3027": medals_table_stats.medals_3027,
			"medals_3028": medals_table_stats.medals_3028,
			"medals_3029": medals_table_stats.medals_3029,
			"medals_3030": medals_table_stats.medals_3030,
			"medals_3034": medals_table_stats.medals_3034,
			"medals_3035": medals_table_stats.medals_3035,
			"medals_3036": medals_table_stats.medals_3036
		},
		"relics_table": {
			"wraith_mask_level": relics_table_stats.wraith_mask_level,
			"wraith_mask_star": relics_table_stats.wraith_mask_star,
			"wraith_mask_effective": relics_table_stats.wraith_mask_effective,
			"clown_mask_level": relics_table_stats.clown_mask_level,
			"clown_mask_star": relics_table_stats.clown_mask_star,
			"clown_mask_effective": relics_table_stats.clown_mask_effective,
			"princess_teddy_bear_level": relics_table_stats.princess_teddy_bear_level,
			"princess_teddy_bear_star": relics_table_stats.princess_teddy_bear_star,
			"princess_teddy_bear_effective": relics_table_stats.princess_teddy_bear_effective,
			"belt_of_might_level": relics_table_stats.belt_of_might_level,
			"belt_of_might_star": relics_table_stats.belt_of_might_star,
			"belt_of_might_effective": relics_table_stats.belt_of_might_effective,
			"beastmaster_whistle_level": relics_table_stats.beastmaster_whistle_level,
			"beastmaster_whistle_star": relics_table_stats.beastmaster_whistle_star,
			"beastmaster_whistle_effective": relics_table_stats.beastmaster_whistle_effective,
			"archmage_robe_level": relics_table_stats.archmage_robe_level,
			"archmage_robe_star": relics_table_stats.archmage_robe_star,
			"archmage_robe_effective": relics_table_stats.archmage_robe_effective,
			"shimmering_gem_level": relics_table_stats.shimmering_gem_level,
			"shimmering_gem_star": relics_table_stats.shimmering_gem_star,
			"bloom_of_eternity_level": relics_table_stats.bloom_of_eternity_level,
			"bloom_of_eternity_star": relics_table_stats.bloom_of_eternity_star,
			"bloom_of_eternity_effective": relics_table_stats.bloom_of_eternity_effective,
			"challenger_headband_level": relics_table_stats.challenger_headband_level,
			"challenger_headband_star": relics_table_stats.challenger_headband_star,
			"jade_gobelet_level": relics_table_stats.jade_gobelet_level,
			"jade_gobelet_star": relics_table_stats.jade_gobelet_star,
			"jade_gobelet_effective": relics_table_stats.jade_gobelet_effective,
			"veteran_plate_level": relics_table_stats.veteran_plate_level,
			"veteran_plate_star": relics_table_stats.veteran_plate_star,
			"dragonscale_level": relics_table_stats.dragonscale_level,
			"dragonscale_star": relics_table_stats.dragonscale_star,
			"dragonscale_effective": relics_table_stats.dragonscale_effective,
			"dragon_tooth_level": relics_table_stats.dragon_tooth_level,
			"dragon_tooth_star": relics_table_stats.dragon_tooth_star,
			"dragon_tooth_effective": relics_table_stats.dragon_tooth_effective,
			"scholar_telescope_level": relics_table_stats.scholar_telescope_level,
			"scholar_telescope_star": relics_table_stats.scholar_telescope_star,
			"pirate_shank_level": relics_table_stats.pirate_shank_level,
			"pirate_shank_star": relics_table_stats.pirate_shank_star,
			"giant_greatsword_level": relics_table_stats.giant_greatsword_level,
			"giant_greatsword_star": relics_table_stats.giant_greatsword_star,
			"giant_greatsword_effective": relics_table_stats.giant_greatsword_effective,
			"healing_potion_level": relics_table_stats.healing_potion_level,
			"healing_potion_star": relics_table_stats.healing_potion_star,
			"whirlwind_mauler_level": relics_table_stats.whirlwind_mauler_level,
			"whirlwind_mauler_star": relics_table_stats.whirlwind_mauler_star,
			"whirlwind_mauler_effective": relics_table_stats.whirlwind_mauler_effective,
			"special_lance_level": relics_table_stats.special_lance_level,
			"special_lance_star": relics_table_stats.special_lance_star,
			"special_lance_effective": relics_table_stats.special_lance_effective,
			"precision_slingshot_level": relics_table_stats.precision_slingshot_level,
			"precision_slingshot_star": relics_table_stats.precision_slingshot_star,
			"maidens_pearl_earring_level": relics_table_stats.maidens_pearl_earring_level,
			"maidens_pearl_earring_star": relics_table_stats.maidens_pearl_earring_star,
			"ancient_shield_level": relics_table_stats.ancient_shield_level,
			"ancient_shield_star": relics_table_stats.ancient_shield_star,
			"ancient_shield_effective": relics_table_stats.ancient_shield_effective,
			"supreme_trinity_alpha_level": relics_table_stats.supreme_trinity_alpha_level,
			"supreme_trinity_alpha_star": relics_table_stats.supreme_trinity_alpha_star,
			"supreme_trinity_alpha_effective": relics_table_stats.supreme_trinity_alpha_effective,
			"golden_apple_level": relics_table_stats.golden_apple_level,
			"golden_apple_star": relics_table_stats.golden_apple_star,
			"golden_apple_effective": relics_table_stats.golden_apple_effective,
			"ancient_stele_level": relics_table_stats.ancient_stele_level,
			"ancient_stele_star": relics_table_stats.ancient_stele_star,
			"ancient_stele_effective": relics_table_stats.ancient_stele_effective,
			"philosopher_stone_level": relics_table_stats.philosopher_stone_level,
			"philosopher_stone_star": relics_table_stats.philosopher_stone_star,
			"philosopher_stone_effective": relics_table_stats.philosopher_stone_effective,
			"dragon_heart_level": relics_table_stats.dragon_heart_level,
			"dragon_heart_star": relics_table_stats.dragon_heart_star,
			"dragon_heart_effective": relics_table_stats.dragon_heart_effective,
			"spectral_duality_level": relics_table_stats.spectral_duality_level,
			"spectral_duality_star": relics_table_stats.spectral_duality_star,
			"spectral_duality_effective": relics_table_stats.spectral_duality_effective,
			"mystic_emblem_level": relics_table_stats.mystic_emblem_level,
			"mystic_emblem_star": relics_table_stats.mystic_emblem_star,
			"immortal_brooch_level": relics_table_stats.immortal_brooch_level,
			"immortal_brooch_star": relics_table_stats.immortal_brooch_star,
			"golden_statue_level": relics_table_stats.golden_statue_level,
			"golden_statue_star": relics_table_stats.golden_statue_star,
			"golden_statue_effective": relics_table_stats.golden_statue_effective,
			"smilling_mask_level": relics_table_stats.smilling_mask_level,
			"smilling_mask_star": relics_table_stats.smilling_mask_star,
			"unmerciful_mask_level": relics_table_stats.unmerciful_mask_level,
			"unmerciful_mask_star": relics_table_stats.unmerciful_mask_star,
			"unmerciful_mask_effective": relics_table_stats.unmerciful_mask_effective,
			"holy_water_level": relics_table_stats.holy_water_level,
			"holy_water_star": relics_table_stats.holy_water_star,
			"holy_water_effective": relics_table_stats.holy_water_effective,
			"book_of_the_dead_level": relics_table_stats.book_of_the_dead_level,
			"book_of_the_dead_star": relics_table_stats.book_of_the_dead_star,
			"book_of_the_dead_effective": relics_table_stats.book_of_the_dead_effective,
			"psionist_treasure_level": relics_table_stats.psionist_treasure_level,
			"psionist_treasure_star": relics_table_stats.psionist_treasure_star,
			"book_of_archery_level": relics_table_stats.book_of_archery_level,
			"book_of_archery_star": relics_table_stats.book_of_archery_star,
			"book_of_archery_effective": relics_table_stats.book_of_archery_effective,
			"book_of_bravery_level": relics_table_stats.book_of_bravery_level,
			"book_of_bravery_star": relics_table_stats.book_of_bravery_star,
			"book_of_bravery_effective": relics_table_stats.book_of_bravery_effective,
			"angelic_heart_level": relics_table_stats.angelic_heart_level,
			"angelic_heart_star": relics_table_stats.angelic_heart_star,
			"angelic_heart_effective": relics_table_stats.angelic_heart_effective,
			"devil_whisper_level": relics_table_stats.devil_whisper_level,
			"devil_whisper_star": relics_table_stats.devil_whisper_star,
			"devil_whisper_effective": relics_table_stats.devil_whisper_effective,
			"stone_of_wisdom_level": relics_table_stats.stone_of_wisdom_level,
			"stone_of_wisdom_star": relics_table_stats.stone_of_wisdom_star,
			"empyrean_mirror_level": relics_table_stats.empyrean_mirror_level,
			"empyrean_mirror_star": relics_table_stats.empyrean_mirror_star,
			"empyrean_mirror_effective": relics_table_stats.empyrean_mirror_effective,
			"fabled_archer_arrow_level": relics_table_stats.fabled_archer_arrow_level,
			"fabled_archer_arrow_star": relics_table_stats.fabled_archer_arrow_star,
			"fabled_archer_arrow_effective": relics_table_stats.fabled_archer_arrow_effective,
			"shiny_gemmed_belt_level": relics_table_stats.shiny_gemmed_belt_level,
			"shiny_gemmed_belt_star": relics_table_stats.shiny_gemmed_belt_star,
			"mythril_flux_mail_level": relics_table_stats.mythril_flux_mail_level,
			"mythril_flux_mail_star": relics_table_stats.mythril_flux_mail_star,
			"mythril_flux_mail_effective": relics_table_stats.mythril_flux_mail_effective,
			"stealth_boots_level": relics_table_stats.stealth_boots_level,
			"stealth_boots_star": relics_table_stats.stealth_boots_star,
			"stealth_boots_effective": relics_table_stats.stealth_boots_effective,
			"assassin_dagger_level": relics_table_stats.assassin_dagger_level,
			"assassin_dagger_star": relics_table_stats.assassin_dagger_star,
			"assassin_dagger_effective": relics_table_stats.assassin_dagger_effective,
			"gold_bunny_level": relics_table_stats.gold_bunny_level,
			"gold_bunny_star": relics_table_stats.gold_bunny_star,
			"lucky_coin_level": relics_table_stats.lucky_coin_level,
			"lucky_coin_star": relics_table_stats.lucky_coin_star,
			"dusken_cask_level": relics_table_stats.dusken_cask_level,
			"dusken_cask_star": relics_table_stats.dusken_cask_star,
			"dragon_eye_level": relics_table_stats.dragon_eye_level,
			"dragon_eye_star": relics_table_stats.dragon_eye_star,
			"dragon_eye_effective": relics_table_stats.dragon_eye_effective,
			"ring_of_greed_level": relics_table_stats.ring_of_greed_level,
			"ring_of_greed_star": relics_table_stats.ring_of_greed_star,
			"genesis_staff_level": relics_table_stats.genesis_staff_level,
			"genesis_staff_star": relics_table_stats.genesis_staff_star,
			"bloodstained_sword_level": relics_table_stats.bloodstained_sword_level,
			"bloodstained_sword_star": relics_table_stats.bloodstained_sword_star,
			"bloodstained_sword_effective": relics_table_stats.bloodstained_sword_effective,
			"starcluster_rage_level": relics_table_stats.starcluster_rage_level,
			"starcluster_rage_star": relics_table_stats.starcluster_rage_star,
			"starcluster_rage_effective": relics_table_stats.starcluster_rage_effective,
			"elven_king_cape_level": relics_table_stats.elven_king_cape_level,
			"elven_king_cape_star": relics_table_stats.elven_king_cape_star,
			"elven_king_cape_effective": relics_table_stats.elven_king_cape_effective,
			"spear_of_yggdrasil_level": relics_table_stats.spear_of_yggdrasil_level,
			"spear_of_yggdrasil_star": relics_table_stats.spear_of_yggdrasil_star,
			"spear_of_yggdrasil_effective": relics_table_stats.spear_of_yggdrasil_effective,
			"dragon_gem_level": relics_table_stats.dragon_gem_level,
			"dragon_gem_star": relics_table_stats.dragon_gem_star,
			"dragon_gem_effective": relics_table_stats.dragon_gem_effective,
			"life_crown_level": relics_table_stats.life_crown_level,
			"life_crown_star": relics_table_stats.life_crown_star,
			"life_crown_effective": relics_table_stats.life_crown_effective,
			"sand_of_time_level": relics_table_stats.sand_of_time_level,
			"sand_of_time_star": relics_table_stats.sand_of_time_star,
			"sand_of_time_effective": relics_table_stats.sand_of_time_effective,
			"first_lightning_level": relics_table_stats.first_lightning_level,
			"first_lightning_star": relics_table_stats.first_lightning_star,
			"oracle_quill_level": relics_table_stats.oracle_quill_level,
			"oracle_quill_star": relics_table_stats.oracle_quill_star,
			"oracle_quill_effective": relics_table_stats.oracle_quill_effective,
			"bloodthirsty_grail_level": relics_table_stats.bloodthirsty_grail_level,
			"bloodthirsty_grail_star": relics_table_stats.bloodthirsty_grail_star,
			"bloodthirsty_grail_effective": relics_table_stats.bloodthirsty_grail_effective,
			"healing_grail_level": relics_table_stats.healing_grail_level,
			"healing_grail_star": relics_table_stats.healing_grail_star,
			"healing_grail_effective": relics_table_stats.healing_grail_effective,
			"cupids_necklace_level": relics_table_stats.cupids_necklace_level,
			"cupids_necklace_star": relics_table_stats.cupids_necklace_star,
			"life_staff_level": relics_table_stats.life_staff_level,
			"life_staff_star": relics_table_stats.life_staff_star,
			"life_staff_effective": relics_table_stats.life_staff_effective,
			"light_grail_level": relics_table_stats.light_grail_level,
			"light_grail_star": relics_table_stats.light_grail_star,
			"primal_fire_level": relics_table_stats.primal_fire_level,
			"primal_fire_star": relics_table_stats.primal_fire_star,
			"primal_fire_effective": relics_table_stats.primal_fire_effective
		},
		"weapon_skins_table": {
			"demon_blade_rain_1": weapon_skins_table_stats.demon_blade_rain_1,
			"antiquated_sword_1": weapon_skins_table_stats.antiquated_sword_1,
			"gale_force_1": weapon_skins_table_stats.gale_force_1,
			"death_scythe_1": weapon_skins_table_stats.death_scythe_1,
			"boomerang_1": weapon_skins_table_stats.boomerang_1,
			"brightspear_1": weapon_skins_table_stats.brightspear_1,
			"saw_blade_1": weapon_skins_table_stats.saw_blade_1,
			"brave_bow_1": weapon_skins_table_stats.brave_bow_1,
			"stalker_staff_1": weapon_skins_table_stats.stalker_staff_1
		}
	}
	return JsonResponse(data, safe=False)


@db_maintenance
@login_required
def show_debug(request, pbid):
	user_credential = request.session['user_credential']
	if checkContributor(user_credential,request):
		with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
			local_data = json.load(f)
		try:
			user_stats = user.objects.get(public_id=pbid)
		except user.DoesNotExist:
			messages.info(request,"user doesn't exists")
			return HttpResponseRedirect('/')
		other_model = user_stats.getOtherModels()
		stuff_table_stats = other_model['stuff_table']
		talent_table_stats = other_model['talent_table']
		altar_table_stats = other_model['altar_table']
		jewel_level_table_stats = other_model['jewel_level_table']
		egg_table_stats = other_model['egg_table']
		egg_equipped_table_stats = other_model['egg_equipped_table']
		dragon_table_stats = other_model['dragon_table']
		runes_table_stats = other_model['runes_table']
		refine_table_stats = other_model['refine_table']
		medals_table_stats = other_model['medals_table']
		relics_table_stats = other_model['relics_table']
		weapon_skins_table_stats = other_model['weapon_skins_table']
		################################# REQUÊTE DES ENTRÉES DE L'USERS #######################################################
		stuff_altar_ascension = altar_table_stats.stuff_altar_ascension
		heros_altar_ascension = altar_table_stats.heros_altar_ascension
		refine_weapon_enhanced_equipment = int(refine_table_stats.weapon_refine_basic_stats)/100
		refine_armor_enhanced_equipment = int(refine_table_stats.armor_refine_basic_stats)/100
		refine_ring1_enhanced_equipment = int(refine_table_stats.ring1_refine_basic_stats)/100
		refine_ring2_enhanced_equipment = int(refine_table_stats.ring2_refine_basic_stats)/100
		refine_bracelet_enhanced_equipment = int(refine_table_stats.bracelet_refine_basic_stats)/100
		refine_locket_enhanced_equipment = int(refine_table_stats.locket_refine_basic_stats)/100
		refine_book_enhanced_equipment = int(refine_table_stats.book_refine_basic_stats)/100
		brave_privileges_level = int(user_stats.brave_privileges_level)
		## Get Talents Stats
		talent_stats_dict = talent_table_stats.getTalentStats()
		## Get all Relics Stats
		relics_stats:dict = relics_table_stats.relics_Stats()
		## Get Altar Ascension Stats
		altar_stuff_ascension_atk = local_data["StuffAltarAscension"][str(stuff_altar_ascension) + '_attack']
		altar_stuff_ascension_hp = local_data["StuffAltarAscension"][str(stuff_altar_ascension) + '_hp']
		altar_stuff_ascension_equipment_base = local_data["StuffAltarAscension"][str(stuff_altar_ascension) + '_equipment_base']
		altar_heros_ascension_atk = local_data['HerosAltarAscension'][str(heros_altar_ascension) + '_attack']
		altar_heros_ascension_hp = local_data['HerosAltarAscension'][str(heros_altar_ascension) + '_hp']
		altar_heros_ascension_heros_base = local_data['HerosAltarAscension'][str(heros_altar_ascension) + '_heros_base']
		altar_heros_ascension_dmg_elite = local_data['HerosAltarAscension'][str(heros_altar_ascension) + '_dmg_elite']
		## Get Altar Stats 
		altar_stuff_atk = altar_table_stats.CalculAltar("stuff","attack",relics_stats.get('eqpm_altar_stats_var',0.0))
		altar_stuff_hp = altar_table_stats.CalculAltar("stuff","hp",relics_stats.get('eqpm_altar_stats_var',0.0))
		altar_hero_atk = altar_table_stats.CalculAltar("heros","attack",relics_stats.get('eqpm_altar_stats_var',0.0)) ##laisser le S (le nom du field prend un s)
		altar_hero_hp = altar_table_stats.CalculAltar("heros","hp",relics_stats.get('eqpm_altar_stats_var',0.0))
		## Get Passiv Stats From Type 3 Egg
		egg_arch_leader_passiv = egg_table_stats.GetPassivEggStats3("arch_leader",missing_data)
		egg_skeleton_king_passiv = egg_table_stats.GetPassivEggStats3("skeleton_king",missing_data)
		egg_crimson_witch_passiv = egg_table_stats.GetPassivEggStats3("crimson_witch",missing_data)
		egg_queen_bee_passiv = egg_table_stats.GetPassivEggStats3("queen_bee",missing_data)
		egg_ice_worm_passiv = egg_table_stats.GetPassivEggStats3("ice_worm",missing_data)
		egg_medusa_boss_passiv = egg_table_stats.GetPassivEggStats3("medusa_boss",missing_data)
		egg_ice_demon_passiv = egg_table_stats.GetPassivEggStats3("ice_demon",missing_data)
		egg_giant_owl_passiv = egg_table_stats.GetPassivEggStats3("giant_owl",missing_data)
		egg_fire_demon_passiv = egg_table_stats.GetPassivEggStats3("fire_demon",missing_data)
		egg_krab_boss_passiv = egg_table_stats.GetPassivEggStats3("krab_boss",missing_data)
		egg_desert_goliath_passiv = egg_table_stats.GetPassivEggStats3("desert_goliath",missing_data)
		egg_scythe_pharoah_passiv = egg_table_stats.GetPassivEggStats3("scythe_pharoah",missing_data)
		egg_infernal_demon_passiv = egg_table_stats.GetPassivEggStats3("infernal_demon",missing_data)
		egg_sinister_touch_passiv = egg_table_stats.GetPassivEggStats3("sinister_touch",missing_data)
		egg_fireworm_queen_passiv = egg_table_stats.GetPassivEggStats3("fireworm_queen",missing_data)
		## Get Brave Privilege Stats
		brave_privileges_stats = local_data["BravePrivileges"]['level' + str(brave_privileges_level)]
		## Get Special Bonus Stats
		BonusSpe_jewel_weapon = jewel_level_table_stats.JewelSpeBonusStatsRecup('weapon',brave_privileges_stats['Weapon JSSSA'],relics_stats.get("jewel_attack_bonus_var",0))
		BonusSpe_jewel_armor = jewel_level_table_stats.JewelSpeBonusStatsRecup('armor',brave_privileges_stats['Armor JSSSA'],relics_stats.get("jewel_hp_bonus_var",0))
		BonusSpe_jewel_ring1 = jewel_level_table_stats.JewelSpeBonusStatsRecup('ring1',brave_privileges_stats['Ring JSSSA'])
		BonusSpe_jewel_ring2 = jewel_level_table_stats.JewelSpeBonusStatsRecup('ring2',brave_privileges_stats['Ring JSSSA'])
		BonusSpe_jewel_bracelet = jewel_level_table_stats.JewelSpeBonusStatsRecup('bracelet',brave_privileges_stats['Bracelet JSSSA'],relics_stats.get("jewel_attack_bonus_var",0))
		BonusSpe_jewel_locket = jewel_level_table_stats.JewelSpeBonusStatsRecup('locket',brave_privileges_stats['Locket JSSSA'],relics_stats.get("jewel_attack_bonus_var",0))
		BonusSpe_jewel_book = jewel_level_table_stats.JewelSpeBonusStatsRecup('book',brave_privileges_stats['Spellbook JSSSA'])
		## DRAGON
		relics_dragon_base_stats = relics_stats.get('dragon_base_stats_var',0.0)
		dragon_stats_dict = dragon_table_stats.DragonStatueStats(relics_dragon_base_stats)
		## Get Dragon passiv Skills
		dragons_skills = dragon_table_stats.getPassivSkillDragon()
		## Get All Stats of Equipped Egg
		activ_egg_stats = egg_equipped_table_stats.GetEggStats(missing_data)
		## Get Rune Line Stats
		runelineRecovery = runes_table_stats.getValueLineRecovery()
		## Get Weapon Skin Stats
		weapon_skin_stats = weapon_skins_table_stats.getWeaponSkinStats()
		## Get Weapon Coeff Damage Multiplier
		weapon_dmg_multiplier = stuff_table_stats.getWeaponCoeff()
		## Get all Medals Stats
		medal_stats = medals_table_stats.medal_calc()
		# Get All Jewel's Stats
		stats_jewel_dict = jewel_level_table_stats.JewelStatsRecup(float(relics_stats.get("jewel_attack_bonus_var",0)),float(relics_stats.get("jewel_hp_bonus_var",0)))
		############################################## CALCUL #######################################################
		egg_var_passiv_heros_power_up = int(egg_arch_leader_passiv[3]) + int(egg_medusa_boss_passiv[3]) + int(egg_fire_demon_passiv[3]) + int(egg_krab_boss_passiv[3]) + int(egg_skeleton_king_passiv[1]) + int(egg_skeleton_king_passiv[3]) + int(egg_desert_goliath_passiv[1]) + int(egg_desert_goliath_passiv[3]) + int(egg_ice_demon_passiv[1]) + int(egg_ice_demon_passiv[3]) + int(egg_fireworm_queen_passiv[3]) + int(egg_sinister_touch_passiv[1]) + int(egg_infernal_demon_passiv[3]) + int(egg_scythe_pharoah_passiv[3])
		egg_var_passiv_enhanced_equipment = int(egg_crimson_witch_passiv[3]) + int(egg_queen_bee_passiv[3]) + int(egg_ice_worm_passiv[1]) + int(egg_ice_worm_passiv[3]) + int(egg_giant_owl_passiv[1]) + int(egg_giant_owl_passiv[3]) + int(egg_infernal_demon_passiv[1]) + int(egg_sinister_touch_passiv[3])
		cumul_var_passiv_power_up_hero = (float(relics_stats.get('hero_base_stats_increased_var',0.0)) + float(medal_stats['hero_base_enhanced']) + float(talent_stats_dict['talents_hero_power_up']) + float(egg_var_passiv_heros_power_up) + float(altar_heros_ascension_heros_base))/100
		cumul_var_passiv_enhanced_equipment = (float(runelineRecovery.get('var_enhanced_eqpm',0.0)) + float(relics_stats.get('enhance_eqpm_var',0.0)) + float(medal_stats['enhance_equipment']) + float(talent_stats_dict['talents_enhanced_equipment']) + float(egg_var_passiv_enhanced_equipment) + float(altar_stuff_ascension_equipment_base))/100+1

		## Get Stuff Stats
		stuff_activ_stats = stuff_table_stats.getStuffStats(cumul_var_passiv_enhanced_equipment,refine_weapon_enhanced_equipment,refine_armor_enhanced_equipment,refine_ring1_enhanced_equipment,refine_ring2_enhanced_equipment,refine_bracelet_enhanced_equipment,refine_locket_enhanced_equipment,refine_book_enhanced_equipment,weapon_skin_stats,relics_stats.get("ring_basic_stats_var",0.0))
		data = {
			"altar_stuff_ascension_atk":altar_stuff_ascension_atk,
			"altar_stuff_ascension_hp":altar_stuff_ascension_hp,
			"altar_stuff_ascension_equipment_base":altar_stuff_ascension_equipment_base,
			"altar_heros_ascension_atk":altar_heros_ascension_atk,
			"altar_heros_ascension_hp":altar_heros_ascension_hp,
			"altar_heros_ascension_heros_base":altar_heros_ascension_heros_base,
			"altar_heros_ascension_dmg_elite":altar_heros_ascension_dmg_elite,
			"altar_stuff_atk":altar_stuff_atk,
			"altar_stuff_hp":altar_stuff_hp,
			"altar_hero_atk":altar_hero_atk,
			"altar_hero_hp":altar_hero_hp,
			"talent_stats_dict":talent_stats_dict,
			"relics_stats":relics_stats,
			"brave_privileges_stats":brave_privileges_stats,
			"BonusSpe_jewel_weapon":BonusSpe_jewel_weapon,
			"BonusSpe_jewel_armor":BonusSpe_jewel_armor,
			"BonusSpe_jewel_ring1":BonusSpe_jewel_ring1,
			"BonusSpe_jewel_ring2":BonusSpe_jewel_ring2,
			"BonusSpe_jewel_bracelet":BonusSpe_jewel_bracelet,
			"BonusSpe_jewel_locket":BonusSpe_jewel_locket,
			"BonusSpe_jewel_book":BonusSpe_jewel_book,
			"relics_dragon_base_stats":relics_dragon_base_stats,
			"dragon_stats_dict":dragon_stats_dict,
			"dragons_skills":dragons_skills,
			"activ_egg_stats":activ_egg_stats,
			"weapon_skin_stats":weapon_skin_stats,
			"weapon_dmg_multiplier":weapon_dmg_multiplier,
			"medal_stats":medal_stats,
			"stats_jewel_dict":stats_jewel_dict,
			"egg_var_passiv_heros_power_up":egg_var_passiv_heros_power_up,
			"egg_var_passiv_enhanced_equipment":egg_var_passiv_enhanced_equipment,
			"cumul_var_passiv_power_up_hero":cumul_var_passiv_power_up_hero,
			"cumul_var_passiv_enhanced_equipment":cumul_var_passiv_enhanced_equipment,
			"stuff_activ_stats":stuff_activ_stats,
		}
		return JsonResponse(data, safe=False)
	else:
		return HttpResponseRedirect("/")