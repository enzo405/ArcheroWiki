from datetime import datetime
from PIL import Image
from pathlib import Path
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from discord_webhook import DiscordWebhook, DiscordEmbed
from django.contrib import messages
from .data import *
from difflib import SequenceMatcher
from . import models
import http.cookies
import random as random
import json
import string
import time
import re
import urllib.parse


WEBHOOK_URL = "https://discord.com/api/webhooks/#########/#############################################"
WEBHOOK_URL2 = "https://discord.com/api/webhooks/#########/#############################################"

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

def checkCookie(cookie_value:dict):
	requestCookie = cookie_value.copy()
	result = {}
	for k,v in requestCookie.items():
		check_credential = checkUsernameCredentials(k,v)
		if check_credential[0]:
			result.update({k:v})
	return result

def login_required(func):
	def wrapper(request, *args, **kwargs):
		result = checkCookie(request.COOKIES)
		if len(result) == 0:
			messages.warning(request, f"You need to login first")
			return render(request, "login.html")
		elif len(result) >= 2:
			send_webhook(f"Log : {result} \n{request.COOKIES}\n{request.build_absolute_uri()}")
		request.session['user_credential'] = result
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
	with open('calculator/static/json/requetes.json', "r") as jsonFile:
		request_json_file = json.load(jsonFile)
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


def checkUsernameCredentials(username_raw,id_raw):
	pattern = re.compile(r'^\d{1}-\d{6,12}$')    # Compile un motif de regex pour les identifiants de jeu valides
	decoded_bytes = urllib.parse.unquote(username_raw).encode('utf-8') # Décode le nom d'utilisateur brut en octets et encode la chaîne de caractères décodée en octets
	ingame_name = decoded_bytes.decode('utf-8') # Remplace tous les caractères illégaux par "*" après avoir converti la chaîne de bytes en une chaîne de caractères en utf-8
	ingame_id = urllib.parse.unquote(id_raw)   # Décode l'identifiant de jeu brut
	unavailable_username = ['csrftoken','sessionid','windowInnerWidth','windowInnerHeight', 'modeDisplay', 'messages', 'sessionid']
	if 3 <= len(ingame_name) < 20 and ingame_name not in unavailable_username:
		if re.fullmatch(pattern, ingame_id) and ingame_id != "" and ingame_id != None and all(c.isdigit() or c == '-' for c in ingame_id):
			return True, ingame_name, ingame_id
		else:
			return False, ingame_name, ingame_id,"Ingame id incorrect"
	else:
		return False, ingame_name, ingame_id,"Username not allowed"


def checkIllegalKey(string:str):
	for i in string:
		try:
			cookies = http.cookies.SimpleCookie()
			cookies[str(i)] = 'check'  # Cette ligne provoque une CookieError
		except http.cookies.CookieError:
			return i
	return string

def send_webhook(msg):
	wh = DiscordWebhook(url=WEBHOOK_URL, content=msg, rate_limit_retry=True)
	wh.execute()

def send_embed(author_name:str,title_embed:str,description_embed:str,field_name:str,field_value:str,e_color:int, request, alert:bool):
	if alert:
		content_msg = "<@&1091459880700874882>"
	else:
		content_msg = ""
	webhook = DiscordWebhook(url=WEBHOOK_URL, content=content_msg, rate_limit_retry=True, allowed_mentions={"roles": ["<@&1091459880700874882>",]})
	embed = DiscordEmbed(title=str(title_embed), description=str(description_embed), color=e_color)
	embed.set_author(
		name=str(author_name),
		icon_url="https://stats.wiki-archero.com/static/image/favicon.png",
	)
	embed.add_embed_field(name=str(field_name), value=str(field_value), inline=False)
	embed.set_footer(text=f'{request.COOKIES}', icon_url='')
	webhook.add_embed(embed)
	webhook.execute()


def checkTheme_Request(request, cookie_result):
	requestJson(request,cookie_result)
	if "modeDisplay" in list(request.COOKIES):
		return "yes"
	else:
		return "no"	

def calculatePrice(lvl1, lvl2, type, rank=None):
	if type == "talents":
		talent_cost_gold = DataPrice['talent']['gold']
		return talent_cost_gold[lvl2] - talent_cost_gold[lvl1]
	elif type == "items":
		item_cost_gold = DataPrice['item']['gold']
		item_cost_scroll = DataPrice['item']['scroll']
		return [item_cost_gold[lvl2] - item_cost_gold[lvl1], item_cost_scroll[lvl2] - item_cost_scroll[lvl1]]
	elif type == "heroes":
		heros_cost_gold = DataPrice['hero']['gold']
		heros_cost_sapphire = DataPrice['hero']['sapphire']
		return [heros_cost_gold[lvl2] - heros_cost_gold[lvl1], heros_cost_sapphire[lvl2] - heros_cost_sapphire[lvl1]]
	elif type == "dragons":
		dragon_cost_gold = DataPrice['dragon']['gold']
		dragon_cost_magestone = DataPrice['dragon']['magestone']
		result = [dragon_cost_gold[lvl2] - dragon_cost_gold[lvl1], dragon_cost_magestone[lvl2] - dragon_cost_magestone[lvl1]]
		if rank == "A":
			return [result[0],result[1]]
		elif rank == "S":
			return [int(result[0])*1.5,int(result[1])*1.5]
		elif rank == "SS":
			return [int(result[0])*2,int(result[1])*2]
	elif type == "relics":
		relics_cost_gold = DataPrice['relics']['gold']
		relics_cost_starlight = DataPrice['relics']['starlight']
		result = [relics_cost_gold[lvl2] - relics_cost_gold[lvl1], relics_cost_starlight[lvl2] - relics_cost_starlight[lvl1]]
		if rank == "A":
			return [result[0],result[1]]
		elif rank == "S":
			return [int(result[0])*1.5,int(result[1])*1.5]
		elif rank == "SS":
			return [int(result[0])*2,int(result[1])*2]