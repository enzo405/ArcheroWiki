from .forms import DamageCalculatorForm
from .models import articleMenu,user,stuff_table,hero_table,talent_table,skin_table,altar_table,jewel_level_table,egg_table,egg_equipped_table,dragon_table,runes_table,reforge_table,refine_table,medals_table,relics_table,weapon_skins_table,dmg_calc_table,promo_code
from .function import delete_visitor,checkDarkMode,checkMessages,checkCookie,checkUsernameCredentials,checkIllegalKey,send_webhook,send_embed,MakeLogAddRequestJson,calculatePrice,makeCookieheader,db_maintenance, getProfileWithCookie, login_required, checkContributor
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from http.cookies import CookieError
from math import *
from urllib.request import urlopen
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import timedelta, datetime
import json, os, sys, traceback
from const import WEBHOOK_URL, c_hostname, DISCORD_NOTIF_ROLE_ID, DISCORD_ERROR_ROLE_ID, DEV_MODE

lang = ["English","Francais","Deutsch","Russian","Española"]
missing_data = []

@db_maintenance
@delete_visitor("menu")
@checkMessages
def menu(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	list_article = list(articleMenu.objects.all().filter(display=True).order_by('index'))
	return render(request, 'base/menu.html', {"darkmode": checkDarkMode(request), "header_msg": "Menu Archero Wiki", 'lang':lang, "sidebarContent":SidebarContent, "cookieUsername":makeCookieheader(cookie_result),"list_article":list_article, "dev_mode":DEV_MODE})

@db_maintenance
@delete_visitor("news")
@checkMessages
def news(request,titleArticle=None):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	try:
		article = articleMenu.objects.get(title=titleArticle)
	except articleMenu.DoesNotExist:
		request.session['error_message'] = f"{titleArticle} Article doesn't exist" 
		return HttpResponseRedirect('/')
	return render(request, 'wiki/article-news.html', {"darkmode": checkDarkMode(request), "header_msg": "Menu Archero Wiki", 'lang':lang, "sidebarContent":SidebarContent, "cookieUsername":makeCookieheader(cookie_result), "article":article})


def maze(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	with urlopen("https://config-archero.habby.mobi/data/config/MazeConfig.json") as url:
		maze_data_api = json.load(url)
	return render(request, 'wiki/maze.html', {"data_json":maze_data_api, "darkmode": checkDarkMode(request), "header_msg": "maze","lang":lang, "sidebarContent":SidebarContent, "cookieUsername":makeCookieheader(cookie_result)})

def csrf_failure(request, reason=""):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	profil = "no"
	public_id =''
	try:
		ingame_name_cookie,ingame_id_cookie = list(cookie_result.items())[0]
		user_profile = getProfileWithCookie(ingame_id_cookie,ingame_name_cookie)
		if user_profile[0]:
			profil = "yes"
			user_stats = user_profile[1]
			public_id = user_stats.public_id
	except IndexError:
		pass
	MakeLogAddRequestJson(request,cookie_result)
	return render(request,'base/csrf_failure.html', {"darkmode": checkDarkMode(request), "header_msg": "CSRF FAILURE","lang":lang, "profil":profil, "public_id":public_id, "sidebarContent":SidebarContent, "cookieUsername":makeCookieheader(cookie_result)})

@checkMessages
def login(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_value = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_value)
	if (len(cookie_value) >= 1 and "visitor" not in list(cookie_value)): ## normally len(cookie_value) will have maximum 1 length but to be sure 
		cookie_request_name,cookie_request_id = list(cookie_value.items())[0]
		profile = getProfileWithCookie(cookie_request_id,cookie_request_name)
		if profile[0] == False and profile[1] != None:
			return render(request, "base/login.html", {"darkmode":checkDarkMode(request), "sidebarContent":SidebarContent})
		send_webhook(f'{cookie_value} tried to access Login but was redirected to Home\n{request.COOKIES}')
		request.session['error_message'] = f"You can't login again, your username is {cookie_request_name}"
		return HttpResponseRedirect("/")
	else:
		return render(request, "base/login.html", {"darkmode":checkDarkMode(request), "sidebarContent":SidebarContent})

def login_processing(request, username_raw, id_raw):
	response = redirect("/")
	cookie_value = checkCookie(request)
	if len(cookie_value) != 0:
		cookie_request_name,cookie_request_id = list(cookie_value.items())[0]
		profile = getProfileWithCookie(cookie_request_id,cookie_request_name)
		if profile[0]:
			request.session['info_message'] = f"You are already logged in"
			return response
		elif profile[0] == False and profile[1] != None:
			# si il a pas de profil mais qu'il a un user_credential dans les cookies/session
			response.delete_cookie(key=cookie_request_name,path="/")
			request.session.clear()
	boolCheck = checkUsernameCredentials(username_raw,id_raw,login=True)
	if boolCheck["access"]:
		response.delete_cookie('visitor', path='/')
		expires = datetime.now() + timedelta(days=365)
		try:
			response.set_cookie(key=boolCheck["ingame_name"], value=boolCheck["ingame_id"], expires=expires, httponly=True, samesite="Strict")
		except CookieError as e:
			username_legal = checkIllegalKey(username_raw)
			send_webhook(f"<@&{DISCORD_NOTIF_ROLE_ID}> : {e}")
			request.session['error_message'] = f"Login Failed (forbidden character \"{username_legal}\")"
			return response
		request.session['success_message'] = f"Successful Login ({boolCheck['ingame_name']})"
		send_embed(boolCheck["ingame_name"],"Successful Login",description_embed=f"",field_name=f"login/processing/{username_raw}/{id_raw}/",field_value=f"Credentials : `{boolCheck['ingame_name']}`|`{boolCheck['ingame_id']}`\n\n**Response Cookies** : \n{response.cookies}",e_color="32ec08",request=request, alert=False, admin_log=boolCheck.get('admin_log',None))
	else:
		request.session['error_message'] = f"Login Failed : {boolCheck['error_message']}"
		send_embed(boolCheck["ingame_name"],"Login Failed",description_embed=boolCheck["error_message"],field_name=f"login/processing/{username_raw}/{id_raw}/",field_value=f"Credentials : `{boolCheck['ingame_name']}`|`{boolCheck['ingame_id']}`\n\n**Response Cookies** : \n{response.cookies}",e_color="d50400",request=request, alert=True, admin_log=boolCheck.get('admin_log',None))
	return response

@delete_visitor("wiki")
def wiki_menu(request, article=None):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	article_label = str(article).replace('_',' ').capitalize()
	if article != None:
		name_title = article_label
	else:
		name_title = None
	ctx = {
		"darkmode": checkDarkMode(request),
		"lang":lang,
		"sidebarContent":SidebarContent,
		"WikiContent":local_data["WikiContent"],
		"cookieUsername":makeCookieheader(cookie_result),
		"name_title": name_title,
		"article": article
	}
	if article is not None or local_data["WikiContent"].get(article):
		ctx["header_msg"] = f"{article_label} - Wiki"
	else:
		ctx["header_msg"] = "Wiki"
	return render(request, "wiki/menu.html", ctx)

@delete_visitor("item_desc")
def item_description(request, item=None):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	ctx = {
		"darkmode": checkDarkMode(request),
		"header_msg": "Item Description",
		"lang":lang,
		"item":"no",
		"sidebarContent":SidebarContent,
		"ItemData":local_data["ItemData"],
		"cookieUsername":makeCookieheader(cookie_result)
	}
	if item is None or not local_data["ItemData"].get(str(item).replace('_',' '),False):
		item = "Expedition_Fist"
	else:
		ctx.update({"item":"yes"})
	data = local_data["ItemData"]
	item_name = str(item).replace('_',' ')
	item_data = data[item_name]
	temp = list(data)
	try:
		index_after = data[temp[temp.index(item_name) + 1]]
	except (ValueError, IndexError):
		index_after = data[str(temp[0]).replace('_',' ')]
	try:
		index_before = data[temp[temp.index(item_name) - 1]]
	except (ValueError, IndexError):
		index_before = data[str(temp[-1]).replace('_',' ')]
	ctx.update({
		"name":item_data['value'].replace('_',' '),
		"item_data":item_data,
		"url_cpy":request.build_absolute_uri(),
		"header_msg": f"{item_data['value'].replace('_',' ')} - Description",
		"index_after": index_after,
		"index_before": index_before,
	})
	return render(request, "wiki/item_description.html", ctx)

@delete_visitor("skill_list")
def skill_description(request, skill=None):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	ctx = {}
	MakeLogAddRequestJson(request,cookie_result)
	if skill is None or not local_data["SkillData"].get(skill.replace("_"," "),False):
		skill = "Attack_Boost"
		ctx.update({"skill":"no"})
	else:
		ctx.update({"skill":"yes"})
	skill_name = skill.replace("_"," ")
	data = local_data["SkillData"]
	skill_data = data[skill_name]
	image_skill = f"image/skill/{str(skill).lower().replace(' - ', '_').replace(' ', '_').replace('one-eyed', 'one_eyed')}.png"
	url_cpy = request.build_absolute_uri()
	temp = list(data)
	try:
		index_after = data[temp[temp.index(skill_name) + 1]]
	except (ValueError, IndexError):
		index_after = data[temp[0]]
	try:
		index_before = data[temp[temp.index(skill_name) - 1]]
	except (ValueError, IndexError):
		index_before = data[temp[-1]]
	ctx.update({
		"sidebarContent":SidebarContent,
		"SkillData":local_data["SkillData"],
		"cookieUsername":makeCookieheader(cookie_result),
		"darkmode": checkDarkMode(request),
		"header_msg": "Skill Description",
		"lang":lang,
		"name":skill_name,
		"skill_data": skill_data,
		"image_skill":image_skill,
		"url_cpy":url_cpy,
		"header_msg": f"{skill_name} - Description",
		"index_after": index_after,
		"index_before": index_before,
	})
	return render(request, "wiki/skill_description.html", ctx)

@delete_visitor("heroes_desc")
def heros_description(request, hero=None):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	ctx = {
		"darkmode": checkDarkMode(request),
		"header_msg": "Heroes Description",
		"lang":lang,
		"hero":"no", ## keep this for the meta tag
		"sidebarContent":SidebarContent,
		"HeroData":local_data["HeroData"],
		"cookieUsername":makeCookieheader(cookie_result)
	}
	if hero is None or not local_data["HeroData"].get(hero,False):
		hero = "Taiga"
	else:
		ctx.update({"hero":"yes"})
	data = local_data["HeroData"]
	hero_data = data[hero]
	temp = list(data)
	try:
		index_after = temp[temp.index(hero) + 1]
	except (ValueError, IndexError):
		index_after = temp[0]
	try:
		index_before = temp[temp.index(hero) - 1]
	except (ValueError, IndexError):
		index_before = temp[-1]
	ctx.update({
		"name_hero": hero,
		"hero_data": hero_data,
		"hero_image": f'image/hero_icon/icon_{str(hero)}.png',
		"url_cpy": request.build_absolute_uri(),
		"header_msg": f"{hero} - Description",
		"index_after": index_after,
		"index_before": index_before,
	})
	return render(request, "wiki/heros_description.html",ctx)

def upgrade_cost(request,cost_type:str="None",lvl1:int=999,lvl2:int=999,rank:str="None"):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	all_rank = ["A","S","SS"]
	content = ""
	ctx = {
		"darkmode": checkDarkMode(request),
		"header_msg": "Upgrade Cost",
		"lang":lang,
		"cost_type":cost_type,
		"lvl1":lvl1,
		"lvl2":lvl2,
		"rank":rank,
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(cookie_result)
	}
	if cost_type == "items":
		max_lvl = 170
		if (0 <= lvl1 <= max_lvl) and (0 <= lvl2 <= max_lvl):
			if lvl1 > lvl2:
				temp = lvl1
				lvl1 = lvl2
				lvl2 = temp
			price = calculatePrice(lvl1,lvl2,cost_type)
			content = {
				"eTitle": "Equipment Upgrade Cost",
				"eDescription": f"To upgrade equipment from level {lvl1} to {lvl2}",
				"eImage": "/static/image/wiki-image/Cost_Item.png",
				"eField1": f'{int(price[0]):,}',
				"eField2": f'{int(price[1]):,}',
				"currency1": ['Gold :','gold'],
				"currency2": ['Scrolls :','scroll'],
			}
		else:
			messages.error(request,f"The levels need to be between 0 and {max_lvl}")
			return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/1/2/")
	elif cost_type == "heroes":
		if lvl1 <= lvl2 and (0 <= lvl1 <= 119) and (1 <= lvl2 <= 120):
			price = calculatePrice(lvl1,lvl2,cost_type)
			content = {
				"eTitle": "Heroes Upgrade Cost",
				"eDescription": f"To upgrade heroes from level {lvl1} to {lvl2}",
				"eImage": "/static/image/wiki-image/Cost_Heroes.png",
				"eField1": f'{int(price[0]):,}',
				"eField2": f'{int(price[1]):,}',
				"currency1": ['Gold :','gold'],
				"currency2": ['Sapphire :','sapphire'],
			}
		else:
			messages.error(request,f"The levels need to be between 0 and 120")
			return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/1/2/")
	elif cost_type == "talents":
		if lvl1 <= lvl2 and (0 <= lvl1 <= 205) and (1 <= lvl2 <= 206):
			price = calculatePrice(lvl1,lvl2,cost_type)
			content = {
				"eTitle": "Talents Upgrade Cost",
				"eDescription": f"To upgrade talents from level {lvl1} to {lvl2}",
				"eImage": "/static/image/wiki-image/Cost_Talent.png",
				"eField1": f'{int(price):,}',
				"eField2": f'<br>',
				"currency1": ['Gold :','gold'],
				"currency2": ['',''],
			}
		else:
			messages.error(request,"The levels need to be between 0 and 206")
			return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/1/2/")
	elif cost_type == "dragons":
		if lvl1 <= lvl2 and (0 <= lvl1 <= 119) and (1 <= lvl2 <= 120):
			if rank in all_rank:
				price = calculatePrice(lvl1,lvl2,cost_type,rank)
				content = {
					"eTitle": "Dragon Upgrade Cost",
					"eDescription": f"To upgrade dragons from level {lvl1} to {lvl2}",
					"eImage": "/static/image/wiki-image/Cost_Dragon" + str(rank).upper() + ".png",
					"eField1": f'{int(price[0]):,}',
					"eField2": f'{int(price[1]):,}',
					"currency1": ['Gold :','gold'],
					"currency2": ['Magestones :','magestone'],
				}
			else:
				messages.error(request,"The rank need to be whether A, S or SS")
				return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/{lvl1}/{lvl2}/A/")
		else:
			messages.error(request,"The levels need to be between 0 and 120")
			return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/1/2/{rank}/")
	elif cost_type == "relics":
		if lvl1 <= lvl2 and (0 <= lvl1 <= 29) and (1 <= lvl2 <= 30):
			if rank in all_rank:
				price = calculatePrice(lvl1,lvl2,cost_type,rank)
				content = {
					"eTitle": "Relics Upgrade Cost",
					"eDescription": f"To upgrade relics from level {lvl1} to {lvl2}",
					"eImage": "/static/image/wiki-image/Cost_Relics" + str(rank).upper() + ".png",
					"eField1": f'{int(price[0]):,}',
					"eField2": f'{int(price[1]):,}',
					"currency1": ['Gold :','gold'],
					"currency2": ['Starlight :','starlight'],
				}
			else:
				messages.error("The rank need to be whether A, S or SS")
				return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/{lvl1}/{lvl2}/A/")
		else:
			messages.error(request,"The levels need to be between 0 and 30")
			return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/1/2/{rank}/")
	ctx.update({"content":content})
	return render(request, "wiki/upgrade_cost.html", ctx)


def ghssetGrid(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	ctx = {
		'darkmode':checkDarkMode(request),
		"header_msg": "Google Sheet Wiki",
		"lang":lang,
		"GsheetData":local_data['GsheetData'],
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(cookie_result)
	}
	return render(request, "wiki/gsheet.html", ctx)

@db_maintenance
def promocode(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	all_active_code = []
	promo_codes = promo_code.objects.all().filter(is_active=True)
	for i in promo_codes:
		expireDate = i.expire
		if i.expire == None:
			expireDate = "Unknown"
		r1 = [i.reward_1_amount,i.reward_1_type]
		r2 = [i.reward_2_amount,i.reward_2_type]
		r3 = [i.reward_3_amount,i.reward_3_type]
		r4 = [i.reward_4_amount,i.reward_4_type]
		if str(r1[1]) != "none":
			result = [i.code,expireDate,[r1]]
			if str(r2[1]) != "none":
				result = [i.code,expireDate,[r1,r2]]
				if str(r3[1]) != "none":
					result = [i.code,expireDate,[r1,r2,r3]]
					if str(r4[1]) != "none":
						result = [i.code,expireDate,[r1,r2,r3,r4]]
			all_active_code.append(result)
	ctx = {
		"darkmode": checkDarkMode(request),
		"header_msg": "Promo Code",
		"lang":lang,
		"promo_code":all_active_code,
		"len_promo":len(all_active_code),
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(cookie_result)
	}
	return render(request, "wiki/promo-code.html", ctx)

@db_maintenance
@checkMessages
def damage(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	user_stats = ""
	selfHasProfil = "no"
	if len(cookie_result) != 0:
		ingame_name_cookie,ingame_id_cookie = list(cookie_result.items())[0]
		profile = getProfileWithCookie(ingame_id_cookie,ingame_name_cookie)
		if ingame_id_cookie == "0-000000" and ingame_name_cookie == "visitor":
			selfHasProfil = "login"
		elif profile[0]:
			user_stats = profile[1]
			selfHasProfil = "yes"
		elif not profile[0] and profile[1] != None:
			selfHasProfil = "login"
			messages.error(request,f'You attempted to access {profile[1].ingame_name}<br>But your login username is "{ingame_name_cookie}".')
	else:
		selfHasProfil = "login"
	chapter_1_to_21 =  user.objects.get(ingame_id="0-000001").public_id
	chapter_22_to_34 = user.objects.get(ingame_id="0-000002").public_id
	chapter_34_to_42 = user.objects.get(ingame_id="0-000003").public_id
	chapter_ch42 =  user.objects.get(ingame_id="0-000004").public_id
	ctx = {
		"darkmode": checkDarkMode(request),
		"header_msg": "Damage Calculator",
		"selfHasProfil":selfHasProfil,
		"selfStats":user_stats,
		"lang":lang,
		"chapter_1_to_21":chapter_1_to_21,
		"chapter_22_to_34":chapter_22_to_34,
		"chapter_34_to_42":chapter_34_to_42,
		"chapter_ch42":chapter_ch42,
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(cookie_result)
		}
	return render(request, "wiki/damage.html", ctx)

@db_maintenance
def dmgCalc_processing(request,pbid):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	global missing_data
	user_stats = user.objects.get(public_id=pbid)
	stuff_table_stats = stuff_table.objects.get(user_profile=user_stats)
	hero_table_stats = hero_table.objects.get(user_profile=user_stats)
	talent_table_stats = talent_table.objects.get(user_profile=user_stats)
	skin_table_stats = skin_table.objects.get(user_profile=user_stats)
	altar_table_stats = altar_table.objects.get(user_profile=user_stats)
	jewel_level_table_stats = jewel_level_table.objects.get(user_profile=user_stats)
	egg_table_stats = egg_table.objects.get(user_profile=user_stats)
	egg_equipped_table_stats = egg_equipped_table.objects.get(user_profile=user_stats)
	dragon_table_stats = dragon_table.objects.get(user_profile=user_stats)
	runes_table_stats = runes_table.objects.get(user_profile=user_stats)
	reforge_table_stats = reforge_table.objects.get(user_profile=user_stats)
	refine_table_stats = refine_table.objects.get(user_profile=user_stats)
	medals_table_stats = medals_table.objects.get(user_profile=user_stats)
	relics_table_stats = relics_table.objects.get(user_profile=user_stats)
	weapon_skins_table_stats = weapon_skins_table.objects.get(user_profile=user_stats)

	atk_base_hero_choosen = user_stats.atk_base_stats_hero_choosen
	stuff_altar_ascension = altar_table_stats.stuff_altar_ascension
	heros_altar_ascension = altar_table_stats.heros_altar_ascension
	refine_weapon_atk = refine_table_stats.weapon_refine_atk
	refine_weapon_enhanced_equipment = int(refine_table_stats.weapon_refine_basic_stats)/100
	refine_armor_enhanced_equipment = int(refine_table_stats.armor_refine_basic_stats)/100
	refine_ring1_atk = refine_table_stats.ring1_refine_atk
	refine_ring1_enhanced_equipment = int(refine_table_stats.ring1_refine_basic_stats)/100
	refine_ring2_atk = refine_table_stats.ring2_refine_atk
	refine_ring2_enhanced_equipment = int(refine_table_stats.ring2_refine_basic_stats)/100
	refine_bracelet_atk = refine_table_stats.bracelet_refine_atk
	refine_bracelet_enhanced_equipment = int(refine_table_stats.bracelet_refine_basic_stats)/100
	refine_locket_enhanced_equipment = int(refine_table_stats.locket_refine_basic_stats)/100
	refine_book_enhanced_equipment = int(refine_table_stats.book_refine_basic_stats)/100
	brave_privileges_level = int(user_stats.brave_privileges_level)
	## Get Talents Stats
	talent_stats_dict = talent_table_stats.getTalentStats()
	## Get all Relics Stats
	relics_stats:dict = relics_table_stats.relics_Stats()
	## Get Altar Ascension Stats
	altar_stuff_ascension_atk = local_data["StuffAltarAscension"]['attack'][stuff_altar_ascension]
	altar_stuff_ascension_equipment_base = local_data["StuffAltarAscension"]['equipment_base'][stuff_altar_ascension]
	altar_heros_ascension_atk = local_data['HerosAltarAscension']['attack'][heros_altar_ascension]
	altar_heros_ascension_heros_base = local_data['HerosAltarAscension']['heros_base'][heros_altar_ascension]
	altar_heros_ascension_dmg_elite = local_data['HerosAltarAscension']['dmg_elite'][heros_altar_ascension]
	## Get Altar Stats 
	altar_stuff_atk = altar_table_stats.CalculAltar("stuff","attack",relics_stats.get('eqpm_altar_stats_var',0.0))
	altar_hero_atk = altar_table_stats.CalculAltar("heros","attack",relics_stats.get('eqpm_altar_stats_var',0.0)) ##laisser le S (le nom du field prend un s)
	# Get All Heroes Stats
	hero_Atreus = hero_table_stats.HerosStatsRecup("Atreus")
	hero_Urasil = hero_table_stats.HerosStatsRecup("Urasil")
	hero_Phoren = hero_table_stats.HerosStatsRecup("Phoren")
	hero_Taranis = hero_table_stats.HerosStatsRecup("Taranis")
	hero_Helix = hero_table_stats.HerosStatsRecup("Helix") 
	hero_Meowgik = hero_table_stats.HerosStatsRecup("Meowgik")
	hero_Shari = hero_table_stats.HerosStatsRecup("Shari")
	hero_Ayana = hero_table_stats.HerosStatsRecup("Ayana")
	hero_Onir = hero_table_stats.HerosStatsRecup("Onir") 
	hero_Rolla = hero_table_stats.HerosStatsRecup("Rolla")
	hero_Bonnie = hero_table_stats.HerosStatsRecup("Bonnie")
	hero_Sylvan = hero_table_stats.HerosStatsRecup("Sylvan")
	hero_Shade = hero_table_stats.HerosStatsRecup("Shade") 
	hero_Ophelia = hero_table_stats.HerosStatsRecup("Ophelia")
	hero_Ryan = hero_table_stats.HerosStatsRecup("Ryan")
	hero_Lina = hero_table_stats.HerosStatsRecup("Lina")
	hero_Aquea = hero_table_stats.HerosStatsRecup("Aquea")
	hero_Shingen = hero_table_stats.HerosStatsRecup("Shingen") 
	hero_Gugu = hero_table_stats.HerosStatsRecup("Gugu")
	hero_Iris = hero_table_stats.HerosStatsRecup("Iris")
	hero_Blazo = hero_table_stats.HerosStatsRecup("Blazo")
	hero_Melinda = hero_table_stats.HerosStatsRecup("Melinda")
	hero_Elaine = hero_table_stats.HerosStatsRecup("Elaine")
	hero_Bobo = hero_table_stats.HerosStatsRecup("Bobo")
	hero_Stella = hero_table_stats.HerosStatsRecup("Stella")
	## Get Skin Atk and Hp
	skin_atk_boost = skin_table_stats.skin_attack
	## Get Passiv Stats From Type 1 Egg
	egg_green_bat_passiv = egg_table_stats.GetPassivEggStats1("green_bat", missing_data)
	egg_bomb_ghost_passiv = egg_table_stats.GetPassivEggStats1("bomb_ghost",missing_data)
	egg_piranha_passiv = egg_table_stats.GetPassivEggStats1("piranha",missing_data)
	## Get Passiv Stats From Type 2 Egg
	egg_skeleton_archer_passiv = egg_table_stats.GetPassivEggStats2("skeleton_archer",missing_data)
	egg_skeleton_soldier_passiv = egg_table_stats.GetPassivEggStats2("skeleton_soldier",missing_data)
	egg_fire_mage_passiv = egg_table_stats.GetPassivEggStats2("fire_mage",missing_data)
	egg_ice_mage_passiv = egg_table_stats.GetPassivEggStats2("ice_mage",missing_data)
	egg_flame_ghost_passiv = egg_table_stats.GetPassivEggStats2("flame_ghost",missing_data)
	egg_tornado_demon_passiv = egg_table_stats.GetPassivEggStats2("tornado_demon",missing_data)
	egg_skull_wizard_passiv = egg_table_stats.GetPassivEggStats2("skull_wizard",missing_data)
	egg_crazy_spider_passiv = egg_table_stats.GetPassivEggStats2("crazy_spider",missing_data)
	egg_fire_element_passiv = egg_table_stats.GetPassivEggStats2("fire_element",missing_data)
	egg_pea_shooter_passiv = egg_table_stats.GetPassivEggStats2("pea_shooter",missing_data)
	egg_shadow_assassin_passiv = egg_table_stats.GetPassivEggStats2("shadow_assassin",missing_data)
	egg_one_eyed_bat_passiv = egg_table_stats.GetPassivEggStats2("one_eyed_bat",missing_data)
	egg_scarlet_mage_passiv = egg_table_stats.GetPassivEggStats2("scarlet_mage",missing_data)
	egg_icefire_phantom_passiv = egg_table_stats.GetPassivEggStats2("icefire_phantom",missing_data)
	egg_purple_phantom_passiv = egg_table_stats.GetPassivEggStats2("purple_phantom",missing_data)
	egg_savage_spider_passiv = egg_table_stats.GetPassivEggStats2("savage_spider",missing_data)
	egg_flaming_bug_passiv = egg_table_stats.GetPassivEggStats2("flaming_bug",missing_data)
	egg_crimson_zombie_passiv = egg_table_stats.GetPassivEggStats2("crimson_zombie",missing_data)
	egg_elite_archer_passiv = egg_table_stats.GetPassivEggStats2("elite_archer",missing_data)
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
	BonusSpe_jewel_ring1 = jewel_level_table_stats.JewelSpeBonusStatsRecup('ring1',brave_privileges_stats['Ring JSSSA'])
	BonusSpe_jewel_bracelet = jewel_level_table_stats.JewelSpeBonusStatsRecup('bracelet',brave_privileges_stats['Bracelet JSSSA'],relics_stats.get("jewel_attack_bonus_var",0))
	BonusSpe_jewel_book = jewel_level_table_stats.JewelSpeBonusStatsRecup('book',brave_privileges_stats['Spellbook JSSSA'])
	## DRAGON
	relics_dragon_base_stats = relics_stats.get('dragon_base_stats_var',0.0)
	dragon_stats_dict = dragon_table_stats.DragonStatueStats(relics_dragon_base_stats)
	## Get Dragon passiv Skills
	dragons_skills = dragon_table_stats.getPassivSkillDragon()
	## Get All Stats of Equipped Egg
	activ_egg_stats = egg_equipped_table_stats.GetEggStats(missing_data)
	## Get Reforge Stats
	reforge_atk_power = reforge_table_stats.ReforgePowerCourage("power")
	reforge_atk_courage = reforge_table_stats.ReforgePowerCourage("courage")
	## Get Rune Line Stats
	runelinePower = runes_table_stats.getValueLinePower()
	runelineRecovery = runes_table_stats.getValueLineRecovery()
	runelineCourage = runes_table_stats.getValueLineCourage()
	## Get Weapon Skin Stats
	weapon_skin_stats = weapon_skins_table_stats.getWeaponSkinStats()
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

	cumul_talent_flat_passiv_atk = int(talent_stats_dict['talents_power'])
	cumul_runes_flat_passiv_atk = int(reforge_atk_power) + int(reforge_atk_courage) # + int(runes_power_attack_flat) + int(runes_courage_attack_flat)
	cumul_hero_flat_passiv_atk = int(hero_Atreus[5]) + int(hero_Urasil[0]) + int(hero_Phoren[6]) + int(hero_Helix[5]) + int(hero_Meowgik[0]) + int(hero_Ayana[6]) + int(hero_Rolla[0]) + int(hero_Bonnie[5]) + int(hero_Shade[6]) + int(hero_Ophelia[0]) + int(hero_Ophelia[2]) + int(hero_Lina[0]) + int(hero_Lina[5]) + int(hero_Aquea[5]) + int(hero_Iris[5]) + int(hero_Melinda[6]) + int(hero_Iris[1]) + int(hero_Blazo[1]) + int(hero_Stella[0])
	cumul_skin_flat_passiv_atk = int(skin_atk_boost)
	cumul_egg_flat_passiv_atk = int(egg_bomb_ghost_passiv[1]) + int(egg_green_bat_passiv[1]) + int(egg_piranha_passiv[1]) + int(egg_crazy_spider_passiv[1]) + int(egg_fire_mage_passiv[1]) + int(egg_skeleton_archer_passiv[1]) + int(egg_skeleton_soldier_passiv[1]) + int(egg_fire_element_passiv[1]) + int(egg_flame_ghost_passiv[1]) + int(egg_ice_mage_passiv[1]) + int(egg_pea_shooter_passiv[1]) + int(egg_shadow_assassin_passiv[1]) + int(egg_skull_wizard_passiv[1]) + int(egg_tornado_demon_passiv[1]) + int(egg_savage_spider_passiv[1]) + int(egg_flaming_bug_passiv[1]) + int(egg_one_eyed_bat_passiv[1]) + int(egg_elite_archer_passiv[1]) + int(egg_icefire_phantom_passiv[1]) + int(egg_purple_phantom_passiv[1]) + int(egg_scarlet_mage_passiv[1]) + int(egg_arch_leader_passiv[0]) + int(egg_crimson_witch_passiv[0]) + int(egg_medusa_boss_passiv[0]) + int(egg_ice_worm_passiv[0]) + int(egg_desert_goliath_passiv[0]) + int(egg_ice_demon_passiv[0]) + int(egg_fire_demon_passiv[1]) + int(egg_crimson_zombie_passiv[1]) + int(egg_scythe_pharoah_passiv[1]) + int(egg_infernal_demon_passiv[0]) + int(egg_fireworm_queen_passiv[0])
	cumul_altar_flat_passiv_atk = int(altar_stuff_atk) + int(altar_hero_atk)
	cumul_jewel_flat_activ_atk = int(stats_jewel_dict.get('attack_flat',0)) + int(BonusSpe_jewel_weapon.get('attack_flat',0)) + int(BonusSpe_jewel_bracelet.get('attack_flat',0))
	cumul_old_flat_passiv_atk = int(cumul_talent_flat_passiv_atk) + int(cumul_runes_flat_passiv_atk) + int(cumul_hero_flat_passiv_atk) + int(cumul_skin_flat_passiv_atk) + int(cumul_egg_flat_passiv_atk)
	cumul_refine_flat_activ_atk =  int(refine_weapon_atk) + int(refine_ring1_atk) + int(refine_ring2_atk) + int(refine_bracelet_atk)
	cumul_dragon_flat_activ_atk = int(dragon_stats_dict.get("Attack",0))
	cumul_stuff_flat_activ_atk = round(stuff_activ_stats['weapon_total'] + stuff_activ_stats['bracelet_total'])

	cumul_heros_var_passiv_atk = float(hero_Taranis[2]) + float(hero_Meowgik[2]) + float(hero_Ayana[2]) + float(hero_Rolla[2]) + float(hero_Sylvan[2]) + float(hero_Aquea[2]) + float(hero_Iris[2]) + float(hero_Bonnie[4]) + float(hero_Shade[7]) + float(hero_Melinda[7]) + float(hero_Bobo[1]) + float(hero_Bobo[4]) + float(hero_Stella[2])
	cumul_heros_var_activ_atk = float(hero_Onir[3]) + float(hero_Bonnie[3])
	cumul_altar_var_passiv_atk = float(altar_heros_ascension_atk) + float(altar_stuff_ascension_atk)
	cumul_privileges_var_passiv_atk = float(brave_privileges_stats['Attack Var'])
	cumul_jewel_var_activ_atk =  (float(BonusSpe_jewel_weapon.get('attack_var',0)) + float(BonusSpe_jewel_ring1.get('attack_var',0)) + float(BonusSpe_jewel_book.get('attack_var',0)))/100
	cumul_stuff_var_activ_atk = (stuff_activ_stats['weapon_attack_var'] + stuff_activ_stats['bracelet_attack_var'] + stuff_activ_stats['ring1_atk_var'] + stuff_activ_stats['ring2_atk_var'])

	cumul_var_atk = (float(cumul_heros_var_passiv_atk) + float(cumul_heros_var_activ_atk) + float(cumul_altar_var_passiv_atk) + float(cumul_privileges_var_passiv_atk) + float(medal_stats['attack_var']) + float(relics_stats.get('attack_var',0.0)))/100
	global_stats_atk_flat = int(cumul_stuff_flat_activ_atk) + int(activ_egg_stats["Attack"]) + int(cumul_altar_flat_passiv_atk) + int(cumul_dragon_flat_activ_atk) + int(brave_privileges_stats['Attack Flat']) + int(medal_stats['attack']) + int(relics_stats.get('attack_flat',0))
	hero_atk_step = [
		int(user_stats.global_atk_save),
		int(cumul_old_flat_passiv_atk), # + int(runes_power_attack_flat) + int(runes_courage_attack_flat)
		float(cumul_var_atk), # float(runes_power_attack_var) + float(runes_courage_attack_var)
		## atk_base_hero_choosen
		int(atk_base_hero_choosen),
		float(cumul_var_passiv_power_up_hero),
		#global_stats_atk_flat
		int(global_stats_atk_flat), # + int(hero_base_modified_stats_atk) + cumul_all_bonus_passif_atk
		#global_stats_atk
		float(cumul_stuff_var_activ_atk),
		float(cumul_jewel_var_activ_atk),
		int(cumul_jewel_flat_activ_atk),
		int(cumul_refine_flat_activ_atk),
		int(runelinePower.get("attack_flat",0)),
		int(runelineCourage.get("attack_flat",0)),
		float(runelinePower.get("attack_var",0.0)),
		float(runelineCourage.get("attack_var",0.0)),
		float(runelineCourage.get('courage_hero_attack_flat',0)),
		float(runelineCourage.get('courage_hero_attack_var',0.0))
	]

	if request.method == "GET":
		try:
			calc_user_dmg = dmg_calc_table.objects.get(user_profile=user_stats)
			calc_user_dmg.hero_atk = hero_atk_step
			calc_user_dmg.save()
			return HttpResponseRedirect(f"/wiki/damage-calculator/{pbid}/")
		except dmg_calc_table.DoesNotExist:
			return HttpResponseRedirect(f"/stats/calc/{pbid}/2/?log=False")
	else :
		return HttpResponseRedirect("/wiki/damage-calculator/")

@db_maintenance
@checkMessages
def damageCalc(request,pbid):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	try:
		user_stats = user.objects.get(public_id=pbid)
		calc_user_dmg = dmg_calc_table.objects.get(user_profile=user_stats.pk)
		runes_table_stats = runes_table.objects.get(user_profile=user_stats.pk)
	except (user.DoesNotExist,dmg_calc_table.DoesNotExist,runes_table.DoesNotExist):	
		return HttpResponseRedirect(f"/wiki/damage-calculator/calc/{pbid}/")
	ctx = {
		'darkmode':checkDarkMode(request),
		"header_msg": "Damage Calc",
		"lang":lang,
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(cookie_result)
	}
	if request.method == "GET":
		damage_calc_form = DamageCalculatorForm()
		resultCalcDamg = calc_user_dmg.calculDamage()
		ctx['averageDamage'] = resultCalcDamg['averageDamageAll']
		ctx['crit_dmg'] = float(calc_user_dmg.crit_dmg)
		ctx['crit_rate'] = float(calc_user_dmg.crit_rate)
		ctx["mob_ground_melee_damage"] = resultCalcDamg['mob_ground_melee_damage']
		ctx["mob_ground_range_damage"] = resultCalcDamg['mob_ground_range_damage']
		ctx["mob_airborne_melee_damage"] = resultCalcDamg['mob_airborne_melee_damage']
		ctx["mob_airborne_range_damage"] = resultCalcDamg['mob_airborne_range_damage']
		ctx["boss_ground_melee_damage"] = resultCalcDamg['boss_ground_melee_damage']
		ctx["boss_ground_range_damage"] = resultCalcDamg['boss_ground_range_damage']
		ctx["boss_airborne_melee_damage"] = resultCalcDamg['boss_airborne_melee_damage']
		ctx["boss_airborne_range_damage"] = resultCalcDamg['boss_airborne_range_damage']
		ctx["vars_dict"] =  runes_table_stats.getRunesDmgCalc()
	elif request.method == "POST":
		damage_calc_form = DamageCalculatorForm(request.POST)
		if damage_calc_form.is_valid() and 'runes' in request.POST:
			listHeroStepAtk = calc_user_dmg.hero_atk
			param_runes_display = runes_table_stats.getRunesDmgCalc()
			power_rune = runes_table_stats.getValueLinePower()
			courage_rune = runes_table_stats.getValueLineCourage()
			runes = damage_calc_form.cleaned_data['runes']
			first_select = request.POST.get('firstSelect',None)
			second_select = request.POST.get('secondSelect',None)
			third_select = request.POST.get('thirdSelect',None)
			fourth_select = request.POST.get('fourthSelect',None)
			fifth_select = request.POST.get('fifthSelect',None)
			first_input = damage_calc_form.cleaned_data['firstInput']
			second_input = damage_calc_form.cleaned_data['secondInput']
			third_input = damage_calc_form.cleaned_data['thirdInput']
			fourth_input = damage_calc_form.cleaned_data['fourthInput']
			fifth_input = damage_calc_form.cleaned_data['fifthInput']
			inputRune = {first_select: first_input,second_select: second_input,third_select: third_input,fourth_select: fourth_input,fifth_select: fifth_input}

			power_vars = {
				"courage_first_select": param_runes_display['courage_first_select'],
				"courage_first_input": param_runes_display['courage_first_input'],
				"courage_second_select": param_runes_display['courage_second_select'],
				"courage_second_input": param_runes_display['courage_second_input'],
				"courage_third_select": param_runes_display['courage_third_select'],
				"courage_third_input": param_runes_display['courage_third_input'],
				"courage_fourth_select": param_runes_display['courage_fourth_select'],
				"courage_fourth_input": param_runes_display['courage_fourth_input'],
				"courage_fifth_select": param_runes_display['courage_fifth_select'],
				"courage_fifth_input": param_runes_display['courage_fifth_input'],
				"power_first_select":first_select,
				"power_first_input":first_input,
				"power_second_select":second_select,
				"power_second_input":second_input,
				"power_third_select":third_select,
				"power_third_input":third_input,
				"power_fourth_select":fourth_select,
				"power_fourth_input":fourth_input,
				"power_fifth_select":fifth_select,
				"power_fifth_input":fifth_input
			}
			courage_vars = {
				"courage_first_select": first_select,
				"courage_first_input": first_input,
				"courage_second_select": second_select,
				"courage_second_input": second_input,
				"courage_third_select": third_select,
				"courage_third_input": third_input,
				"courage_fourth_select": fourth_select,
				"courage_fourth_input": fourth_input,
				"courage_fifth_select": fifth_select,
				"courage_fifth_input": fifth_input,
				"power_first_select":param_runes_display["power_first_select"],
				"power_first_input":param_runes_display["power_first_input"],
				"power_second_select":param_runes_display["power_second_select"],
				"power_second_input":param_runes_display["power_second_input"],
				"power_third_select":param_runes_display["power_third_select"],
				"power_third_input":param_runes_display["power_third_input"],
				"power_fourth_select":param_runes_display["power_fourth_select"],
				"power_fourth_input":param_runes_display["power_fourth_input"],
				"power_fifth_select":param_runes_display["power_fifth_select"],
				"power_fifth_input":param_runes_display["power_fifth_input"]
			}
			vars_dict = power_vars if runes == 'power' else courage_vars
			if runes == 'power':
				atk_power_flat = inputRune.get("attack_flat",0)
				atk_courage_flat = courage_rune.get("attack_flat",0)
				atk_power_var = inputRune.get("attack_var",0.0)
				atk_courage_var = courage_rune.get("attack_var",0.0)
				courage_hero_atk_flat = courage_rune.get("courage_hero_attack_flat",0)
				courage_hero_atk_var = courage_rune.get("courage_hero_attack_var",0.0)
			else:
				atk_power_flat = power_rune.get("attack_flat",0)
				atk_courage_flat = inputRune.get("attack_flat",0)
				atk_power_var = power_rune.get("attack_var",0.0)
				atk_courage_var = inputRune.get("attack_var",0.0)
				courage_hero_atk_flat = inputRune.get("courage_hero_attack_flat",0)
				courage_hero_atk_var = inputRune.get("courage_hero_attack_var",0.0)
			cumul_var_atk = (float(atk_power_var)/100 + float(atk_courage_var)/100 + float(listHeroStepAtk[2]))
			hero_modified_base_atk = (int(listHeroStepAtk[3]) - int(courage_hero_atk_flat)) * (float(courage_hero_atk_var) + float(listHeroStepAtk[4]) + 1) + int(courage_hero_atk_flat)
			cumul_flat_atk = int(listHeroStepAtk[1]) + int(atk_power_flat) + int(atk_courage_flat)
			global_stats_atk_flat = float(hero_modified_base_atk) + float(cumul_flat_atk) + float(listHeroStepAtk[5])
			global_stats_atk = global_stats_atk_flat + (global_stats_atk_flat*float(cumul_var_atk)) + (global_stats_atk_flat*float(listHeroStepAtk[6])) + (global_stats_atk_flat*float(listHeroStepAtk[7])) + listHeroStepAtk[8] + listHeroStepAtk[9]
			
			# Liste des attributs avec leur valeur par défaut et leur nom correspondant dans l'objet 'calc_user_dmg'
			attributes = [
				('var_crit_dmg', 0.0, 'crit_dmg'),
				('var_crit_rate', 0.0, 'crit_rate'),
				('flat_dmg_mob', 0, 'flat_dmg_vs_mobs'),
				('var_dmg_mob', 0.0, 'var_dmg_vs_mobs'),
				('flat_dmg_ground', 0, 'flat_dmg_vs_ground'),
				('var_dmg_ground', 0.0, 'var_dmg_vs_ground'),
				('flat_dmg_melee', 0, 'flat_dmg_vs_melee'),
				('var_dmg_melee', 0.0, 'var_dmg_vs_melee'),
				('flat_dmg_airborne', 0, 'flat_dmg_vs_airborne'),
				('var_dmg_airborne', 0.0, 'var_dmg_vs_airborne'),
				('flat_dmg_boss', 0, 'flat_dmg_vs_boss'),
				('var_dmg_boss', 0.0, 'var_dmg_vs_boss'),
				('flat_dmg_ranged', 0, 'flat_dmg_vs_range'),
				('var_dmg_ranged', 0.0, 'var_dmg_vs_range'),
				('flat_all_dmg', 0, 'flat_dmg_all'),
				('var_all_dmg', 0.0, 'var_dmg_all')
			]

			input_values = {}
			for attr, default_value, attr_name in attributes:
				input_value = inputRune.get(attr, False)
				input_values[attr_name] = float(input_value) - float(power_rune.get(attr, default_value)) if input_value != False else 0
				# Calcul de la valeur en soustrayant la valeur d'entrée de la valeur de 'power_rune' (utilise la valeur par défaut si la clé n'existe pas)
  				# Si la valeur d'entrée est False, la valeur est mise à 0

			result_values = {}
			for attr_name in input_values:
				result_values[attr_name] = input_values[attr_name] + getattr(calc_user_dmg, attr_name)
				# Ajout de la valeur d'entrée à la valeur correspondante dans l'objet 'calc_user_dmg'

			resultCalcDamg = calc_user_dmg.calculDamage(global_atk_save=global_stats_atk, **result_values)
			ctx.update({
				"method": request.method,"runes": runes,"vars_dict":vars_dict,
				"firstSelect": first_select,"firstInput": first_input,"secondSelect": second_select,"secondInput": second_input,
				"thirdSelect": third_select,"thirdInput": third_input,"fourthSelect": fourth_select,"fourthInput": fourth_input,
				"fifthSelect": fifth_select,"fifthInput": fifth_input,"averageDamage": resultCalcDamg['averageDamageAll'],"crit_dmg": resultCalcDamg['crit_dmg'],
				"crit_rate": resultCalcDamg['crit_rate'],"mob_ground_melee_damage": resultCalcDamg['mob_ground_melee_damage'],"mob_ground_range_damage": resultCalcDamg['mob_ground_range_damage'],
				"mob_airborne_melee_damage": resultCalcDamg['mob_airborne_melee_damage'],"mob_airborne_range_damage": resultCalcDamg['mob_airborne_range_damage'],
				"boss_ground_melee_damage": resultCalcDamg['boss_ground_melee_damage'],"boss_ground_range_damage": resultCalcDamg['boss_ground_range_damage'],
				"boss_airborne_melee_damage": resultCalcDamg['boss_airborne_melee_damage'],"boss_airborne_range_damage": resultCalcDamg['boss_airborne_range_damage'],
			})
		else:
			form_error = damage_calc_form.errors.items()
			for k,v in form_error:
				error_msg = f"{k} : {str(v[0])}"
			request.session['error_message'] = error_msg
			return HttpResponseRedirect(f"/wiki/damage-calculator/{pbid}/")
	else:
		return HttpResponseRedirect(f"/wiki/damage-calculator/{pbid}/")
	ctx['damage_calc_form'] = damage_calc_form
	return render(request, "wiki/dmg_calc.html", ctx)


def handler404(request, exception):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	ctx = {
		'darkmode':checkDarkMode(request),
		"header_msg":"Page Not Found",
		"lang":lang,
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(cookie_result)
	}
	return render(request,'base/404.html', ctx, status=404)

def handler500(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	allfile = os.listdir('calculator/static/traceback_file/')
	for file in allfile:
		os.remove(f'calculator/static/traceback_file/{file}')
	exc_info = list(sys.exc_info())
	exc_output = list(traceback.format_exception(exc_info[1]))
	cookieRequest = checkCookie(request)
	try:
		username = list(cookieRequest)[0]
	except IndexError:
		username = 'unknown'
	with open(f'calculator/static/traceback_file/{username}.txt','a', encoding='utf-8') as exc_value:
		for i in exc_output:
			exc_value.write(i)
	webhook = DiscordWebhook(url=WEBHOOK_URL, content=f"<@&{DISCORD_ERROR_ROLE_ID}>", rate_limit_retry=True)
	embed = DiscordEmbed(title='Error 500 - Internal Server Error', description='', color='963e3e')
	embed.set_author(
		name=username.capitalize(),
		icon_url=f"{c_hostname}/static/image/favicon.png",
	)
	embed.add_embed_field(name='Request', value=f"{request.method} | {request.build_absolute_uri()}", inline=False)
	embed.add_embed_field(name='Cookie', value=f"{request.COOKIES}", inline=False)
	webhook.add_embed(embed)
	with open(f'calculator/static/traceback_file/{username}.txt','r', encoding='utf-8') as f:
		webhook.add_file(file=f.read(), filename=f'{username}.txt')
	webhook.execute()
	messages.error(request,"Oops! Something went wrong<br>An error occurred while processing your request. Please try again later.")
	return render(request,'base/500.html', {'darkmode':checkDarkMode(request),"header_msg":"Internal Server Error", 'lang':lang,"sidebarContent":SidebarContent},status=500)


def rickroll(request):
	send_webhook(f'Someone has been rickrolled')
	return HttpResponseRedirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


def tos(request):
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	return render(request,'base/tos.html',{"darkmode": checkDarkMode(request)})

def changelog(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	with open(f'calculator/static/json/commits.json','r', encoding='utf-8') as commit:
		commit_json = json.load(commit)
	return render(request,'base/changelog.html',{"commit_json":commit_json,"darkmode": checkDarkMode(request), "header_msg": "Change Log", 'lang':lang, "sidebarContent":SidebarContent,"cookieUsername":makeCookieheader(cookie_result)})

@delete_visitor("theorycraft")
def theorycraft(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	cookie_result = checkCookie(request)
	MakeLogAddRequestJson(request,cookie_result)
	return render(request, "wiki/theorycraft.html", {"darkmode":checkDarkMode(request), "header_msg": "Archero Calculation", "Theorycraft":local_data['Theorycraft'],"sidebarContent":local_data['SidebarContent'],"cookieUsername":makeCookieheader(cookie_result)})


def delete_cookie(request:HttpResponse,key,name_redirect):
	response = redirect(name_redirect)
	response.delete_cookie(key)
	send_embed(
		author_name="",
		title_embed="Deleted Cookie",
		description_embed=f"",
		field_name=f"Cookies key: {key}",
		field_value=f"Redirected at {name_redirect}",
		e_color="32ec08",
		request=request,
		alert=False
	)
	return response

def delete_session(request):
	key_container = request.session.get("user_credential",None)
	if key_container != None:
		del request.session["user_credential"]
		send_webhook(f'User Credentials Deleted: Session Key {"user_credential"}\n{"user_credential"} was containing {key_container}')
	else:
		send_webhook(f"{key_container} tried to logout.\nRedirected to menu\n__**Cookie**__: {request.COOKIES}\n__**Session**__: {str(request.session.items())}")
	return redirect("menu")


def redirect_skill(request, skill=None):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	if skill != None and local_data["SkillData"].get(skill.replace("_"," "),False):
		return redirect(f"/wiki/skill/{skill}")
	else:
		return redirect("/wiki/skill")

## DEV MODE URL
def set_cookie(request,key_cookie,value_cookie):
	response = redirect("/")
	expires = datetime.now() + timedelta(days=365)
	response.set_cookie(key=key_cookie, value=value_cookie, expires=expires, httponly=True, samesite="Strict")
	return response

def set_session(request,key_cookie,value_cookie):
	request.session["user_credential"] = {key_cookie:value_cookie}
	return redirect("/")

def page_set(request:WSGIRequest):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	cookie_result = checkCookie(request)
	select_choice = request.GET.get("select_choice")
	key = request.GET.get("key")
	value = request.GET.get("value")
	ctx = {
		"header_msg": "Page Set Cookie/Session",
		'lang':lang,
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(cookie_result),
		"cookie": request.COOKIES,
		"session": request.session,
	}
	if select_choice and key and value:
		return redirect(f'/set_{select_choice}/{key}/{value}/')
	return render(request, 'base/page_set.html',ctx)