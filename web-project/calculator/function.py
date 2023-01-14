from datetime import datetime
import json
from PIL import Image
from pathlib import Path
import random as random
import string
from discord_webhook import DiscordWebhook, DiscordEmbed

def makeLog(request, myLog):
	dict_log = {
		"dateLog": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
		"container": "archero",
		"app": "archero",
		"url": {
			"request method":request.method,
			"request path": request.path,
		},
		"header": {
			"Host": f"{request.headers['Host']}",
			"User-Agent": f"{request.headers['User-Agent']}",
			"Cookie": f"{request.COOKIES}",
			"AUTH":f"{request.user}: {request.user.is_authenticated}",
		},
		"myLog":{
			"ingame_id_user":myLog["ingame_id_user"],
			"ingame_name_user":myLog["ingame_name_user"],
			"missing_data":myLog["missing_data"],
			"stats_submit":myLog["stats_submit"],
			"cookie_value_pop":myLog["cookie_value_pop"],
			"error_form":myLog["error_form_msg"],
			"index_ingame_id_cookie":myLog["index_ingame_id_cookie"],
		}
	}
	json_log = json.dumps(dict_log, indent=1)
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

def RoundTen(x):
	if int(x) % 10==0:
		x = x
	else:
		while int(x) % 10>0:
			x=x-1
	return x

def all_formIsValid(valid_User, valid_StuffTable, valid_HeroTable, valid_TalentTable, valid_SkinTable, valid_AltarTable, valid_JewelTypeTable, valid_JewelLevelTable, valid_EggTable, valid_EggEquippedTable, valid_DragonTable, valid_RunesTable, valid_ReforgeTable, valid_RefineTable):
	if valid_User and valid_StuffTable and valid_HeroTable and valid_TalentTable and valid_SkinTable and valid_AltarTable and valid_JewelTypeTable and valid_JewelLevelTable and valid_EggTable and valid_EggEquippedTable and valid_DragonTable and valid_RunesTable and valid_ReforgeTable and valid_RefineTable:
		return True
	else:
		return False

def findFormError(valid_User, valid_StuffTable, valid_HeroTable, valid_TalentTable, valid_SkinTable, valid_AltarTable, valid_JewelTypeTable, valid_JewelLevelTable, valid_EggTable, valid_EggEquippedTable, valid_DragonTable, valid_RunesTable, valid_ReforgeTable, valid_RefineTable):
	listform = [valid_User, valid_StuffTable, valid_HeroTable, valid_TalentTable, valid_SkinTable, valid_AltarTable, valid_JewelTypeTable, valid_JewelLevelTable, valid_EggTable, valid_EggEquippedTable, valid_DragonTable, valid_RunesTable, valid_ReforgeTable, valid_RefineTable]
	for i in listform:
		if i != "":
			form_error = i.errors.items()
			for k,v in form_error:
				return k,v
		else:
			return





################################# FONCTION CALCUL #######################################################
def CalculAltar(base,level,levelRoundTen,inc):
		diff = level - levelRoundTen
		if 1 <= diff <= 9:
			total = base+((level - levelRoundTen)*inc)
		else:
			total = base
		return total

def ReforgePowerCourage(reforge_stats):
	if int(reforge_stats) <=400:
		stats_reforge = int(reforge_stats) 
	elif int(reforge_stats) > 400:
		stats_reforge = 400+(int(reforge_stats)-400)/50*30
	return stats_reforge

def ReforgeSaviourRecoLuck(reforge_stats):
	if int(reforge_stats) <=400:
		stats_reforge = (int(reforge_stats)/20)*60
	elif int(reforge_stats) > 400:
		stats_reforge = 1200+(int(reforge_stats)-400)/50*100
	return stats_reforge

def CourageBoostHero(heros_equipped,runes_courage_boost):
	hero = runes_courage_boost.split("_")[0]
	boost = runes_courage_boost.split("_")[1]
	if heros_equipped == hero:
		boost_runes = boost
	else:
		boost_runes = 0
	return boost_runes

def GetRingDamage(ring_damage_type,total):
	dict_result = {
		"boss units dmg": "0",
		"mobs units dmg": "0",
		"ranged units dmg": "0",
		"melee units dmg": "0",
		"airborne units dmg": "0",
		"ground units dmg": "0",
		"elite mobs dmg": "0",
		"non-elite mobs dmg": "0",
		"0":"0",  ## au cas où le ring choisi est none
		ring_damage_type:total,
	}
	return dict_result


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
	if user in liste_username:
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
			"username":username,
			"ingame_id":username_id,
			"number_request":0
		}
		request_json_file['user'].append(data)
	elif bool_func == False:
		for i in request_json_file['user']:
			if i['username'] == username:
				i['number_request'] += 1

	with open('calculator/static/json/requetes.json', "w") as jsonFile:
		json.dump(request_json_file, jsonFile)