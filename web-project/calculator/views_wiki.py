from .forms import DamageCalculatorForm
from .models import ArticleMenu,user,StuffTable,HeroTable,TalentTable,SkinTable,AltarTable,JewelLevelTable,EggTable,EggEquippedTable,DragonTable,RunesTable,ReforgeTable,RefineTable,MedalsTable,RelicsTable,WeaponSkinsTable,DamageCalcTable,PromoCode,PromoCodeReward
from .function import checkDarkMode,checkCookie,checkUsernameCredentials,checkIllegalKey,send_webhook,send_embed,calculatePrice,makeCookieheader, getProfileWithCookie, makeLog, loadContent
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
from app.settings import WEBHOOK_URL, c_hostname, DISCORD_NOTIF_ROLE_ID, DISCORD_ERROR_ROLE_ID, DEV_MODE
from django.utils.translation import get_language, gettext as _, gettext_lazy
from django.utils.text import format_lazy
from .local_data import LocalDataContentWiki
from datetime import datetime

missing_data = []

@loadContent(checkMessages=True, db_maintenance=True)
def menu(request):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	list_article = list(ArticleMenu.objects.all().filter(display=True).order_by('index'))
	return render(request, 'base/menu.html', {"darkmode": checkDarkMode(request), "header_msg":_("Menu Archero Wiki"), "sidebarContent":SidebarContent, "cookieUsername":makeCookieheader(cookie_result),"list_article":list_article, "dev_mode":DEV_MODE})

@loadContent(checkMessages=True, db_maintenance=True)
def news(request,titleArticle=None):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	try:
		article = ArticleMenu.objects.get(title=titleArticle)
	except ArticleMenu.DoesNotExist:
		request.session['error_message'] = f"{titleArticle} Article doesn't exist"
		return HttpResponseRedirect(f'/{get_language()}/')
	return render(request, 'wiki/article-news.html', {"darkmode": checkDarkMode(request), "header_msg":_("Menu Archero Wiki"), "sidebarContent":SidebarContent, "cookieUsername":makeCookieheader(cookie_result), "article":article, "article_title": article.title})

@loadContent()
def maze(request):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	with urlopen("https://config-archero.habby.mobi/data/config/MazeConfig.json") as url:
		maze_data_api = json.load(url)
	return render(request, 'wiki/maze.html', {"data_json":maze_data_api, "darkmode": checkDarkMode(request), "header_msg":_("maze"), "sidebarContent":SidebarContent, "cookieUsername":makeCookieheader(cookie_result)})

@loadContent()
def csrf_failure(request, reason=""):
	SidebarContent = LocalDataContentWiki['SidebarContent']
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
	makeLog(request)
	return render(request,'base/csrf_failure.html', {"darkmode": checkDarkMode(request), "header_msg":_("CSRF FAILURE"), "profil":profil, "public_id":public_id, "sidebarContent":SidebarContent, "cookieUsername":makeCookieheader(cookie_result)})

@loadContent(checkMessages=True)
def login(request):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_value = checkCookie(request)
	makeLog(request)
	if (len(cookie_value) >= 1 and "visitor" not in list(cookie_value)): ## normally len(cookie_value) will have maximum 1 length but to be sure 
		cookie_request_name,cookie_request_id = list(cookie_value.items())[0]
		profile = getProfileWithCookie(cookie_request_id,cookie_request_name)
		if profile[0] == False and profile[1] != None:
			return render(request, "base/login.html", {"darkmode":checkDarkMode(request), "sidebarContent":SidebarContent})
		send_webhook(f'{cookie_value} tried to access Login but was redirected to Home\n{request.COOKIES}')
		request.session['error_message'] = f"You can't login again, your username is {cookie_request_name}"
		return HttpResponseRedirect(f'/{get_language()}/')
	else:
		return render(request, "base/login.html", {"darkmode":checkDarkMode(request), "sidebarContent":SidebarContent})

def login_processing(request, username_raw, id_raw):
	response = redirect(f"/{get_language()}")
	cookie_value = checkCookie(request)
	if len(cookie_value) != 0:
		cookie_request_name,cookie_request_id = list(cookie_value.items())[0]
		profile = getProfileWithCookie(cookie_request_id,cookie_request_name)
		if profile[0]:
			request.session['info_message'] = "You are already logged in"
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
		send_embed(boolCheck["ingame_name"],"Successful Login",description_embed="",field_name=f"login/processing/{username_raw}/{id_raw}/",field_value=f"Credentials : `{boolCheck['ingame_name']}`|`{boolCheck['ingame_id']}`\n\n**Response Cookies** : \n{response.cookies}",e_color="32ec08",request=request, alert=False, admin_log=boolCheck.get('admin_log',None))
	else:
		request.session['error_message'] = f"Login Failed : {boolCheck['error_message']}"
		send_embed(boolCheck["ingame_name"],"Login Failed",description_embed=boolCheck["error_message"],field_name=f"login/processing/{username_raw}/{id_raw}/",field_value=f"Credentials : `{boolCheck['ingame_name']}`|`{boolCheck['ingame_id']}`\n\n**Response Cookies** : \n{response.cookies}",e_color="d50400",request=request, alert=True, admin_log=boolCheck.get('admin_log',None))
	return response

@loadContent()
def wiki_menu(request, article=None):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	article_label = str(article).replace('_',' ').capitalize()
	if article != None:
		name_title = article_label
	else:
		name_title = None
	ctx = {
		"darkmode": checkDarkMode(request),
		"sidebarContent":SidebarContent,
		"WikiContent":LocalDataContentWiki["WikiContent"],
		"cookieUsername":makeCookieheader(cookie_result),
		"name_title": name_title,
		"article": article,
		"current_url": request.build_absolute_uri(),
		"current_article": LocalDataContentWiki["WikiContent"].get(article),
	}
	if article is not None or LocalDataContentWiki["WikiContent"].get(article):
		ctx["header_msg"] = _(f"{article_label} - Wiki")
	else:
		ctx["header_msg"] = _("Wiki")
	return render(request, "wiki/menu.html", ctx)

@loadContent()
def item_description(request, item=None):
	
	item_data = LocalDataContentWiki["ItemData"].get(str(item), None)
	if item_data is None:
		item = "Expedition_Fist"
		item_data = LocalDataContentWiki["ItemData"][item]
	
	temp = list(LocalDataContentWiki["ItemData"])
	index_after = temp[(temp.index(item) + 1) % len(temp)]
	index_before = temp[(temp.index(item) - 1) % len(temp)]
	
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	
	ctx = {
		"darkmode": checkDarkMode(request),
		"item": "yes" if item_data else "no",
		"sidebarContent": SidebarContent,
		"ItemData": LocalDataContentWiki["ItemData"],
		"cookieUsername": makeCookieheader(cookie_result),
		"name": item_data['displayName'] if item_data else "",
		"item_data": item_data,
		"url_cpy": request.build_absolute_uri(),
		"header_msg": item_data['displayName'] if item_data else "",
		"index_after": [index_after,LocalDataContentWiki["ItemData"][index_after]],
		"index_before": [index_before,LocalDataContentWiki["ItemData"][index_before]],
	}
	
	return render(request, "wiki/item_description.html", ctx)

@loadContent()
def skill_description(request, skill=None):

	skill_data = LocalDataContentWiki["SkillData"].get(str(skill), None)
	if skill_data is None:
		skill = "Attack_Boost"
		skill_data = LocalDataContentWiki["SkillData"][skill]
	
	image_skill = f"image/skill/{skill.replace(' - ', '_').replace('one-eyed', 'one_eyed').lower()}.png"
	
	temp = list(LocalDataContentWiki["SkillData"])
	index_after = temp[(temp.index(skill) + 1) % len(temp)]
	index_before = temp[(temp.index(skill) - 1) % len(temp)]
	
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	
	ctx = {
		"sidebarContent": SidebarContent,
		"SkillData": LocalDataContentWiki["SkillData"],
		"cookieUsername": makeCookieheader(cookie_result),
		"darkmode": checkDarkMode(request),
		"name": skill_data['displayName'],
		"skill": "yes" if skill_data else "no",
		"skill_data": skill_data,
		"image_skill": image_skill,
		"url_cpy": request.build_absolute_uri(),
		"header_msg": skill_data['displayName'] if skill_data else "",
		"index_after": index_after,
		"index_before": index_before
	}
	
	return render(request, "wiki/skill_description.html", ctx)

@loadContent()
def heros_description(request, hero=None):
	
	hero_data = LocalDataContentWiki["HeroData"].get(hero, None)
	if hero_data is None:
		hero = "Taiga"
		hero_data = LocalDataContentWiki["HeroData"][hero]
	
	temp = list(LocalDataContentWiki["HeroData"])
	index_after = temp[(temp.index(hero) + 1) % len(temp)]
	index_before = temp[(temp.index(hero) - 1) % len(temp)]
	
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	
	ctx = {
		"darkmode": checkDarkMode(request),
		"hero": "yes" if hero_data else "no",
		"sidebarContent": SidebarContent,
		"HeroData": LocalDataContentWiki["HeroData"],
		"cookieUsername": makeCookieheader(cookie_result),
		"hero_data_hero_assist_evolve": hero_data['hero_assist_evolve'],
		"name_hero": hero_data['displayName'],
		"name_hero_initial": hero,
		"hero_data": hero_data,
		"hero_image": f'image/hero_icon/icon_{hero}.png',
		"url_cpy": request.build_absolute_uri(),
		"header_msg": hero_data['displayName'] if hero_data else "",
		"index_after": index_after,
		"index_before": index_before,
	}
	
	return render(request, "wiki/heros_description.html", ctx)

@loadContent()
def upgrade_cost(request,cost_type:str="None",lvl1:int=1,lvl2:int=2,rank:str="None"):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	all_rank = ["A","S","SS"]
	content = ""
	ctx = {
		"darkmode": checkDarkMode(request),
		"header_msg":_("Upgrade Cost"),
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
				"eTitle": _("Equipment Upgrade Cost"),
				"eDescription": format_lazy("{intro} {level1} {to} {level2}", intro=gettext_lazy("To upgrade equipment from level "),level1=lvl1, to=gettext_lazy("to"), level2=lvl2),
				"eImage": "/static/image/wiki-image/Cost_Item.png",
				"eField1": f'{int(price[0]):,}',
				"eField2": f'{int(price[1]):,}',
				"currency1": [_('Gold :'),'gold'],
				"currency2": [_('Scrolls :'),'scroll'],
			}
		else:
			messages.error(request,_(f"The levels need to be between 0 and {max_lvl}"))
			return HttpResponseRedirect(f"/{get_language()}/wiki/upgrade/{cost_type}/1/2/")
	elif cost_type == "heroes":
		if lvl1 <= lvl2 and (0 <= lvl1 <= 119) and (1 <= lvl2 <= 120):
			price = calculatePrice(lvl1,lvl2,cost_type)
			content = {
				"eTitle": _("Heroes Upgrade Cost"),
				"eDescription": format_lazy("{intro} {level1} {to} {level2}", intro=gettext_lazy("To upgrade heroes from level "),level1=lvl1, to=gettext_lazy("to"), level2=lvl2),
				"eImage": "/static/image/wiki-image/Cost_Heroes.png",
				"eField1": f'{int(price[0]):,}',
				"eField2": f'{int(price[1]):,}',
				"currency1": [_('Gold :'),'gold'],
				"currency2": [_('Sapphire :'),'sapphire'],
			}
			print(content)
		else:
			messages.error(request,_("The levels need to be between 0 and 120"))
			return HttpResponseRedirect(f"/{get_language()}/wiki/upgrade/{cost_type}/1/2/")
	elif cost_type == "talents":
		if lvl1 <= lvl2 and (0 <= lvl1 <= 205) and (1 <= lvl2 <= 206):
			price = calculatePrice(lvl1,lvl2,cost_type)
			content = {
				"eTitle": _("Talents Upgrade Cost"),
				"eDescription": format_lazy("{intro} {level1} {to} {level2}", intro=gettext_lazy("To upgrade talents from level "),level1=lvl1, to=gettext_lazy("to"), level2=lvl2),
				"eImage": "/static/image/wiki-image/Cost_Talent.png",
				"eField1": f'{int(price):,}',
				"eField2": f'<br>',
				"currency1": [_('Gold :'),'gold'],
				"currency2": ['',''],
			}
		else:
			messages.error(request,_("The levels need to be between 0 and 206"))
			return HttpResponseRedirect(f"/{get_language()}/wiki/upgrade/{cost_type}/1/2/")
	elif cost_type == "dragons":
		if lvl1 <= lvl2 and (0 <= lvl1 <= 119) and (1 <= lvl2 <= 120):
			if rank in all_rank:
				price = calculatePrice(lvl1,lvl2,cost_type,rank)
				content = {
					"eTitle": _("Dragon Upgrade Cost"),
					"eDescription": format_lazy("{intro} {level1} {to} {level2}", intro=gettext_lazy("To upgrade dragons from level "),level1=lvl1, to=gettext_lazy("to"), level2=lvl2),
					"eImage": "/static/image/wiki-image/Cost_Dragon" + str(rank).upper() + ".png",
					"eField1": f'{int(price[0]):,}',
					"eField2": f'{int(price[1]):,}',
					"currency1": [_('Gold :'),'gold'],
					"currency2": [_('Magestones :'),'magestone'],
				}
			else:
				messages.error(request,_("The rank need to be whether A, S or SS"))
				return HttpResponseRedirect(f"/{get_language()}/wiki/upgrade/{cost_type}/{lvl1}/{lvl2}/A/")
		else:
			messages.error(request,_("The levels need to be between 0 and 120"))
			return HttpResponseRedirect(f"/{get_language()}/wiki/upgrade/{cost_type}/1/2/{rank}/")
	elif cost_type == "relics":
		if lvl1 <= lvl2 and (0 <= lvl1 <= 29) and (1 <= lvl2 <= 30):
			if rank in all_rank:
				price = calculatePrice(lvl1,lvl2,cost_type,rank)
				content = {
					"eTitle": _("Relics Upgrade Cost"),
					"eDescription": format_lazy("{intro} {level1} {to} {level2}", intro=gettext_lazy("To upgrade relics from level "),level1=lvl1, to=gettext_lazy("to"), level2=lvl2),
					"eImage": "/static/image/wiki-image/Cost_Relics" + str(rank).upper() + ".png",
					"eField1": f'{int(price[0]):,}',
					"eField2": f'{int(price[1]):,}',
					"currency1": [_('Gold :'),'gold'],
					"currency2": [_('Starlight :'),'starlight'],
				}
			else:
				messages.error(request,_("The rank need to be whether A, S or SS"))
				return HttpResponseRedirect(f"/{get_language()}/wiki/upgrade/{cost_type}/{lvl1}/{lvl2}/A/")
		else:
			messages.error(request,_("The levels need to be between 0 and 30"))
			return HttpResponseRedirect(f"/{get_language()}/wiki/upgrade/{cost_type}/1/2/{rank}/")
	ctx.update({"content":content})
	return render(request, "wiki/upgrade_cost.html", ctx)

@loadContent()
def gsheetGrid(request):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	ctx = {
		'darkmode':checkDarkMode(request),
		"header_msg":_("Google Sheet Wiki"),
		"GsheetData":LocalDataContentWiki['GsheetData'],
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(cookie_result)
	}
	return render(request, "wiki/gsheet.html", ctx)

@loadContent(db_maintenance=True)
def promocode(request):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	allActiveCode = {}
	promoCodes = PromoCode.objects.all().filter(is_active=True)
	for promoCode in promoCodes:
		if promoCode.deactivateIfExpired():
			datetime_object = datetime.strptime(str(promoCode.expire), "%Y-%m-%d")
			send_webhook(f"Promo Code {promoCode.code} has been deactivated because it expired <t:{int(datetime_object.timestamp())}:F>")
			continue
		promoData = []
		codeRewards = PromoCodeReward.objects.all().filter(promocodeId=promoCode.pk)
		for reward in codeRewards:
			promoData.append(reward)
		allActiveCode[promoCode] = promoData
	ctx = {
		"darkmode": checkDarkMode(request),
		"header_msg":_("Promo Code"),
		"promo_code":allActiveCode,
		"len_promo":len(allActiveCode.keys()),
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(cookie_result)
	}
	return render(request, "wiki/promo-code.html", ctx)

@loadContent(db_maintenance=True,checkMessages=True)
def damage(request):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
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
			messages.error(request,_(f'You attempted to access {profile[1].ingame_name}<br>But your login username is "{ingame_name_cookie}".'))
	else:
		selfHasProfil = "login"
	list_damage_profile = user.objects.filter(ingame_id__iregex=r'^0-00000(?!0)').order_by('ingame_id')
	ctx = {
		"darkmode": checkDarkMode(request),
		"header_msg":_("Damage Calculator"),
		"selfHasProfil":selfHasProfil,
		"selfStats":user_stats,
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(cookie_result),
		"list_damage_profile":list_damage_profile
	}
	return render(request, "wiki/damage.html", ctx)

@loadContent(db_maintenance=True)
def dmgCalc_processing(request,pbid):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	global missing_data
	user_stats = user.objects.get(public_id=pbid)
	StuffTable_stats = StuffTable.objects.get(user_profile=user_stats)
	HeroTable_stats = HeroTable.objects.get(user_profile=user_stats)
	TalentTable_stats = TalentTable.objects.get(user_profile=user_stats)
	SkinTable_stats = SkinTable.objects.get(user_profile=user_stats)
	AltarTable_stats = AltarTable.objects.get(user_profile=user_stats)
	JewelLevelTable_stats = JewelLevelTable.objects.get(user_profile=user_stats)
	EggTable_stats = EggTable.objects.get(user_profile=user_stats)
	EggEquippedTable_stats = EggEquippedTable.objects.get(user_profile=user_stats)
	DragonTable_stats = DragonTable.objects.get(user_profile=user_stats)
	RunesTable_stats = RunesTable.objects.get(user_profile=user_stats)
	ReforgeTable_stats = ReforgeTable.objects.get(user_profile=user_stats)
	RefineTable_stats = RefineTable.objects.get(user_profile=user_stats)
	MedalsTable_stats = MedalsTable.objects.get(user_profile=user_stats)
	RelicsTable_stats = RelicsTable.objects.get(user_profile=user_stats)
	WeaponSkinsTable_stats = WeaponSkinsTable.objects.get(user_profile=user_stats)

	atk_base_hero_choosen = user_stats.atk_base_stats_hero_choosen
	stuff_altar_ascension = AltarTable_stats.stuff_altar_ascension
	heros_altar_ascension = AltarTable_stats.heros_altar_ascension
	refine_weapon_atk = RefineTable_stats.weapon_refine_atk
	refine_weapon_enhanced_equipment = int(RefineTable_stats.weapon_refine_basic_stats)/100
	refine_armor_enhanced_equipment = int(RefineTable_stats.armor_refine_basic_stats)/100
	refine_ring1_atk = RefineTable_stats.ring1_refine_atk
	refine_ring1_enhanced_equipment = int(RefineTable_stats.ring1_refine_basic_stats)/100
	refine_ring2_atk = RefineTable_stats.ring2_refine_atk
	refine_ring2_enhanced_equipment = int(RefineTable_stats.ring2_refine_basic_stats)/100
	refine_bracelet_atk = RefineTable_stats.bracelet_refine_atk
	refine_bracelet_enhanced_equipment = int(RefineTable_stats.bracelet_refine_basic_stats)/100
	refine_locket_enhanced_equipment = int(RefineTable_stats.locket_refine_basic_stats)/100
	refine_book_enhanced_equipment = int(RefineTable_stats.book_refine_basic_stats)/100
	brave_privileges_level = int(user_stats.brave_privileges_level)
	## Get Talents Stats
	talent_stats_dict = TalentTable_stats.getTalentStats()
	## Get all Relics Stats
	relics_stats:dict = RelicsTable_stats.relics_Stats()
	## Get Altar Ascension Stats
	altar_stuff_ascension_atk = local_data["StuffAltarAscension"]['attack'][stuff_altar_ascension]
	altar_stuff_ascension_equipment_base = local_data["StuffAltarAscension"]['equipment_base'][stuff_altar_ascension]
	altar_heros_ascension_atk = local_data['HerosAltarAscension']['attack'][heros_altar_ascension]
	altar_heros_ascension_heros_base = local_data['HerosAltarAscension']['heros_base'][heros_altar_ascension]
	altar_heros_ascension_dmg_elite = local_data['HerosAltarAscension']['dmg_elite'][heros_altar_ascension]
	## Get Altar Stats 
	altar_stuff_atk = AltarTable_stats.CalculAltar("stuff","attack",relics_stats.get('eqpm_altar_stats_var',0.0))
	altar_hero_atk = AltarTable_stats.CalculAltar("heros","attack",relics_stats.get('eqpm_altar_stats_var',0.0)) ##laisser le S (le nom du field prend un s)
	# Get All Heroes Stats
	hero_Atreus = HeroTable_stats.HerosStatsRecup("Atreus")
	hero_Urasil = HeroTable_stats.HerosStatsRecup("Urasil")
	hero_Phoren = HeroTable_stats.HerosStatsRecup("Phoren")
	hero_Taranis = HeroTable_stats.HerosStatsRecup("Taranis")
	hero_Helix = HeroTable_stats.HerosStatsRecup("Helix") 
	hero_Meowgik = HeroTable_stats.HerosStatsRecup("Meowgik")
	hero_Shari = HeroTable_stats.HerosStatsRecup("Shari")
	hero_Ayana = HeroTable_stats.HerosStatsRecup("Ayana")
	hero_Onir = HeroTable_stats.HerosStatsRecup("Onir") 
	hero_Rolla = HeroTable_stats.HerosStatsRecup("Rolla")
	hero_Bonnie = HeroTable_stats.HerosStatsRecup("Bonnie")
	hero_Sylvan = HeroTable_stats.HerosStatsRecup("Sylvan")
	hero_Shade = HeroTable_stats.HerosStatsRecup("Shade") 
	hero_Ophelia = HeroTable_stats.HerosStatsRecup("Ophelia")
	hero_Ryan = HeroTable_stats.HerosStatsRecup("Ryan")
	hero_Lina = HeroTable_stats.HerosStatsRecup("Lina")
	hero_Aquea = HeroTable_stats.HerosStatsRecup("Aquea")
	hero_Shingen = HeroTable_stats.HerosStatsRecup("Shingen") 
	hero_Gugu = HeroTable_stats.HerosStatsRecup("Gugu")
	hero_Iris = HeroTable_stats.HerosStatsRecup("Iris")
	hero_Blazo = HeroTable_stats.HerosStatsRecup("Blazo")
	hero_Melinda = HeroTable_stats.HerosStatsRecup("Melinda")
	hero_Elaine = HeroTable_stats.HerosStatsRecup("Elaine")
	hero_Bobo = HeroTable_stats.HerosStatsRecup("Bobo")
	hero_Stella = HeroTable_stats.HerosStatsRecup("Stella")
	hero_Taiga = HeroTable_stats.HerosStatsRecup("Taiga")
	## Get Skin Atk and Hp
	skin_atk_boost = SkinTable_stats.skin_attack
	## Get Passiv Stats From Type 1 Egg
	egg_green_bat_passiv = EggTable_stats.GetPassivEggStats1("green_bat", missing_data)
	egg_bomb_ghost_passiv = EggTable_stats.GetPassivEggStats1("bomb_ghost",missing_data)
	egg_piranha_passiv = EggTable_stats.GetPassivEggStats1("piranha",missing_data)
	## Get Passiv Stats From Type 2 Egg
	egg_skeleton_archer_passiv = EggTable_stats.GetPassivEggStats2("skeleton_archer",missing_data)
	egg_skeleton_soldier_passiv = EggTable_stats.GetPassivEggStats2("skeleton_soldier",missing_data)
	egg_fire_mage_passiv = EggTable_stats.GetPassivEggStats2("fire_mage",missing_data)
	egg_ice_mage_passiv = EggTable_stats.GetPassivEggStats2("ice_mage",missing_data)
	egg_flame_ghost_passiv = EggTable_stats.GetPassivEggStats2("flame_ghost",missing_data)
	egg_tornado_demon_passiv = EggTable_stats.GetPassivEggStats2("tornado_demon",missing_data)
	egg_skull_wizard_passiv = EggTable_stats.GetPassivEggStats2("skull_wizard",missing_data)
	egg_crazy_spider_passiv = EggTable_stats.GetPassivEggStats2("crazy_spider",missing_data)
	egg_fire_element_passiv = EggTable_stats.GetPassivEggStats2("fire_element",missing_data)
	egg_pea_shooter_passiv = EggTable_stats.GetPassivEggStats2("pea_shooter",missing_data)
	egg_shadow_assassin_passiv = EggTable_stats.GetPassivEggStats2("shadow_assassin",missing_data)
	egg_one_eyed_bat_passiv = EggTable_stats.GetPassivEggStats2("one_eyed_bat",missing_data)
	egg_scarlet_mage_passiv = EggTable_stats.GetPassivEggStats2("scarlet_mage",missing_data)
	egg_icefire_phantom_passiv = EggTable_stats.GetPassivEggStats2("icefire_phantom",missing_data)
	egg_purple_phantom_passiv = EggTable_stats.GetPassivEggStats2("purple_phantom",missing_data)
	egg_savage_spider_passiv = EggTable_stats.GetPassivEggStats2("savage_spider",missing_data)
	egg_flaming_bug_passiv = EggTable_stats.GetPassivEggStats2("flaming_bug",missing_data)
	egg_crimson_zombie_passiv = EggTable_stats.GetPassivEggStats2("crimson_zombie",missing_data)
	egg_elite_archer_passiv = EggTable_stats.GetPassivEggStats2("elite_archer",missing_data)
	## Get Passiv Stats From Type 3 Egg
	egg_arch_leader_passiv = EggTable_stats.GetPassivEggStats3("arch_leader",missing_data)
	egg_skeleton_king_passiv = EggTable_stats.GetPassivEggStats3("skeleton_king",missing_data)
	egg_crimson_witch_passiv = EggTable_stats.GetPassivEggStats3("crimson_witch",missing_data)
	egg_queen_bee_passiv = EggTable_stats.GetPassivEggStats3("queen_bee",missing_data)
	egg_ice_worm_passiv = EggTable_stats.GetPassivEggStats3("ice_worm",missing_data)
	egg_medusa_boss_passiv = EggTable_stats.GetPassivEggStats3("medusa_boss",missing_data)
	egg_ice_demon_passiv = EggTable_stats.GetPassivEggStats3("ice_demon",missing_data)
	egg_giant_owl_passiv = EggTable_stats.GetPassivEggStats3("giant_owl",missing_data)
	egg_fire_demon_passiv = EggTable_stats.GetPassivEggStats3("fire_demon",missing_data)
	egg_krab_boss_passiv = EggTable_stats.GetPassivEggStats3("krab_boss",missing_data)
	egg_desert_goliath_passiv = EggTable_stats.GetPassivEggStats3("desert_goliath",missing_data)
	egg_scythe_pharoah_passiv = EggTable_stats.GetPassivEggStats3("scythe_pharoah",missing_data)
	egg_infernal_demon_passiv = EggTable_stats.GetPassivEggStats3("infernal_demon",missing_data)
	egg_sinister_touch_passiv = EggTable_stats.GetPassivEggStats3("sinister_touch",missing_data)
	egg_fireworm_queen_passiv = EggTable_stats.GetPassivEggStats3("fireworm_queen",missing_data)
	## Get Brave Privilege Stats
	brave_privileges_stats = local_data["BravePrivileges"]['level' + str(brave_privileges_level)]
	## Get Special Bonus Stats
	BonusSpe_jewel_weapon = JewelLevelTable_stats.JewelSpeBonusStatsRecup('weapon',brave_privileges_stats['Weapon JSSSA'],relics_stats.get("jewel_attack_bonus_var",0))
	BonusSpe_jewel_ring1 = JewelLevelTable_stats.JewelSpeBonusStatsRecup('ring1',brave_privileges_stats['Ring JSSSA'])
	BonusSpe_jewel_bracelet = JewelLevelTable_stats.JewelSpeBonusStatsRecup('bracelet',brave_privileges_stats['Bracelet JSSSA'],relics_stats.get("jewel_attack_bonus_var",0))
	BonusSpe_jewel_book = JewelLevelTable_stats.JewelSpeBonusStatsRecup('book',brave_privileges_stats['Spellbook JSSSA'])
	## DRAGON
	relics_dragon_base_stats = relics_stats.get('dragon_base_stats_var',0.0)
	dragon_stats_dict = DragonTable_stats.DragonStatueStats(relics_dragon_base_stats)
	## Get Dragon passiv Skills
	dragons_skills = DragonTable_stats.getPassivSkillDragon()
	## Get All Stats of Equipped Egg
	activ_egg_stats = EggEquippedTable_stats.GetEggStats(missing_data)
	## Get Reforge Stats
	reforge_atk_power = ReforgeTable_stats.ReforgePowerCourage("power")
	reforge_atk_courage = ReforgeTable_stats.ReforgePowerCourage("courage")
	## Get Rune Line Stats
	runelinePower = RunesTable_stats.getValueLinePower()
	runelineRecovery = RunesTable_stats.getValueLineRecovery()
	runelineCourage = RunesTable_stats.getValueLineCourage()
	## Get Weapon Skin Stats
	weapon_skin_stats = WeaponSkinsTable_stats.getWeaponSkinStats()
	## Get all Medals Stats
	medal_stats = MedalsTable_stats.medal_calc()
	# Get All Jewel's Stats
	stats_jewel_dict = JewelLevelTable_stats.JewelStatsRecup(float(relics_stats.get("jewel_attack_bonus_var",0)),float(relics_stats.get("jewel_hp_bonus_var",0)))
############################################## CALCUL #######################################################
	egg_var_passiv_heros_power_up = int(egg_arch_leader_passiv[3]) + int(egg_medusa_boss_passiv[3]) + int(egg_fire_demon_passiv[3]) + int(egg_krab_boss_passiv[3]) + int(egg_skeleton_king_passiv[1]) + int(egg_skeleton_king_passiv[3]) + int(egg_desert_goliath_passiv[1]) + int(egg_desert_goliath_passiv[3]) + int(egg_ice_demon_passiv[1]) + int(egg_ice_demon_passiv[3]) + int(egg_fireworm_queen_passiv[3]) + int(egg_sinister_touch_passiv[1]) + int(egg_infernal_demon_passiv[3]) + int(egg_scythe_pharoah_passiv[3])
	egg_var_passiv_enhanced_equipment = int(egg_crimson_witch_passiv[3]) + int(egg_queen_bee_passiv[3]) + int(egg_ice_worm_passiv[1]) + int(egg_ice_worm_passiv[3]) + int(egg_giant_owl_passiv[1]) + int(egg_giant_owl_passiv[3]) + int(egg_infernal_demon_passiv[1]) + int(egg_sinister_touch_passiv[3])
	cumul_var_passiv_power_up_hero = (float(relics_stats.get('hero_base_stats_increased_var',0.0)) + float(medal_stats['hero_base_enhanced']) + float(talent_stats_dict['talents_hero_power_up']) + float(egg_var_passiv_heros_power_up) + float(altar_heros_ascension_heros_base))/100
	cumul_var_passiv_enhanced_equipment = (float(runelineRecovery.get('var_enhanced_eqpm',0.0)) + float(relics_stats.get('enhance_eqpm_var',0.0)) + float(medal_stats['enhance_equipment']) + float(talent_stats_dict['talents_enhanced_equipment']) + float(egg_var_passiv_enhanced_equipment) + float(altar_stuff_ascension_equipment_base))/100+1
	
	## Get Stuff Stats
	stuff_activ_stats = StuffTable_stats.getStuffStats(cumul_var_passiv_enhanced_equipment,refine_weapon_enhanced_equipment,refine_armor_enhanced_equipment,refine_ring1_enhanced_equipment,refine_ring2_enhanced_equipment,refine_bracelet_enhanced_equipment,refine_locket_enhanced_equipment,refine_book_enhanced_equipment,weapon_skin_stats,relics_stats.get("ring_basic_stats_var",0.0))

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
	cumul_stuff_flat_activ_atk = round(stuff_activ_stats['weapon_total'] + stuff_activ_stats['bracelet_total'] + stuff_activ_stats.get("ring_attack_flat",0))

	cumul_heros_var_passiv_atk = float(hero_Taranis[2]) + float(hero_Meowgik[2]) + float(hero_Ayana[2]) + float(hero_Rolla[2]) + float(hero_Sylvan[2]) + float(hero_Aquea[2]) + float(hero_Iris[2]) + float(hero_Bonnie[4]) + float(hero_Shade[7]) + float(hero_Melinda[7]) + float(hero_Bobo[1]) + float(hero_Bobo[4]) + float(hero_Stella[2]) + float(hero_Taiga[6])
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
			calc_user_dmg = DamageCalcTable.objects.get(user_profile=user_stats)
			calc_user_dmg.hero_atk = hero_atk_step
			calc_user_dmg.save()
			return HttpResponseRedirect(f"/{get_language()}/wiki/damage-calculator/{pbid}/")
		except DamageCalcTable.DoesNotExist:
			return HttpResponseRedirect(f"/stats/calc/{pbid}/2/?log=False")
	else :
		return HttpResponseRedirect(f"/{get_language()}/wiki/damage-calculator/")

@loadContent(db_maintenance=True,checkMessages=True)
def damageCalc(request,pbid):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	try:
		user_stats = user.objects.get(public_id=pbid)
		calc_user_dmg = DamageCalcTable.objects.get(user_profile=user_stats.pk)
		RunesTable_stats = RunesTable.objects.get(user_profile=user_stats.pk)
	except (user.DoesNotExist,DamageCalcTable.DoesNotExist,RunesTable.DoesNotExist):	
		return HttpResponseRedirect(f"/{get_language()}/wiki/damage-calculator/calc/{pbid}/")
	ctx = {
		'darkmode':checkDarkMode(request),
		"header_msg":_("Damage Calc"),
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(cookie_result)
	}
	if request.method == "GET":
		damage_calc_form = DamageCalculatorForm()
		resultCalcDamg = calc_user_dmg.calculDamage()
		ctx['averageDamage'] = resultCalcDamg['averageDamageAll']
		ctx['crit_dmg'] = str(calc_user_dmg.crit_dmg) + "%"
		ctx['crit_rate'] = str(calc_user_dmg.crit_rate) + "%"
		ctx["mob_ground_melee_damage"] = resultCalcDamg['mob_ground_melee_damage']
		ctx["mob_ground_range_damage"] = resultCalcDamg['mob_ground_range_damage']
		ctx["mob_airborne_melee_damage"] = resultCalcDamg['mob_airborne_melee_damage']
		ctx["mob_airborne_range_damage"] = resultCalcDamg['mob_airborne_range_damage']
		ctx["boss_ground_melee_damage"] = resultCalcDamg['boss_ground_melee_damage']
		ctx["boss_ground_range_damage"] = resultCalcDamg['boss_ground_range_damage']
		ctx["boss_airborne_melee_damage"] = resultCalcDamg['boss_airborne_melee_damage']
		ctx["boss_airborne_range_damage"] = resultCalcDamg['boss_airborne_range_damage']
		ctx["vars_dict"] =  RunesTable_stats.getRunesDmgCalc()
	elif request.method == "POST":
		damage_calc_form = DamageCalculatorForm(request.POST)
		if damage_calc_form.is_valid() and 'runes' in request.POST:
			listHeroStepAtk = calc_user_dmg.hero_atk
			param_runes_display = RunesTable_stats.getRunesDmgCalc()
			power_rune = RunesTable_stats.getValueLinePower()
			courage_rune = RunesTable_stats.getValueLineCourage()
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
				"fifthSelect": fifth_select,"fifthInput": fifth_input,"averageDamage": resultCalcDamg['averageDamageAll'],"crit_dmg": str(resultCalcDamg['crit_dmg']) + "%",
				"crit_rate": str(resultCalcDamg['crit_rate']) + "%","mob_ground_melee_damage": resultCalcDamg['mob_ground_melee_damage'],"mob_ground_range_damage": resultCalcDamg['mob_ground_range_damage'],
				"mob_airborne_melee_damage": resultCalcDamg['mob_airborne_melee_damage'],"mob_airborne_range_damage": resultCalcDamg['mob_airborne_range_damage'],
				"boss_ground_melee_damage": resultCalcDamg['boss_ground_melee_damage'],"boss_ground_range_damage": resultCalcDamg['boss_ground_range_damage'],
				"boss_airborne_melee_damage": resultCalcDamg['boss_airborne_melee_damage'],"boss_airborne_range_damage": resultCalcDamg['boss_airborne_range_damage'],
			})
		else:
			form_error = damage_calc_form.errors.items()
			for k,v in form_error:
				error_msg = f"{k} : {str(v[0])}"
			request.session['error_message'] = error_msg
			return HttpResponseRedirect(f"/{get_language()}/wiki/damage-calculator/{pbid}/")
	else:
		return HttpResponseRedirect(f"/{get_language()}/wiki/damage-calculator/{pbid}/")
	ctx['damage_calc_form'] = damage_calc_form
	return render(request, "wiki/dmg_calc.html", ctx)

@loadContent()
def handler404(request, exception):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	ctx = {
		'darkmode':checkDarkMode(request),
		"header_msg":_("Page Not Found"),
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(cookie_result)
	}
	return render(request,'base/404.html', ctx, status=404)

@loadContent()
def handler500(request):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
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
	messages.error(request,_("Oops! Something went wrong<br>An error occurred while processing your request. Please try again later."))
	return render(request,'base/500.html', {'darkmode':checkDarkMode(request),"header_msg":_("Internal Server Error"),"sidebarContent":SidebarContent},status=500)


@loadContent()
def tos(request):
	makeLog(request)
	return render(request,'base/tos.html',{"darkmode": checkDarkMode(request)})

@loadContent()
def changelog(request):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	cookie_result = checkCookie(request)
	makeLog(request)
	with open(f'calculator/static/json/commits.json','r', encoding='utf-8') as commit:
		commit_json = json.load(commit)
	return render(request,'base/changelog.html',{"commit_json":commit_json,"darkmode": checkDarkMode(request), "header_msg":_("Change Log"),  "sidebarContent":SidebarContent,"cookieUsername":makeCookieheader(cookie_result)})

@loadContent()
def theorycraft(request):
	cookie_result = checkCookie(request)
	makeLog(request)
	return render(request, "wiki/theorycraft.html", {"darkmode":checkDarkMode(request), "header_msg":_("Archero Calculation"), "Theorycraft":LocalDataContentWiki['Theorycraft'],"sidebarContent":LocalDataContentWiki['SidebarContent'],"cookieUsername":makeCookieheader(cookie_result)})


def delete_cookie(request:HttpResponse,key,name_redirect):
	response = redirect(name_redirect)
	response.delete_cookie(key)
	send_embed(
		author_name="",
		title_embed="Deleted Cookie",
		description_embed="",
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


## DEV MODE URL
def set_cookie(request,key_cookie,value_cookie):
	response = redirect("/")
	expires = datetime.now() + timedelta(days=365)
	response.set_cookie(key=key_cookie, value=value_cookie, expires=expires, httponly=True, samesite="Strict")
	return response

def set_session(request,key_cookie,value_cookie):
	request.session["user_credential"] = {key_cookie:value_cookie}
	return redirect("/")

@loadContent()
def page_set(request:WSGIRequest):
	if DEV_MODE:
		SidebarContent = LocalDataContentWiki['SidebarContent']
		cookie_result = checkCookie(request)
		select_choice = request.GET.get("select_choice")
		key = request.GET.get("key")
		value = request.GET.get("value")
		ctx = {
			"header_msg":_("Page Set Cookie/Session"),
			"sidebarContent":SidebarContent,
			"cookieUsername":makeCookieheader(cookie_result),
			"cookie": request.COOKIES,
			"session": request.session,
		}
		if select_choice and key and value:
			return redirect(f'/set_{select_choice}/{key}/{value}/')
		return render(request, 'base/page_set.html',ctx)
	else:
		return HttpResponseRedirect('/')