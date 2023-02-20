from datetime import datetime
import json
from PIL import Image
from pathlib import Path
import random as random
import string
from discord_webhook import DiscordWebhook, DiscordEmbed
from .data import *
from difflib import SequenceMatcher
import time
from . import models


# def makeLog(request, myLog):
# 	dict_log = {
# 		"dateLog": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
# 		"container": "archero",
# 		"app": "archero",
# 		"url": {
# 			"request method":request.method,
# 			"request path": request.path,
# 		},
# 		"header": {
# 			"Host": f"{request.headers['Host']}",
# 			"User-Agent": f"{request.headers['User-Agent']}",
# 			"Cookie": f"{request.COOKIES}",
# 			"AUTH":f"{request.user}: {request.user.is_authenticated}",
# 		},
# 		"myLog":{
# 			"ingame_id_user":myLog["ingame_id_user"],
# 			"ingame_name_user":myLog["ingame_name_user"],
# 			"missing_data":myLog["missing_data"],
# 			"stats_submit":myLog["stats_submit"],
# 			"cookie_value_pop":myLog["cookie_value_pop"],
# 			"error_form":myLog["error_form_msg"],
# 			"index_ingame_id_cookie":myLog["index_ingame_id_cookie"],
# 		}
# 	}
# 	json_log = json.dumps(dict_log, indent=1)
# 	print(json_log)

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


def all_formIsValid(valid_User, valid_StuffTable, valid_HeroTable, valid_TalentTable, valid_SkinTable, valid_AltarTable, valid_JewelTypeTable, valid_JewelLevelTable, valid_EggTable, valid_EggEquippedTable, valid_DragonTable, valid_RunesTable, valid_ReforgeTable, valid_RefineTable, valid_MedalTable, valid_RelicTable):
	if valid_User and valid_StuffTable and valid_HeroTable and valid_TalentTable and valid_SkinTable and valid_AltarTable and valid_JewelTypeTable and valid_JewelLevelTable and valid_EggTable and valid_EggEquippedTable and valid_DragonTable and valid_RunesTable and valid_ReforgeTable and valid_RefineTable and valid_MedalTable and valid_RelicTable:
		return True
	else:
		return False

def findFormError(valid_User, valid_StuffTable, valid_HeroTable, valid_TalentTable, valid_SkinTable, valid_AltarTable, valid_JewelTypeTable, valid_JewelLevelTable, valid_EggTable, valid_EggEquippedTable, valid_DragonTable, valid_RunesTable, valid_ReforgeTable, valid_RefineTable, valid_MedalTable, valid_RelicTable):
	listform = [valid_User, valid_StuffTable, valid_HeroTable, valid_TalentTable, valid_SkinTable, valid_AltarTable, valid_JewelTypeTable, valid_JewelLevelTable, valid_EggTable, valid_EggEquippedTable, valid_DragonTable, valid_RunesTable, valid_ReforgeTable, valid_RefineTable,valid_MedalTable,valid_RelicTable]
	for i in listform:
		if i != "":
			form_error = i.errors.items()
			for k,v in form_error:
				return k,v
		else:
			return


################################# FONCTION CALCUL #######################################################

def medal_calc(medalsList):
	attack = 0
	attack_var = 0
	hp = 0
	hp_var = 0
	hero_base_enhanced = 0
	enhance_equipment = 0
	for i in medalsList:
		if i.split("-")[0] == "True":
			type_medal_boost = MedalsStats["type_" + str(i.split("-")[1])]
			if type_medal_boost == "Attack":
				attack += MedalsStats["stats_" + str(i.split("-")[1])]
			elif type_medal_boost == "Attack%":
				attack_var += MedalsStats["stats_" + str(i.split("-")[1])]
			elif type_medal_boost == "Hp":
				hp += MedalsStats["stats_" + str(i.split("-")[1])]
			elif type_medal_boost == "Hp%":
				attack_var += MedalsStats["stats_" + str(i.split("-")[1])]
			elif type_medal_boost == "Hero Base Enhanced":
				hero_base_enhanced += MedalsStats["stats_" + str(i.split("-")[1])]
			elif type_medal_boost == "Enhance Equipment":
				enhance_equipment += MedalsStats["stats_" + str(i.split("-")[1])]
	returned_stats = {
		"attack":attack,
		"attack_var":attack_var,
		"hp":hp,
		"hp_var":hp_var,
		"hero_base_enhanced":hero_base_enhanced,
		"enhance_equipment":enhance_equipment
	}
	return returned_stats

def relics_Stats(list_relic):
		stats = {
			'':0,
			"attack": 0,
			"attack_var": 0,
			"hp": 0,
			"hp_var": 0,
			"enhance_equipment_var": 0,
			"hero_base_stats_increased_var": 0,
			"crit_chance_var": 0,
			"damage_ranged_units": 0,
			"damage_melee_units": 0,
			"damage_humanoid_enemies_var": 0,
			"damage_undead_var": 0,
			"damage_heroes_var": 0,
			"elemental_damage_var": 0,
			"damage_mobs": 0,
			"damage_mobs_var": 0,
			"damage_bosses": 0,
			"damage_bosses_var": 0,
			"damage_ground_units": 0,
			"damage_ground_units_var": 0,
			"damage_airborne_units": 0,
			"damage_airborne_units_var": 0,
			"weapon_melee_damage_var": 0,
			"weapon_ranged_damage_var": 0,
			"dodge":0,
			"attack_jewel_base":0,
		}
		relic_name = ["wraith_mask","clown_mask","princess_teddy_bear","belt_of_might","beastmaster_whistle","archmage_robe","shimmering_gem","bloom_of_eternity","challenger_headband","jade_gobelet","veteran_plate","dragonscale","dragon_tooth","scholar_telescope","pirate_shank","giant_greatsword","healing_potion","whirlwind_mauler","special_lance","precision_slingshot","supreme_trinity_alpha","golden_apple","ancient_stele","philosopher_stone","dragon_heart","spectral_duality","mystic_emblem","immortal_brooch","golden_statue","smilling_mask","unmerciful_mask","holy_water","book_of_the_dead","psionist_treasure","book_of_archery","book_of_bravery","angelic_heart","devil_whisper","stone_of_wisdom","empyrean_mirror","fabled_archer_arrow","shiny_gemmed_belt","mythril_flux_mail","stealth_boots","assassin_dagger","gold_bunny","genesis_staff","bloodstained_sword","starcluster_rage","elven_king_cape","spear_of_yggdrasil","dragon_gem","life_crown","sand_of_time","first_lightning","oracle_quill","bloodthirsty_grail","healing_grail","cupids_necklace"]
		for i in range(0,len(list_relic)):
			relic = relic_name[i]
			relic_boost = list_relic[i]
			for x in range(0,len(relic_boost)):
				search_data = RelicLabel[str(relic)+ "_" +str(x+1)]
				new_value = float(stats[search_data]) + float(relic_boost[x])
				stats.update({search_data:new_value})
		return stats

def calculDamage(ingame_id):
	user_stats = models.user.objects.get(ingame_id=ingame_id)
	calc_user_dmg = models.dmg_calc_table.objects.get(ingame_id=ingame_id)
	crit_dmg = int(calc_user_dmg.crit_dmg)/100
	mob_ground_melee = round((int(user_stats.global_atk_save) + int(calc_user_dmg.flat_dmg_vs_ground) + int(calc_user_dmg.flat_dmg_vs_mobs) + int(calc_user_dmg.flat_dmg_vs_melee) + int(calc_user_dmg.flat_dmg_all))*(float(calc_user_dmg.var_dmg_vs_melee/100) + float(calc_user_dmg.var_dmg_vs_ground/100) + float(1))*(float(calc_user_dmg.var_dmg_vs_mobs/100) + float(1))*(float(calc_user_dmg.var_dmg_all/100) + float(1))*(float(calc_user_dmg.weapon_coeff)))
	mob_ground_range = round((int(user_stats.global_atk_save) + int(calc_user_dmg.flat_dmg_vs_ground) + int(calc_user_dmg.flat_dmg_vs_mobs) + int(calc_user_dmg.flat_dmg_vs_range) + int(calc_user_dmg.flat_dmg_all))*(float(calc_user_dmg.var_dmg_vs_range/100) + float(calc_user_dmg.var_dmg_vs_ground/100) + float(1))*(float(calc_user_dmg.var_dmg_vs_mobs/100) + float(1))*(float(calc_user_dmg.var_dmg_all/100) + float(1))*(float(calc_user_dmg.weapon_coeff)))
	mob_airborne_melee = round((int(user_stats.global_atk_save) + int(calc_user_dmg.flat_dmg_vs_airborne) + int(calc_user_dmg.flat_dmg_vs_mobs) + int(calc_user_dmg.flat_dmg_vs_melee) + int(calc_user_dmg.flat_dmg_all))*(float(calc_user_dmg.var_dmg_vs_melee/100) + float(calc_user_dmg.var_dmg_vs_airborne/100) + float(1))*(float(calc_user_dmg.var_dmg_vs_mobs/100) + float(1))*(float(calc_user_dmg.var_dmg_all/100) + float(1))*(float(calc_user_dmg.weapon_coeff)))
	mob_airborne_range = round((int(user_stats.global_atk_save) + int(calc_user_dmg.flat_dmg_vs_airborne) + int(calc_user_dmg.flat_dmg_vs_mobs) + int(calc_user_dmg.flat_dmg_vs_range) + int(calc_user_dmg.flat_dmg_all))*(float(calc_user_dmg.var_dmg_vs_range/100) + float(calc_user_dmg.var_dmg_vs_airborne/100) + float(1))*(float(calc_user_dmg.var_dmg_vs_mobs/100) + float(1))*(float(calc_user_dmg.var_dmg_all/100) + float(1))*(float(calc_user_dmg.weapon_coeff)))
	boss_ground_melee = round((int(user_stats.global_atk_save) + int(calc_user_dmg.flat_dmg_vs_ground) + int(calc_user_dmg.flat_dmg_vs_boss) + int(calc_user_dmg.flat_dmg_vs_melee) + int(calc_user_dmg.flat_dmg_all))*(float(calc_user_dmg.var_dmg_vs_melee/100) + float(calc_user_dmg.var_dmg_vs_ground/100) + float(1))*(float(calc_user_dmg.var_dmg_vs_boss/100) + float(1))*(float(calc_user_dmg.var_dmg_all/100) + float(1))*(float(calc_user_dmg.weapon_coeff)))
	boss_ground_range = round((int(user_stats.global_atk_save) + int(calc_user_dmg.flat_dmg_vs_ground) + int(calc_user_dmg.flat_dmg_vs_boss) + int(calc_user_dmg.flat_dmg_vs_range) + int(calc_user_dmg.flat_dmg_all))*(float(calc_user_dmg.var_dmg_vs_range/100) + float(calc_user_dmg.var_dmg_vs_ground/100) + float(1))*(float(calc_user_dmg.var_dmg_vs_boss/100) + float(1))*(float(calc_user_dmg.var_dmg_all/100) + float(1))*(float(calc_user_dmg.weapon_coeff)))
	boss_airborne_melee = round((int(user_stats.global_atk_save) + int(calc_user_dmg.flat_dmg_vs_airborne) + int(calc_user_dmg.flat_dmg_vs_boss) + int(calc_user_dmg.flat_dmg_vs_melee) + int(calc_user_dmg.flat_dmg_all))*(float(calc_user_dmg.var_dmg_vs_melee/100) + float(calc_user_dmg.var_dmg_vs_airborne/100) + float(1))*(float(calc_user_dmg.var_dmg_vs_boss/100) + float(1))*(float(calc_user_dmg.var_dmg_all/100) + float(1))*(float(calc_user_dmg.weapon_coeff)))
	boss_airborne_range = round((int(user_stats.global_atk_save) + int(calc_user_dmg.flat_dmg_vs_airborne) + int(calc_user_dmg.flat_dmg_vs_boss) + int(calc_user_dmg.flat_dmg_vs_range) + int(calc_user_dmg.flat_dmg_all))*(float(calc_user_dmg.var_dmg_vs_range/100) + float(calc_user_dmg.var_dmg_vs_airborne/100) + float(1))*(float(calc_user_dmg.var_dmg_vs_boss/100) + float(1))*(float(calc_user_dmg.var_dmg_all/100) + float(1))*(float(calc_user_dmg.weapon_coeff)))
	
	mob_ground_melee_damage = [mob_ground_melee,int(mob_ground_melee*crit_dmg)]
	mob_ground_range_damage = [mob_ground_range,int(mob_ground_range*crit_dmg)]
	mob_airborne_melee_damage = [mob_airborne_melee,int(mob_airborne_melee*crit_dmg)]
	mob_airborne_range_damage = [mob_airborne_range,int(mob_airborne_range*crit_dmg)]
	boss_ground_melee_damage = [boss_ground_melee,int(boss_ground_melee*crit_dmg)]
	boss_ground_range_damage = [boss_ground_range,int(boss_ground_range*crit_dmg)]
	boss_airborne_melee_damage = [boss_airborne_melee,int(boss_airborne_melee*crit_dmg)]
	boss_airborne_range_damage = [boss_airborne_range,int(boss_airborne_range*crit_dmg)]
	averageDamage = round(
		int(mob_ground_melee_damage[0])+
		int(mob_ground_range_damage[0])+
		int(mob_airborne_melee_damage[0])+
		int(mob_airborne_range_damage[0])+
		int(boss_ground_melee_damage[0])+
		int(boss_ground_range_damage[0])+
		int(boss_airborne_melee_damage[0])+
		int(boss_airborne_range_damage[0])
	)/8
	averageDamageAll = round(averageDamage * (1 + (calc_user_dmg.crit_rate/100) * (crit_dmg - 1)))
	return {
		"averageDamageAll": averageDamageAll,
		"mob_ground_melee_damage": [mob_ground_melee,int(mob_ground_melee*crit_dmg)],
		"mob_ground_range_damage": [mob_ground_range,int(mob_ground_range*crit_dmg)],
		"mob_airborne_melee_damage": [mob_airborne_melee,int(mob_airborne_melee*crit_dmg)],
		"mob_airborne_range_damage": [mob_airborne_range,int(mob_airborne_range*crit_dmg)],
		"boss_ground_melee_damage": [boss_ground_melee,int(boss_ground_melee*crit_dmg)],
		"boss_ground_range_damage": [boss_ground_range,int(boss_ground_range*crit_dmg)],
		"boss_airborne_melee_damage": [boss_airborne_melee,int(boss_airborne_melee*crit_dmg)],
		"boss_airborne_range_damage": [boss_airborne_range,int(boss_airborne_range*crit_dmg)],
	}

################################# FONCTION RESTE #######################################################

def checkCookie(cookie_value):
	cookiePopList = ['csrftoken','sessionid','windowInnerWidth','windowInnerHeight', 'modeDisplay']
	for i in cookiePopList:
		try:
			cookie_value.pop(i)
		except:
			pass
	return cookie_value


def checkDarkMode(cookie_value):
	return cookie_value

def userExist(json, user):
	liste_username = []
	for i in list(json['user']):
		liste_username.append(i['username'])
	if str(user).lower() in liste_username:
		return False
	else:
		return True

def requestJson(request):
	with open('calculator/static/json/requetes.json', "r") as jsonFile:
		request_json_file = json.load(jsonFile)
	cookie = checkCookie(request.COOKIES)
	try:
		username = list(cookie)[0]
		username_id = request.COOKIES[username]
	except:
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
	a = a.replace('*', '') ## pour ceux qui ont mis un character unterdis dans le cookie 
	b = b.replace('*', '') ## vu que le character interdis est remplacé par un *
	return SequenceMatcher(None, a, b).ratio()

def create_unique_id():
	unique_id = str(time.time()).replace('.','')
	return unique_id


def send_webhook(msg):
	wh = DiscordWebhook(url='WEBHOOK_URL', content=msg, rate_limit_retry=True)
	response = wh.execute()