from .data import *
from .forms import *
from .function import *
from .models import *
from . import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from math import *
from urllib.request import urlopen
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import os
import sys
import traceback

app_version = os.environ.get('APP_VERSION')
lang = ["English","Francais","Deutsch","Russian","Española"]

def menu(request):
	cookie_keys = checkDarkMode(request.COOKIES)
	if "modeDisplay" in list(cookie_keys):
		darkmode = "yes"
	else:
		darkmode = "no"
	dict_log_menu = {
		"ingame_id_user":"",
		"ingame_name_user":"",
		"missing_data":"",
		"stats_submit":"",
		"cookie_value_pop":"",
		"error_form_msg":"",
		"index_ingame_id_cookie":"",
	}
	makeLog(request,dict_log_menu)
	requestJson(request)
	return render(request, 'menu.html', {"darkmode": darkmode, "header_msg": "Menu Archero Wiki", 'lang':lang})

def maze(request):
	cookie_keys = checkDarkMode(request.COOKIES)
	if "modeDisplay" in list(cookie_keys):
		darkmode = "yes"
	else:
		darkmode = "no"
	dict_log_maze = {
		"ingame_id_user":"",
		"ingame_name_user":"",
		"missing_data":"",
		"stats_submit":"",
		"cookie_value_pop":"",
		"error_form_msg":"",
		"index_ingame_id_cookie":"",
	}
	makeLog(request,dict_log_maze)
	with urlopen("https://config-archero.habby.mobi/data/config/MazeConfig.json") as url:
		data_json = json.load(url)
	requestJson(request)
	return render(request, 'wiki/get_maze.html', {"data_json":data_json, "darkmode": darkmode, "header_msg": "maze","lang":lang})


def csrf_failure(request, reason=""):
	dict_log_csrf_failure = {
		"ingame_id_user":"",
		"ingame_name_user":"",
		"missing_data":"",
		"stats_submit":"",
		"cookie_value_pop":"",
		"error_form_msg":"",
		"index_ingame_id_cookie":"",
	}
	makeLog(request,dict_log_csrf_failure)
	cookie_keys = checkDarkMode(request.COOKIES)
	if "modeDisplay" in list(cookie_keys):
		darkmode = "yes"
	else:
		darkmode = "no"
	return render(request,'base/csrf_failure.html', {"darkmode": darkmode, "header_msg": "CSRF FAILURE","lang":lang})


def login(request):
	dict_log_login = {
		"ingame_id_user":"",
		"ingame_name_user":"",
		"missing_data":"",
		"stats_submit":"",
		"cookie_value_pop":"",
		"error_form_msg":"",
		"index_ingame_id_cookie":"",
	}
	makeLog(request,dict_log_login)
	cookie_value = checkCookie(request.COOKIES)
	requestJson(request)
	if len(cookie_value) >= 1 and "visitor" not in list(cookie_value.keys()):
		return HttpResponseRedirect("/")
	else:
		return render(request, "login.html")

def wiki_theorycrafting(request):
	cookie_keys = checkDarkMode(request.COOKIES)
	if "modeDisplay" in list(cookie_keys):
		darkmode = "yes"
	else:
		darkmode = "no"
	requestJson(request)
	return render(request, "wiki/theorycraft.html", {"darkmode": darkmode, "header_msg": "TheoryCrafting","lang":lang})

def item_description(request):
	cookie_keys = checkDarkMode(request.COOKIES)
	if "modeDisplay" in list(cookie_keys):
		darkmode = "yes"
	else:
		darkmode = "no"
	requestJson(request)
	return render(request, "wiki/item_description.html", {"darkmode": darkmode, "header_msg": "Item Description","lang":lang})

def skill_description(request):
	cookie_keys = checkDarkMode(request.COOKIES)
	if "modeDisplay" in list(cookie_keys):
		darkmode = "yes"
	else:
		darkmode = "no"
	requestJson(request)
	return render(request, "wiki/skill_description.html", {"darkmode": darkmode, "header_msg": "Skill Description","lang":lang})

def heros_description(request):
	cookie_keys = checkDarkMode(request.COOKIES)
	if "modeDisplay" in list(cookie_keys):
		darkmode = "yes"
	else:
		darkmode = "no"
	requestJson(request)
	return render(request, "wiki/heros_description.html", {"darkmode": darkmode, "header_msg": "Heros Description","lang":lang})

def damage(request):
	cookie_keys = checkDarkMode(request.COOKIES)
	if "modeDisplay" in list(cookie_keys):
		darkmode = "yes"
	else:
		darkmode = "no"
	cookie_value = checkCookie(request.COOKIES)
	try:
		ingame_id_cookie = list(cookie_value.values())[0]
		ingame_name_cookie = list(cookie_value.keys())[0]
		user_stats = ""
		if ingame_id_cookie == "0-000000" and ingame_name_cookie == "visitor":
			selfHasProfil = "no"
		else:
			user_stats = models.user.objects.get(ingame_id=ingame_id_cookie)	
			selfHasProfil = "yes"
	except:
		user_stats = ""
		selfHasProfil = "no"
	return render(request, "wiki/damage.html", {"darkmode": darkmode, "header_msg": "Damage Help","selfHasProfil":selfHasProfil,"selfStats":user_stats,"lang":lang})


def dmgCalc_processing(request,iid):
	iid_modified1 = ''.join(i for i in str(iid) if i.isdigit())
	iid_modified = iid_modified1[0] + "-" + iid_modified1[1:-1] + iid_modified1[-1]
	user_stats = models.user.objects.get(ingame_id=iid_modified)
	stuff_table_stats = models.stuff_table.objects.get(ingame_id=iid_modified)
	hero_table_stats = models.hero_table.objects.get(ingame_id=iid_modified)
	talent_table_stats = models.talent_table.objects.get(ingame_id=iid_modified)
	skin_table_stats = models.skin_table.objects.get(ingame_id=iid_modified)
	altar_table_stats = models.altar_table.objects.get(ingame_id=iid_modified)
	jewel_type_table_stats = models.jewel_type_table.objects.get(ingame_id=iid_modified)
	jewel_level_table_stats = models.jewel_level_table.objects.get(ingame_id=iid_modified)
	egg_table_stats = models.egg_table.objects.get(ingame_id=iid_modified)
	egg_equipped_table_stats = models.egg_equipped_table.objects.get(ingame_id=iid_modified)
	dragon_table_stats = models.dragon_table.objects.get(ingame_id=iid_modified)
	runes_table_stats = models.runes_table.objects.get(ingame_id=iid_modified)
	reforge_table_stats = models.reforge_table.objects.get(ingame_id=iid_modified)
	refine_table_stats = models.refine_table.objects.get(ingame_id=iid_modified)

	weapon_name_choosen = stuff_table_stats.weapon_choosen
	weapon_rarity_choosen = stuff_table_stats.weapon_rarity
	weapon_level_choosen = stuff_table_stats.weapon_level #ça ressort le nom de l'arme choisie
	armor_name_choosen = stuff_table_stats.armor_choosen
	armor_rarity_choosen = stuff_table_stats.armor_rarity
	armor_level_choosen = stuff_table_stats.armor_level
	ring1_name_choosen = stuff_table_stats.ring1_choosen
	ring1_rarity_choosen = stuff_table_stats.ring1_rarity
	ring1_level_choosen = stuff_table_stats.ring1_level
	ring2_name_choosen = stuff_table_stats.ring2_choosen
	ring2_rarity_choosen = stuff_table_stats.ring2_rarity
	ring2_level_choosen = stuff_table_stats.ring2_level
	pet1_name_choosen = stuff_table_stats.pet1_choosen
	pet1_rarity_choosen = stuff_table_stats.pet1_rarity
	pet1_level_choosen = stuff_table_stats.pet1_level
	pet2_name_choosen = stuff_table_stats.pet2_choosen
	pet2_rarity_choosen = stuff_table_stats.pet2_rarity
	pet2_level_choosen = stuff_table_stats.pet2_level
	bracelet_name_choosen = stuff_table_stats.bracelet_choosen
	bracelet_rarity_choosen = stuff_table_stats.bracelet_rarity
	bracelet_level_choosen = stuff_table_stats.bracelet_level
	locket_name_choosen = stuff_table_stats.locket_choosen
	locket_rarity_choosen = stuff_table_stats.locket_rarity
	locket_level_choosen = stuff_table_stats.locket_level
	book_name_choosen = stuff_table_stats.book_choosen.replace("'","")
	book_rarity_choosen = stuff_table_stats.book_rarity
	book_level_choosen = stuff_table_stats.book_level

	strength_level = talent_table_stats.strength_level
	power_level = talent_table_stats.power_level
	recover_level = talent_table_stats.recover_level
	block_level = talent_table_stats.block_level
	iron_bulwark_level = talent_table_stats.iron_bulwark_level
	enhanced_equipment_level = talent_table_stats.enhanced_equipment_level
	hero_power_up_level = talent_table_stats.hero_power_up_level

	choosen_hero = user_stats.choosen_hero
	atk_base_stats_hero_choosen = user_stats.atk_base_stats_hero_choosen
	health_base_stats_hero_choosen = user_stats.health_base_stats_hero_choosen

	stuff_altar_level = altar_table_stats.stuff_altar_level
	stuff_altar_ascension = altar_table_stats.stuff_altar_ascension
	heros_altar_level = altar_table_stats.heros_altar_level
	heros_altar_ascension = altar_table_stats.heros_altar_ascension

	atk_given_from_skin = skin_table_stats.skin_attack
	hp_given_from_skin = skin_table_stats.skin_health

	atreus_level = hero_table_stats.atreus_level
	atreus_star = hero_table_stats.atreus_star
	urasil_level = hero_table_stats.urasil_level
	urasil_star = hero_table_stats.urasil_star
	phoren_level = hero_table_stats.phoren_level
	phoren_star = hero_table_stats.phoren_star
	taranis_level = hero_table_stats.taranis_level
	taranis_star = hero_table_stats.taranis_star
	helix_level = hero_table_stats.helix_level
	helix_star = hero_table_stats.helix_star 
	meowgik_level = hero_table_stats.meowgik_level
	meowgik_star = hero_table_stats.meowgik_star
	shari_level = hero_table_stats.shari_level
	shari_star = hero_table_stats.shari_star
	ayana_level = hero_table_stats.ayana_level
	ayana_star = hero_table_stats.ayana_star
	onir_level = hero_table_stats.onir_level
	onir_star = hero_table_stats.onir_star 
	rolla_level = hero_table_stats.rolla_level
	rolla_star = hero_table_stats.rolla_star
	bonnie_level = hero_table_stats.bonnie_level
	bonnie_star = hero_table_stats.bonnie_star
	sylvan_level = hero_table_stats.sylvan_level
	sylvan_star = hero_table_stats.sylvan_star
	shade_level = hero_table_stats.shade_level
	shade_star = hero_table_stats.shade_star 
	ophelia_level = hero_table_stats.ophelia_level
	ophelia_star = hero_table_stats.ophelia_star
	ryan_level = hero_table_stats.ryan_level
	ryan_star = hero_table_stats.ryan_star
	lina_level = hero_table_stats.lina_level
	lina_star = hero_table_stats.lina_star
	aquea_level = hero_table_stats.aquea_level
	aquea_star = hero_table_stats.aquea_star
	shingen_level = hero_table_stats.shingen_level
	shingen_star = hero_table_stats.shingen_star 
	gugu_level = hero_table_stats.gugu_level
	gugu_star = hero_table_stats.gugu_star
	iris_level = hero_table_stats.iris_level
	iris_star = hero_table_stats.iris_star
	blazo_level = hero_table_stats.blazo_level
	blazo_star = hero_table_stats.blazo_star
	melinda_level = hero_table_stats.melinda_level
	melinda_star = hero_table_stats.melinda_star
	elaine_level = hero_table_stats.elaine_level
	elaine_star = hero_table_stats.elaine_star
	
	weapon_jewel1 = str(jewel_type_table_stats.weapon_jewel1_type) + "_" + str(jewel_level_table_stats.weapon_jewel1_level)
	weapon_jewel2 = str(jewel_type_table_stats.weapon_jewel2_type) + "_" + str(jewel_level_table_stats.weapon_jewel2_level)
	weapon_jewel3 = str(jewel_type_table_stats.weapon_jewel3_type) + "_" + str(jewel_level_table_stats.weapon_jewel3_level)
	weapon_jewel4 = str(jewel_type_table_stats.weapon_jewel4_type) + "_" + str(jewel_level_table_stats.weapon_jewel4_level)
	armor_jewel1 = str(jewel_type_table_stats.armor_jewel1_type) + "_" + str(jewel_level_table_stats.armor_jewel1_level)
	armor_jewel2 = str(jewel_type_table_stats.armor_jewel2_type) + "_" + str(jewel_level_table_stats.armor_jewel2_level)
	armor_jewel3 = str(jewel_type_table_stats.armor_jewel3_type) + "_" + str(jewel_level_table_stats.armor_jewel3_level)
	armor_jewel4 = str(jewel_type_table_stats.armor_jewel4_type) + "_" + str(jewel_level_table_stats.armor_jewel4_level)
	ring1_jewel1 = str(jewel_type_table_stats.ring1_jewel1_type) + "_" + str(jewel_level_table_stats.ring1_jewel1_level)
	ring1_jewel2 = str(jewel_type_table_stats.ring1_jewel2_type) + "_" + str(jewel_level_table_stats.ring1_jewel2_level)
	ring1_jewel3 = str(jewel_type_table_stats.ring1_jewel3_type) + "_" + str(jewel_level_table_stats.ring1_jewel3_level)
	ring1_jewel4 = str(jewel_type_table_stats.ring1_jewel4_type)  + "_" + str(jewel_level_table_stats.ring1_jewel4_level)
	ring2_jewel1 = str(jewel_type_table_stats.ring2_jewel1_type) + "_" + str(jewel_level_table_stats.ring2_jewel1_level)
	ring2_jewel2 = str(jewel_type_table_stats.ring2_jewel2_type) + "_" + str(jewel_level_table_stats.ring2_jewel2_level)
	ring2_jewel3 = str(jewel_type_table_stats.ring2_jewel3_type) + "_" + str(jewel_level_table_stats.ring2_jewel3_level)
	ring2_jewel4 = str(jewel_type_table_stats.ring2_jewel4_type)  + "_" + str(jewel_level_table_stats.ring2_jewel4_level)
	pet1_jewel1 = str(jewel_type_table_stats.pet1_jewel1_type) + "_" + str(jewel_level_table_stats.pet1_jewel1_level)
	pet1_jewel2 = str(jewel_type_table_stats.pet1_jewel2_type) + "_" + str(jewel_level_table_stats.pet1_jewel2_level)
	pet1_jewel3 = str(jewel_type_table_stats.pet1_jewel3_type) + "_" + str(jewel_level_table_stats.pet1_jewel3_level)
	pet1_jewel4 = str(jewel_type_table_stats.pet1_jewel4_type) + "_" + str(jewel_level_table_stats.pet1_jewel4_level)
	pet2_jewel1 = str(jewel_type_table_stats.pet2_jewel1_type) + "_" + str(jewel_level_table_stats.pet2_jewel1_level)
	pet2_jewel2 = str(jewel_type_table_stats.pet2_jewel2_type) + "_" + str(jewel_level_table_stats.pet2_jewel2_level)
	pet2_jewel3 = str(jewel_type_table_stats.pet2_jewel3_type) + "_" + str(jewel_level_table_stats.pet2_jewel3_level)
	pet2_jewel4 = str(jewel_type_table_stats.pet2_jewel4_type) + "_" + str(jewel_level_table_stats.pet2_jewel4_level)
	bracelet_jewel1 = str(jewel_type_table_stats.bracelet_jewel1_type) + "_" + str(jewel_level_table_stats.bracelet_jewel1_level)
	bracelet_jewel2 = str(jewel_type_table_stats.bracelet_jewel2_type) + "_" + str(jewel_level_table_stats.bracelet_jewel2_level)
	bracelet_jewel3 = str(jewel_type_table_stats.bracelet_jewel3_type) + "_" + str(jewel_level_table_stats.bracelet_jewel3_level)
	bracelet_jewel4 = str(jewel_type_table_stats.bracelet_jewel4_type) + "_" + str(jewel_level_table_stats.bracelet_jewel4_level)
	locket_jewel1 = str(jewel_type_table_stats.locket_jewel1_type) + "_" + str(jewel_level_table_stats.locket_jewel1_level)
	locket_jewel2 = str(jewel_type_table_stats.locket_jewel2_type) + "_" + str(jewel_level_table_stats.locket_jewel2_level)
	locket_jewel3 = str(jewel_type_table_stats.locket_jewel3_type) + "_" + str(jewel_level_table_stats.locket_jewel3_level)
	locket_jewel4 = str(jewel_type_table_stats.locket_jewel4_type) + "_" + str(jewel_level_table_stats.locket_jewel4_level)
	book_jewel1 = str(jewel_type_table_stats.book_jewel1_type) + "_" + str(jewel_level_table_stats.book_jewel1_level)
	book_jewel2 = str(jewel_type_table_stats.book_jewel2_type) + "_" + str(jewel_level_table_stats.book_jewel2_level)
	book_jewel3 = str(jewel_type_table_stats.book_jewel3_type) + "_" + str(jewel_level_table_stats.book_jewel3_level)
	book_jewel4 = str(jewel_type_table_stats.book_jewel4_type) + "_" + str(jewel_level_table_stats.book_jewel4_level)

	power_reforge_stats = reforge_table_stats.reforge_power
	saviour_reforge_stats = reforge_table_stats.reforge_saviour
	recovery_reforge_stats = reforge_table_stats.reforge_recovery
	courage_reforge_stats = reforge_table_stats.reforge_courage
	luck_reforge_stats = reforge_table_stats.reforge_luck
	runes_power_attack_flat = runes_table_stats.power_attack_flat
	runes_power_attack_var = runes_table_stats.power_attack_var
	runes_saviour_hp_flat = runes_table_stats.saviour_hp_flat
	runes_saviour_hp_var = runes_table_stats.saviour_hp_var
	runes_recovery_hp_flat = runes_table_stats.recovery_hp_flat
	runes_courage_attack_flat = runes_table_stats.courage_attack_flat
	runes_courage_attack_var = runes_table_stats.courage_attack_var
	runes_courage_hero_attack_flat = runes_table_stats.selected_hero_courage_attack_flat + "_" + str(runes_table_stats.courage_hero_attack_flat)
	runes_courage_hero_attack_var = runes_table_stats.selected_hero_courage_attack_var + "_" + str(runes_table_stats.courage_hero_attack_var)
	runes_courage_hero_hp_flat = runes_table_stats.selected_hero_courage_hp_flat + "_" + str(runes_table_stats.courage_hero_hp_flat)
	runes_courage_hero_hp_var = runes_table_stats.selected_hero_courage_hp_var + "_" + str(runes_table_stats.courage_hero_hp_var)
	runes_luck_hp_flat  = runes_table_stats.luck_hp_flat 
	runes_luck_hp_var  = runes_table_stats.luck_hp_var 

	dragon1_type = dragon_table_stats.dragon1_type
	dragon2_type = dragon_table_stats.dragon2_type
	dragon3_type = dragon_table_stats.dragon3_type
	dragon1_rarity = dragon_table_stats.dragon1_rarity.replace(" ","_")
	dragon2_rarity = dragon_table_stats.dragon2_rarity.replace(" ","_")
	dragon3_rarity = dragon_table_stats.dragon3_rarity.replace(" ","_")
	dragon1_level = dragon_table_stats.dragon1_level 
	dragon2_level = dragon_table_stats.dragon2_level 
	dragon3_level = dragon_table_stats.dragon3_level
	dragon1_4thboost_level = dragon_table_stats.dragon_1_boost_4_mythic
	dragon2_4thboost_level = dragon_table_stats.dragon_2_boost_4_mythic
	dragon3_4thboost_level = dragon_table_stats.dragon_3_boost_4_mythic

	green_bat_star = egg_table_stats.green_bat.replace("⭐","")
	vase_star = egg_table_stats.vase.replace("⭐","")
	bomb_ghost_star = egg_table_stats.bomb_ghost.replace("⭐","")
	rock_puppet_star = egg_table_stats.rock_puppet.replace("⭐","")
	party_tree_star = egg_table_stats.party_tree.replace("⭐","")
	wolfhound_star = egg_table_stats.wolfhound.replace("⭐","")
	skeleton_archer_star = egg_table_stats.skeleton_archer.replace("⭐","")
	skeleton_soldier_star = egg_table_stats.skeleton_soldier.replace("⭐","")
	wasp_star = egg_table_stats.wasp.replace("⭐","")
	fire_mage_star = egg_table_stats.fire_mage.replace("⭐","")
	medusa_star = egg_table_stats.medusa.replace("⭐","")
	ice_mage_star = egg_table_stats.ice_mage.replace("⭐","")
	fire_lizard_star = egg_table_stats.fire_lizard.replace("⭐","")
	flame_ghost_star = egg_table_stats.flame_ghost.replace("⭐","")
	thorny_snake_star = egg_table_stats.thorny_snake.replace("⭐","")
	tornado_demon_star = egg_table_stats.tornado_demon.replace("⭐","")
	piranha_star = egg_table_stats.piranha.replace("⭐","")
	zombie_star = egg_table_stats.zombie.replace("⭐","")
	scarecrow_star = egg_table_stats.scarecrow.replace("⭐","")
	long_dragon_star = egg_table_stats.long_dragon.replace("⭐","")
	skull_wizard_star = egg_table_stats.skull_wizard.replace("⭐","")
	lava_golem_star = egg_table_stats.lava_golem.replace("⭐","")
	ice_golem_star = egg_table_stats.ice_golem.replace("⭐","")
	cactus_star = egg_table_stats.cactus.replace("⭐","")
	crazy_spider_star = egg_table_stats.crazy_spider.replace("⭐","")
	fire_element_star = egg_table_stats.fire_element.replace("⭐","")
	skeleton_swordsman_star = egg_table_stats.skeleton_swordsman.replace("⭐","")
	scythe_mage_star = egg_table_stats.scythe_mage.replace("⭐","")
	pea_shooter_star = egg_table_stats.pea_shooter.replace("⭐","")
	shadow_assassin_star = egg_table_stats.shadow_assassin.replace("⭐","")
	tornado_mage_star = egg_table_stats.tornado_mage.replace("⭐","")
	spitting_mushroom_star = egg_table_stats.spitting_mushroom.replace("⭐","")
	rolling_mushroom_star = egg_table_stats.rolling_mushroom.replace("⭐","")
	fallen_bat_star = egg_table_stats.fallen_bat.replace("⭐","")
	one_eyed_bat_star = egg_table_stats.one_eyed_bat.replace("⭐","")
	scarlet_mage_star = egg_table_stats.scarlet_mage.replace("⭐","")
	icefire_phantom_star = egg_table_stats.icefire_phantom.replace("⭐","")
	purple_phantom_star = egg_table_stats.purple_phantom.replace("⭐","")
	tundra_dragon_star = egg_table_stats.tundra_dragon.replace("⭐","")
	sandian_star = egg_table_stats.sandian.replace("⭐","")
	nether_puppet_star = egg_table_stats.nether_puppet.replace("⭐","")
	psionic_scarecrow_star = egg_table_stats.psionic_scarecrow.replace("⭐","")
	steel_dryad_star = egg_table_stats.steel_dryad.replace("⭐","")
	savage_spider_star = egg_table_stats.savage_spider.replace("⭐","")
	flaming_bug_star = egg_table_stats.flaming_bug.replace("⭐","")
	elite_archer_star = egg_table_stats.elite_archer.replace("⭐","")
	little_dragon_star = egg_table_stats.little_dragon.replace("⭐","")
	arch_leader_star = egg_table_stats.arch_leader.replace("⭐","")
	skeleton_king_star = egg_table_stats.skeleton_king.replace("⭐","")
	crimson_witch_star = egg_table_stats.crimson_witch.replace("⭐","")
	rage_golem_star = egg_table_stats.rage_golem.replace("⭐","")
	queen_bee_star = egg_table_stats.queen_bee.replace("⭐","")
	ice_worm_star = egg_table_stats.ice_worm.replace("⭐","")
	medusa_boss_star = egg_table_stats.medusa_boss.replace("⭐","")
	ice_demon_star = egg_table_stats.ice_demon.replace("⭐","")
	giant_owl_star = egg_table_stats.giant_owl.replace("⭐","")
	fire_demon_star = egg_table_stats.fire_demon.replace("⭐","")
	krab_boss_star = egg_table_stats.krab_boss.replace("⭐","")
	desert_goliath_star = egg_table_stats.desert_goliath.replace("⭐","")

	selected_egg1 = egg_equipped_table_stats.egg_equipped1.lower().replace(" ","_")
	selected_egg2 = egg_equipped_table_stats.egg_equipped2.lower().replace(" ","_")
	selected_egg3 = egg_equipped_table_stats.egg_equipped3.lower().replace(" ","_")
	selected_egg4 = egg_equipped_table_stats.egg_equipped4.lower().replace(" ","_")
	selected_egg5 = egg_equipped_table_stats.egg_equipped5.lower().replace(" ","_")

	weapon_refine_atk = refine_table_stats.weapon_refine_atk
	weapon_refine_basic_stats = int(refine_table_stats.weapon_refine_basic_stats)/100
	armor_refine_hp = refine_table_stats.armor_refine_hp
	armor_refine_basic_stats = int(refine_table_stats.armor_refine_basic_stats)/100
	ring1_refine_atk = refine_table_stats.ring1_refine_atk
	ring1_refine_basic_stats = int(refine_table_stats.ring1_refine_basic_stats)/100
	ring2_refine_atk = refine_table_stats.ring2_refine_atk
	ring2_refine_basic_stats = int(refine_table_stats.ring2_refine_basic_stats)/100
	bracelet_refine_atk = refine_table_stats.bracelet_refine_atk
	bracelet_refine_basic_stats = int(refine_table_stats.bracelet_refine_basic_stats)/100
	locket_refine_hp = refine_table_stats.locket_refine_hp
	locket_refine_basic_stats = int(refine_table_stats.locket_refine_basic_stats)/100
	book_refine_hp = refine_table_stats.book_refine_hp
	book_refine_basic_stats = int(refine_table_stats.book_refine_basic_stats)/100

	brave_privileges_level = int(user_stats.brave_privileges_level)

################################# FONCTION CALCUL #######################################################
	def HerosStatsRecup(heros,heros_level,heros_star, choosen_hero):
		stats_hero_star  = HerosStats[str(heros).lower() + "_star_" + str(heros_star).replace("⭐","")]
		stats_hero_lvl  = HerosStats[str(heros).lower() + "_" + str(heros_level)]
		if heros != "Shari":
			Blvl20 = stats_hero_lvl[0]
			Blvl60 = stats_hero_lvl[2]
			Blvl120 = stats_hero_lvl[4]
			Bs2 = stats_hero_star[0]
			Bs7 = stats_hero_star[1]
			Bs8 = stats_hero_star[2]
			if heros != choosen_hero:
				Blvl40 = 0
				Blvl80 = 0
			else:
				Blvl40 = stats_hero_lvl[1]
				Blvl80 = stats_hero_lvl[3]
		else:
			Blvl40 = stats_hero_lvl[1]
			Blvl80 = stats_hero_lvl[3]
			Blvl120 = stats_hero_lvl[4]
			Bs2 = stats_hero_star[0]
			Bs7 = stats_hero_star[1]
			Bs8 = stats_hero_star[2]
			if heros != choosen_hero:
				Blvl20 = 0
				Blvl60 = 0
			else:
				Blvl20 = stats_hero_lvl[0]
				Blvl60 = stats_hero_lvl[2]
		return Blvl20, Blvl40, Blvl60, Blvl80, Blvl120, Bs2, Bs7, Bs8

	def JewelStatsRecup(weapon_1,weapon_2,weapon_3,weapon_4,armor_1,armor_2,armor_3,armor_4,ring1_1,ring1_2,ring1_3,ring1_4,ring2_1,ring2_2,ring2_3,ring2_4,pet1_1,pet1_2,pet1_3,pet1_4,pet2_1,pet2_2,pet2_3,pet2_4,bracelet_1,bracelet_2,bracelet_3,bracelet_4,locket_1,locket_2,locket_3,locket_4,book_1,book_2,book_3,book_4):
		list_type = [weapon_1,weapon_2,weapon_3,weapon_4,armor_1,armor_2,armor_3,armor_4,ring1_1,ring1_2,ring1_3,ring1_4,ring2_1,ring2_2,ring2_3,ring2_4,pet1_1,pet1_2,pet1_3,pet1_4,pet2_1,pet2_2,pet2_3,pet2_4,bracelet_1,bracelet_2,bracelet_3,bracelet_4,locket_1,locket_2,locket_3,locket_4,book_1,book_2,book_3,book_4]
		###### BONUS 1 ######
		atk_ruby = 0
		atk_kunzite = 0
		atk_tourmaline = 0
		pv_lapis = 0
		pv_emerald = 0
		proj_res_topaz = 0
		front_res_amber = 0
		collision_res_amethyst = 0
		pv_calaite = 0
		###### BONUS 2 ######
		dmg_to_boss = 0
		dmg_to_mobs = 0
		dmg_to_elite = 0
		red_he_lapis = 0
		drop_pv_emerald = 0
		crit_dmg_topaz = 0
		elementary_dmg_amber = 0
		pm_when_hurt_amethyst = 0
		mp_max_calaite = 0

		for x in list_type:
			a = x.split("_")[0]
			if a == "ruby":
				ruby_b1 = atk_ruby
				ruby_b2 = dmg_to_boss
				atk_ruby = int(JewelStats["ruby_lvl" + str(x.split("_")[1]) + "_bonus1"])
				dmg_to_boss = int(JewelStats["ruby_lvl" + str(x.split("_")[1]) + "_bonus2"])
				atk_ruby += ruby_b1
				dmg_to_boss +=  ruby_b2
			if a == "kunzite":
				kunzite_b1 = atk_kunzite
				kunzite_b2 = dmg_to_mobs
				atk_kunzite = int(JewelStats["kunzite_lvl" + str(x.split("_")[1]) + "_bonus1"])
				dmg_to_mobs = int(JewelStats["kunzite_lvl" + str(x.split("_")[1]) + "_bonus2"])
				atk_kunzite += kunzite_b1
				dmg_to_mobs +=  kunzite_b2
			if a == "tourmaline":
				tourmaline_b1 = atk_tourmaline
				tourmaline_b2 = dmg_to_elite
				atk_tourmaline = int(JewelStats["tourmaline_lvl" + str(x.split("_")[1]) + "_bonus1"])
				dmg_to_elite = int(JewelStats["tourmaline_lvl" + str(x.split("_")[1]) + "_bonus2"])
				atk_tourmaline += tourmaline_b1
				dmg_to_elite +=  tourmaline_b2
			if a == "lapis":
				lapis_b1 = pv_lapis
				lapis_b2 = red_he_lapis
				pv_lapis = int(JewelStats["lapis_lvl" + str(x.split("_")[1]) + "_bonus1"])
				red_he_lapis = int(JewelStats["lapis_lvl" + str(x.split("_")[1]) + "_bonus2"])
				pv_lapis += lapis_b1
				red_he_lapis +=  lapis_b2
			if a == "emerald":
				emerald_b1 = pv_emerald
				emerald_b2 = drop_pv_emerald
				pv_emerald = int(JewelStats["emerald_lvl" + str(x.split("_")[1]) + "_bonus1"])
				drop_pv_emerald = int(JewelStats["emerald_lvl" + str(x.split("_")[1]) + "_bonus2"])
				pv_emerald += emerald_b1
				drop_pv_emerald +=  emerald_b2
			if a == "topaz":
				topaz_b1 = proj_res_topaz
				topaz_b2 = crit_dmg_topaz
				proj_res_topaz = int(JewelStats["topaz_lvl" + str(x.split("_")[1]) + "_bonus1"])
				crit_dmg_topaz = int(JewelStats["topaz_lvl" + str(x.split("_")[1]) + "_bonus2"])
				proj_res_topaz += topaz_b1
				crit_dmg_topaz +=  topaz_b2
			if a == "amber":
				amber_b1 = front_res_amber
				amber_b2 = elementary_dmg_amber
				front_res_amber = int(JewelStats["amber_lvl" + str(x.split("_")[1]) + "_bonus1"])
				elementary_dmg_amber = int(JewelStats["amber_lvl" + str(x.split("_")[1]) + "_bonus2"])
				front_res_amber += amber_b1
				elementary_dmg_amber +=  amber_b2
			if a == "amethyst":
				amethyst_b1 = collision_res_amethyst
				amethyst_b2 = pm_when_hurt_amethyst
				collision_res_amethyst = int(JewelStats["amethyst_lvl" + str(x.split("_")[1]) + "_bonus1"])
				pm_when_hurt_amethyst = int(JewelStats["amethyst_lvl" + str(x.split("_")[1]) + "_bonus2"])
				collision_res_amethyst += amethyst_b1
				pm_when_hurt_amethyst +=  amethyst_b2
			if a == "calaite":
				calaite_b1 = pv_calaite
				calaite_b2 = mp_max_calaite
				pv_calaite = int(JewelStats["calaite_lvl" + str(x.split("_")[1]) + "_bonus1"])
				mp_max_calaite = int(JewelStats["calaite_lvl" + str(x.split("_")[1]) + "_bonus2"])
				pv_calaite += calaite_b1
				mp_max_calaite +=  calaite_b2
		dict_result = {
			'attack_ruby':atk_ruby,
			'attack_kunzite':atk_kunzite,
			'attack_tourmaline':atk_tourmaline,
			'pv_lapis':pv_lapis,
			'pv_emerald':pv_emerald,
			'proj_res_topaz':proj_res_topaz,
			'front_res_amber':front_res_amber,
			'collision_res_amethyst':collision_res_amethyst,
			'pv_calaite':pv_calaite,
			'dmg_to_boss':dmg_to_boss,
			'dmg_to_mobs':dmg_to_mobs,
			'dmg_to_elite':dmg_to_elite,
			'red_he_lapis':red_he_lapis,
			'drop_pv_emerald':drop_pv_emerald,
			'crit_dmg_topaz':crit_dmg_topaz,
			'elementary_dmg_amber':elementary_dmg_amber,
			'pm_when_hurt_amethyst':pm_when_hurt_amethyst,
			'mp_max_calaite':mp_max_calaite,
		}
		return dict_result

	def JewelSpeBonusStatsRecup(type,jewel1,jewel2,jewel3,jewel4,brave_boost):
		jewel1_level = int(jewel1.split("_")[1])
		jewel2_level = int(jewel2.split("_")[1])
		jewel3_level = int(jewel3.split("_")[1])
		jewel4_level = int(jewel4.split("_")[1])
		if jewel1.split("_")[0] == "none":
			jewel1_level = 0
		if jewel2.split("_")[0] == "none":
			jewel2_level = 0
		if jewel3.split("_")[0] == "none":
			jewel3_level = 0
		if jewel4.split("_")[0] == "none":
			jewel4_level = 0
		result = int(jewel1_level) + int(jewel2_level) + int(jewel3_level) + int(jewel4_level) + int(brave_boost)
		if result >= 4:
			spe_bonus = JewelSpeBonus[str(type) + "_sb_lvl4"]
			if result >= 8:
				spe_bonus = JewelSpeBonus[str(type) + "_sb_lvl8"]
				if result >= 16:
					spe_bonus = JewelSpeBonus[str(type) + "_sb_lvl16"]
					if result >= 28:
						spe_bonus = JewelSpeBonus[str(type) + "_sb_lvl28"]
						if result >= 38:
							spe_bonus = JewelSpeBonus[str(type) + "_sb_lvl38"]
							if result >= 48:
								spe_bonus = JewelSpeBonus[str(type) + "_sb_lvl48"]
		else:
			spe_bonus = [0,0,0,0,0,0]
		return spe_bonus

	def DragonStatueStats(dragon_type, dragon_rarity, dragon_level, dragon_4thboost_level):
		base_stats1 = DragonStats[str(dragon_type).lower() + "_" + str(dragon_rarity).lower() + "_base_1"]
		base_stats2 = DragonStats[str(dragon_type).lower() + "_" + str(dragon_rarity).lower() + "_base_2"]
		b1_type = DragonStats[str(dragon_type).lower() + "_bonus1"]
		b2_type = DragonStats[str(dragon_type).lower() + "_bonus2"]
		inc_stats1 = DragonStats[str(dragon_type).lower() + "_" + str(dragon_rarity).lower() + "_inc_1"]
		inc_stats2 = DragonStats[str(dragon_type).lower() + "_" + str(dragon_rarity).lower() + "_inc_2"]
		if dragon_rarity == "Mythic" and int(dragon_4thboost_level) > 0:
			inc_mythic_boost = DragonStats[str(dragon_type).lower() + "_mythic_boost_inc" ]
			inc_mythic_boost_float = float(inc_mythic_boost[0]) * (int(dragon_4thboost_level)-1) +int(inc_mythic_boost[1])
			inc_stats1_modified = round(float(inc_stats1) * (float(inc_mythic_boost_float)/100+1))
			inc_stats2_modified = round(float(inc_stats2) * (float(inc_mythic_boost_float)/100+1))
			result_stats1 = (float(base_stats1) + (float(dragon_level)-1)*inc_stats1_modified)*(float(inc_mythic_boost[1])/100+1)  ## c'est pas les bonnes formules mais 
			result_stats2 = (float(base_stats2) + (float(dragon_level)-1)*inc_stats2_modified)*(float(inc_mythic_boost[1])/100+1)  ## le résultat est proches de la réalité
		else:
			result_stats1 = int(base_stats1) + (int(dragon_level)-1)*int(inc_stats1)
			result_stats2 = int(base_stats2) + (int(dragon_level)-1)*int(inc_stats2)
			inc_stats1_modified = 0
			inc_stats2_modified = 0
		if dragon_rarity == "Mythic" or dragon_rarity == "Ancient Legendary":
			b3_type = DragonStats[str(dragon_type).lower() + "_bonus3"]
			b3_boost = DragonStats[str(dragon_type).lower() + "_stats_boost3"]
		else:
			b3_type = 0
			b3_boost = 0
		dict_result = {
			"Attack":"0",
			"Max Hp":"0",
			"Damage To Mobs":"0",
			"Damage To Melee Units":"0",
			"Damage To Ranged Units":"0",
			"Damage To Ground Units":"0",
			"Rear Damage Resistance":"0",
			"Front Damage Resistance":"0",
			"Healling effect of Red Heart":"0",
			"Collision Damage Resistance":"0",
			"Mana Points Recovery effect":"0",
			"":"0",
			"HP drops":"0",
			"Melee Units Damage reduced":"0",
			"Weapon Melee Damage":"0",
			"Mana Points Regeneration":"0",
			"Summoned Creature Damage":"0",
			"Max Mp":"0",
			"":"0",
			b1_type: round(result_stats1),
			b2_type: round(result_stats2),
			b3_type: float(b3_boost),
			"inc_stats1_modified":round(inc_stats1_modified),
			"inc_stats2_modified":round(inc_stats2_modified),
		}
		return dict_result

	def GetEggStats(egg_name,egg_level):
		if egg_name != "choose":
			egg_name = egg_name.replace("-","_")
			mob_stat = MobsStats[str(egg_name) + "_" + str(egg_level)]
			stats_type = MobsStats[str(egg_name) + "_stats_type"]
			len_mob_stats = len(mob_stat)
			try:
				for i in mob_stat:
					int(i)
			except ValueError as e:
				mob_stat = []
				for i in range (len_mob_stats):
					mob_stat.append(0)
			dict_stats = {
				"Attack": "0",
				"Max Hp": "0", ##mettre ici pour pas avoir keyword error
				"Critic Damage": "0",
				"Damage To Bosses": "0",
				"Damage To Mobs": "0",
				"Damage To Ground Units": "0",
				"Damage To Ranged Units": "0",
				"Damage To Melee Units": "0",
				"Damage To Airborne Units": "0",
				stats_type[0]: mob_stat[0],
				stats_type[1]: mob_stat[1],
				stats_type[2]: mob_stat[2],
			}
		else:
			dict_stats = {
				"Attack":"0",
				"Critic Damage": "0",
				"Max Hp":"0",
				"Damage To Bosses": "0",
				"Damage To Mobs": "0",
				"Damage To Ground Units": "0",
				"Damage To Ranged Units": "0",
				"Damage To Melee Units": "0",
				"Damage To Airborne Units": "0",
			}
		return dict_stats


	def GetPassifEggStats1(egg,egg_level):
		passif_stats = [0,0,0,0]
		if int(egg_level) >= 5:
			passif_stats = PassivMobsStats1[str(egg) + "_5"]
			if int(egg_level) >= 10:
				passif_stats = PassivMobsStats1[str(egg) + "_10"]
				if int(egg_level) >= 13:
					passif_stats = PassivMobsStats1[str(egg) + "_13"]
					if int(egg_level) >= 17:
						passif_stats = PassivMobsStats1[str(egg) + "_17"]
		try:
			for i in passif_stats:
				int(i)
		except ValueError as e:
			passif_stats = [0,0,0,0]
		return passif_stats

	def GetPassifEggStats2(egg,egg_level):
		passif_stats = [0,0,0,0,0]
		if int(egg_level) >= 4:
			passif_stats = PassivMobsStats2[str(egg) + "_4"]
			if int(egg_level) >= 7:
				passif_stats = PassivMobsStats2[str(egg) + "_7"]
				if int(egg_level) >= 10:
					passif_stats = PassivMobsStats2[str(egg) + "_10"]
					if int(egg_level) >= 13:
						passif_stats = PassivMobsStats2[str(egg) + "_13"]
						if int(egg_level) >= 17:
							passif_stats = PassivMobsStats2[str(egg) + "_17"]
		try:
			for i in passif_stats:
				int(i)
		except ValueError as e:
			passif_stats = [0,0,0,0,0]
		return passif_stats
	
	def GetPassifEggStats3(egg,egg_level):
		passif_stats = [0,0,0,0,0]
		if int(egg_level) >= 3:
			passif_stats = PassivMobsStats3[str(egg) + "_3"]
			if int(egg_level) >= 6:
				passif_stats = PassivMobsStats3[str(egg) + "_6"]
				if int(egg_level) >= 8:
					passif_stats = PassivMobsStats3[str(egg) + "_8"]
					if int(egg_level) >= 10:
						passif_stats = PassivMobsStats3[str(egg) + "_10"]
						if int(egg_level) >= 13:
							passif_stats = PassivMobsStats3[str(egg) + "_13"]
		try:
			for i in passif_stats:
				int(i)
		except ValueError as e:
			passif_stats = [0,0,0,0,0]
		return passif_stats

	def GetStarEquippedEgg(selected_egg):
		selected_egg = selected_egg.replace("-","_")
		dict_egg_star = {
			"choose": 0,"green_bat": green_bat_star,
			"vase": vase_star,"bomb_ghost": bomb_ghost_star,
			"rock_puppet": rock_puppet_star,"party_tree": party_tree_star,
			"wolfhound": wolfhound_star,"skeleton_archer": skeleton_archer_star,
			"skeleton_soldier": skeleton_soldier_star,
			"wasp": wasp_star,"fire_mage": fire_mage_star,
			"medusa": medusa_star,"ice_mage": ice_mage_star,
			"fire_lizard": fire_lizard_star,"flame_ghost": flame_ghost_star,
			"thorny_snake": thorny_snake_star,"tornado_demon": tornado_demon_star,
			"piranha": piranha_star,"zombie": zombie_star,
			"scarecrow": scarecrow_star,"long_dragon": long_dragon_star,
			"skull_wizard": skull_wizard_star,"lava_golem": lava_golem_star,
			"ice_golem": ice_golem_star,"cactus": cactus_star,
			"crazy_spider": crazy_spider_star,"fire_element": fire_element_star,
			"skeleton_swordsman": skeleton_swordsman_star,"scythe_mage": scythe_mage_star,
			"pea_shooter": pea_shooter_star,"shadow_assassin": shadow_assassin_star,
			"tornado_mage": tornado_mage_star,"spitting_mushroom": spitting_mushroom_star,
			"rolling_mushroom": rolling_mushroom_star,"fallen_bat": fallen_bat_star,
			"one_eyed_bat": one_eyed_bat_star,"scarlet_mage": scarlet_mage_star,
			"icefire_phantom": icefire_phantom_star,"purple_phantom": purple_phantom_star,
			"tundra_dragon": tundra_dragon_star,"sandian": sandian_star,
			"nether_puppet": nether_puppet_star,"psionic_scarecrow": psionic_scarecrow_star,
			"steel_dryad": steel_dryad_star,"savage_spider": savage_spider_star,
			"flaming_bug": flaming_bug_star,"elite_archer": elite_archer_star,
			"little_dragon": little_dragon_star,"arch_leader": arch_leader_star,
			"skeleton_king": skeleton_king_star,"crimson_witch": crimson_witch_star,
			"rage_golem": rage_golem_star,"queen_bee": queen_bee_star,
			"ice_worm": ice_worm_star,"medusa_boss": medusa_boss_star,
			"ice_demon": ice_demon_star,"giant_owl": giant_owl_star,
			"fire_demon": fire_demon_star,"krab_boss": krab_boss_star,
			"desert_goliath": desert_goliath_star,
		}
		egg_star = dict_egg_star[selected_egg]
		return egg_star

################################### TRAITEMENT DES ENTRÉES DE L'USERS + REQUÊTE DANS LES DATA LOCALES #############################################
	weapon_inc_raw = StatsWeapon[(str(weapon_name_choosen) + " " +  str(weapon_rarity_choosen) + " " +  "inc_atk").lower().replace(" ","_")]
	weapon_base_raw = StatsWeapon[(str(weapon_name_choosen) + " " +  str(weapon_rarity_choosen) + " " +  "base_atk").lower().replace(" ","_")]
	weapon_var_raw = StatsWeapon[(str(weapon_name_choosen) + " " +  str(weapon_rarity_choosen) + " " +  "var_atk").lower().replace(" ","_")]
	weapon_crit_raw = StatsWeapon[(str(weapon_name_choosen) + " " +  str(weapon_rarity_choosen) + " " +  "crit").lower().replace(" ","_")]

	armor_inc_raw = StatsArmor[(str(armor_name_choosen) + " " +  str(armor_rarity_choosen) + " " +  "inc_hp").lower().replace(" ","_")]
	armor_base_raw = StatsArmor[(str(armor_name_choosen) + " " +  str(armor_rarity_choosen) + " " +  "base_hp").lower().replace(" ","_")]
	armor_var_raw = StatsArmor[(str(armor_name_choosen) + " " +  str(armor_rarity_choosen) + " " +  "var_hp").lower().replace(" ","_")]
	armor_evade_raw = StatsArmor[(str(armor_name_choosen) + " " +  str(armor_rarity_choosen) + " " +  "evade").lower().replace(" ","_")]
	armor_resistance_raw = StatsArmor[(str(armor_name_choosen) + " " +  str(armor_rarity_choosen) + " " +  "resistance").lower().replace(" ","_")]
	armor_resistance_type_raw = StatsArmor[(str(armor_name_choosen) + "_resistance_type").lower().replace(" ","_")]

	ring1_inc_raw = StatsRing[(str(ring1_name_choosen) + " " +  str(ring1_rarity_choosen) + " " +  "inc_damage").lower().replace(" ","_")]
	ring1_base_raw = StatsRing[(str(ring1_name_choosen) + " " +  str(ring1_rarity_choosen) + " " +  "base_damage").lower().replace(" ","_")]
	ring1_hp_raw = StatsRing[(str(ring1_name_choosen) + " " +  str(ring1_rarity_choosen) + " " +  "hp").lower().replace(" ","_")]
	ring1_atk_raw = StatsRing[(str(ring1_name_choosen) + " " +  str(ring1_rarity_choosen) + " " +  "atk").lower().replace(" ","_")]
	ring1_evade_raw = StatsRing[(str(ring1_name_choosen) + " " +  str(ring1_rarity_choosen) + " " +  "evade").lower().replace(" ","_")]
	ring1_resistance_raw = StatsRing[(str(ring1_name_choosen) + " " +  str(ring1_rarity_choosen) + " " +  "resistance").lower().replace(" ","_")]
	ring1_crit_chance_raw = StatsRing[(str(ring1_name_choosen) + " " +  str(ring1_rarity_choosen) + " " +  "crit_chance").lower().replace(" ","_")]
	ring1_crit_damage_raw = StatsRing[(str(ring1_name_choosen) + " " +  str(ring1_rarity_choosen) + " " +  "crit_damage").lower().replace(" ","_")]
	ring1_mythic_resistance_raw = StatsRing[(str(ring1_name_choosen) + " " +  str(ring1_rarity_choosen) + " " +  "resistance_mythic").lower().replace(" ","_")]
	ring1_resistance_type_raw = StatsRing[(str(ring1_name_choosen) + "_resistance_type").lower().replace(" ","_")]
	ring1_mythic_resistance_type_raw = StatsRing[(str(ring1_name_choosen) + "_mythic_resistance_type").lower().replace(" ","_")]
	ring1_damage_type_raw = StatsRing[(str(ring1_name_choosen) + "_damage_type").lower().replace(" ","_")]

	ring2_inc_raw = StatsRing[(str(ring2_name_choosen) + " " +  str(ring2_rarity_choosen) + " " +  "inc_damage").lower().replace(" ","_")]
	ring2_base_raw = StatsRing[(str(ring2_name_choosen) + " " +  str(ring2_rarity_choosen) + " " +  "base_damage").lower().replace(" ","_")]
	ring2_hp_raw = StatsRing[(str(ring2_name_choosen) + " " +  str(ring2_rarity_choosen) + " " +  "hp").lower().replace(" ","_")]
	ring2_atk_raw = StatsRing[(str(ring2_name_choosen) + " " +  str(ring2_rarity_choosen) + " " +  "atk").lower().replace(" ","_")]
	ring2_evade_raw = StatsRing[(str(ring2_name_choosen) + " " +  str(ring2_rarity_choosen) + " " +  "evade").lower().replace(" ","_")]
	ring2_resistance_raw = StatsRing[(str(ring2_name_choosen) + " " +  str(ring2_rarity_choosen) + " " +  "resistance").lower().replace(" ","_")]
	ring2_crit_chance_raw = StatsRing[(str(ring2_name_choosen) + " " +  str(ring2_rarity_choosen) + " " +  "crit_chance").lower().replace(" ","_")]
	ring2_crit_damage_raw = StatsRing[(str(ring2_name_choosen) + " " +  str(ring2_rarity_choosen) + " " +  "crit_damage").lower().replace(" ","_")]
	ring2_mythic_resistance_raw = StatsRing[(str(ring2_name_choosen) + " " +  str(ring2_rarity_choosen) + " " +  "resistance_mythic").lower().replace(" ","_")]
	ring2_resistance_type_raw = StatsRing[(str(ring2_name_choosen) + "_resistance_type").lower().replace(" ","_")]
	ring2_mythic_resistance_type_raw = StatsRing[(str(ring2_name_choosen) + "_mythic_resistance_type").lower().replace(" ","_")]
	ring2_damage_type_raw = StatsRing[(str(ring2_name_choosen) + "_damage_type").lower().replace(" ","_")]
	
	bracelet_inc_raw = StatsBracelet[(str(bracelet_name_choosen) + " " +  str(bracelet_rarity_choosen) + " " +  "inc_atk").lower().replace(" ","_")]
	bracelet_base_raw = StatsBracelet[(str(bracelet_name_choosen) + " " +  str(bracelet_rarity_choosen) + " " +  "base_atk").lower().replace(" ","_")]
	bracelet_var_raw = StatsBracelet[(str(bracelet_name_choosen) + " " +  str(bracelet_rarity_choosen) + " " +  "var_atk").lower().replace(" ","_")]
	bracelet_crit_raw = StatsBracelet[(str(bracelet_name_choosen) + " " +  str(bracelet_rarity_choosen) + " " +  "crit").lower().replace(" ","_")]

	locket_inc_raw = StatsLocket[(str(locket_name_choosen) + " " +  str(locket_rarity_choosen) + " " +  "inc_hp").lower().replace(" ","_")]
	locket_base_raw = StatsLocket[(str(locket_name_choosen) + " " +  str(locket_rarity_choosen) + " " +  "base_hp").lower().replace(" ","_")]
	locket_evade_raw = StatsLocket[(str(locket_name_choosen) + " " +  str(locket_rarity_choosen) + " " +  "evade").lower().replace(" ","_")]
	locket_var_raw = StatsLocket[(str(locket_name_choosen) + " " +  str(locket_rarity_choosen) + " " +  "var_hp").lower().replace(" ","_")]
	locket_resistance_raw = StatsLocket[(str(locket_name_choosen) + " " +  str(locket_rarity_choosen) + " " +  "resistance").lower().replace(" ","_")]
	locket_resistance_type_raw = StatsLocket[(str(locket_name_choosen) + "_resistance_type").lower().replace(" ","_")]

	book_inc_raw = StatsBook[(str(book_name_choosen.replace("'","")) + " " +  str(book_rarity_choosen) + " " +  "inc_hp").lower().replace(" ","_")]
	book_base_raw = StatsBook[(str(book_name_choosen) + " " +  str(book_rarity_choosen) + " " +  "base_hp").lower().replace(" ","_")]
	book_var_raw = StatsBook[(str(book_name_choosen) + " " +  str(book_rarity_choosen) + " " +  "var_hp").lower().replace(" ","_")]
	book_resistance_raw = StatsBook[(str(book_name_choosen) + " " +  str(book_rarity_choosen) + " " +  "resistance").lower().replace(" ","_")]
	book_resistance2_raw = StatsBook[(str(book_name_choosen) + " " +  str(book_rarity_choosen) + " " +  "resistance2").lower().replace(" ","_")]
	book_resistance_type_raw = StatsBook[(str(book_name_choosen) + "_resistance_type").lower().replace(" ","_")]
	book_resistance2_type_raw = StatsBook[(str(book_name_choosen) + "_resistance2_type").lower().replace(" ","_")]

	talents_strength = TalentStats["strength_" + str(strength_level)]
	talents_power = TalentStats["power_" + str(power_level)]
	talents_recover = TalentStats["recover_" + str(recover_level)]
	talents_block = TalentStats["block_" + str(block_level)]
	talents_iron_bulwark = TalentStats["iron_bulwark_" + str(iron_bulwark_level)]
	talents_enhanced_equipment = TalentStats["enhanced_equipment_" + str(enhanced_equipment_level)]
	talents_hero_power_up = TalentStats["hero_power_up_" + str(hero_power_up_level)]


	altar_stuff_ascension_atk = StuffAltarAscension[str(stuff_altar_ascension) + '_attack']
	altar_stuff_ascension_hp = StuffAltarAscension[str(stuff_altar_ascension) + '_hp']
	altar_stuff_ascension_healing_effect = StuffAltarAscension[str(stuff_altar_ascension) + '_healing_effect']
	altar_stuff_ascension_equipment_base = StuffAltarAscension[str(stuff_altar_ascension) + '_equipment_base']

	altar_heros_ascension_atk = HerosAltarAscension[str(heros_altar_ascension) + '_attack']
	altar_heros_ascension_hp = HerosAltarAscension[str(heros_altar_ascension) + '_hp']
	altar_heros_ascension_hp_drop = HerosAltarAscension[str(heros_altar_ascension) + '_hp_drop']
	altar_heros_ascension_heros_base = HerosAltarAscension[str(heros_altar_ascension) + '_heros_base']

	altar_stuff_atk = CalculAltar(
		int(StuffAltar[str(RoundTen(stuff_altar_level)) + '_attack']),
		int(stuff_altar_level),
		int(RoundTen(stuff_altar_level)),
		int(StuffAltar[str(RoundTen(stuff_altar_level)) + '_inc_attack'])
	)

	altar_stuff_hp = CalculAltar(
		int(StuffAltar[str(RoundTen(stuff_altar_level)) + '_hp']),
		int(stuff_altar_level),
		int(RoundTen(stuff_altar_level)),
		int(StuffAltar[str(RoundTen(stuff_altar_level)) + '_inc_hp'])
	)

	altar_hero_atk = CalculAltar(
		int(HerosAltar[str(RoundTen(heros_altar_level)) + '_attack']),
		int(heros_altar_level),
		int(RoundTen(heros_altar_level)),
		int(HerosAltar[str(RoundTen(heros_altar_level)) + '_inc_attack'])
	)

	altar_hero_hp = CalculAltar(
		int(HerosAltar[str(RoundTen(heros_altar_level)) + '_hp']),
		int(heros_altar_level),
		int(RoundTen(heros_altar_level)),
		int(HerosAltar[str(RoundTen(heros_altar_level)) + '_inc_hp'])
	)

	AtreusStats = HerosStatsRecup("Atreus",atreus_level,atreus_star,choosen_hero)
	UrasilStats = HerosStatsRecup("Urasil",urasil_level,urasil_star,choosen_hero)
	PhorenStats = HerosStatsRecup("Phoren",phoren_level,phoren_star,choosen_hero)
	TaranisStats = HerosStatsRecup("Taranis",taranis_level, taranis_star, choosen_hero)
	HelixStats = HerosStatsRecup("Helix",helix_level, helix_star, choosen_hero) 
	MeowgikStats = HerosStatsRecup("Meowgik",meowgik_level, meowgik_star, choosen_hero)
	ShariStats = HerosStatsRecup("Shari",shari_level, shari_star, choosen_hero)
	AyanaStats = HerosStatsRecup("Ayana",ayana_level, ayana_star, choosen_hero)
	OnirStats = HerosStatsRecup("Onir",onir_level, onir_star, choosen_hero) 
	RollaStats = HerosStatsRecup("Rolla",rolla_level, rolla_star, choosen_hero)
	BonnieStats = HerosStatsRecup("Bonnie",bonnie_level, bonnie_star, choosen_hero)
	SylvanStats = HerosStatsRecup("Sylvan",sylvan_level, sylvan_star, choosen_hero)
	ShadeStats = HerosStatsRecup("Shade",shade_level, shade_star, choosen_hero) 
	OpheliaStats = HerosStatsRecup("Ophelia",ophelia_level, ophelia_star, choosen_hero)
	RyanStats = HerosStatsRecup("Ryan",ryan_level, ryan_star, choosen_hero)
	LinaStats = HerosStatsRecup("Lina",lina_level, lina_star, choosen_hero)
	AqueaStats = HerosStatsRecup("Aquea",aquea_level, aquea_star, choosen_hero)
	ShingenStats = HerosStatsRecup("Shingen",shingen_level, shingen_star, choosen_hero) 
	GuguStats = HerosStatsRecup("Gugu",gugu_level, gugu_star, choosen_hero)
	IrisStats = HerosStatsRecup("Iris",iris_level, iris_star, choosen_hero)
	BlazoStats = HerosStatsRecup("Blazo",blazo_level, blazo_star, choosen_hero)
	MelindaStats = HerosStatsRecup("Melinda",melinda_level, melinda_star, choosen_hero)
	ElaineStats = HerosStatsRecup("Elaine",elaine_level, elaine_star, choosen_hero)

	skin_health_boost = hp_given_from_skin
	skin_atk_boost = atk_given_from_skin
	stats_jewel = JewelStatsRecup(weapon_jewel1,weapon_jewel2,weapon_jewel3,weapon_jewel4,armor_jewel1,armor_jewel2,armor_jewel3,armor_jewel4,ring1_jewel1,ring1_jewel2,ring1_jewel3,ring1_jewel4,ring2_jewel1,ring2_jewel2,ring2_jewel3,ring2_jewel4,pet1_jewel1,pet1_jewel2,pet1_jewel3,pet1_jewel4,pet2_jewel1,pet2_jewel2,pet2_jewel3,pet2_jewel4,bracelet_jewel1,bracelet_jewel2,bracelet_jewel3,bracelet_jewel4,locket_jewel1,locket_jewel2,locket_jewel3,locket_jewel4,book_jewel1,book_jewel2,book_jewel3,book_jewel4)

	brave_privileges_stats = BravePrivileges['level' + str(brave_privileges_level)]

	BonusSpe_jewel_weapon = JewelSpeBonusStatsRecup('weapon',weapon_jewel1,weapon_jewel2,weapon_jewel3,weapon_jewel4,brave_privileges_stats['Weapon JSSSA'])
	BonusSpe_jewel_armor = JewelSpeBonusStatsRecup('armor',armor_jewel1,armor_jewel2,armor_jewel3,armor_jewel4,brave_privileges_stats['Armor JSSSA'])
	BonusSpe_jewel_ring1 = JewelSpeBonusStatsRecup('ring1',ring1_jewel1,ring1_jewel2,ring1_jewel3,ring1_jewel4,brave_privileges_stats['Ring JSSSA'])
	BonusSpe_jewel_ring2 = JewelSpeBonusStatsRecup('ring2',ring2_jewel1,ring2_jewel2,ring2_jewel3,ring2_jewel4,brave_privileges_stats['Ring JSSSA'])
	BonusSpe_jewel_pet1 = JewelSpeBonusStatsRecup('pet1',pet1_jewel1,pet1_jewel2,pet1_jewel3,pet1_jewel4,brave_privileges_stats['Spirit JSSSA'])
	BonusSpe_jewel_pet2 = JewelSpeBonusStatsRecup('pet2',pet2_jewel1,pet2_jewel2,pet2_jewel3,pet2_jewel4,brave_privileges_stats['Spirit JSSSA'])
	BonusSpe_jewel_bracelet = JewelSpeBonusStatsRecup('bracelet',bracelet_jewel1,bracelet_jewel2,bracelet_jewel3,bracelet_jewel4,brave_privileges_stats['Bracelet JSSSA'])
	BonusSpe_jewel_locket = JewelSpeBonusStatsRecup('locket',locket_jewel1,locket_jewel2,locket_jewel3,locket_jewel4,brave_privileges_stats['Locket JSSSA'])
	BonusSpe_jewel_book = JewelSpeBonusStatsRecup('book',book_jewel1,book_jewel2,book_jewel3,book_jewel4,brave_privileges_stats['Spellbook JSSSA'])

	jewel_lvl_weapon = int(weapon_jewel1.split("_")[1]) + int(weapon_jewel2.split("_")[1]) + int(weapon_jewel3.split("_")[1]) + int(weapon_jewel4.split("_")[1])
	jewel_lvl_armor = int(armor_jewel1.split("_")[1]) + int(armor_jewel2.split("_")[1]) + int(armor_jewel3.split("_")[1]) + int(armor_jewel4.split("_")[1])
	jewel_lvl_ring1 = int(ring1_jewel1.split("_")[1]) + int(ring1_jewel2.split("_")[1]) + int(ring1_jewel3.split("_")[1]) + int(ring1_jewel4.split("_")[1])
	jewel_lvl_ring2 = int(ring2_jewel1.split("_")[1]) + int(ring2_jewel2.split("_")[1]) + int(ring2_jewel3.split("_")[1]) + int(ring2_jewel4.split("_")[1])
	jewel_lvl_pet1 = int(pet1_jewel1.split("_")[1]) + int(pet1_jewel2.split("_")[1]) + int(pet1_jewel3.split("_")[1]) + int(pet1_jewel4.split("_")[1])
	jewel_lvl_pet2 = int(pet2_jewel1.split("_")[1]) + int(pet2_jewel2.split("_")[1]) + int(pet2_jewel3.split("_")[1]) + int(pet2_jewel4.split("_")[1])
	jewel_lvl_bracelet = int(bracelet_jewel1.split("_")[1]) + int(bracelet_jewel2.split("_")[1]) + int(bracelet_jewel3.split("_")[1]) + int(bracelet_jewel4.split("_")[1])
	jewel_lvl_locket = int(locket_jewel1.split("_")[1]) + int(locket_jewel2.split("_")[1]) + int(locket_jewel3.split("_")[1]) + int(locket_jewel4.split("_")[1])
	jewel_lvl_book = int(book_jewel1.split("_")[1]) + int(weapon_jewel2.split("_")[1]) + int(weapon_jewel3.split("_")[1]) + int(weapon_jewel4.split("_")[1])

	atk_power_reforge = ReforgePowerCourage(power_reforge_stats)
	atk_courage_reforge = ReforgePowerCourage(courage_reforge_stats)
	hp_saviour_reforge = ReforgeSaviourRecoLuck(saviour_reforge_stats)
	hp_recovery_reforge = ReforgeSaviourRecoLuck(recovery_reforge_stats)
	hp_luck_reforge = ReforgeSaviourRecoLuck(luck_reforge_stats)
	courage_hero_attack_flat = CourageBoostHero(choosen_hero,runes_courage_hero_attack_flat)
	courage_hero_attack_var = float(CourageBoostHero(choosen_hero,runes_courage_hero_attack_var))/100
	courage_hero_hp_flat = CourageBoostHero(choosen_hero,runes_courage_hero_hp_flat)
	courage_hero_hp_var = float(CourageBoostHero(choosen_hero,runes_courage_hero_hp_var))/100

	selected_egg1_stats = GetEggStats(selected_egg1,GetStarEquippedEgg(selected_egg1))
	selected_egg2_stats = GetEggStats(selected_egg2,GetStarEquippedEgg(selected_egg2))
	selected_egg3_stats = GetEggStats(selected_egg3,GetStarEquippedEgg(selected_egg3))
	selected_egg4_stats = GetEggStats(selected_egg4,GetStarEquippedEgg(selected_egg4)) #ça ressort pas quand y'a 2 fois none
	selected_egg5_stats = GetEggStats(selected_egg5,GetStarEquippedEgg(selected_egg5)) #ça ressort pas quand y'a 2 fois none

	green_bat_passif_stats = GetPassifEggStats1("green_bat", green_bat_star)
	vase_passif_stats = GetPassifEggStats1("vase",vase_star)
	bomb_ghost_passif_stats = GetPassifEggStats1("bomb_ghost",bomb_ghost_star)
	rock_puppet_passif_stats = GetPassifEggStats1("rock_puppet",rock_puppet_star)
	party_tree_passif_stats = GetPassifEggStats1("party_tree",party_tree_star)
	zombie_passif_stats = GetPassifEggStats1("zombie",zombie_star)
	piranha_passif_stats = GetPassifEggStats1("piranha",piranha_star)

	wolfhound_passif_stats = GetPassifEggStats2("wolfhound",wolfhound_star)
	skeleton_archer_passif_stats = GetPassifEggStats2("skeleton_archer",skeleton_archer_star)
	skeleton_soldier_passif_stats = GetPassifEggStats2("skeleton_soldier",skeleton_soldier_star)
	wasp_passif_stats = GetPassifEggStats2("wasp",wasp_star)
	fire_mage_passif_stats = GetPassifEggStats2("fire_mage",fire_mage_star)
	medusa_passif_stats = GetPassifEggStats2("medusa",medusa_star)
	ice_mage_passif_stats = GetPassifEggStats2("ice_mage",ice_mage_star)
	fire_lizard_passif_stats = GetPassifEggStats2("fire_lizard",fire_lizard_star)
	flame_ghost_passif_stats = GetPassifEggStats2("flame_ghost",flame_ghost_star)
	thorny_snake_passif_stats = GetPassifEggStats2("thorny_snake",thorny_snake_star)
	tornado_demon_passif_stats = GetPassifEggStats2("tornado_demon",tornado_demon_star)
	scarecrow_passif_stats = GetPassifEggStats2("scarecrow",scarecrow_star)
	long_dragon_passif_stats = GetPassifEggStats2("long_dragon",long_dragon_star)
	skull_wizard_passif_stats = GetPassifEggStats2("skull_wizard",skull_wizard_star)
	lava_golem_passif_stats = GetPassifEggStats2("lava_golem",lava_golem_star)
	ice_golem_passif_stats = GetPassifEggStats2("ice_golem",ice_golem_star)
	cactus_passif_stats = GetPassifEggStats2("cactus",cactus_star)
	crazy_spider_passif_stats = GetPassifEggStats2("crazy_spider",crazy_spider_star)
	fire_element_passif_stats = GetPassifEggStats2("fire_element",fire_element_star)
	skeleton_swordsman_passif_stats = GetPassifEggStats2("skeleton_swordsman",skeleton_swordsman_star)
	scythe_mage_passif_stats = GetPassifEggStats2("scythe_mage",scythe_mage_star)
	pea_shooter_passif_stats = GetPassifEggStats2("pea_shooter",pea_shooter_star)
	shadow_assassin_passif_stats = GetPassifEggStats2("shadow_assassin",shadow_assassin_star)
	tornado_mage_passif_stats = GetPassifEggStats2("tornado_mage",tornado_mage_star)
	spitting_mushroom_passif_stats = GetPassifEggStats2("spitting_mushroom",spitting_mushroom_star)
	rolling_mushroom_passif_stats = GetPassifEggStats2("rolling_mushroom",rolling_mushroom_star)
	fallen_bat_passif_stats = GetPassifEggStats2("fallen_bat",fallen_bat_star)
	one_eyed_bat_passif_stats = GetPassifEggStats2("one_eyed_bat",one_eyed_bat_star)
	scarlet_mage_passif_stats = GetPassifEggStats2("scarlet_mage",scarlet_mage_star)
	icefire_phantom_passif_stats = GetPassifEggStats2("icefire_phantom",icefire_phantom_star)
	purple_phantom_passif_stats = GetPassifEggStats2("purple_phantom",purple_phantom_star)
	tundra_dragon_passif_stats = GetPassifEggStats2("tundra_dragon",tundra_dragon_star)
	sandian_passif_stats = GetPassifEggStats2("sandian",sandian_star)
	nether_puppet_passif_stats = GetPassifEggStats2("nether_puppet",nether_puppet_star)
	psionic_scarecrow_passif_stats = GetPassifEggStats2("psionic_scarecrow",psionic_scarecrow_star)
	steel_dryad_passif_stats = GetPassifEggStats2("steel_dryad",steel_dryad_star)
	savage_spider_passif_stats = GetPassifEggStats2("savage_spider",savage_spider_star)
	flaming_bug_passif_stats = GetPassifEggStats2("flaming_bug",flaming_bug_star)
	elite_archer_passif_stats = GetPassifEggStats2("elite_archer",elite_archer_star)
	little_dragon_passif_stats = GetPassifEggStats2("little_dragon",little_dragon_star)
	rage_golem_passif_stats = GetPassifEggStats2("rage_golem",rage_golem_star)

	arch_leader_passif_stats = GetPassifEggStats3("arch_leader",arch_leader_star)
	skeleton_king_passif_stats = GetPassifEggStats3("skeleton_king",skeleton_king_star)
	crimson_witch_passif_stats = GetPassifEggStats3("crimson_witch",crimson_witch_star)
	queen_bee_passif_stats = GetPassifEggStats3("queen_bee",queen_bee_star)
	ice_worm_passif_stats = GetPassifEggStats3("ice_worm",ice_worm_star)
	medusa_boss_passif_stats = GetPassifEggStats3("medusa_boss",medusa_boss_star)
	ice_demon_passif_stats = GetPassifEggStats3("ice_demon",ice_demon_star)
	giant_owl_passif_stats = GetPassifEggStats3("giant_owl",giant_owl_star)
	fire_demon_passif_stats = GetPassifEggStats3("fire_demon",fire_demon_star)
	krab_boss_passif_stats = GetPassifEggStats3("krab_boss",krab_boss_star)
	desert_goliath_passif_stats = GetPassifEggStats3("desert_goliath",desert_goliath_star)

	stats_dragon_1 = DragonStatueStats(dragon1_type,dragon1_rarity,dragon1_level,dragon1_4thboost_level)
	stats_dragon_2 = DragonStatueStats(dragon2_type,dragon2_rarity,dragon2_level,dragon2_4thboost_level)
	stats_dragon_3 = DragonStatueStats(dragon3_type,dragon3_rarity,dragon3_level,dragon3_4thboost_level)

############################################## CALCUL #######################################################
	egg_passiv_heros_power_up = int(arch_leader_passif_stats[3]) + int(medusa_boss_passif_stats[3]) + int(fire_demon_passif_stats[3]) + int(krab_boss_passif_stats[3]) + int(skeleton_king_passif_stats[1]) + int(skeleton_king_passif_stats[3]) + int(desert_goliath_passif_stats[1]) + int(desert_goliath_passif_stats[3]) + int(ice_demon_passif_stats[1]) + int(ice_demon_passif_stats[3])
	power_up_hero_base_total = float(int(talents_hero_power_up) + int(egg_passiv_heros_power_up) + int(altar_heros_ascension_heros_base))/100
	egg_passiv_enhanced_equipment = int(crimson_witch_passif_stats[3]) + int(queen_bee_passif_stats[3]) + int(ice_worm_passif_stats[1]) + int(ice_worm_passif_stats[3]) + int(giant_owl_passif_stats[1]) + int(giant_owl_passif_stats[3])
	enhanced_equipment_total = float(int(talents_enhanced_equipment) + int(egg_passiv_enhanced_equipment) + int(altar_stuff_ascension_equipment_base))/100+1
	cumul_talent_bonus_passif_atk = int(talents_power)
	cumul_talent_bonus_passif_hp = int(talents_strength)
	#cumul_runes_bonus_passif_atk = int(atk_power_reforge) + int(atk_courage_reforge) + int(runes_power_attack_flat) + int(runes_courage_attack_flat)
	cumul_runes_bonus_passif_hp = int(hp_recovery_reforge) + int(hp_saviour_reforge) + int(hp_luck_reforge) + int(runes_recovery_hp_flat) + int(runes_saviour_hp_flat) + int(runes_luck_hp_flat)
	cumul_hero_bonus_passif_atk = int(AtreusStats[5]) + int(UrasilStats[0]) + int(PhorenStats[6]) + int(HelixStats[5]) + int(MeowgikStats[0]) + int(AyanaStats[6]) + int(RollaStats[0]) + int(BonnieStats[5]) + int(ShadeStats[6]) + int(OpheliaStats[0]) + int(OpheliaStats[2]) + int(LinaStats[0]) + int(LinaStats[5]) + int(AqueaStats[5]) + int(IrisStats[5]) + int(MelindaStats[6]) + int(IrisStats[1]) + int(BlazoStats[1])
	cumul_hero_bonus_passif_hp = int(AtreusStats[0]) + int(AtreusStats[6]) + int(UrasilStats[5]) + int(TaranisStats[5]) + int(MeowgikStats[6]) + int(ShariStats[1]) + int(ShariStats[5]) + int(OnirStats[0]) + int(OnirStats[5]) + int(BonnieStats[6]) + int(SylvanStats[0]) + int(LinaStats[6]) + int(AqueaStats[0]) + int(AqueaStats[6]) + int(ShingenStats[6]) + int(IrisStats[0]) + int(BlazoStats[6]) + int(ElaineStats[5]) + int(ElaineStats[6])
	cumul_skin_bonus_passif_atk = int(skin_atk_boost)
	cumul_skin_bonus_passif_hp = int(skin_health_boost)
	cumul_egg_bonus_passif_atk = int(bomb_ghost_passif_stats[1]) + int(green_bat_passif_stats[1]) + int(piranha_passif_stats[1]) + int(crazy_spider_passif_stats[1]) + int(fire_mage_passif_stats[1]) + int(skeleton_archer_passif_stats[1]) + int(skeleton_soldier_passif_stats[1]) + int(fire_element_passif_stats[1]) + int(flame_ghost_passif_stats[1]) + int(ice_mage_passif_stats[1]) + int(pea_shooter_passif_stats[1]) + int(shadow_assassin_passif_stats[1]) + int(skull_wizard_passif_stats[1]) + int(tornado_demon_passif_stats[1]) + int(savage_spider_passif_stats[1]) + int(flaming_bug_passif_stats[1]) + int(one_eyed_bat_passif_stats[1]) + int(elite_archer_passif_stats[1]) + int(icefire_phantom_passif_stats[1]) + int(purple_phantom_passif_stats[1]) + int(scarlet_mage_passif_stats[1]) + int(arch_leader_passif_stats[0]) + int(crimson_witch_passif_stats[0]) + int(medusa_boss_passif_stats[0]) + int(ice_worm_passif_stats[0]) + int(desert_goliath_passif_stats[0]) + int(ice_demon_passif_stats[0]) + int(fire_demon_passif_stats[1]) 
	cumul_egg_bonus_passif_hp = int(green_bat_passif_stats[3]) + int(party_tree_passif_stats[1]) + int(rock_puppet_passif_stats[1]) +  int(vase_passif_stats[1]) + int(zombie_passif_stats[1]) + int(fire_lizard_passif_stats[1]) + int(long_dragon_passif_stats[1]) + int(scarecrow_passif_stats[1]) + int(skeleton_swordsman_passif_stats[1]) + int(tornado_mage_passif_stats[1]) + int(wasp_passif_stats[1]) + int(cactus_passif_stats[1]) + int(ice_golem_passif_stats[1]) + int(scythe_mage_passif_stats[1]) + int(skull_wizard_passif_stats[4]) + int(fallen_bat_passif_stats[1]) + int(nether_puppet_passif_stats[1]) + int(psionic_scarecrow_passif_stats[1]) + int(spitting_mushroom_passif_stats[1]) + int(steel_dryad_passif_stats[1]) + int(tundra_dragon_passif_stats[1]) +  int(little_dragon_passif_stats[1]) + int(rage_golem_passif_stats[1]) + int(krab_boss_passif_stats[1]) + int(skeleton_king_passif_stats[0]) + int(queen_bee_passif_stats[0]) + int(fire_demon_passif_stats[0])

	#coeff_1_runes_var_passif_atk = float(runes_power_attack_var) + float(runes_courage_attack_var)
	coeff_1_runes_var_passif_hp = float(runes_saviour_hp_var) + float(runes_luck_hp_var)
	coeff_1_heros_var_passif_atk = float(TaranisStats[2]) + float(MeowgikStats[2]) + float(AyanaStats[2]) + float(RollaStats[2]) + float(SylvanStats[2]) + float(AqueaStats[2]) + float(IrisStats[2]) + float(BonnieStats[4]) + float(ShadeStats[7]) + float(MelindaStats[7])
	coeff_1_heros_var_passif_hp = float(AtreusStats[2]) + float(HelixStats[2]) + float(BonnieStats[2]) + float(ShadeStats[2]) + float(LinaStats[2]) + float(ShingenStats[2]) + float(BlazoStats[2]) + float(RyanStats[4]) + float(GuguStats[4]) + float(BlazoStats[4]) + float(AtreusStats[7]) + float(RollaStats[7])  + float(ElaineStats[7]) + float(ElaineStats[2])
	coeff_1_heros_var_actif_atk = float(OnirStats[3]) + float(BonnieStats[3])
	coeff_1_heros_var_actif_hp = float(UrasilStats[3]) + float(SylvanStats[3]) + float(OpheliaStats[3]) + float(RyanStats[1]) + float(ElaineStats[1]) 
	coeff_1_altar_var_passif_atk = float(altar_heros_ascension_atk) + float(altar_stuff_ascension_atk)
	coeff_1_altar_var_passif_hp = float(altar_heros_ascension_hp) + float(altar_stuff_ascension_hp)
	coeff_1_brave_privileges_var_passif_atk = float(brave_privileges_stats['Attack Var'])
	coeff_1_brave_privileges_var_passif_hp = float(brave_privileges_stats['Hp Var'])

	weapon_inc = round(int(weapon_inc_raw)*(enhanced_equipment_total+float(weapon_refine_basic_stats)),2)
	weapon_base = round(int(weapon_base_raw)*(enhanced_equipment_total+float(weapon_refine_basic_stats)),2)
	weapon_level = int(weapon_level_choosen)-1
	weapon_attack_var = float(weapon_var_raw)/100
	weapon_total = ceil(int(weapon_base)+(int(weapon_level)*float(weapon_inc)))
	armor_inc = round(int(armor_inc_raw)*(enhanced_equipment_total+float(armor_refine_basic_stats)),2)
	armor_base = round(int(armor_base_raw)*(enhanced_equipment_total+float(armor_refine_basic_stats)),2)
	armor_level = int(armor_level_choosen)-1
	armor_hp_var = float(armor_var_raw)/100
	armor_total = ceil(int(armor_base)+(int(armor_level)*float(armor_inc)))
	ring1_atk_var = float(ring1_atk_raw)/100
	ring1_hp_var = float(ring1_hp_raw)/100
	ring1_inc = int(ring1_inc_raw)*(1+float(ring1_refine_basic_stats))
	ring1_base = int(ring1_base_raw)*(1+float(ring1_refine_basic_stats))
	ring1_level = int(ring1_level_choosen)-1
	ring1_total = ceil(int(ring1_base)+(int(ring1_level)*float(ring1_inc)))
	ring2_atk_var = float(ring2_atk_raw)/100
	ring2_hp_var = float(ring2_hp_raw)/100
	ring2_inc = int(ring2_inc_raw)*(1+float(ring2_refine_basic_stats))
	ring2_base = int(ring2_base_raw)*(1+float(ring2_refine_basic_stats))
	ring2_level = int(ring2_level_choosen)-1
	ring2_total = ceil(int(ring2_base)+(int(ring2_level)*float(ring2_inc)))
	bracelet_inc = round(int(bracelet_inc_raw)*(enhanced_equipment_total+float(bracelet_refine_basic_stats)),2)
	bracelet_base = round(int(bracelet_base_raw)*(enhanced_equipment_total+float(bracelet_refine_basic_stats)),2)
	bracelet_level = int(bracelet_level_choosen)-1
	bracelet_attack_var = float(bracelet_var_raw)/100
	bracelet_total = ceil(int(bracelet_base)+(int(bracelet_level)*float(bracelet_inc)))
	locket_inc = round(int(locket_inc_raw)*(enhanced_equipment_total+float(locket_refine_basic_stats)),2)
	locket_base = round(int(locket_base_raw)*(enhanced_equipment_total+float(locket_refine_basic_stats)),2)
	locket_level = int(locket_level_choosen)-1
	locket_hp_var = float(locket_var_raw)/100
	locket_total = ceil(int(locket_base)+(int(locket_level)*float(locket_inc)))
	book_inc = round(int(book_inc_raw)*(enhanced_equipment_total+float(book_refine_basic_stats)),2)
	book_base = round(int(book_base_raw)*(enhanced_equipment_total+float(book_refine_basic_stats)),2)
	book_level = int(book_level_choosen)-1
	book_hp_var = float(book_var_raw)/100
	book_total = ceil(int(book_base)+(int(book_level)*float(book_inc)))

	egg_stats_active_atk = int(selected_egg1_stats["Attack"]) + int(selected_egg2_stats["Attack"]) + int(selected_egg3_stats["Attack"]) + int(selected_egg4_stats["Attack"]) + int(selected_egg5_stats["Attack"])
	egg_stats_active_hp = int(selected_egg1_stats["Max Hp"]) + int(selected_egg2_stats["Max Hp"]) + int(selected_egg3_stats["Max Hp"]) + int(selected_egg4_stats["Max Hp"]) + int(selected_egg5_stats["Max Hp"])
	cumul_atlar_passiv_flat_atk = int(altar_stuff_atk) + int(altar_hero_atk)
	cumul_atlar_passiv_flat_hp = int(altar_stuff_hp) + int(altar_hero_hp)
	cumul_fixe_bonus_jewel_atk_flat = int(stats_jewel['attack_ruby']) + int(stats_jewel['attack_kunzite']) + int(stats_jewel['attack_tourmaline']) + int(BonusSpe_jewel_weapon[0]) + int(BonusSpe_jewel_weapon[4]) + int(BonusSpe_jewel_bracelet[0]) + int(BonusSpe_jewel_bracelet[2]) + int(BonusSpe_jewel_bracelet[4])
	cumul_fixe_bonus_jewel_hp_flat = int(stats_jewel['pv_emerald']) + int(stats_jewel['pv_lapis']) + int(stats_jewel['pv_calaite']) + int(BonusSpe_jewel_armor[0]) + int(BonusSpe_jewel_armor[4]) + int(BonusSpe_jewel_bracelet[1]) + int(BonusSpe_jewel_locket[2]) + int(BonusSpe_jewel_locket[4])	
	cumul_all_bonus_passif_atk = int(cumul_talent_bonus_passif_atk) + int(cumul_hero_bonus_passif_atk) + int(cumul_skin_bonus_passif_atk) + int(cumul_egg_bonus_passif_atk) + int(atk_power_reforge) + int(atk_courage_reforge)
	cumul_all_bonus_passif_hp = int(cumul_talent_bonus_passif_hp) + int(cumul_runes_bonus_passif_hp) + int(cumul_hero_bonus_passif_hp) + int(cumul_skin_bonus_passif_hp) + int(cumul_egg_bonus_passif_hp)
	cumul_all_refine_passif_atk =  int(weapon_refine_atk) + int(ring1_refine_atk) + int(ring2_refine_atk) + int(bracelet_refine_atk)
	cumul_all_refine_passif_hp = int(armor_refine_hp) + int(locket_refine_hp) + int(book_refine_hp)

	cumul_dragon_stats_atk = int(stats_dragon_1["Attack"]) + int(stats_dragon_2["Attack"]) + int(stats_dragon_3["Attack"])
	cumul_dragon_stats_hp = int(stats_dragon_1["Max Hp"]) + int(stats_dragon_2["Max Hp"]) + int(stats_dragon_3["Max Hp"])
	cumul_fixe_bonus_jewel_atk_var =  (float(BonusSpe_jewel_weapon[2]) + float(BonusSpe_jewel_ring1[5]) + float(BonusSpe_jewel_book[2]))/100
	cumul_fixe_bonus_jewel_hp_var = (float(BonusSpe_jewel_book[3]) + float(BonusSpe_jewel_ring2[5]))/100
	cumul_var_bonus_eqpm_atk = (weapon_attack_var + bracelet_attack_var + ring1_atk_var + ring2_atk_var)
	cumul_var_bonus_eqpm_hp = (armor_hp_var + book_hp_var + ring1_hp_var + ring2_hp_var + locket_hp_var)	
	cumul_fixes_bonus_eqpm_atk = round(weapon_total + bracelet_total)
	cumul_fixes_bonus_eqpm_hp = round(armor_total + locket_total + book_total)
	coeff1_atk = (float(coeff_1_heros_var_passif_atk) + float(coeff_1_heros_var_actif_atk) + float(coeff_1_altar_var_passif_atk) + float(coeff_1_brave_privileges_var_passif_atk))
	coeff1_hp = round(((float(coeff_1_runes_var_passif_hp) + float(coeff_1_heros_var_passif_hp) + float(coeff_1_heros_var_actif_hp) + float(coeff_1_altar_var_passif_hp) + float(coeff_1_brave_privileges_var_passif_hp))/100),4)
	hero_base_modified_stats_atk = (int(atk_base_stats_hero_choosen) - int(courage_hero_attack_flat)) * (float(courage_hero_attack_var) + float(power_up_hero_base_total) + 1) + int(courage_hero_attack_flat)
	hero_base_modified_stats_hp = (int(health_base_stats_hero_choosen) - int(courage_hero_hp_flat)) * (float(courage_hero_hp_var) + float(power_up_hero_base_total) + 1) + int(courage_hero_hp_flat)

	
	global_stats_atk_flat = int(cumul_fixes_bonus_eqpm_atk) + int(egg_stats_active_atk) + int(cumul_atlar_passiv_flat_atk) + int(cumul_dragon_stats_atk) + int(brave_privileges_stats['Attack Flat'])
	global_stats_hp_flat = (floor(hero_base_modified_stats_hp)) + int(cumul_all_bonus_passif_hp) + int(cumul_fixes_bonus_eqpm_hp) + int(egg_stats_active_hp) + int(cumul_atlar_passiv_flat_hp) + int(cumul_dragon_stats_hp) + int(brave_privileges_stats['Hp Flat'])
	global_stats_atk = global_stats_atk_flat + (global_stats_atk_flat*float(coeff1_atk/100)) + (global_stats_atk_flat*float(cumul_var_bonus_eqpm_atk)) + (global_stats_atk_flat*float(cumul_fixe_bonus_jewel_atk_var)) + cumul_fixe_bonus_jewel_atk_flat + cumul_all_refine_passif_atk
	global_stats_hp = global_stats_hp_flat + (global_stats_hp_flat*float(coeff1_hp)) + (global_stats_hp_flat*float(cumul_var_bonus_eqpm_hp)) + (global_stats_hp_flat*float(cumul_fixe_bonus_jewel_hp_var)) + cumul_fixe_bonus_jewel_hp_flat + cumul_all_refine_passif_hp

	hero_atk_step = [
		user_stats.global_atk_save,
		cumul_all_bonus_passif_atk, # + int(runes_power_attack_flat) + int(runes_courage_attack_flat)
		coeff1_atk, # float(runes_power_attack_var) + float(runes_courage_attack_var)
		## hero_base_modified_stats_atk
		atk_base_stats_hero_choosen,
		power_up_hero_base_total,
		#global_stats_atk_flat
		global_stats_atk_flat, # + int(hero_base_modified_stats_atk) + cumul_all_bonus_passif_atk
		#global_stats_atk
		cumul_var_bonus_eqpm_atk,
		cumul_fixe_bonus_jewel_atk_var,
		cumul_fixe_bonus_jewel_atk_flat,
		cumul_all_refine_passif_atk,
		runes_power_attack_flat,
		runes_courage_attack_flat,
		runes_power_attack_var,
		runes_courage_attack_var,
		int(courage_hero_attack_flat),
		courage_hero_attack_var
	]

############################################# RÉSULTAT #############################################
# glyphs +1.5% boss dmg, glyphs +1.8% melee dmg, runes dmg_mobs +207 ?
#melee airborne boss =>  
#melee ground boss => fire demon (other than the egg) IG 52028 / calc 51626


	global_critic_damage = 7 + 200 + int(stats_jewel['crit_dmg_topaz']) + int(weapon_crit_raw) + int(ring1_crit_damage_raw) + int(ring2_crit_damage_raw) + int(bracelet_crit_raw) + int(selected_egg1_stats['Critic Damage']) + int(selected_egg2_stats['Critic Damage']) + int(selected_egg3_stats['Critic Damage']) + int(selected_egg4_stats['Critic Damage']) + int(UrasilStats[2]) + int(TaranisStats[3]) + int(HelixStats[0]) + int(AyanaStats[5]) + int(RollaStats[6]) + int(BonnieStats[0]) + int(ShadeStats[4]) + int(BonusSpe_jewel_weapon[1])
	
	flat_boss_damage = int(selected_egg1_stats['Damage To Bosses']) + int(selected_egg2_stats['Damage To Bosses']) + int(selected_egg3_stats['Damage To Bosses']) + int(selected_egg4_stats['Damage To Bosses']) + int(GetRingDamage(ring1_damage_type_raw,ring1_total)['boss units dmg']) + int(GetRingDamage(ring2_damage_type_raw,ring2_total)['boss units dmg']) + int(stats_jewel['dmg_to_boss'])
	var_boss_damage =  0

	flat_mobs_damage =  int(stats_dragon_1["Damage To Mobs"]) + int(stats_dragon_2["Damage To Mobs"]) + int(stats_dragon_3["Damage To Mobs"]) + int(selected_egg1_stats['Damage To Mobs']) + int(selected_egg2_stats['Damage To Mobs']) + int(selected_egg3_stats['Damage To Mobs']) + int(selected_egg4_stats['Damage To Mobs']) + int(GetRingDamage(ring1_damage_type_raw,ring1_total)['mobs units dmg']) + int(GetRingDamage(ring2_damage_type_raw,ring2_total)['mobs units dmg']) + int(stats_jewel['dmg_to_mobs'])
	var_mobs_damage = 0

	flat_ranged_damage = int(stats_dragon_1["Damage To Ranged Units"]) + int(stats_dragon_2["Damage To Ranged Units"]) + int(stats_dragon_3["Damage To Ranged Units"]) + int(GetRingDamage(ring1_damage_type_raw,ring1_total)['ranged units dmg']) + int(GetRingDamage(ring2_damage_type_raw,ring2_total)['ranged units dmg']) + int(selected_egg1_stats['Damage To Ranged Units']) + int(selected_egg2_stats['Damage To Ranged Units']) + int(selected_egg3_stats['Damage To Ranged Units']) + int(selected_egg4_stats['Damage To Ranged Units']) + int(RyanStats[0]) + int(MelindaStats[0]) + int(SylvanStats[5]) + int(RyanStats[5]) + int(MelindaStats[5]) + int(HelixStats[6]) + int(GuguStats[6])
	var_ranged_damage = float(GuguStats[2]) + float(AyanaStats[4]) + float(MelindaStats[4]) + float(SylvanStats[4]) + float(PhorenStats[4]) + float(AtreusStats[1]) + float(AyanaStats[1]) + float(SylvanStats[1])
	
	flat_ground_damage = int(stats_dragon_1["Damage To Ground Units"]) + int(stats_dragon_2["Damage To Ground Units"]) + int(stats_dragon_3["Damage To Ground Units"]) + int(GetRingDamage(ring1_damage_type_raw,ring1_total)['ground units dmg']) + int(GetRingDamage(ring2_damage_type_raw,ring2_total)['ground units dmg']) + int(selected_egg1_stats['Damage To Ground Units']) + int(selected_egg2_stats['Damage To Ground Units']) + int(selected_egg3_stats['Damage To Ground Units']) + int(selected_egg4_stats['Damage To Ground Units']) + int(ShadeStats[0]) + int(OpheliaStats[5]) + int(BlazoStats[5]) + int(SylvanStats[6])
	var_ground_damage = float(OnirStats[4]) + float(ShingenStats[4]) + float(PhorenStats[7]) + float(OnirStats[1]) + float(BlazoStats[3])
	
	flat_airborne_damage = int(GetRingDamage(ring1_damage_type_raw,ring1_total)['airborne units dmg']) + int(GetRingDamage(ring2_damage_type_raw,ring2_total)['airborne units dmg']) + int(selected_egg1_stats['Damage To Airborne Units']) + int(selected_egg2_stats['Damage To Airborne Units']) + int(selected_egg3_stats['Damage To Airborne Units']) + int(selected_egg4_stats['Damage To Airborne Units']) + int(AyanaStats[0]) + int(GuguStats[0]) + int(RyanStats[2]) + int(PhorenStats[5]) + int(GuguStats[5]) + int(TaranisStats[6]) + int(RyanStats[6]) + int(IrisStats[6]) + int(ElaineStats[0])
	var_airborne_damage = float(TaranisStats[4]) + float(IrisStats[4]) + float(TaranisStats[1])
	
	flat_melee_damage = int(stats_dragon_1["Damage To Melee Units"]) + int(stats_dragon_2["Damage To Melee Units"]) + int(stats_dragon_3["Damage To Melee Units"]) + int(GetRingDamage(ring1_damage_type_raw,ring1_total)['melee units dmg']) + int(GetRingDamage(ring2_damage_type_raw,ring2_total)['melee units dmg']) + int(selected_egg1_stats['Damage To Melee Units']) + int(selected_egg2_stats['Damage To Melee Units']) + int(selected_egg3_stats['Damage To Melee Units']) + int(selected_egg4_stats['Damage To Melee Units']) + int(ShariStats[0]) + int(ShingenStats[0]) + int(BlazoStats[0]) + int(RollaStats[5]) + int(ShingenStats[5]) + int(ShariStats[6])
	var_melee_damage = float(ShariStats[3]) + float(MelindaStats[2]) + float(UrasilStats[4]) + float(OpheliaStats[4]) + float(LinaStats[4]) + float(UrasilStats[1]) + float(OpheliaStats[1]) + float(ShingenStats[3]) + float(ElaineStats[4])
	
	flat_elemental_damage = 0
	var_elemental_damage = float((stats_jewel['elementary_dmg_amber']) + float(SylvanStats[7]))
	
	flat_all_damage = 0
	var_all_damage = 0
	weapon_dmg_multiplier = WeaponHiddenStats[str(weapon_name_choosen.lower().replace(" ","_")) + "_dmg_multiplier"]

	cookie_keys = checkDarkMode(request.COOKIES)
	
	if "modeDisplay" in list(cookie_keys):
		darkmode = "yes"
	else:
		darkmode = "no"
	if request.method == "GET":
		try:
			models.dmg_calc_table.objects.get(ingame_id=iid_modified)
			calc_user_dmg = models.dmg_calc_table.objects.filter(ingame_id=iid_modified)
			calc_user_dmg.update(
				ingame_id = user_stats.ingame_id,
				hero_atk = hero_atk_step,
				weapon_coeff = weapon_dmg_multiplier,
				flat_dmg_vs_ground = flat_ground_damage,
				flat_dmg_vs_airborne = flat_airborne_damage,
				flat_dmg_vs_melee = flat_melee_damage,
				flat_dmg_vs_range = flat_ranged_damage,
				flat_dmg_vs_mobs = flat_mobs_damage,
				flat_dmg_vs_boss = flat_boss_damage,
				flat_dmg_element = flat_elemental_damage,
				flat_dmg_all = flat_all_damage,
				var_dmg_vs_ground = var_ground_damage,
				var_dmg_vs_airborne = var_airborne_damage,
				var_dmg_vs_melee = var_melee_damage,
				var_dmg_vs_range = var_ranged_damage,
				var_dmg_vs_mobs = var_mobs_damage,
				var_dmg_vs_boss = var_boss_damage,
				var_dmg_element = var_elemental_damage,
				var_dmg_all = var_all_damage,
				crit_dmg = global_critic_damage
			)
		except Exception as e:
			calc_user_dmg = dmg_calc_table(
				ingame_id = user_stats.ingame_id,
				hero_atk = hero_atk_step,
				weapon_coeff = weapon_dmg_multiplier,
				flat_dmg_vs_ground = flat_ground_damage,
				flat_dmg_vs_airborne = flat_airborne_damage,
				flat_dmg_vs_melee = flat_melee_damage,
				flat_dmg_vs_range = flat_ranged_damage,
				flat_dmg_vs_mobs = flat_mobs_damage,
				flat_dmg_vs_boss = flat_boss_damage,
				flat_dmg_element = flat_elemental_damage,
				flat_dmg_all = flat_all_damage,
				var_dmg_vs_ground = var_ground_damage,
				var_dmg_vs_airborne = var_airborne_damage,
				var_dmg_vs_melee = var_melee_damage,
				var_dmg_vs_range = var_ranged_damage,
				var_dmg_vs_mobs = var_mobs_damage,
				var_dmg_vs_boss = var_boss_damage,
				var_dmg_element = var_elemental_damage,
				var_dmg_all = var_all_damage,
				crit_dmg = global_critic_damage
			)
			calc_user_dmg.save()
		return HttpResponseRedirect(f"/wiki/damage_calculator/{iid}/", {"darkmode": darkmode,"header_msg":"Stats Calculator","lang":lang})
	else :
		return HttpResponseRedirect("/wiki/damage_calculator/", {"darkmode": darkmode,"header_msg":"Damage Calculator","lang":lang})


def damageCalc(request,iid):
	cookie_keys = checkDarkMode(request.COOKIES)
	if "modeDisplay" in list(cookie_keys):
		darkmode = "yes"
	else:
		darkmode = "no"

	iid_modified1 = ''.join(i for i in str(iid) if i.isdigit())
	iid_modified = iid_modified1[0] + "-" + iid_modified1[1:-1] + iid_modified1[-1]
	calc_user_dmg = models.dmg_calc_table.objects.get(ingame_id=iid_modified)
	ctx = {
		"ingame_id": calc_user_dmg.ingame_id,
		"paramDmgTable": calc_user_dmg.hero_atk,
		"weapon_coeff": calc_user_dmg.weapon_coeff,
		"flat_dmg_vs_ground": calc_user_dmg.flat_dmg_vs_ground,
		"flat_dmg_vs_airborne": calc_user_dmg.flat_dmg_vs_airborne,
		"flat_dmg_vs_melee": calc_user_dmg.flat_dmg_vs_melee,
		"flat_dmg_vs_range": calc_user_dmg.flat_dmg_vs_range,
		"flat_dmg_vs_mobs": calc_user_dmg.flat_dmg_vs_mobs,
		"flat_dmg_vs_boss": calc_user_dmg.flat_dmg_vs_boss,
		"flat_dmg_element": calc_user_dmg.flat_dmg_element,
		"flat_dmg_all": calc_user_dmg.flat_dmg_all,
		"var_dmg_vs_ground": calc_user_dmg.var_dmg_vs_ground,
		"var_dmg_vs_airborne": calc_user_dmg.var_dmg_vs_airborne,
		"var_dmg_vs_melee": calc_user_dmg.var_dmg_vs_melee,
		"var_dmg_vs_range": calc_user_dmg.var_dmg_vs_range,
		"var_dmg_vs_mobs": calc_user_dmg.var_dmg_vs_mobs,
		"var_dmg_vs_boss": calc_user_dmg.var_dmg_vs_boss,
		"var_dmg_element": calc_user_dmg.var_dmg_element,
		"var_dmg_all": calc_user_dmg.var_dmg_all,
		"crit_dmg": calc_user_dmg.crit_dmg,
		'darkmode':darkmode,
		"header_msg": "Damage Calc",
		"lang":lang
	}
	requestJson(request)
	return render(request, "wiki/dmg_calc.html", ctx)


def ghssetGrid(request):
	cookie_keys = checkDarkMode(request.COOKIES)
	if "modeDisplay" in list(cookie_keys):
		darkmode = "yes"
	else:
		darkmode = "no"
	ctx = {
		'darkmode':darkmode,
		"header_msg": "Google Sheet Wiki",
		"lang":lang
	}
	requestJson(request)
	return render(request, "wiki/gsheet.html", ctx)


def handler404(request, exception):
	cookie_keys = checkDarkMode(request.COOKIES)
	if "modeDisplay" in list(cookie_keys):
		darkmode = "yes"
	else:
		darkmode = "no"
	ctx = {
		'darkmode':darkmode,
		"header_msg":"Page Not Found",
		"lang":lang
	}
	return render(request,'base/404.html', ctx, status=404)

def handler500(request):
	allfile = os.listdir('calculator/static/traceback_file/')
	for file in allfile:
		os.remove(f'calculator/static/traceback_file/{file}')
	exc_info = list(sys.exc_info())
	exc_output = list(traceback.format_exception(exc_info[1]))
	cookieRequest = checkCookie(request.COOKIES)
	try:
		username = list(cookieRequest)[0]
	except:
		username = 'unknown'
	with open(f'calculator/static/traceback_file/{username}.txt','a', encoding='utf-8') as exc_value:
		for i in exc_output:
			exc_value.write(i)
	webhook = DiscordWebhook(url='$URLWEBHOOK', content="<@382930544385851392>", rate_limit_retry=True)
	embed = DiscordEmbed(title='Error 500 - Internal Server Error', description='', color='963e3e')
	embed.set_author(
		name=username.capitalize(),
		icon_url="https://stats.wiki-archero.com/static/image/favicon.png",
	)
	embed.add_embed_field(name='Request', value=f"{request.method} | {request.path}", inline=False)
	embed.add_embed_field(name='Cookie', value=f"{request.COOKIES}", inline=False)
	webhook.add_embed(embed)
	with open(f'calculator/static/traceback_file/{username}.txt','r', encoding='utf-8') as f:
		webhook.add_file(file=f.read(), filename=f'{username}.txt')
	response = webhook.execute()
	return render(request,'base/500.html', {"header_msg":"Internal Error Server", 'lang':lang},status=500)