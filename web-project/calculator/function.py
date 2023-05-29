from PIL import Image
from pathlib import Path
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from const import ADMIN_LOG_WEBHOOK_URL,WEBHOOK_URL, DEV_MODE, DISCORD_CLIENT_ID, DISCORD_CLIENT_SECRET, c_hostname, DISCORD_NOTIF_ROLE_ID, ADMIN_CREDENTIAL
import random as random
from .models import Token, ServerManagement, Contributor, user
from difflib import SequenceMatcher
from django.contrib import messages
from discord_webhook import DiscordWebhook, DiscordEmbed
# :param url: your discord webhook url (type: str)
# :keyword id: webhook id (type: str)
# :keyword content: the message contents (type: str)
# :keyword username: override the default username of the webhook
# :keyword avatar_url: override the default avatar of the webhook
# :keyword tts: true if this is a TTS message
# :keyword file: to apply file(s) with message
# :keyword filename: apply custom file name on attached file content(s)
# :keyword embeds: list of embedded rich content
# :keyword allowed_mentions: allowed mentions for the message
import json, string, time, re, urllib.parse, string, datetime, requests, os, http.cookies

APP_VERSION = os.environ.get('APP_VERSION')
# docker-compose up -d --env-file=myenvfile.env

def makeLog(request):
	dict_log = {
		"dateLog": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
		"container": "archero",
		"app": APP_VERSION,
		"url": {
			"request method":request.method,
			"request path": request.build_absolute_uri(),
		},
		"header": {
			"Host": f"{request.headers['Host']}",
			"User-Agent": f"{request.headers['User-Agent']}",
			"Cookie": f"{request.COOKIES}",
			"AUTH":f"{request.user}: {request.user.is_authenticated}",
		}
	}
	json_log = json.dumps(dict_log, indent=1)
	if not DEV_MODE:
		print(json_log)

def remove_same_int(string):
	result = ''.join(sorted(set(string),key=string.index))
	return result

def transform_token_id(initial_token):
	token_result = ''
	for i in str(initial_token):
		all_string = string.ascii_uppercase + string.ascii_lowercase
		str_int_shuffle = i.join(random.choice(all_string) for y in range(12))
		str_token_order = remove_same_int(str_int_shuffle)
		str_token = list(str_token_order)
		random.shuffle(str_token)
		result_first_string = ''.join(str_token)
		token_result += result_first_string
	return token_result

def chemin(type,name,rarity):
	if name=="none":
		return Path(f"calculator/static/image/{type}/none_common.png")
	chemin =  Path(f"calculator/static/image/{type}/{name}_{rarity}.png")
	return chemin

def resize(img:Image.Image):
	if img.size == (1,1):
		return img
	return img.resize((228,228))

def resize_book(img):
	if img.size == (1,1):
		return img
	return img.resize((250,250))


def all_formIsValid(valid_User, valid_StuffTable, valid_HeroTable, valid_TalentTable, valid_SkinTable, valid_AltarTable, valid_JewelTypeTable, valid_JewelLevelTable, valid_EggTable, valid_EggEquippedTable, valid_DragonTable, valid_RunesTable, valid_ReforgeTable, valid_RefineTable, valid_MedalTable, valid_RelicTable, valid_WeaponSkinTable):
	if valid_User and valid_StuffTable and valid_HeroTable and valid_TalentTable and valid_SkinTable and valid_AltarTable and valid_JewelTypeTable and valid_JewelLevelTable and valid_EggTable and valid_EggEquippedTable and valid_DragonTable and valid_RunesTable and valid_ReforgeTable and valid_RefineTable and valid_MedalTable and valid_RelicTable and valid_WeaponSkinTable:
		return True
	else:
		return False

def findFormError(valid_User, valid_StuffTable, valid_HeroTable, valid_TalentTable, valid_SkinTable, valid_AltarTable, valid_JewelTypeTable, valid_JewelLevelTable, valid_EggTable, valid_EggEquippedTable, valid_DragonTable, valid_RunesTable, valid_ReforgeTable, valid_RefineTable, valid_MedalTable, valid_RelicTable, valid_SkinWeaponTable):
	listform = [valid_User, valid_StuffTable, valid_HeroTable, valid_TalentTable, valid_SkinTable, valid_AltarTable, valid_JewelTypeTable, valid_JewelLevelTable, valid_EggTable, valid_EggEquippedTable, valid_DragonTable, valid_RunesTable, valid_ReforgeTable, valid_RefineTable,valid_MedalTable,valid_RelicTable,valid_SkinWeaponTable]
	for i in listform:
		if i != "":
			form_error = i.errors.items()
			for k,v in form_error:
				return k,v
		else:
			return


################################# FONCTION RESTE #######################################################

def checkCookie(cookie_value:dict) -> dict:
	requestCookie = cookie_value.copy()
	result = {}
	for k,v in requestCookie.items():
		if checkUsernameCredentials(k,v)["access"]:
			result[k] = v
			if len(result) >= 2:
				cookie_value.pop(k,v)
	if len(result) != 0:
		result = {list(result.keys())[0]: list(result.values())[0]}
	return result


def checkTokenValidity(token, length):
	if len(token) != length:
		return False
	for c in token:
		if c not in string.ascii_letters and not c.isdigit():
			return False
	try:
		Token.objects.get(key=token)
	except Token.DoesNotExist:
		return False
	return True


def db_maintenance(func):
	def wrapper(request, *args, **kwargs):
		try:
			server_instance = ServerManagement.objects.get(pk=1)
			isMaintenance = server_instance.isMaintenance
		except ServerManagement.DoesNotExist:
			isMaintenance = True
			## si ça n'existe pas alors on affiche database maintenance car cela veut dire que soit la db n'est pas crée
			#  (lors d'une monté de version) soit que j'ai pas recrée l'instance ServerManagement
		if isMaintenance:
			with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
				local_data = json.load(f)
			SidebarContent = local_data['SidebarContent']
			if "modeDisplay" in list(request.COOKIES):
				darkmode = "yes"
			else:
				darkmode = "no"
			return render(request, "base/maintenance.html", {"darkmode": darkmode,"header_msg": "Database Maintenance","sidebarContent":SidebarContent})
		else:
			return func(request, *args, **kwargs)
	return wrapper


def checkMessages(func):
    def wrapper(request, *args, **kwargs):
        message_types = ['error_message', 'info_message', 'success_message']
        for message_type in message_types:
            message = request.session.pop(message_type, None)
            if message:
                message_function = getattr(messages, message_type.split('_')[0])
                message_function(request, message)
        return func(request, *args, **kwargs)
    return wrapper

def login_required(func):
	def wrapper(request, *args, **kwargs):
		result = checkCookie(request.COOKIES)
		if len(result) == 0:
			if "visitor" in list(request.COOKIES.keys()):
				request.session['user_credential'] = {"visitor":"0-000000"}
				return func(request, *args, **kwargs)
			messages.warning(request, f"You need to login first")
			return HttpResponseRedirect('/login')
		request.session['user_credential'] = result
		return func(request, *args, **kwargs)
	return wrapper


def editor_login(func):
	def wrapper(request, *args, **kwargs):
		REDIRECT_URI = f"http://{request.META['HTTP_HOST']}/data/"
		if request.user.is_authenticated:
			try:
				token = Token.objects.get(user=request.user)
				if checkTokenValidity(token.key,40):
					status = "authorized"
					if 'access_token' in request.session:
						access_token = request.session['access_token']
						headers = {'Authorization': f'Bearer {access_token}'}
						response = requests.get(f'https://discord.com/api/users/@me', headers=headers)
						response_data = response.json()
					elif 'code' in request.GET:
						code = request.GET.get('code')
						data = {
							'client_id': DISCORD_CLIENT_ID,
							'client_secret': DISCORD_CLIENT_SECRET,
							'grant_type': 'authorization_code',
							'code': code,
							'redirect_uri': REDIRECT_URI,
							'scope': 'identify',
						}
						headers = {'Content-Type': 'application/x-www-form-urlencoded'}
						response = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
						response_data = response.json()
						request.session['access_token'] = response_data['access_token']
					else:
						params = {
							'client_id': DISCORD_CLIENT_ID,
							'redirect_uri': REDIRECT_URI,
							'response_type': 'code',
							'scope': 'identify',
						}
						authorize_url = 'https://discord.com/api/oauth2/authorize?' + urlencode(params)
						return redirect(authorize_url)
					headers = {'Authorization': f'Bearer {access_token}'}
					response = requests.get('https://discord.com/api/users/@me', headers=headers)
					response_data = response.json()
					token.discord_acc_rely = f"{response_data['username']}#{response_data['discriminator']}"
					token.discord_user_id = response_data['id']
					token.save()
					request.session['response_data'] = response_data
				else:
					status = "not_auth"
			except Token.DoesNotExist:
				status = "not_auth"
		else:
			status = "not_auth"
		request.session['status'] = status
		return func(request, *args, **kwargs)
	return wrapper


def userExist(json, user):
	liste_username = []
	for i in list(json['user']):
		liste_username.append(i['username'])
	if str(user).lower() in liste_username:
		return False
	else:
		return True

def requestJson(request,cookie):
	if not DEV_MODE:
		with open('calculator/static/json/requetes.json', "r") as jsonFile:
			request_json_file = json.load(jsonFile)
		try:
			username = list(cookie)[0]
			username_id = request.COOKIES[username]
		except (IndexError, KeyError) as e:
			username = 'unknown'
			username_id = "9-999999"
		bool_func = userExist(request_json_file, username)
		if bool_func == True:
			data = {
				"username":username.lower(),
				"ingame_id":username_id,
				"number_request":1
			}
			request_json_file['user'].append(data)
		elif bool_func == False:
			for i in request_json_file['user']:
				if i['username'] == username:
					i['number_request'] += 1
		with open('calculator/static/json/requetes.json', "w") as jsonFile:
			json.dump(request_json_file, jsonFile)


def clearFile(f):
	data_init = {"user": []}
	json.dump(data_init, f)
	f.close()


def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()


def create_unique_id():
	unique_id = str(time.time()).replace('.','')
	return unique_id


def checkUsernameCredentials(username_raw,id_raw) -> dict:
	pattern = re.compile(r'^\d{1}-\d{6,12}$')    # Compile un motif de regex pour les identifiants de jeu valides
	decoded_bytes = urllib.parse.unquote(username_raw).encode('utf-8') # Décode le nom d'utilisateur brut en octets et encode la chaîne de caractères décodée en octets
	ingame_name = decoded_bytes.decode('utf-8') # Remplace tous les caractères illégaux par "*" après avoir converti la chaîne de bytes en une chaîne de caractères en utf-8
	ingame_id = urllib.parse.unquote(id_raw)   # Décode l'identifiant de jeu brut
	unavailable_username = ['csrftoken','sessionid','windowInnerWidth','windowInnerHeight', 'modeDisplay', 'messages']
	for k,v in ADMIN_CREDENTIAL.items():
		if ingame_id == v and ingame_name.lower() == k:
			return {"access":True,"ingame_name": ingame_name.replace(' ',''),"ingame_id": ingame_id,"admin_log":True}
	if ingame_id != "0-000000" and ingame_name != "visitor":
		if 3 <= len(ingame_name) < 20 and ingame_name not in unavailable_username:
			if re.fullmatch(pattern, ingame_id) and ingame_id != "" and ingame_id != None and all(c.isdigit() or c == '-' for c in ingame_id):
				return {"access":True,"ingame_name": ingame_name.replace(' ',''),"ingame_id": ingame_id}
			else:
				return {"access":False,"ingame_name": ingame_name,"ingame_id": ingame_id,"error_message": "Ingame id incorrect"}
		else:
			return {"access":False,"ingame_name": ingame_name,"ingame_id": ingame_id,"error_message": "Username not allowed"}
	elif ingame_id == "0-000000":
		return {"access":False,"ingame_name": ingame_name,"ingame_id": ingame_id,"error_message": "Ingame Id not allowed"}


def checkIllegalKey(string:str):
	for i in string:
		try:
			cookies = http.cookies.SimpleCookie()
			cookies[str(i)] = 'check'  # Cette ligne provoque une CookieError
		except http.cookies.CookieError:
			return i
	return string

def send_webhook(msg, **kwargs):
	if kwargs.get("admin_log",False) != False:
		wh = DiscordWebhook(url=ADMIN_LOG_WEBHOOK_URL, content=msg, rate_limit_retry=True)
	else:
		wh = DiscordWebhook(url=WEBHOOK_URL, content=msg, rate_limit_retry=True)
	wh.execute()

def send_embed(author_name:str,title_embed:str,description_embed:str,field_name:str,field_value:str,e_color:int, request, alert:bool, **kwargs):
	if alert:
		content_msg = f"<@&{DISCORD_NOTIF_ROLE_ID}>"
	else:
		content_msg = ""
	avatar_url = kwargs.get('avatar_url',f"{c_hostname}/static/image/favicon.png")
	browser = request.META.get('HTTP_USER_AGENT',"None")
	if kwargs.get("admin_log") != None:
		webhook = DiscordWebhook(url=ADMIN_LOG_WEBHOOK_URL, content=content_msg, rate_limit_retry=True)
	else:
		webhook = DiscordWebhook(url=WEBHOOK_URL, content=content_msg, rate_limit_retry=True)
	embed = DiscordEmbed(title=str(title_embed), description=f"{str(description_embed)}", color=e_color)
	embed.set_author(
		name=str(author_name),
		icon_url=str(avatar_url),
	)
	embed.add_embed_field(name=str(field_name), value=str(field_value), inline=False)
	embed.add_embed_field(name="", value=browser, inline=True)
	embed.set_footer(text=f'{request.COOKIES}', icon_url='')
	webhook.add_embed(embed)
	webhook.execute()


def checkTheme_Request(request, cookie_result):
	makeLog(request)
	requestJson(request,cookie_result)
	if "modeDisplay" in list(request.COOKIES):
		return "yes"
	else:
		return "no"	

def calculatePrice(lvl1, lvl2, type, rank=None):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	if type == "talents":
		talent_cost_gold = local_data["DataPrice"]['talent']['gold']
		return talent_cost_gold[lvl2] - talent_cost_gold[lvl1]
	elif type == "items":
		item_cost_gold = local_data["DataPrice"]['item']['gold']
		item_cost_scroll = local_data["DataPrice"]['item']['scroll']
		return [item_cost_gold[lvl2] - item_cost_gold[lvl1], item_cost_scroll[lvl2] - item_cost_scroll[lvl1]]
	elif type == "heroes":
		heros_cost_gold = local_data["DataPrice"]['hero']['gold']
		heros_cost_sapphire = local_data["DataPrice"]['hero']['sapphire']
		return [heros_cost_gold[lvl2] - heros_cost_gold[lvl1], heros_cost_sapphire[lvl2] - heros_cost_sapphire[lvl1]]
	elif type == "dragons":
		dragon_cost_gold = local_data["DataPrice"]['dragon']['gold']
		dragon_cost_magestone = local_data["DataPrice"]['dragon']['magestone']
		result = [dragon_cost_gold[lvl2] - dragon_cost_gold[lvl1], dragon_cost_magestone[lvl2] - dragon_cost_magestone[lvl1]]
		if rank == "A":
			return [result[0],result[1]]
		elif rank == "S":
			return [int(result[0])*1.5,int(result[1])*1.5]
		elif rank == "SS":
			return [int(result[0])*2,int(result[1])*2]
	elif type == "relics":
		relics_cost_gold = local_data["DataPrice"]['relics']['gold']
		relics_cost_starlight = local_data["DataPrice"]['relics']['starlight']
		result = [relics_cost_gold[lvl2] - relics_cost_gold[lvl1], relics_cost_starlight[lvl2] - relics_cost_starlight[lvl1]]
		if rank == "A":
			return [result[0],result[1]]
		elif rank == "S":
			return [int(result[0])*1.5,int(result[1])*1.5]
		elif rank == "SS":
			return [int(result[0])*2,int(result[1])*2]

def makeCookieheader(cookieResult: dict) -> str:
	result = ""
	if cookieResult.get("visitor") is None:
		result = " - ".join([key + " | " + value for key, value in cookieResult.items()])
	return result


def checkContributor(cookie_result:dict) -> bool:
	username = list(dict(cookie_result).keys())[0]
	ingame_id = cookie_result[username]
	if Contributor.objects.filter(label=f"{username}|{ingame_id}").exists():
		return True
	else:
		return False

def getProfileWithCookie(ingame_id: str, ingame_name: str, **kwargs) -> tuple[bool, user|None]:
	try:
		pbid = kwargs.get("public_id",None)
		if pbid != None:
			user_profile = user.objects.get(ingame_id=ingame_id, public_id=pbid)
		else:
			user_profile = user.objects.get(ingame_id=ingame_id)
	except user.DoesNotExist:
		return False, None
	resultSimilarity = similar(user_profile.ingame_name.lower(), ingame_name.lower())
	if resultSimilarity >= 1 or resultSimilarity >= 0.7:
		if 0.7 <= resultSimilarity <= 0.99:
			send_webhook(f"{ingame_name.lower()} accessed {user_profile.ingame_name.lower()}'s Profile and the similarity is {resultSimilarity}\n[Admin Panel Link User]({c_hostname}/luhcaran/calculator/user/{user_profile.pk}/change/)")
		return True, user_profile
	else:
		return False, user_profile