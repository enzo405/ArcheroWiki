from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from math import *
from .forms import UserForm,StuffForm,HeroForm,TalentForm,SkinForm,AltarForm,JewelTypeForm,JewelLevelForm,EggForm,EggEquippedForm,DragonForm,RunesForm,ReforgeForm,RefineForm,MedalsForm,RelicsForm,WeaponSkinForm
from .image import create_image
from .models import user,StuffTable,HeroTable,TalentTable,SkinTable,AltarTable,JewelTypeTable,JewelLevelTable,EggTable,EggEquippedTable,DragonTable,RunesTable,ReforgeTable,RefineTable,MedalsTable,RelicsTable,WeaponSkinsTable,DamageCalcTable
from .function import checkDarkMode,getCredentialForNonLoginRequired,checkMessages,all_formIsValid,findFormError,checkCookie,login_required,create_unique_id,send_embed,makeLog, makeCookieheader, db_maintenance, checkContributor, getProfileWithCookie, loadContent
import json, os
from app.settings import DEV_MODE, c_hostname, DEBUG_STATS
from django.utils.translation import gettext as _, get_language
from .data.wiki_data import LocalDataContentWiki

missing_data = []

# Put a try catch if the database is empty, because when makeing `python manage.py makemigrations|migrate` it will give an error because the calculator_user relation doesn't exist
try:
	user_init_primary_key = user.objects.get(ingame_id="0-000000", ingame_name="user_init").pk
except:
	user_init_primary_key = 6
## HHttpResponseRedirect doesn't allow messages.<type>(request,<message:str>) because the messages are stored in the user's session, and a new request means a new session.
## redirect allow messages.<type>(request,<message:str>)

@loadContent(db_maintenance=True)
def views_calc_stats(request,pbid:int,redirectPath:int):
	global missing_data
	with open("calculator/data/calculator_data.json", 'r', encoding="utf-8") as f:
		calculator_data = json.load(f)
	missing_data.clear()
	try:
		user_stats = user.objects.get(public_id=pbid)
	except user.DoesNotExist:
		return HttpResponseRedirect(f'{get_language()}/')
	ingame_name = user_stats.ingame_name
	other_model = user_stats.getOtherModels()
	StuffTable_stats = other_model['StuffTable']
	HeroTable_stats = other_model['HeroTable']
	TalentTable_stats = other_model['TalentTable']
	SkinTable_stats = other_model['SkinTable']
	AltarTable_stats = other_model['AltarTable']
	JewelLevelTable_stats = other_model['JewelLevelTable']
	EggTable_stats = other_model['EggTable']
	EggEquippedTable_stats = other_model['EggEquippedTable']
	DragonTable_stats = other_model['DragonTable']
	RunesTable_stats = other_model['RunesTable']
	ReforgeTable_stats = other_model['ReforgeTable']
	RefineTable_stats = other_model['RefineTable']
	MedalsTable_stats = other_model['MedalsTable']
	RelicsTable_stats = other_model['RelicsTable']
	WeaponSkinsTable_stats = other_model['WeaponSkinsTable']
	try:
		os.remove(f"calculator/static/image/stuff_save/{int(pbid)}.png")
	except (FileNotFoundError,IsADirectoryError,OSError):
		pass
	################################# REQUÊTE DES ENTRÉES DE L'USERS #######################################################
	atk_base_hero_choosen = user_stats.atk_base_stats_hero_choosen
	health_base_hero_choosen = user_stats.health_base_stats_hero_choosen
	stuff_altar_ascension = AltarTable_stats.stuff_altar_ascension
	heros_altar_ascension = AltarTable_stats.heros_altar_ascension
	refine_weapon_atk = RefineTable_stats.weapon_refine_atk
	refine_weapon_enhanced_equipment = int(RefineTable_stats.weapon_refine_basic_stats)/100
	refine_armor_hp = RefineTable_stats.armor_refine_hp
	refine_armor_enhanced_equipment = int(RefineTable_stats.armor_refine_basic_stats)/100
	refine_ring1_atk = RefineTable_stats.ring1_refine_atk
	refine_ring1_enhanced_equipment = int(RefineTable_stats.ring1_refine_basic_stats)/100
	refine_ring2_atk = RefineTable_stats.ring2_refine_atk
	refine_ring2_enhanced_equipment = int(RefineTable_stats.ring2_refine_basic_stats)/100
	refine_bracelet_atk = RefineTable_stats.bracelet_refine_atk
	refine_bracelet_enhanced_equipment = int(RefineTable_stats.bracelet_refine_basic_stats)/100
	refine_locket_hp = RefineTable_stats.locket_refine_hp
	refine_locket_enhanced_equipment = int(RefineTable_stats.locket_refine_basic_stats)/100
	refine_book_hp = RefineTable_stats.book_refine_hp
	refine_book_enhanced_equipment = int(RefineTable_stats.book_refine_basic_stats)/100
	brave_privileges_level = int(user_stats.brave_privileges_level)
	## Get Talents Stats
	talent_stats_dict = TalentTable_stats.getTalentStats()
	## Get all Relics Stats
	relics_stats:dict = RelicsTable_stats.relics_Stats()
	## Get Altar Ascension Stats
	altar_stuff_ascension_atk = calculator_data["StuffAltarAscension"]['attack'][stuff_altar_ascension]
	altar_stuff_ascension_hp = calculator_data["StuffAltarAscension"]['hp'][stuff_altar_ascension]
	altar_stuff_ascension_healing_effect = calculator_data["StuffAltarAscension"]['healing_effect'][stuff_altar_ascension]
	altar_stuff_ascension_equipment_base = calculator_data["StuffAltarAscension"]['equipment_base'][stuff_altar_ascension]
	altar_heros_ascension_atk = calculator_data['HerosAltarAscension']['attack'][heros_altar_ascension]
	altar_heros_ascension_hp = calculator_data['HerosAltarAscension']['hp'][heros_altar_ascension]
	altar_heros_ascension_hp_drop = calculator_data['HerosAltarAscension']['hp_drop'][heros_altar_ascension]
	altar_heros_ascension_heros_base = calculator_data['HerosAltarAscension']['heros_base'][heros_altar_ascension]
	altar_heros_ascension_dmg_elite = calculator_data['HerosAltarAscension']['dmg_elite'][heros_altar_ascension]
	## Get Altar Stats 
	altar_stuff_atk = AltarTable_stats.CalculAltar("stuff","attack",relics_stats.get('eqpm_altar_stats_var',0.0))
	altar_stuff_hp = AltarTable_stats.CalculAltar("stuff","hp",relics_stats.get('eqpm_altar_stats_var',0.0))
	altar_stuff_healing_effect = AltarTable_stats.CalculAltar("stuff","healing_effect",relics_stats.get('eqpm_altar_stats_var',0.0))
	altar_hero_atk = AltarTable_stats.CalculAltar("heros","attack",relics_stats.get('eqpm_altar_stats_var',0.0)) ##laisser le S (le nom du field prend un s)
	altar_hero_hp = AltarTable_stats.CalculAltar("heros","hp",relics_stats.get('eqpm_altar_stats_var',0.0))
	altar_hero_projectile_resistance = AltarTable_stats.CalculAltar("heros","projectile_resistance",relics_stats.get('eqpm_altar_stats_var',0.0))
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
	skin_health_boost = SkinTable_stats.skin_health
	skin_atk_boost = SkinTable_stats.skin_attack
	## Get Passiv Stats From Type 1 Egg
	egg_green_bat_passiv = EggTable_stats.GetPassivEggStats1("green_bat", missing_data)
	egg_vase_passiv = EggTable_stats.GetPassivEggStats1("vase",missing_data)
	egg_bomb_ghost_passiv = EggTable_stats.GetPassivEggStats1("bomb_ghost",missing_data)
	egg_rock_puppet_passiv = EggTable_stats.GetPassivEggStats1("rock_puppet",missing_data)
	egg_party_tree_passiv = EggTable_stats.GetPassivEggStats1("party_tree",missing_data)
	egg_zombie_passiv = EggTable_stats.GetPassivEggStats1("zombie",missing_data)
	egg_piranha_passiv = EggTable_stats.GetPassivEggStats1("piranha",missing_data)
	## Get Passiv Stats From Type 2 Egg
	egg_wolfhound_passiv = EggTable_stats.GetPassivEggStats2("wolfhound",missing_data)
	egg_skeleton_archer_passiv = EggTable_stats.GetPassivEggStats2("skeleton_archer",missing_data)
	egg_skeleton_soldier_passiv = EggTable_stats.GetPassivEggStats2("skeleton_soldier",missing_data)
	egg_wasp_passiv = EggTable_stats.GetPassivEggStats2("wasp",missing_data)
	egg_fire_mage_passiv = EggTable_stats.GetPassivEggStats2("fire_mage",missing_data)
	egg_medusa_passiv = EggTable_stats.GetPassivEggStats2("medusa",missing_data)
	egg_ice_mage_passiv = EggTable_stats.GetPassivEggStats2("ice_mage",missing_data)
	egg_fire_lizard_passiv = EggTable_stats.GetPassivEggStats2("fire_lizard",missing_data)
	egg_flame_ghost_passiv = EggTable_stats.GetPassivEggStats2("flame_ghost",missing_data)
	egg_thorny_snake_passiv = EggTable_stats.GetPassivEggStats2("thorny_snake",missing_data)
	egg_tornado_demon_passiv = EggTable_stats.GetPassivEggStats2("tornado_demon",missing_data)
	egg_scarecrow_passiv = EggTable_stats.GetPassivEggStats2("scarecrow",missing_data)
	egg_long_dragon_passiv = EggTable_stats.GetPassivEggStats2("long_dragon",missing_data)
	egg_skull_wizard_passiv = EggTable_stats.GetPassivEggStats2("skull_wizard",missing_data)
	egg_lava_golem_passiv = EggTable_stats.GetPassivEggStats2("lava_golem",missing_data)
	egg_ice_golem_passiv = EggTable_stats.GetPassivEggStats2("ice_golem",missing_data)
	egg_cactus_passiv = EggTable_stats.GetPassivEggStats2("cactus",missing_data)
	egg_crazy_spider_passiv = EggTable_stats.GetPassivEggStats2("crazy_spider",missing_data)
	egg_fire_element_passiv = EggTable_stats.GetPassivEggStats2("fire_element",missing_data)
	egg_skeleton_swordsman_passiv = EggTable_stats.GetPassivEggStats2("skeleton_swordsman",missing_data)
	egg_scythe_mage_passiv = EggTable_stats.GetPassivEggStats2("scythe_mage",missing_data)
	egg_pea_shooter_passiv = EggTable_stats.GetPassivEggStats2("pea_shooter",missing_data)
	egg_shadow_assassin_passiv = EggTable_stats.GetPassivEggStats2("shadow_assassin",missing_data)
	egg_tornado_mage_passiv = EggTable_stats.GetPassivEggStats2("tornado_mage",missing_data)
	egg_spitting_mushroom_passiv = EggTable_stats.GetPassivEggStats2("spitting_mushroom",missing_data)
	egg_rolling_mushroom_passiv = EggTable_stats.GetPassivEggStats2("rolling_mushroom",missing_data)
	egg_fallen_bat_passiv = EggTable_stats.GetPassivEggStats2("fallen_bat",missing_data)
	egg_one_eyed_bat_passiv = EggTable_stats.GetPassivEggStats2("one_eyed_bat",missing_data)
	egg_scarlet_mage_passiv = EggTable_stats.GetPassivEggStats2("scarlet_mage",missing_data)
	egg_icefire_phantom_passiv = EggTable_stats.GetPassivEggStats2("icefire_phantom",missing_data)
	egg_purple_phantom_passiv = EggTable_stats.GetPassivEggStats2("purple_phantom",missing_data)
	egg_tundra_dragon_passiv = EggTable_stats.GetPassivEggStats2("tundra_dragon",missing_data)
	egg_sandian_passiv = EggTable_stats.GetPassivEggStats2("sandian",missing_data)
	egg_nether_puppet_passiv = EggTable_stats.GetPassivEggStats2("nether_puppet",missing_data)
	egg_psionic_scarecrow_passiv = EggTable_stats.GetPassivEggStats2("psionic_scarecrow",missing_data)
	egg_steel_dryad_passiv = EggTable_stats.GetPassivEggStats2("steel_dryad",missing_data)
	egg_savage_spider_passiv = EggTable_stats.GetPassivEggStats2("savage_spider",missing_data)
	egg_flaming_bug_passiv = EggTable_stats.GetPassivEggStats2("flaming_bug",missing_data)
	egg_fat_bat_passiv = EggTable_stats.GetPassivEggStats2("fat_bat",missing_data)
	egg_shark_bro_passiv = EggTable_stats.GetPassivEggStats2("shark_bro",missing_data)
	egg_crimson_zombie_passiv = EggTable_stats.GetPassivEggStats2("crimson_zombie",missing_data)
	egg_plainswolf_passiv = EggTable_stats.GetPassivEggStats2("plainswolf",missing_data)
	egg_elite_archer_passiv = EggTable_stats.GetPassivEggStats2("elite_archer",missing_data)
	egg_little_dragon_passiv = EggTable_stats.GetPassivEggStats2("little_dragon",missing_data)
	egg_rage_golem_passiv = EggTable_stats.GetPassivEggStats2("rage_golem",missing_data)
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
	brave_privileges_stats = calculator_data["BravePrivileges"]['level' + str(brave_privileges_level)]
	## Get Special Bonus Stats
	BonusSpe_jewel_weapon = JewelLevelTable_stats.JewelSpeBonusStatsRecup('weapon',brave_privileges_stats['Weapon JSSSA'],relics_stats.get("jewel_attack_bonus_var",0))
	BonusSpe_jewel_armor = JewelLevelTable_stats.JewelSpeBonusStatsRecup('armor',brave_privileges_stats['Armor JSSSA'],relics_stats.get("jewel_hp_bonus_var",0))
	BonusSpe_jewel_ring1 = JewelLevelTable_stats.JewelSpeBonusStatsRecup('ring1',brave_privileges_stats['Ring JSSSA'])
	BonusSpe_jewel_ring2 = JewelLevelTable_stats.JewelSpeBonusStatsRecup('ring2',brave_privileges_stats['Ring JSSSA'])
	BonusSpe_jewel_bracelet = JewelLevelTable_stats.JewelSpeBonusStatsRecup('bracelet',brave_privileges_stats['Bracelet JSSSA'],relics_stats.get("jewel_attack_bonus_var",0))
	BonusSpe_jewel_locket = JewelLevelTable_stats.JewelSpeBonusStatsRecup('locket',brave_privileges_stats['Locket JSSSA'],relics_stats.get("jewel_attack_bonus_var",0))
	BonusSpe_jewel_book = JewelLevelTable_stats.JewelSpeBonusStatsRecup('book',brave_privileges_stats['Spellbook JSSSA'])
	## Get Global Jewel Level
	all_jewel_lvl_dict = JewelLevelTable_stats.allLevelForImage()
	## DRAGON
	relics_dragon_base_stats = relics_stats.get('dragon_base_stats_var',0.0)
	dragons_stats_dict = DragonTable_stats.DragonStatueStats(relics_dragon_base_stats)
	## Get Dragon passiv Skills
	dragons_skills = DragonTable_stats.getPassivSkillDragon()
	## Get Dragon For Image
	dragon_1 = DragonTable_stats.GetDragon("1")
	dragon_2 = DragonTable_stats.GetDragon("2")
	dragon_3 = DragonTable_stats.GetDragon("3")
	## Get All Stats of Equipped Egg
	activ_egg_stats = EggEquippedTable_stats.GetEggStats(missing_data)
	## Get Reforge Stats
	reforge_atk_power = ReforgeTable_stats.ReforgePowerCourage("power")
	reforge_atk_courage = ReforgeTable_stats.ReforgePowerCourage("courage")
	reforge_hp_saviour = ReforgeTable_stats.ReforgeSaviourRecoLuck("saviour")
	reforge_hp_recovery = ReforgeTable_stats.ReforgeSaviourRecoLuck("recovery")
	reforge_hp_luck = ReforgeTable_stats.ReforgeSaviourRecoLuck("luck")
	## Get Rune Line Stats
	runelinePower = RunesTable_stats.getValueLinePower()
	runelineSaviour = RunesTable_stats.getValueLineSaviour()
	runelineRecovery = RunesTable_stats.getValueLineRecovery()
	runelineCourage = RunesTable_stats.getValueLineCourage()
	runelineLuck = RunesTable_stats.getValueLineLuck()
	## Get Weapon Skin Stats
	weapon_skin_stats = WeaponSkinsTable_stats.getWeaponSkinStats()
	## Get name of skin
	weapon_skin_activ = WeaponSkinsTable_stats.equippedSkin()
	## Get Weapon Coeff Damage Multiplier
	weapon_dmg_multiplier = StuffTable_stats.getWeaponCoeff()
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
	stuff_raw_stats = StuffTable_stats.GetRawStats()

	## Declare cumul variable 
	cumul_talent_flat_passiv_atk = int(talent_stats_dict['talents_power'])
	cumul_talent_flat_passiv_hp = int(talent_stats_dict['talents_strength'])
	cumul_runes_flat_passiv_atk = int(reforge_atk_power) + int(reforge_atk_courage) + int(runelinePower.get('attack_flat',0)) + int(runelineCourage.get('attack_flat',0))
	cumul_runes_flat_passiv_hp = int(reforge_hp_recovery) + int(reforge_hp_saviour) + int(reforge_hp_luck) + int(runelineRecovery.get("hp_flat",0)) + int(runelineSaviour.get("hp_flat",0)) + int(runelineLuck.get("hp_flat",0))
	cumul_hero_flat_passiv_atk = int(hero_Atreus[5]) + int(hero_Urasil[0]) + int(hero_Phoren[6]) + int(hero_Helix[5]) + int(hero_Meowgik[0]) + int(hero_Ayana[6]) + int(hero_Rolla[0]) + int(hero_Bonnie[5]) + int(hero_Shade[6]) + int(hero_Ophelia[0]) + int(hero_Ophelia[2]) + int(hero_Lina[0]) + int(hero_Lina[5]) + int(hero_Aquea[5]) + int(hero_Iris[5]) + int(hero_Melinda[6]) + int(hero_Iris[1]) + int(hero_Blazo[1]) + int(hero_Stella[0])
	cumul_hero_flat_passiv_hp = int(hero_Atreus[0]) + int(hero_Atreus[6]) + int(hero_Urasil[5]) + int(hero_Taranis[5]) + int(hero_Meowgik[6]) + int(hero_Shari[1]) + int(hero_Shari[5]) + int(hero_Onir[0]) + int(hero_Onir[5]) + int(hero_Bonnie[6]) + int(hero_Sylvan[0]) + int(hero_Lina[6]) + int(hero_Aquea[0]) + int(hero_Aquea[6]) + int(hero_Shingen[6]) + int(hero_Iris[0]) + int(hero_Blazo[6]) + int(hero_Elaine[5]) + int(hero_Elaine[6]) + int(hero_Bobo[5]) + int(hero_Bobo[6]) + int(hero_Bobo[0])
	cumul_skin_flat_passiv_atk = int(skin_atk_boost)
	cumul_skin_flat_passiv_hp = int(skin_health_boost)
	cumul_egg_flat_passiv_atk = int(egg_bomb_ghost_passiv[1]) + int(egg_green_bat_passiv[1]) + int(egg_piranha_passiv[1]) + int(egg_crazy_spider_passiv[1]) + int(egg_fire_mage_passiv[1]) + int(egg_skeleton_archer_passiv[1]) + int(egg_skeleton_soldier_passiv[1]) + int(egg_fire_element_passiv[1]) + int(egg_flame_ghost_passiv[1]) + int(egg_ice_mage_passiv[1]) + int(egg_pea_shooter_passiv[1]) + int(egg_shadow_assassin_passiv[1]) + int(egg_skull_wizard_passiv[1]) + int(egg_tornado_demon_passiv[1]) + int(egg_savage_spider_passiv[1]) + int(egg_flaming_bug_passiv[1]) + int(egg_one_eyed_bat_passiv[1]) + int(egg_elite_archer_passiv[1]) + int(egg_icefire_phantom_passiv[1]) + int(egg_purple_phantom_passiv[1]) + int(egg_scarlet_mage_passiv[1]) + int(egg_arch_leader_passiv[0]) + int(egg_crimson_witch_passiv[0]) + int(egg_medusa_boss_passiv[0]) + int(egg_ice_worm_passiv[0]) + int(egg_desert_goliath_passiv[0]) + int(egg_ice_demon_passiv[0]) + int(egg_fire_demon_passiv[1]) + int(egg_crimson_zombie_passiv[1]) + int(egg_scythe_pharoah_passiv[1]) + int(egg_infernal_demon_passiv[0]) + int(egg_fireworm_queen_passiv[0])
	cumul_egg_flat_passiv_hp = int(egg_green_bat_passiv[3]) + int(egg_party_tree_passiv[1]) + int(egg_rock_puppet_passiv[1]) +  int(egg_vase_passiv[1]) + int(egg_zombie_passiv[1]) + int(egg_fire_lizard_passiv[1]) + int(egg_long_dragon_passiv[1]) + int(egg_scarecrow_passiv[1]) + int(egg_skeleton_swordsman_passiv[1]) + int(egg_tornado_mage_passiv[1]) + int(egg_wasp_passiv[1]) + int(egg_cactus_passiv[1]) + int(egg_ice_golem_passiv[1]) + int(egg_scythe_mage_passiv[1]) + int(egg_skull_wizard_passiv[4]) + int(egg_fallen_bat_passiv[1]) + int(egg_nether_puppet_passiv[1]) + int(egg_psionic_scarecrow_passiv[1]) + int(egg_spitting_mushroom_passiv[1]) + int(egg_steel_dryad_passiv[1]) + int(egg_tundra_dragon_passiv[1]) +  int(egg_little_dragon_passiv[1]) + int(egg_rage_golem_passiv[1]) + int(egg_krab_boss_passiv[1]) + int(egg_skeleton_king_passiv[0]) + int(egg_queen_bee_passiv[0]) + int(egg_fire_demon_passiv[0]) + int(egg_plainswolf_passiv[1])
	cumul_altar_flat_passiv_atk = int(altar_stuff_atk) + int(altar_hero_atk)
	cumul_altar_flat_passiv_hp = int(altar_stuff_hp) + int(altar_hero_hp)
	cumul_jewel_flat_activ_atk = int(stats_jewel_dict.get('attack_flat',0)) + int(BonusSpe_jewel_weapon.get('attack_flat',0)) + int(BonusSpe_jewel_bracelet.get('attack_flat',0))
	cumul_jewel_flat_activ_hp = int(stats_jewel_dict.get('hp_flat',0)) + int(BonusSpe_jewel_armor.get('hp_flat',0)) + int(BonusSpe_jewel_bracelet.get('hp_flat',0)) + int(BonusSpe_jewel_locket.get('hp_flat',0))
	cumul_old_flat_passiv_atk = int(cumul_talent_flat_passiv_atk) + int(cumul_runes_flat_passiv_atk) + int(cumul_hero_flat_passiv_atk) + int(cumul_skin_flat_passiv_atk) + int(cumul_egg_flat_passiv_atk)
	cumul_old_flat_passiv_hp = int(cumul_talent_flat_passiv_hp) + int(cumul_runes_flat_passiv_hp) + int(cumul_hero_flat_passiv_hp) + int(cumul_skin_flat_passiv_hp) + int(cumul_egg_flat_passiv_hp)
	cumul_refine_flat_activ_atk =  int(refine_weapon_atk) + int(refine_ring1_atk) + int(refine_ring2_atk) + int(refine_bracelet_atk)
	cumul_refine_flat_activ_hp = int(refine_armor_hp) + int(refine_locket_hp) + int(refine_book_hp)
	cumul_dragon_flat_activ_atk = int(dragons_stats_dict.get("Attack",0))
	cumul_dragon_flat_activ_hp = int(dragons_stats_dict.get("Max Hp",0))
	cumul_stuff_flat_activ_atk = round(stuff_activ_stats['weapon_total'] + stuff_activ_stats['bracelet_total'] + stuff_activ_stats.get("ring_attack_flat",0))
	cumul_stuff_flat_activ_hp = round(stuff_activ_stats['armor_total'] + stuff_activ_stats['locket_total'] + stuff_activ_stats['book_total'])

	cumul_runes_var_passiv_atk = float(runelinePower.get('attack_var',0)) + float(runelineCourage.get('attack_var',0))
	cumul_runes_var_passiv_hp = float(runelineSaviour.get("hp_var",0.0)) + float(runelineLuck.get("hp_var",0.0))
	cumul_heros_var_passiv_atk = float(hero_Taranis[2]) + float(hero_Meowgik[2]) + float(hero_Ayana[2]) + float(hero_Rolla[2]) + float(hero_Sylvan[2]) + float(hero_Aquea[2]) + float(hero_Iris[2]) + float(hero_Bonnie[4]) + float(hero_Shade[7]) + float(hero_Melinda[7]) + float(hero_Bobo[1]) + float(hero_Bobo[4]) + float(hero_Stella[2]) + float(hero_Taiga[6])
	cumul_heros_var_passiv_hp = float(hero_Atreus[2]) + float(hero_Helix[2]) + float(hero_Bonnie[2]) + float(hero_Shade[2]) + float(hero_Lina[2]) + float(hero_Shingen[2]) + float(hero_Blazo[2]) + float(hero_Ryan[4]) + float(hero_Gugu[4]) + float(hero_Blazo[4]) + float(hero_Atreus[7]) + float(hero_Rolla[7])  + float(hero_Elaine[7]) + float(hero_Elaine[2]) + float(hero_Taiga[2])
	cumul_heros_var_activ_atk = float(hero_Onir[3]) + float(hero_Bonnie[3])
	cumul_heros_var_activ_hp = float(hero_Urasil[3]) + float(hero_Sylvan[3]) + float(hero_Ophelia[3]) + float(hero_Ryan[1]) + float(hero_Elaine[1]) 
	cumul_altar_var_passiv_atk = float(altar_heros_ascension_atk) + float(altar_stuff_ascension_atk)
	cumul_altar_var_passiv_hp = float(altar_heros_ascension_hp) + float(altar_stuff_ascension_hp)
	cumul_privileges_var_passiv_atk = float(brave_privileges_stats['Attack Var'])
	cumul_privileges_var_passiv_hp = float(brave_privileges_stats['Hp Var'])
	cumul_jewel_var_activ_atk =  (float(BonusSpe_jewel_weapon.get('attack_var',0)) + float(BonusSpe_jewel_ring1.get('attack_var',0)) + float(BonusSpe_jewel_book.get('attack_var',0)))/100
	cumul_jewel_var_activ_hp = (float(BonusSpe_jewel_book.get('hp_var',0)) + float(BonusSpe_jewel_ring2.get('hp_var',0)))/100
	cumul_stuff_var_activ_atk = (stuff_activ_stats['weapon_attack_var'] + stuff_activ_stats['bracelet_attack_var'] + stuff_activ_stats['ring1_atk_var'] + stuff_activ_stats['ring2_atk_var'])
	cumul_stuff_var_activ_hp = (stuff_activ_stats['armor_hp_var'] + stuff_activ_stats['book_hp_var'] + stuff_activ_stats['ring1_hp_var'] + stuff_activ_stats['ring2_hp_var'] + stuff_activ_stats['locket_hp_var'])

	cumul_heros_var_passiv_crit_dmg = float(hero_Urasil[2]) + float(hero_Taranis[3]) + float(hero_Helix[0]) + float(hero_Ayana[5]) + float(hero_Rolla[6]) + float(hero_Bonnie[0]) + float(hero_Shade[4])
	cumul_heros_var_passiv_crit_rate = float(hero_Elaine[3]) + float(hero_Melinda[3]) + float(hero_Shade[1]) + float(hero_Shade[5]) + float(hero_Shari[2]) + float(hero_Helix[3]) + float(hero_Taranis[0]) + float(hero_Phoren[0]) + float(hero_Phoren[2]) + float(hero_Phoren[3]) + float(hero_Urasil[6]) + float(hero_Stella[1])

	cumul_var_atk = (float(cumul_runes_var_passiv_atk) + float(cumul_heros_var_passiv_atk) + float(cumul_heros_var_activ_atk) + float(cumul_altar_var_passiv_atk) + float(cumul_privileges_var_passiv_atk) + float(medal_stats['attack_var']) + float(relics_stats.get('attack_var',0.0)))/100
	cumul_var_hp = (float(cumul_runes_var_passiv_hp) + float(cumul_heros_var_passiv_hp) + float(cumul_heros_var_activ_hp) + float(cumul_altar_var_passiv_hp) + float(cumul_privileges_var_passiv_hp) + float(medal_stats['hp_var']) + float(relics_stats.get('hp_var',0.0)))/100
	hero_modified_base_atk = (int(atk_base_hero_choosen) - int(runelineCourage.get('courage_hero_attack_flat',0))) * (float(runelineCourage.get('courage_hero_attack_var',0.0)/100) + float(cumul_var_passiv_power_up_hero) + 1) + int(runelineCourage.get('courage_hero_attack_flat',0))
	hero_modified_base_hp = (int(health_base_hero_choosen) - int(runelineCourage.get('courage_hero_hp_flat',0))) * (float(runelineCourage.get('courage_hero_hp_var',0.0)/100) + float(cumul_var_passiv_power_up_hero) + 1) + int(runelineCourage.get('courage_hero_hp_flat',0))
	############################################# RESULT #############################################
	global_critic_damage = 200 + float(dragons_skills.get("Crit Damage",0.0)) + float(runelinePower.get('var_crit_dmg',0.0)) + float(stats_jewel_dict.get('crit_damage',0.0)) + float(stuff_raw_stats['weapon_critdmg_raw']) + float(stuff_raw_stats['ring1_crit_damage_raw']) + float(stuff_raw_stats['ring2_crit_damage_raw']) + float(stuff_raw_stats['bracelet_crit_raw']) + float(activ_egg_stats['Critic Damage']) + float(cumul_heros_var_passiv_crit_dmg) + float(BonusSpe_jewel_weapon.get('crit_damage',0)) + float(hero_Taiga[4])
	global_elemental_damage_flat = 0
	global_elemental_damage_var = float(runelinePower.get('var_elemental_dmg',0.0)) + float(relics_stats.get('elemental_damage_var',0.0)) + float(brave_privileges_stats['Elemental Damage']) + float(stats_jewel_dict.get('elemental_damage_var',0.0)) + float(hero_Sylvan[7])
	global_dodge_chance = 1 - (1-(float(dragons_skills.get("Dodge rate",0.0)))*1-(float(runelineSaviour.get('dodge',0.0)))*1-(float(relics_stats.get('dodge_var',0.0)))*1-(float(BonusSpe_jewel_ring1.get('dodge_var',0.0)))*1-(float(dragons_stats_dict.get("Dodge",0.0)))*1-(float(stuff_raw_stats['armor_dodge_raw']))*1-(float(stuff_raw_stats['locket_dodge_raw']))*1-(float(stuff_raw_stats['ring1_dodge_raw']))*1-(float(stuff_raw_stats['ring2_dodge_raw']))*1-(float(hero_Meowgik[4]))*1-(float(hero_Meowgik[7]))*1-(float(hero_Meowgik[1]))*1-(float(hero_Ayana[3]))*1-(float(hero_Rolla[3]))*1-(float(hero_Lina[1]))*1-(float(hero_Gugu[1]))*1-(float(hero_Iris[3]))*1-(float(hero_Taiga[5]))*1-(float(hero_Taiga[1])))
	global_crit_rate = float(15) + float(runelinePower.get('var_crit_rate',0.0)) + float(BonusSpe_jewel_weapon.get('crit_chance',0)) + float(relics_stats.get('crit_chance',0.0)) + float(brave_privileges_stats['Critic Rate']) + float(stuff_raw_stats['ring1_crit_chance_raw']) + float(stuff_raw_stats['ring2_crit_chance_raw']) + float(cumul_heros_var_passiv_crit_rate) + float(stuff_raw_stats['weapon_critrate_raw'])
	global_boss_damage_flat = int(runelinePower.get('flat_dmg_boss',0)) + int(relics_stats.get('damage_bosses_flat',0)) + int(activ_egg_stats['Damage To Bosses']) + int(stuff_activ_stats.get('boss units dmg',0)) + int(stuff_activ_stats.get('boss units dmg',0)) + int(stats_jewel_dict.get('damage_bosses_flat',0))
	global_boss_damage_var = float(stats_jewel_dict.get('damage_bosses_var',0.0)) + float(stuff_activ_stats.get('boss units dmg var',0.0)) + float(runelinePower.get('var_dmg_boss',0.0)) + float(relics_stats.get('damage_bosses_var',0.0))
	global_mobs_damage_flat = int(runelinePower.get('flat_dmg_mob',0)) + int(relics_stats.get('damage_mobs_flat',0)) + int(dragons_stats_dict.get("Damage To Mobs",0)) + int(activ_egg_stats['Damage To Mobs']) + int(stuff_activ_stats.get('mobs units dmg',0)) + int(stuff_activ_stats.get('mobs units dmg',0)) + int(stats_jewel_dict.get('damage_mobs_flat',0)) + int(hero_Bobo[0])
	global_mobs_damage_var = float(stats_jewel_dict.get('damage_mobs_var',0.0)) + float(stuff_activ_stats.get('mobs units dmg var',0.0)) + float(runelinePower.get('var_dmg_mob',0.0)) + float(relics_stats.get('damage_mobs_var',0.0))
	global_ranged_damage_flat = int(runelinePower.get('flat_dmg_ranged',0)) + int(relics_stats.get('damage_ranged_flat',0)) + int(dragons_stats_dict.get("Damage To Ranged Units",0)) + int(stuff_activ_stats.get('ranged units dmg',0)) + int(stuff_activ_stats.get('ranged units dmg',0)) + int(activ_egg_stats['Damage To Ranged Units']) + int(hero_Ryan[0]) + int(hero_Melinda[0]) + int(hero_Sylvan[5]) + int(hero_Ryan[5]) + int(hero_Melinda[5]) + int(hero_Helix[6]) + int(hero_Gugu[6])
	global_ranged_damage_var = float(stuff_activ_stats.get('ranged units dmg var',0.0)) + float(runelinePower.get('var_dmg_ranged',0.0)) + float(relics_stats.get('damage_ranged_var',0.0)) + float(hero_Bobo[2]) + float(hero_Gugu[2]) + float(hero_Ayana[4]) + float(hero_Melinda[4]) + float(hero_Sylvan[4]) + float(hero_Phoren[4]) + float(hero_Atreus[1]) + float(hero_Ayana[1]) + float(hero_Sylvan[1])
	global_ground_damage_flat = int(runelinePower.get('flat_dmg_ground',0)) + int(relics_stats.get('damage_ground_flat',0)) + int(dragons_stats_dict.get("Damage To Ground Units",0)) + int(stuff_activ_stats.get('ground units dmg',0)) + int(stuff_activ_stats.get('ground units dmg',0)) + int(activ_egg_stats['Damage To Ground Units']) + int(hero_Shade[0]) + int(hero_Ophelia[5]) + int(hero_Blazo[5]) + int(hero_Sylvan[6])
	global_ground_damage_var = float(stuff_activ_stats.get('ground units dmg var',0.0)) + float(runelinePower.get('var_dmg_ground',0.0)) + float(relics_stats.get('damage_ground_var',0.0)) + float(hero_Onir[4]) + float(hero_Shingen[4]) + float(hero_Phoren[7]) + float(hero_Onir[1]) + float(hero_Blazo[3])
	global_airborne_damage_flat = int(runelinePower.get('flat_dmg_airborne',0)) + int(relics_stats.get('damage_airborne_flat',0)) + int(stuff_activ_stats.get('airborne units dmg',0)) + int(stuff_activ_stats.get('airborne units dmg',0)) + int(activ_egg_stats['Damage To Airborne Units']) + int(hero_Ayana[0]) + int(hero_Gugu[0]) + int(hero_Ryan[2]) + int(hero_Phoren[5]) + int(hero_Gugu[5]) + int(hero_Taranis[6]) + int(hero_Ryan[6]) + int(hero_Iris[6]) + int(hero_Elaine[0])
	global_airborne_damage_var = float(stuff_activ_stats.get('airborne units dmg var',0.0)) + float(runelinePower.get('var_dmg_airborne',0.0)) + float(relics_stats.get('damage_airborne_var',0.0)) + float(hero_Taranis[4]) + float(hero_Iris[4]) + float(hero_Taranis[1])
	global_melee_damage_flat = int(runelinePower.get('flat_dmg_melee',0)) + int(relics_stats.get('damage_melee_flat',0)) + int(dragons_stats_dict.get("Damage To Melee Units",0)) + int(stuff_activ_stats.get('melee units dmg',0)) + int(stuff_activ_stats.get('melee units dmg',0)) + int(activ_egg_stats['Damage To Melee Units']) + int(hero_Shari[0]) + int(hero_Shingen[0]) + int(hero_Blazo[0]) + int(hero_Rolla[5]) + int(hero_Shingen[5]) + int(hero_Shari[6])
	global_melee_damage_var = float(stuff_activ_stats.get('melee units dmg var',0.0)) + float(dragons_skills.get("Damage VS melee units",0.0)) + float(runelinePower.get('var_dmg_melee',0.0)) + float(relics_stats.get('damage_melee_var',0.0)) + float(hero_Shari[3]) + float(hero_Melinda[2]) + float(hero_Urasil[4]) + float(hero_Ophelia[4]) + float(hero_Lina[4]) + float(hero_Urasil[1]) + float(hero_Ophelia[1]) + float(hero_Shingen[3]) + float(hero_Elaine[4])
	global_normal_damage_flat = int(stuff_activ_stats.get("non-elite mobs dmg",0))
	global_normal_damage_var = float(stuff_activ_stats.get("non-elite mobs dmg var",0))
	global_elite_damage_flat = int(stuff_activ_stats.get("elite mobs dmg",0)) + int(stats_jewel_dict.get('damage_elite_flat',0))
	global_elite_damage_var = float(stats_jewel_dict.get('damage_elite_var',0.0)) + float(relics_stats.get("damage_elite_var",0.0)) + float(stuff_activ_stats.get("elite mobs dmg var",0)) + float(altar_heros_ascension_dmg_elite) ### RELICS damage_elite_var doesn't work because field isn't added in db and won't be added
	global_all_damage_flat = 0
	global_all_damage_var = float(runelinePower.get('var_all_dmg',0.0))
	weapon_ranged_damage = float(stats_jewel_dict.get('damage_weapon_ranged_var',0.0)) + float(relics_stats.get("damage_weapon_ranged_var",0.0)) + float(hero_Iris[7])
	weapon_melee_damage = float(dragons_stats_dict.get("Weapon Melee Damage",0)) + float(relics_stats.get("damage_weapon_melee_var",0.0)) + float(hero_Shingen[7])
	weapon_damage = float(hero_Stella[7]) + float(stuff_raw_stats['weapon_damage_stats'])

	global_stats_atk_flat = hero_modified_base_atk + int(cumul_old_flat_passiv_atk) + int(cumul_stuff_flat_activ_atk) + int(activ_egg_stats["Attack"]) + int(cumul_altar_flat_passiv_atk) + int(cumul_dragon_flat_activ_atk) + int(brave_privileges_stats['Attack Flat']) + int(medal_stats['attack']) + int(relics_stats.get('attack_flat',0))
	global_stats_hp_flat = hero_modified_base_hp + int(cumul_old_flat_passiv_hp) + int(cumul_stuff_flat_activ_hp) + int(activ_egg_stats["Max Hp"]) + int(cumul_altar_flat_passiv_hp) + int(cumul_dragon_flat_activ_hp) + int(brave_privileges_stats['Hp Flat']) + int(medal_stats['hp']) + int(relics_stats.get('hp_flat',0))
	global_stats_atk = global_stats_atk_flat + (global_stats_atk_flat*float(cumul_var_atk)) + (global_stats_atk_flat*float(cumul_stuff_var_activ_atk)) + (global_stats_atk_flat*float(cumul_jewel_var_activ_atk)) + cumul_jewel_flat_activ_atk + cumul_refine_flat_activ_atk
	global_stats_hp = global_stats_hp_flat + (global_stats_hp_flat*float(cumul_var_hp)) + (global_stats_hp_flat*float(cumul_stuff_var_activ_hp)) + (global_stats_hp_flat*float(cumul_jewel_var_activ_hp)) + cumul_jewel_flat_activ_hp + cumul_refine_flat_activ_hp
	###################### CREATION IMAGE STUFF#############################################################
	create_image(pbid,str(StuffTable_stats.dictionnaire()['weapon_choosen'].lower().replace(" ","_")),
		str(StuffTable_stats.dictionnaire()['weapon_rarity'].lower().replace(" ","_")),int(StuffTable_stats.dictionnaire()['weapon_level']),
		str(StuffTable_stats.dictionnaire()['armor_choosen'].lower().replace(" ","_")),str(StuffTable_stats.dictionnaire()['armor_rarity'].lower().replace(" ","_")),int(StuffTable_stats.dictionnaire()['armor_level']),str(StuffTable_stats.dictionnaire()['ring1_choosen'].lower().replace(" ","_")),
		str(StuffTable_stats.dictionnaire()['ring1_rarity'].lower().replace(" ","_")),int(StuffTable_stats.dictionnaire()['ring1_level']),
		str(StuffTable_stats.dictionnaire()['ring2_choosen'].lower().replace(" ","_")),str(StuffTable_stats.dictionnaire()['ring2_rarity'].lower().replace(" ","_")),int(StuffTable_stats.dictionnaire()['ring2_level']),str(StuffTable_stats.dictionnaire()['pet1_choosen'].lower().replace(" ","_")),
		str(StuffTable_stats.dictionnaire()['pet1_rarity'].lower().replace(" ","_")),int(StuffTable_stats.dictionnaire()['pet1_level']),
		str(StuffTable_stats.dictionnaire()['pet2_choosen'].lower().replace(" ","_")),str(StuffTable_stats.dictionnaire()['pet2_rarity'].lower().replace(" ","_")),int(StuffTable_stats.dictionnaire()['pet2_level']),
		str(StuffTable_stats.dictionnaire()['bracelet_choosen'].lower().replace(" ","_")),str(StuffTable_stats.dictionnaire()['bracelet_rarity'].lower().replace(" ","_")),int(StuffTable_stats.dictionnaire()['bracelet_level']),
		str(StuffTable_stats.dictionnaire()['locket_choosen'].lower().replace(" ","_")),str(StuffTable_stats.dictionnaire()['locket_rarity'].lower().replace(" ","_")),int(StuffTable_stats.dictionnaire()['locket_level']),
		str(StuffTable_stats.dictionnaire()['book_choosen'].lower().replace(" ","_")),str(StuffTable_stats.dictionnaire()['book_rarity'].lower().replace(" ","_")),int(StuffTable_stats.dictionnaire()['book_level']),
		int(round(global_stats_atk)),int(round(global_stats_hp)),int(all_jewel_lvl_dict['jewel_lvl_weapon']),int(all_jewel_lvl_dict['jewel_lvl_armor']),int(all_jewel_lvl_dict['jewel_lvl_ring1']),int(all_jewel_lvl_dict['jewel_lvl_ring2']),int(all_jewel_lvl_dict['jewel_lvl_pet1']),
		int(all_jewel_lvl_dict['jewel_lvl_pet2']),int(all_jewel_lvl_dict['jewel_lvl_bracelet']),int(all_jewel_lvl_dict['jewel_lvl_locket']),int(all_jewel_lvl_dict['jewel_lvl_book']),str(user_stats.choosen_hero),str(dragon_1['dragon_type']),str(dragon_2['dragon_type']),
		str(dragon_3['dragon_type']),str(dragon_1['dragon_rarity']),str(dragon_2['dragon_rarity']),str(dragon_3['dragon_rarity']),weapon_skin_activ)

	user_stats.global_atk_save = int(global_stats_atk)
	user_stats.global_hp_save = int(global_stats_hp)
	user_stats.save()
	try:
		calc_user_dmg = DamageCalcTable.objects.get(user_profile=user_stats)
	except DamageCalcTable.DoesNotExist:
		calc_user_dmg = DamageCalcTable()
		calc_user_dmg.user_profile = user_stats
	finally:
		calc_user_dmg.weapon_coeff = weapon_dmg_multiplier
		calc_user_dmg.flat_dmg_vs_ground = round(global_ground_damage_flat,2)
		calc_user_dmg.flat_dmg_vs_airborne = round(global_airborne_damage_flat,2)
		calc_user_dmg.flat_dmg_vs_melee = round(global_melee_damage_flat,2)
		calc_user_dmg.flat_dmg_vs_range = round(global_ranged_damage_flat,2)
		calc_user_dmg.flat_dmg_vs_mobs = round(global_mobs_damage_flat,2)
		calc_user_dmg.flat_dmg_vs_boss = round(global_boss_damage_flat,2)
		calc_user_dmg.flat_dmg_element = round(global_elemental_damage_flat,2)
		calc_user_dmg.flat_dmg_all = round(global_all_damage_flat,2)
		calc_user_dmg.flat_elite_dmg = round(global_elite_damage_flat,2)
		calc_user_dmg.flat_normal_dmg = round(global_normal_damage_flat,2)
		calc_user_dmg.var_dmg_vs_ground = round(global_ground_damage_var,2)
		calc_user_dmg.var_dmg_vs_airborne = round(global_airborne_damage_var,2)
		calc_user_dmg.var_dmg_vs_melee = round(global_melee_damage_var,2)
		calc_user_dmg.var_dmg_vs_range = round(global_ranged_damage_var,2)
		calc_user_dmg.var_dmg_vs_mobs = round(global_mobs_damage_var,2)
		calc_user_dmg.var_dmg_vs_boss = round(global_boss_damage_var,2)
		calc_user_dmg.var_dmg_element = round(global_elemental_damage_var,2)
		calc_user_dmg.var_dmg_all = round(global_all_damage_var,2)
		calc_user_dmg.var_normal_dmg = round(global_normal_damage_var,2)
		calc_user_dmg.var_elite_dmg = round(global_elite_damage_var,2)
		calc_user_dmg.crit_dmg = round(global_critic_damage,2)
		calc_user_dmg.crit_rate = round(global_crit_rate,2)
		calc_user_dmg.dodge_rate = round(global_dodge_chance,2)
		calc_user_dmg.weapon_damage = weapon_damage
		calc_user_dmg.weapon_melee_damage = weapon_melee_damage
		calc_user_dmg.weapon_ranged_damage = weapon_ranged_damage
		calc_user_dmg.hero_atk = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

		if missing_data != []:
			calc_user_dmg.missing_data = missing_data[0]
		else:
			calc_user_dmg.missing_data = "none"
		calc_user_dmg.save()
	dict_Link = {
		0:f"/calculator/show/{user_stats.public_id}/",
		1:f"/calculator/index/", # pour ne pas faire de boucle infini de redirection (utilisé dans affiche_calc)
		2:f"/wiki/damage-calculator/",
	}
	messages.success(request=request,message=_(f"{ingame_name.capitalize()} updated with success"))
	if request.GET.get("log") != "False":
		send_embed("New Entry",f"{user_stats.ingame_name} | {user_stats.ingame_id}","","",f"[Admin Panel Link User]({c_hostname}/luhcaran/calculator/user/{user_stats.id}/change/)\n[Profile]({c_hostname}/calculator/show/{user_stats.public_id}/) Stats : {user_stats.global_atk_save} | {user_stats.global_hp_save}","A200FF", request,False)
	return HttpResponseRedirect(f'/{get_language()}{dict_Link.get(redirectPath,"/calculator/index/")}')

@loadContent(checkMessages=True)
def affiche_calc(request, pbid:int):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	user_credential = getCredentialForNonLoginRequired(request).get('user_credential')
	makeLog(request)
	try:
		user_stats = user.objects.get(public_id=int(pbid))
		DamageCalcTable_stats = DamageCalcTable.objects.get(user_profile=user_stats)
	except DamageCalcTable.DoesNotExist:
		return HttpResponseRedirect(f"/{get_language()}/stats/calc/{int(pbid)}/1/?log=False")
	except user.DoesNotExist:
		request.session['error_message'] = "User doesn't exist"
		return HttpResponseRedirect(f'/{get_language()}')
	if not os.path.exists(f"calculator/static/image/stuff_save/{int(pbid)}.png"):
		return HttpResponseRedirect(f"/stats/calc/{int(pbid)}/0/?log=False")
	valueError = "no"
	if DamageCalcTable_stats.missing_data != "" and DamageCalcTable_stats.missing_data != "none":
		valueError = "yes"
	ctx = {
		"pbid":pbid,
		"name":user_stats.ingame_name,
		"stats":user_stats,
		"global_stats_atk":user_stats.global_atk_save,
		"global_stats_hp":user_stats.global_hp_save,
		'global_critic_damage': DamageCalcTable_stats.crit_dmg,
		'global_crit_rate': DamageCalcTable_stats.crit_rate,
		'global_dodge_chance': DamageCalcTable_stats.dodge_rate,
		'global_boss_damage': DamageCalcTable_stats.flat_dmg_vs_boss,
		'global_boss_damage_var': DamageCalcTable_stats.var_dmg_vs_boss,
		'global_mobs_damage': DamageCalcTable_stats.flat_dmg_vs_mobs,
		'global_mobs_damage_var': DamageCalcTable_stats.var_dmg_vs_mobs,
		'global_ranged_damage': DamageCalcTable_stats.flat_dmg_vs_range,
		'global_ranged_damage_var': DamageCalcTable_stats.var_dmg_vs_range,
		'global_ground_damage': DamageCalcTable_stats.flat_dmg_vs_ground,
		'global_ground_damage_var': DamageCalcTable_stats.var_dmg_vs_ground,
		'global_airborne_damage': DamageCalcTable_stats.flat_dmg_vs_airborne,
		'global_airborne_damage_var': DamageCalcTable_stats.var_dmg_vs_airborne,
		'global_melee_damage': DamageCalcTable_stats.flat_dmg_vs_melee,
		'global_melee_damage_var': DamageCalcTable_stats.var_dmg_vs_melee,
		'global_elemental_damage': DamageCalcTable_stats.var_dmg_element,
		"global_elite_damage_flat": DamageCalcTable_stats.flat_elite_dmg,
		"global_normal_damage_flat": DamageCalcTable_stats.flat_normal_dmg,
		"global_normal_damage_var": DamageCalcTable_stats.var_normal_dmg,
		"global_elite_damage_var": DamageCalcTable_stats.var_elite_dmg,
		"weapon_damage": DamageCalcTable_stats.weapon_damage,
		"weapon_melee_damage": DamageCalcTable_stats.weapon_melee_damage,
		"weapon_ranged_damage": DamageCalcTable_stats.weapon_ranged_damage,
		"darkmode": checkDarkMode(request),
		"header_msg":_("Stats Calculator"),
		"ValueError": valueError,
		"missing_data": DamageCalcTable_stats.missing_data,
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(user_credential),
		'DEV_MODE':DEV_MODE
	}
	if checkContributor(user_credential,request):
		ctx['DEV_MODE'] = True
	return render(request,'calculator/affiche.html',ctx)

@loadContent(db_maintenance=True,checkMessages=True)
def index_calc(request):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	ingame_name_cookie,ingame_id_cookie,user_credential = getCredentialForNonLoginRequired(request).values()
	makeLog(request)
	profile = getProfileWithCookie(ingame_id_cookie,ingame_name_cookie)

	notuserlist = ['0-000001','0-000002','0-000003','0-000004']
	notuserlist.extend(user.objects.filter(global_atk_save__lt=2800).values_list('ingame_id', flat=True))
	user_liste = user.objects.filter(public_profile=True).exclude(ingame_id__in=notuserlist).order_by('-global_atk_save')[:100]
	
	show_table = "no_profile"
	self_ingame_hero = "unknown"
	user_stats = profile[1] if profile else None
	self_ingame_name = user_stats.ingame_name if user_stats else ""
	self_public_id = user_stats.public_id if user_stats else ""
	self_global_atk_save = user_stats.global_atk_save if user_stats else ""
	self_global_hp_save = user_stats.global_hp_save if user_stats else ""
	rank = "?"
	avatar_src = "/static/image/hero_icon/icon_unknown.png"
	if (ingame_id_cookie == "9-999999" and ingame_name_cookie == "unknown") or (profile and not profile[0] and user_stats):
		show_table = "visitor"
		messages.error(request, _(f'You attempted to access {self_ingame_name}<br>But your login username is "{ingame_name_cookie}".'))
	elif profile and user_stats:
		self_ingame_name = user_stats.ingame_name
		self_ingame_hero = user_stats.choosen_hero
		if os.path.exists(f"calculator/static/image/hero_icon/icon_{self_ingame_hero}.png"):
			avatar_src = f"/static/image/hero_icon/icon_{self_ingame_hero}.png"
		self_public_id = user_stats.public_id
		self_global_atk_save = user_stats.global_atk_save
		self_global_hp_save = user_stats.global_hp_save
		show_table = "yes"
		try:
			rank = list(user_liste).index(user_stats)
		except ValueError:
			rank = "?"
	number_user = user.objects.count()
	return render(request,"calculator/index.html",{
		"listALL": user_liste,
		"self_ingame_name":self_ingame_name,
		"self_global_atk_save":self_global_atk_save,
		"self_global_hp_save":self_global_hp_save,
		"self_public_id":self_public_id,
		"self_ingame_hero": avatar_src,
		"show_table": show_table,
		"rank": rank,
		"darkmode": checkDarkMode(request),
		"header_msg":_("Stats Calculator"),
		"number_user":number_user,
		"ingame_name_cookie":ingame_name_cookie,
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(user_credential)
	})

@loadContent(db_maintenance=True, login_required=True)
def formulaire_calc(request):
	try:
		user.objects.get(pk=user_init_primary_key)
	except user.DoesNotExist:
		new_tempUser = user()
		new_tempUser.pk = user_init_primary_key
		new_tempUser.ingame_id = 0-000000
		new_tempUser.ingame_name = "user_init"
		new_tempUser.global_atk_save = 0
		new_tempUser.global_hp_save = 0
		new_tempUser.choosen_hero = "Atreus"
		new_tempUser.brave_privileges_level = 1
		new_tempUser.atk_base_stats_hero_choosen = 100
		new_tempUser.health_base_stats_hero_choosen = 400
		new_tempUser.public_id = 1678471785674909
		new_tempUser.public_profile = False
		new_tempUser.save()
	SidebarContent = LocalDataContentWiki['SidebarContent']
	user_credential = request.session['user_credential']
	makeLog(request)
	cookie_request_name,cookie_request_id = list(user_credential.items())[0]
	profile = getProfileWithCookie(cookie_request_id,cookie_request_name)
	if request.method == "POST" or profile[0]:
		request.session['info_message'] = f"{profile[1].ingame_name}'s Profile already exists"
		return HttpResponseRedirect(f"/{get_language()}/calculator/index/", {"darkmode": checkDarkMode(request),"header_msg":_("Stats Calculator"),"sidebarContent":SidebarContent})
	elif profile[0] == False and profile[1] != None:
		request.session['error_message'] = f'You can\'t create a new profile, this id is already used by {profile[1].ingame_name}.'
		return HttpResponseRedirect(f"/{get_language()}/calculator/index/", {"darkmode": checkDarkMode(request),"header_msg":_("Stats Calculator"),"sidebarContent":SidebarContent})
	else :
		form_User = UserForm()
		form_StuffTable = StuffForm()
		form_HeroTable = HeroForm()
		form_TalentTable = TalentForm()
		form_SkinTable = SkinForm()
		form_AltarTable = AltarForm()
		form_JewelTypeTable = JewelTypeForm()
		form_JewelLevelTable = JewelLevelForm()
		form_EggTable = EggForm()
		form_EggEquippedTable = EggEquippedForm()
		form_DragonTable = DragonForm()
		form_RunesTable = RunesForm()
		form_ReforgeTable = ReforgeForm()
		form_RefineTable = RefineForm()
		form_MedalTable = MedalsForm()
		form_RelicsTable = RelicsForm()
		form_WeaponSkinTable = WeaponSkinForm()
		user_init = user.objects.get(id=user_init_primary_key)
		ctx = {
			'form_User': form_User,
			'form_StuffTable': form_StuffTable,
			'form_HeroTable': form_HeroTable,
			'form_TalentTable': form_TalentTable,
			'form_SkinTable': form_SkinTable,
			'form_AltarTable': form_AltarTable,
			'form_JewelTypeTable': form_JewelTypeTable,
			'form_JewelLevelTable': form_JewelLevelTable,
			'form_EggTable': form_EggTable,
			'form_EggEquippedTable': form_EggEquippedTable,
			'form_DragonTable': form_DragonTable,
			'form_RunesTable': form_RunesTable,
			'form_ReforgeTable': form_ReforgeTable,
			'form_RefineTable': form_RefineTable,
			'form_MedalTable': form_MedalTable,
			'form_RelicsTable': form_RelicsTable,
			'form_WeaponSkinTable': form_WeaponSkinTable,
			'public_id': create_unique_id(),
			'cookie_request_id': cookie_request_id,
			'cookie_request_name': cookie_request_name,
			"darkmode": checkDarkMode(request),
			"header_msg":_("Create Profile"),
			"pk_id":user_init.pk,
			"sidebarContent":SidebarContent,
			"cookieUsername":makeCookieheader(user_credential)
		}
	return render(request,"calculator/formulaire.html",ctx)

@loadContent(db_maintenance=True, login_required=True)
def traitement_calc(request):
	if request.method == "POST":
		SidebarContent = LocalDataContentWiki['SidebarContent']
		user_credential = request.session['user_credential']
		makeLog(request)
		cookie_request_name,cookie_request_id = list(user_credential.items())[0]
		profile = getProfileWithCookie(cookie_request_id,cookie_request_name)
		if profile[0]:
			request.session['info_message'] = f"{profile[1].ingame_name}'s Profile already exists"
			return HttpResponseRedirect(f"/{get_language()}/calculator/index/", {"darkmode": checkDarkMode(request),"header_msg":_("Stats Calculator"),"sidebarContent":SidebarContent})
		elif profile[0] == False and profile[1] != None:
			request.session['error_message'] = f'You attempted to access {profile[1].ingame_name}<br>But your login username is "{cookie_request_name}".'
			return HttpResponseRedirect(f"/{get_language()}/calculator/index/", {"darkmode": checkDarkMode(request),"header_msg":_("Stats Calculator"),"sidebarContent":SidebarContent})
		form_User = UserForm(request.POST)
		form_StuffTable = StuffForm(request.POST)
		form_HeroTable = HeroForm(request.POST)
		form_TalentTable = TalentForm(request.POST)
		form_SkinTable = SkinForm(request.POST)
		form_AltarTable = AltarForm(request.POST)
		form_JewelTypeTable = JewelTypeForm(request.POST)
		form_JewelLevelTable = JewelLevelForm(request.POST)
		form_EggTable = EggForm(request.POST)
		form_EggEquippedTable = EggEquippedForm(request.POST)
		form_DragonTable = DragonForm(request.POST)
		form_RunesTable = RunesForm(request.POST)
		form_ReforgeTable = ReforgeForm(request.POST)
		form_RefineTable = RefineForm(request.POST)
		form_MedalTable = MedalsForm(request.POST)
		form_RelicsTable = RelicsForm(request.POST)
		form_WeaponSkinTable = WeaponSkinForm(request.POST)
		form_validation = all_formIsValid(form_User.is_valid(),form_StuffTable.is_valid(),form_HeroTable.is_valid(),form_TalentTable.is_valid(),form_SkinTable.is_valid(),form_AltarTable.is_valid(),form_JewelTypeTable.is_valid(),form_JewelLevelTable.is_valid(),form_EggTable.is_valid(),form_EggEquippedTable.is_valid(),form_DragonTable.is_valid(),form_RunesTable.is_valid(),form_ReforgeTable.is_valid(),form_RefineTable.is_valid(), form_MedalTable.is_valid(), form_RelicsTable.is_valid(), form_WeaponSkinTable.is_valid())
		if form_validation:
			stats_User = form_User.save()
			stats_User.save()
			stats_StuffTable = form_StuffTable.save(commit=False)
			stats_HeroTable = form_HeroTable.save(commit=False)
			stats_TalentTable = form_TalentTable.save(commit=False)
			stats_SkinTable = form_SkinTable.save(commit=False)
			stats_AltarTable = form_AltarTable.save(commit=False)
			stats_JewelTypeTable = form_JewelTypeTable.save(commit=False)
			stats_JewelLevelTable = form_JewelLevelTable.save(commit=False)
			stats_EggTable = form_EggTable.save(commit=False)
			stats_EggEquippedTable = form_EggEquippedTable.save(commit=False)
			stats_DragonTable = form_DragonTable.save(commit=False)
			stats_RunesTable = form_RunesTable.save(commit=False)
			stats_ReforgeTable = form_ReforgeTable.save(commit=False)
			stats_RefineTable = form_RefineTable.save(commit=False)
			stats_MedalsTable = form_MedalTable.save(commit=False)
			stats_RelicsTable = form_RelicsTable.save(commit=False)
			stats_WeaponSkinTable = form_WeaponSkinTable.save(commit=False)
			stats_StuffTable.user_profile = stats_User
			stats_HeroTable.user_profile = stats_User
			stats_TalentTable.user_profile = stats_User
			stats_SkinTable.user_profile = stats_User
			stats_AltarTable.user_profile = stats_User
			stats_JewelTypeTable.user_profile = stats_User
			stats_JewelLevelTable.user_profile = stats_User
			stats_EggTable.user_profile = stats_User
			stats_EggEquippedTable.user_profile = stats_User
			stats_DragonTable.user_profile = stats_User
			stats_RunesTable.user_profile = stats_User
			stats_ReforgeTable.user_profile = stats_User
			stats_RefineTable.user_profile = stats_User
			stats_MedalsTable.user_profile = stats_User
			stats_RelicsTable.user_profile = stats_User
			stats_WeaponSkinTable.user_profile = stats_User
			stats_StuffTable.save()
			stats_HeroTable.save()
			stats_TalentTable.save()
			stats_SkinTable.save()
			stats_AltarTable.save()
			stats_JewelTypeTable.save()
			stats_JewelLevelTable.save()
			stats_EggTable.save()
			stats_EggEquippedTable.save()
			stats_DragonTable.save()
			stats_RunesTable.save()
			stats_ReforgeTable.save()
			stats_RefineTable.save()
			stats_MedalsTable.save()
			stats_RelicsTable.save()
			stats_WeaponSkinTable.save()
			pbid_for_url = stats_User.public_id
			return HttpResponseRedirect(f"/stats/calc/{pbid_for_url}/0/")
		else:
			form_User = UserForm(request.POST)
			form_StuffTable = StuffForm(request.POST)
			form_HeroTable = HeroForm(request.POST)
			form_TalentTable = TalentForm(request.POST)
			form_SkinTable = SkinForm(request.POST)
			form_AltarTable = AltarForm(request.POST)
			form_JewelTypeTable = JewelTypeForm(request.POST)
			form_JewelLevelTable = JewelLevelForm(request.POST)
			form_EggTable = EggForm(request.POST)
			form_EggEquippedTable = EggEquippedForm(request.POST)
			form_DragonTable = DragonForm(request.POST)
			form_RunesTable = RunesForm(request.POST)
			form_ReforgeTable = ReforgeForm(request.POST)
			form_RefineTable = RefineForm(request.POST)
			form_MedalTable = MedalsForm(request.POST)
			form_RelicsTable = RelicsForm(request.POST)
			form_WeaponSkinTable = WeaponSkinForm(request.POST)
			pbid = create_unique_id()
			ingame_id = form_User['ingame_id'].data
			ingame_name = form_User['ingame_name'].data
			pk_id = form_StuffTable['user_profile'].data
			form_error = findFormError(form_User, form_StuffTable, form_HeroTable, form_TalentTable, form_SkinTable, form_AltarTable, form_JewelTypeTable, form_JewelLevelTable, form_EggTable, form_EggEquippedTable, form_DragonTable, form_RunesTable, form_ReforgeTable, form_RefineTable, form_MedalTable, form_RelicsTable, form_WeaponSkinTable)
			value_error_msg = (str(form_error).split("'")[1].replace("_"," ") + ": " + str(form_error).split("'")[3]).title()
			return render(request,"calculator/formulaire.html",{"value_error": value_error_msg,'form_User' :form_User,'form_StuffTable' :form_StuffTable,
				'form_HeroTable' :form_HeroTable,'form_TalentTable' :form_TalentTable,'form_SkinTable' :form_SkinTable,'form_AltarTable' :form_AltarTable,
				'form_JewelTypeTable' :form_JewelTypeTable,'form_JewelLevelTable' :form_JewelLevelTable,'form_EggTable' :form_EggTable,
				'form_EggEquippedTable' :form_EggEquippedTable,'form_DragonTable' :form_DragonTable,'form_RunesTable' :form_RunesTable,
				'form_ReforgeTable' :form_ReforgeTable,'form_RefineTable' :form_RefineTable,'form_MedalTable' :form_MedalTable,'form_RelicsTable' :form_RelicsTable,
				'form_WeaponSkinTable' :form_WeaponSkinTable,'darkmode': checkDarkMode(request), "header_msg":_("Create Profile"), "public_id":pbid,"cookie_request_id":ingame_id,
				"cookie_request_name":ingame_name,"pk_id":pk_id,"sidebarContent":SidebarContent,"cookieUsername":makeCookieheader(user_credential)})
	else:
		return HttpResponseRedirect(f"/{get_language()}/calculator/index")

@loadContent(db_maintenance=True, login_required=True)
def update_calc(request, pbid):
	SidebarContent = LocalDataContentWiki['SidebarContent']
	user_credential = request.session['user_credential']
	makeLog(request)
	ingame_name_cookie,ingame_id_cookie = list(user_credential.items())[0]
	profile = getProfileWithCookie(ingame_id_cookie,ingame_name_cookie,public_id=pbid)
	if profile[0] or DEBUG_STATS:
		user_stats = profile[1]
		if DEBUG_STATS:
			user_stats = user.objects.get(public_id=pbid)
	elif profile[0] == False:
		if profile[1] != None:
			request.session['error_message'] = f'You attempted to access {profile[1].ingame_name}<br>But your login username is "{ingame_name_cookie}".'
		return HttpResponseRedirect(f"/{get_language()}/calculator/index/", {"darkmode": checkDarkMode(request),"header_msg":_("Stats Calculator"),"sidebarContent":SidebarContent})
	if request.method == "GET":
		StuffTable_stats = StuffTable.objects.get(user_profile=user_stats)
		HeroTable_stats = HeroTable.objects.get(user_profile=user_stats)
		TalentTable_stats = TalentTable.objects.get(user_profile=user_stats)
		SkinTable_stats = SkinTable.objects.get(user_profile=user_stats)
		AltarTable_stats = AltarTable.objects.get(user_profile=user_stats)
		JewelTypeTable_stats = JewelTypeTable.objects.get(user_profile=user_stats)
		JewelLevelTable_stats = JewelLevelTable.objects.get(user_profile=user_stats)
		EggTable_stats = EggTable.objects.get(user_profile=user_stats)
		EggEquippedTable_stats = EggEquippedTable.objects.get(user_profile=user_stats)
		DragonTable_stats = DragonTable.objects.get(user_profile=user_stats)
		RunesTable_stats = RunesTable.objects.get(user_profile=user_stats)
		ReforgeTable_stats = ReforgeTable.objects.get(user_profile=user_stats)
		RefineTable_stats = RefineTable.objects.get(user_profile=user_stats)
		MedalTable_stats = MedalsTable.objects.get(user_profile=user_stats)
		RelicsTable_stats = RelicsTable.objects.get(user_profile=user_stats)
		WeaponSkinsTable_stats = WeaponSkinsTable.objects.get(user_profile=user_stats)
		user_id = user_stats.ingame_id
		username = user_stats.ingame_name
		public_id = user_stats.public_id
		form_User = UserForm(user_stats.dictionnaire())
		form_StuffTable = StuffForm(StuffTable_stats.dictionnaire())
		form_HeroTable = HeroForm(HeroTable_stats.dictionnaire())
		form_TalentTable = TalentForm(TalentTable_stats.dictionnaire())
		form_SkinTable = SkinForm(SkinTable_stats.dictionnaire())
		form_AltarTable = AltarForm(AltarTable_stats.dictionnaire())
		form_JewelTypeTable = JewelTypeForm(JewelTypeTable_stats.dictionnaire())
		form_JewelLevelTable = JewelLevelForm(JewelLevelTable_stats.dictionnaire())
		form_EggTable = EggForm(EggTable_stats.dictionnaire())
		form_EggEquippedTable = EggEquippedForm(EggEquippedTable_stats.dictionnaire())
		form_DragonTable = DragonForm(DragonTable_stats.dictionnaire())
		form_RunesTable = RunesForm(RunesTable_stats.dictionnaire())
		form_ReforgeTable = ReforgeForm(ReforgeTable_stats.dictionnaire())
		form_RefineTable = RefineForm(RefineTable_stats.dictionnaire())
		form_MedalTable = MedalsForm(MedalTable_stats.dictionnaire())
		form_RelicsTable = RelicsForm(RelicsTable_stats.dictionnaire())
		form_WeaponSkinTable = WeaponSkinForm(WeaponSkinsTable_stats.dictionnaire())
		ctx = {
			'form_User': form_User,
			'form_StuffTable': form_StuffTable,
			'form_HeroTable': form_HeroTable,
			'form_TalentTable': form_TalentTable,
			'form_SkinTable': form_SkinTable,
			'form_AltarTable': form_AltarTable,
			'form_JewelTypeTable': form_JewelTypeTable,
			'form_JewelLevelTable': form_JewelLevelTable,
			'form_EggTable': form_EggTable,
			'form_EggEquippedTable': form_EggEquippedTable,
			'form_DragonTable': form_DragonTable,
			'form_RunesTable': form_RunesTable,
			'form_ReforgeTable': form_ReforgeTable,
			'form_RefineTable': form_RefineTable,
			'form_MedalTable': form_MedalTable,
			'form_RelicsTable': form_RelicsTable,
			'form_WeaponSkinTable': form_WeaponSkinTable,
			"ingame_id":user_id,
			"public_id":public_id,
			"ingame_name": username,
			"pk_id": user_stats.pk,
			"id_token": pbid,
			"form_dragon_1": DragonTable_stats.dragon1_type,
			"form_dragon_2": DragonTable_stats.dragon2_type,
			"form_dragon_3": DragonTable_stats.dragon3_type,
			"darkmode": checkDarkMode(request),
			"header_msg":_("Stats Calculator"),
			"sidebarContent":SidebarContent,
			"cookieUsername":makeCookieheader(user_credential)
		}
		return render(request,'calculator/formulaire.html',ctx)
	else:
		return HttpResponseRedirect(f"/{get_language()}/calculator/index/")

@loadContent(login_required=True)
def updatetraitement_calc(request, pbid):
	if request.method == "POST":
		SidebarContent = LocalDataContentWiki['SidebarContent']
		try:
			user_instance = user.objects.get(public_id=pbid)
		except:
			request.session['error_message'] = 'User doesn\'t exist'
			return HttpResponseRedirect(f"/{get_language()}/calculator/index/")
		user_credential = request.session['user_credential']
		makeLog(request)
		StuffTable_stats = StuffTable.objects.get(user_profile=user_instance)
		HeroTable_stats = HeroTable.objects.get(user_profile=user_instance)
		TalentTable_stats = TalentTable.objects.get(user_profile=user_instance)
		SkinTable_stats = SkinTable.objects.get(user_profile=user_instance)
		AltarTable_stats = AltarTable.objects.get(user_profile=user_instance)
		JewelTypeTable_stats = JewelTypeTable.objects.get(user_profile=user_instance)
		JewelLevelTable_stats = JewelLevelTable.objects.get(user_profile=user_instance)
		EggTable_stats = EggTable.objects.get(user_profile=user_instance)
		EggEquippedTable_stats = EggEquippedTable.objects.get(user_profile=user_instance)
		DragonTable_stats = DragonTable.objects.get(user_profile=user_instance)
		RunesTable_stats = RunesTable.objects.get(user_profile=user_instance)
		ReforgeTable_stats = ReforgeTable.objects.get(user_profile=user_instance)
		RefineTable_stats = RefineTable.objects.get(user_profile=user_instance)
		MedalTableStats = MedalsTable.objects.get(user_profile=user_instance)
		RelicsTable_stats = RelicsTable.objects.get(user_profile=user_instance)
		WeaponSkinsTable_stats = WeaponSkinsTable.objects.get(user_profile=user_instance)
		form_User = UserForm(request.POST,instance=user_instance)
		form_StuffTable = StuffForm(request.POST,instance=StuffTable_stats)
		form_HeroTable = HeroForm(request.POST,instance=HeroTable_stats)
		form_TalentTable = TalentForm(request.POST,instance=TalentTable_stats)
		form_SkinTable = SkinForm(request.POST,instance=SkinTable_stats)
		form_AltarTable = AltarForm(request.POST,instance=AltarTable_stats)
		form_JewelTypeTable = JewelTypeForm(request.POST,instance=JewelTypeTable_stats)
		form_JewelLevelTable = JewelLevelForm(request.POST,instance=JewelLevelTable_stats)
		form_EggTable = EggForm(request.POST,instance=EggTable_stats)
		form_EggEquippedTable = EggEquippedForm(request.POST,instance=EggEquippedTable_stats)
		form_DragonTable = DragonForm(request.POST,instance=DragonTable_stats)
		form_RunesTable = RunesForm(request.POST,instance=RunesTable_stats)
		form_ReforgeTable = ReforgeForm(request.POST,instance=ReforgeTable_stats)
		form_RefineTable = RefineForm(request.POST,instance=RefineTable_stats)
		form_MedalTable = MedalsForm(request.POST,instance=MedalTableStats)
		form_RelicsTable = RelicsForm(request.POST,instance=RelicsTable_stats)
		form_WeaponSkinTable = WeaponSkinForm(request.POST,instance=WeaponSkinsTable_stats)
		form_validation = all_formIsValid(form_User.is_valid(),form_StuffTable.is_valid(),form_HeroTable.is_valid(),form_TalentTable.is_valid(),form_SkinTable.is_valid(),form_AltarTable.is_valid(),form_JewelTypeTable.is_valid(),form_JewelLevelTable.is_valid(),form_EggTable.is_valid(),form_EggEquippedTable.is_valid(),form_DragonTable.is_valid(),form_RunesTable.is_valid(),form_ReforgeTable.is_valid(),form_RefineTable.is_valid(), form_MedalTable.is_valid(), form_RelicsTable.is_valid(), form_WeaponSkinTable.is_valid())
		if form_validation:
			stats_User = form_User.save(commit=False)
			stats_StuffTable = form_StuffTable.save(commit=False)
			stats_HeroTable = form_HeroTable.save(commit=False)
			stats_TalentTable = form_TalentTable.save(commit=False)
			stats_SkinTable = form_SkinTable.save(commit=False)
			stats_AltarTable = form_AltarTable.save(commit=False)
			stats_JewelTypeTable = form_JewelTypeTable.save(commit=False)
			stats_JewelLevelTable = form_JewelLevelTable.save(commit=False)
			stats_EggTable = form_EggTable.save(commit=False)
			stats_EggEquippedTable = form_EggEquippedTable.save(commit=False)
			stats_DragonTable = form_DragonTable.save(commit=False)
			stats_RunesTable = form_RunesTable.save(commit=False)
			stats_ReforgeTable = form_ReforgeTable.save(commit=False)
			stats_RefineTable = form_RefineTable.save(commit=False)
			stats_MedalTable = form_MedalTable.save(commit=False)
			stats_RelicsTable = form_RelicsTable.save(commit=False)
			stats_WeaponSkinTable = form_WeaponSkinTable.save(commit=False)
			if stats_User.public_id != user_instance.public_id:
				stats_User.public_id = user_instance.public_id
			if stats_User.ingame_id != user_instance.ingame_id:
				stats_User.ingame_id = user_instance.ingame_id
			if stats_User.ingame_name != user_instance.ingame_name:
				stats_User.ingame_name = user_instance.ingame_name
			stats_User.save()
			stats_StuffTable.save()
			stats_HeroTable.save()
			stats_TalentTable.save()
			stats_SkinTable.save()
			stats_AltarTable.save()
			stats_JewelTypeTable.save()
			stats_JewelLevelTable.save()
			stats_EggTable.save()
			stats_EggEquippedTable.save()
			stats_DragonTable.save()
			stats_RunesTable.save()
			stats_ReforgeTable.save()
			stats_RefineTable.save()
			stats_MedalTable.save()
			stats_RelicsTable.save()
			stats_WeaponSkinTable.save()
			return HttpResponseRedirect(f"/stats/calc/{user_instance.public_id}/0/")
		else:
			form_User = UserForm(request.POST,instance=user_instance)
			form_StuffTable = StuffForm(request.POST,instance=StuffTable_stats)
			form_HeroTable = HeroForm(request.POST,instance=HeroTable_stats)
			form_TalentTable = TalentForm(request.POST,instance=TalentTable_stats)
			form_SkinTable = SkinForm(request.POST,instance=SkinTable_stats)
			form_AltarTable = AltarForm(request.POST,instance=AltarTable_stats)
			form_JewelTypeTable = JewelTypeForm(request.POST,instance=JewelTypeTable_stats)
			form_JewelLevelTable = JewelLevelForm(request.POST,instance=JewelLevelTable_stats)
			form_EggTable = EggForm(request.POST,instance=EggTable_stats)
			form_EggEquippedTable = EggEquippedForm(request.POST,instance=EggEquippedTable_stats)
			form_DragonTable = DragonForm(request.POST,instance=DragonTable_stats)
			form_RunesTable = RunesForm(request.POST,instance=RunesTable_stats)
			form_ReforgeTable = ReforgeForm(request.POST,instance=ReforgeTable_stats)
			form_RefineTable = RefineForm(request.POST,instance=RefineTable_stats)
			form_MedalTable = MedalsForm(request.POST,instance=MedalTableStats)
			form_RelicsTable = RelicsForm(request.POST,instance=RelicsTable_stats)
			form_WeaponSkinTable = WeaponSkinForm(request.POST,instance=WeaponSkinsTable_stats)
			form_error = findFormError(form_User, form_StuffTable, form_HeroTable, form_TalentTable, form_SkinTable, form_AltarTable, form_JewelTypeTable, form_JewelLevelTable, form_EggTable, form_EggEquippedTable, form_DragonTable, form_RunesTable, form_ReforgeTable, form_RefineTable, form_MedalTable, form_RelicsTable, form_WeaponSkinTable)
			value_error_msg = (str(form_error).split("'")[1].replace("_"," ") + ": " + str(form_error).split("'")[3]).title()
			ctx = {
				"ingame_id":user_instance.ingame_id,
				"public_id":user_instance.public_id,
				"ingame_name": user_instance.ingame_name,
				"pk_id": user_instance.pk,
				"form_dragon_1": DragonTable_stats.dragon1_type,
				"form_dragon_2": DragonTable_stats.dragon2_type,
				"form_dragon_3": DragonTable_stats.dragon3_type,
				'form_User': form_User,'form_StuffTable': form_StuffTable,
				'form_HeroTable' :form_HeroTable,'form_TalentTable' :form_TalentTable,'form_SkinTable' :form_SkinTable,'form_AltarTable' :form_AltarTable,
				'form_JewelTypeTable' :form_JewelTypeTable,'form_JewelLevelTable' :form_JewelLevelTable,'form_EggTable' :form_EggTable,
				'form_EggEquippedTable' :form_EggEquippedTable,'form_DragonTable' :form_DragonTable,'form_RunesTable' :form_RunesTable,
				'form_ReforgeTable' :form_ReforgeTable,'form_RefineTable' :form_RefineTable,"form_MedalTable":form_MedalTable,"form_RelicsTable":form_RelicsTable,
				"form_WeaponSkinTable":form_WeaponSkinTable,"id_token": pbid, "value_error": value_error_msg,"darkmode": checkDarkMode(request),
				"header_msg":_("Stats Calculator"),"sidebarContent":SidebarContent,"cookieUsername":makeCookieheader(user_credential)
			}
			return render(request,"calculator/formulaire.html",ctx)
	else:
		return HttpResponseRedirect(f"/{get_language()}/calculator/index")

@loadContent(db_maintenance=True)
def delete_user(request, pbid):
	target = user.objects.get(public_id=pbid)
	if request.user.is_superuser:
		target.delete()
		try:
			os.remove(f"calculator/static/image/stuff_save/stuff_{target.ingame_name}.png")
		except (FileNotFoundError,IsADirectoryError,OSError):
			pass
	else:
		cookie_value = checkCookie(request)
		try:
			ingame_name_cookie = list(cookie_value.keys())[0]
		except:
			ingame_name_cookie = "unknown"
		send_embed(ingame_name_cookie,target.ingame_name,f"{ingame_name_cookie} tried to delete {target.ingame_name}'s profile","","",'FF0000',request,True)
	return HttpResponseRedirect(f"/{get_language()}/calculator/index")


@loadContent(db_maintenance=True)
def duplicate_user(request):
	if request.user.is_superuser and request.method == "GET":
		user_list = user.objects.all()
		SidebarContent = LocalDataContentWiki['SidebarContent']
		return render(request, "calculator/duplicate_user.html", {"user_list":user_list, "sidebarContent":SidebarContent, "header_msg": "Duplicate User"})
	elif request.user.is_superuser and request.method == "POST":
		pbid_from_post = request.POST['pbid']
		target = user.objects.get(public_id=pbid_from_post)
		target.duplicate(request.POST['ingame_name'],request.POST['ingame_id'])
	return HttpResponseRedirect(f"/{get_language()}/calculator/index")

@loadContent(db_maintenance=True)
def admin_reload_stats(request,pbid):
	user_credential = request.session.get('user_credential')
	if checkContributor(user_credential,request):
		try:
			os.remove(f"calculator/static/image/stuff_save/{pbid}.png")
		except (FileNotFoundError,IsADirectoryError,OSError):
			pass
		return HttpResponseRedirect(f"/calculator/show/{pbid}/?log=False")
	else:
		return HttpResponseRedirect(f"/{get_language()}/calculator/index")