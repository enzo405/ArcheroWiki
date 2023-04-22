from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from math import *
from .forms import User,StuffTable,HeroTable,TalentTable,SkinTable,AltarTable,JewelTypeTable,JewelLevelTable,EggTable,EggEquippedTable,DragonTable,RunesTable,ReforgeTable,RefineTable,MedalsTable,RelicsTable,WeaponSkinTable
from .image import create_image
from .models import user,stuff_table,hero_table,talent_table,skin_table,altar_table,jewel_type_table,jewel_level_table,egg_table,egg_equipped_table,dragon_table,runes_table,reforge_table,refine_table,medals_table,relics_table,weapon_skins_table,dmg_calc_table
from .function import all_formIsValid,findFormError,checkCookie,login_required,similar,create_unique_id,send_webhook,send_embed,checkTheme_Request, makeCookieheader
import json, os
from const import DEV_MODE

missing_data = []
lang = ["English","Francais","Deutsch","Russian","Española"]
user_init_primary_key = 6


@login_required
def views_calc_stats(request,pbid:str,redirectPath:int):
	global missing_data
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	missing_data.clear()
	try:
		user_stats = user.objects.get(public_id=pbid)
	except:
		return HttpResponseRedirect('/')
	user_credential = request.session['user_credential']
	ingame_name = user_stats.ingame_name
	other_model = user_stats.getOtherModels()
	stuff_table_stats = other_model['stuff_table']
	hero_table_stats = other_model['hero_table']
	talent_table_stats = other_model['talent_table']
	skin_table_stats = other_model['skin_table']
	altar_table_stats = other_model['altar_table']
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
	try:
		os.remove(f"calculator/static/image/stuff_save/{pbid}.png")
	except:
		pass
	################################# REQUÊTE DES ENTRÉES DE L'USERS #######################################################
	atk_base_hero_choosen = user_stats.atk_base_stats_hero_choosen
	health_base_hero_choosen = user_stats.health_base_stats_hero_choosen
	stuff_altar_ascension = altar_table_stats.stuff_altar_ascension
	heros_altar_ascension = altar_table_stats.heros_altar_ascension
	runes_power_attack_flat = runes_table_stats.power_attack_flat
	runes_power_attack_var = runes_table_stats.power_attack_var
	runes_saviour_hp_flat = runes_table_stats.saviour_hp_flat
	runes_saviour_hp_var = runes_table_stats.saviour_hp_var
	runes_recovery_hp_flat = runes_table_stats.recovery_hp_flat
	runes_courage_attack_flat = runes_table_stats.courage_attack_flat
	runes_courage_attack_var = runes_table_stats.courage_attack_var
	runes_luck_hp_flat  = runes_table_stats.luck_hp_flat 
	runes_luck_hp_var  = runes_table_stats.luck_hp_var
	refine_weapon_atk = refine_table_stats.weapon_refine_atk
	refine_weapon_enhanced_equipment = int(refine_table_stats.weapon_refine_basic_stats)/100
	refine_armor_hp = refine_table_stats.armor_refine_hp
	refine_armor_enhanced_equipment = int(refine_table_stats.armor_refine_basic_stats)/100
	refine_ring1_atk = refine_table_stats.ring1_refine_atk
	refine_ring1_enhanced_equipment = int(refine_table_stats.ring1_refine_basic_stats)/100
	refine_ring2_atk = refine_table_stats.ring2_refine_atk
	refine_ring2_enhanced_equipment = int(refine_table_stats.ring2_refine_basic_stats)/100
	refine_bracelet_atk = refine_table_stats.bracelet_refine_atk
	refine_bracelet_enhanced_equipment = int(refine_table_stats.bracelet_refine_basic_stats)/100
	refine_locket_hp = refine_table_stats.locket_refine_hp
	refine_locket_enhanced_equipment = int(refine_table_stats.locket_refine_basic_stats)/100
	refine_book_hp = refine_table_stats.book_refine_hp
	refine_book_enhanced_equipment = int(refine_table_stats.book_refine_basic_stats)/100
	brave_privileges_level = int(user_stats.brave_privileges_level)
	## Get Talents Stats
	talent_stats_dict = talent_table_stats.getTalentStats()
	## Get Altar Ascension Stats
	altar_stuff_ascension_atk = local_data["StuffAltarAscension"][str(stuff_altar_ascension) + '_attack']
	altar_stuff_ascension_hp = local_data["StuffAltarAscension"][str(stuff_altar_ascension) + '_hp']
	altar_stuff_ascension_healing_effect = local_data["StuffAltarAscension"][str(stuff_altar_ascension) + '_healing_effect']
	altar_stuff_ascension_equipment_base = local_data["StuffAltarAscension"][str(stuff_altar_ascension) + '_equipment_base']
	altar_heros_ascension_atk = local_data['HerosAltarAscension'][str(heros_altar_ascension) + '_attack']
	altar_heros_ascension_hp = local_data['HerosAltarAscension'][str(heros_altar_ascension) + '_hp']
	altar_heros_ascension_hp_drop = local_data['HerosAltarAscension'][str(heros_altar_ascension) + '_hp_drop']
	altar_heros_ascension_heros_base = local_data['HerosAltarAscension'][str(heros_altar_ascension) + '_heros_base']
	altar_heros_ascension_dmg_elite = local_data['HerosAltarAscension'][str(heros_altar_ascension) + '_dmg_elite']
	## Get Altar Stats 
	altar_stuff_atk = altar_table_stats.CalculAltar("stuff","attack")
	altar_stuff_hp = altar_table_stats.CalculAltar("stuff","hp")
	altar_hero_atk = altar_table_stats.CalculAltar("heros","attack") ##laissé le S (le nom du field prend un s)
	altar_hero_hp = altar_table_stats.CalculAltar("heros","hp")
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
	skin_health_boost = skin_table_stats.skin_health
	skin_atk_boost = skin_table_stats.skin_attack
	## Get Passiv Stats From Type 1 Egg
	egg_green_bat_passiv = egg_table_stats.GetPassivEggStats1("green_bat", missing_data)
	egg_vase_passiv = egg_table_stats.GetPassivEggStats1("vase",missing_data)
	egg_bomb_ghost_passiv = egg_table_stats.GetPassivEggStats1("bomb_ghost",missing_data)
	egg_rock_puppet_passiv = egg_table_stats.GetPassivEggStats1("rock_puppet",missing_data)
	egg_party_tree_passiv = egg_table_stats.GetPassivEggStats1("party_tree",missing_data)
	egg_zombie_passiv = egg_table_stats.GetPassivEggStats1("zombie",missing_data)
	egg_piranha_passiv = egg_table_stats.GetPassivEggStats1("piranha",missing_data)
	## Get Passiv Stats From Type 2 Egg
	egg_wolfhound_passiv = egg_table_stats.GetPassivEggStats2("wolfhound",missing_data)
	egg_skeleton_archer_passiv = egg_table_stats.GetPassivEggStats2("skeleton_archer",missing_data)
	egg_skeleton_soldier_passiv = egg_table_stats.GetPassivEggStats2("skeleton_soldier",missing_data)
	egg_wasp_passiv = egg_table_stats.GetPassivEggStats2("wasp",missing_data)
	egg_fire_mage_passiv = egg_table_stats.GetPassivEggStats2("fire_mage",missing_data)
	egg_medusa_passiv = egg_table_stats.GetPassivEggStats2("medusa",missing_data)
	egg_ice_mage_passiv = egg_table_stats.GetPassivEggStats2("ice_mage",missing_data)
	egg_fire_lizard_passiv = egg_table_stats.GetPassivEggStats2("fire_lizard",missing_data)
	egg_flame_ghost_passiv = egg_table_stats.GetPassivEggStats2("flame_ghost",missing_data)
	egg_thorny_snake_passiv = egg_table_stats.GetPassivEggStats2("thorny_snake",missing_data)
	egg_tornado_demon_passiv = egg_table_stats.GetPassivEggStats2("tornado_demon",missing_data)
	egg_scarecrow_passiv = egg_table_stats.GetPassivEggStats2("scarecrow",missing_data)
	egg_long_dragon_passiv = egg_table_stats.GetPassivEggStats2("long_dragon",missing_data)
	egg_skull_wizard_passiv = egg_table_stats.GetPassivEggStats2("skull_wizard",missing_data)
	egg_lava_golem_passiv = egg_table_stats.GetPassivEggStats2("lava_golem",missing_data)
	egg_ice_golem_passiv = egg_table_stats.GetPassivEggStats2("ice_golem",missing_data)
	egg_cactus_passiv = egg_table_stats.GetPassivEggStats2("cactus",missing_data)
	egg_crazy_spider_passiv = egg_table_stats.GetPassivEggStats2("crazy_spider",missing_data)
	egg_fire_element_passiv = egg_table_stats.GetPassivEggStats2("fire_element",missing_data)
	egg_skeleton_swordsman_passiv = egg_table_stats.GetPassivEggStats2("skeleton_swordsman",missing_data)
	egg_scythe_mage_passiv = egg_table_stats.GetPassivEggStats2("scythe_mage",missing_data)
	egg_pea_shooter_passiv = egg_table_stats.GetPassivEggStats2("pea_shooter",missing_data)
	egg_shadow_assassin_passiv = egg_table_stats.GetPassivEggStats2("shadow_assassin",missing_data)
	egg_tornado_mage_passiv = egg_table_stats.GetPassivEggStats2("tornado_mage",missing_data)
	egg_spitting_mushroom_passiv = egg_table_stats.GetPassivEggStats2("spitting_mushroom",missing_data)
	egg_rolling_mushroom_passiv = egg_table_stats.GetPassivEggStats2("rolling_mushroom",missing_data)
	egg_fallen_bat_passiv = egg_table_stats.GetPassivEggStats2("fallen_bat",missing_data)
	egg_one_eyed_bat_passiv = egg_table_stats.GetPassivEggStats2("one_eyed_bat",missing_data)
	egg_scarlet_mage_passiv = egg_table_stats.GetPassivEggStats2("scarlet_mage",missing_data)
	egg_icefire_phantom_passiv = egg_table_stats.GetPassivEggStats2("icefire_phantom",missing_data)
	egg_purple_phantom_passiv = egg_table_stats.GetPassivEggStats2("purple_phantom",missing_data)
	egg_tundra_dragon_passiv = egg_table_stats.GetPassivEggStats2("tundra_dragon",missing_data)
	egg_sandian_passiv = egg_table_stats.GetPassivEggStats2("sandian",missing_data)
	egg_nether_puppet_passiv = egg_table_stats.GetPassivEggStats2("nether_puppet",missing_data)
	egg_psionic_scarecrow_passiv = egg_table_stats.GetPassivEggStats2("psionic_scarecrow",missing_data)
	egg_steel_dryad_passiv = egg_table_stats.GetPassivEggStats2("steel_dryad",missing_data)
	egg_savage_spider_passiv = egg_table_stats.GetPassivEggStats2("savage_spider",missing_data)
	egg_flaming_bug_passiv = egg_table_stats.GetPassivEggStats2("flaming_bug",missing_data)
	egg_fat_bat_passiv = egg_table_stats.GetPassivEggStats2("fat_bat",missing_data)
	egg_shark_bro_passiv = egg_table_stats.GetPassivEggStats2("shark_bro",missing_data)
	egg_crimson_zombie_passiv = egg_table_stats.GetPassivEggStats2("crimson_zombie",missing_data)
	egg_plainswolf_passiv = egg_table_stats.GetPassivEggStats2("plainswolf",missing_data)
	egg_elite_archer_passiv = egg_table_stats.GetPassivEggStats2("elite_archer",missing_data)
	egg_little_dragon_passiv = egg_table_stats.GetPassivEggStats2("little_dragon",missing_data)
	egg_rage_golem_passiv = egg_table_stats.GetPassivEggStats2("rage_golem",missing_data)
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
	BonusSpe_jewel_weapon = jewel_level_table_stats.JewelSpeBonusStatsRecup('weapon',brave_privileges_stats['Weapon JSSSA'])
	BonusSpe_jewel_armor = jewel_level_table_stats.JewelSpeBonusStatsRecup('armor',brave_privileges_stats['Armor JSSSA'])
	BonusSpe_jewel_ring1 = jewel_level_table_stats.JewelSpeBonusStatsRecup('ring1',brave_privileges_stats['Ring JSSSA'])
	BonusSpe_jewel_ring2 = jewel_level_table_stats.JewelSpeBonusStatsRecup('ring2',brave_privileges_stats['Ring JSSSA'])
	BonusSpe_jewel_pet1 = jewel_level_table_stats.JewelSpeBonusStatsRecup('pet1',brave_privileges_stats['Spirit JSSSA'])
	BonusSpe_jewel_pet2 = jewel_level_table_stats.JewelSpeBonusStatsRecup('pet2',brave_privileges_stats['Spirit JSSSA'])
	BonusSpe_jewel_bracelet = jewel_level_table_stats.JewelSpeBonusStatsRecup('bracelet',brave_privileges_stats['Bracelet JSSSA'])
	BonusSpe_jewel_locket = jewel_level_table_stats.JewelSpeBonusStatsRecup('locket',brave_privileges_stats['Locket JSSSA'])
	BonusSpe_jewel_book = jewel_level_table_stats.JewelSpeBonusStatsRecup('book',brave_privileges_stats['Spellbook JSSSA'])
	## Get Global Jewel Level
	all_jewel_lvl_dict = jewel_level_table_stats.allLevelForImage()
	## DRAGON
	dragon_1_stats_dict = dragon_table_stats.DragonStatueStats("1")
	dragon_2_stats_dict = dragon_table_stats.DragonStatueStats("2")
	dragon_3_stats_dict = dragon_table_stats.DragonStatueStats("3")
	## Get Dragon passiv Skills
	dragons_skills = dragon_table_stats.getPassivSkillDragon()
	## Get Dragon For Image
	dragon_1 = dragon_table_stats.GetDragon("1")
	dragon_2 = dragon_table_stats.GetDragon("2")
	dragon_3 = dragon_table_stats.GetDragon("3")
	## Get All Stats of Equipped Egg
	activ_egg_stats = egg_equipped_table_stats.GetEggStats(missing_data)
	## Get Reforge Stats
	reforge_atk_power = reforge_table_stats.ReforgePowerCourage("power")
	reforge_atk_courage = reforge_table_stats.ReforgePowerCourage("courage")
	reforge_hp_saviour = reforge_table_stats.ReforgeSaviourRecoLuck("saviour")
	reforge_hp_recovery = reforge_table_stats.ReforgeSaviourRecoLuck("recovery")
	reforge_hp_luck = reforge_table_stats.ReforgeSaviourRecoLuck("luck")
	rune_courage_hero = runes_table_stats.CourageBoostHero(user_stats.choosen_hero)
	## Get Rune Line Stats
	rune_line_stats = runes_table_stats.getValueLine()
	## Get Weapon Skin Stats
	weapon_skin_stats = weapon_skins_table_stats.getWeaponSkinStats()
	## Get name of skin
	weapon_skin_activ = weapon_skins_table_stats.equippedSkin()
	## Get Weapon Coeff Damage Multiplier
	weapon_dmg_multiplier = stuff_table_stats.getWeaponCoeff()
	## Get all Medals Stats
	medal_stats = medals_table_stats.medal_calc()
	## Get all Relics Stats
	relics_stats = relics_table_stats.relics_Stats()
	# Get All Jewel's Stats
	stats_jewel_dict = jewel_level_table_stats.JewelStatsRecup(float(relics_stats['attack_jewel_base']))
	############################################## CALCUL #######################################################
	egg_var_passiv_heros_power_up = int(egg_arch_leader_passiv[3]) + int(egg_medusa_boss_passiv[3]) + int(egg_fire_demon_passiv[3]) + int(egg_krab_boss_passiv[3]) + int(egg_skeleton_king_passiv[1]) + int(egg_skeleton_king_passiv[3]) + int(egg_desert_goliath_passiv[1]) + int(egg_desert_goliath_passiv[3]) + int(egg_ice_demon_passiv[1]) + int(egg_ice_demon_passiv[3]) + int(egg_fireworm_queen_passiv[3]) + int(egg_sinister_touch_passiv[1]) + int(egg_infernal_demon_passiv[3]) + int(egg_scythe_pharoah_passiv[3])
	egg_var_passiv_enhanced_equipment = int(egg_crimson_witch_passiv[3]) + int(egg_queen_bee_passiv[3]) + int(egg_ice_worm_passiv[1]) + int(egg_ice_worm_passiv[3]) + int(egg_giant_owl_passiv[1]) + int(egg_giant_owl_passiv[3]) + int(egg_infernal_demon_passiv[1]) + int(egg_sinister_touch_passiv[3])
	cumul_var_passiv_power_up_hero = (float(relics_stats['hero_base_stats_increased_var']) + float(medal_stats['hero_base_enhanced']) + float(talent_stats_dict['talents_hero_power_up']) + float(egg_var_passiv_heros_power_up) + float(altar_heros_ascension_heros_base))/100
	cumul_var_passiv_enhanced_equipment = (float(rune_line_stats['var_enhanced_eqpm']) + float(relics_stats['enhance_equipment_var']) + float(medal_stats['enhance_equipment']) + float(talent_stats_dict['talents_enhanced_equipment']) + float(egg_var_passiv_enhanced_equipment) + float(altar_stuff_ascension_equipment_base))/100+1

	## Get Stuff Stats
	stuff_activ_stats = stuff_table_stats.getStuffStats(cumul_var_passiv_enhanced_equipment,refine_weapon_enhanced_equipment,refine_armor_enhanced_equipment,refine_ring1_enhanced_equipment,refine_ring2_enhanced_equipment,refine_bracelet_enhanced_equipment,refine_locket_enhanced_equipment,refine_book_enhanced_equipment,weapon_skin_stats)
	stuff_raw_stats = stuff_table_stats.GetRawStats()
	
	## Declare cumul variable 
	cumul_talent_flat_passiv_atk = int(talent_stats_dict['talents_power'])
	cumul_talent_flat_passiv_hp = int(talent_stats_dict['talents_strength'])
	cumul_runes_flat_passiv_atk = int(reforge_atk_power) + int(reforge_atk_courage) + int(runes_power_attack_flat) + int(runes_courage_attack_flat)
	cumul_runes_flat_passiv_hp = int(reforge_hp_recovery) + int(reforge_hp_saviour) + int(reforge_hp_luck) + int(runes_recovery_hp_flat) + int(runes_saviour_hp_flat) + int(runes_luck_hp_flat)
	cumul_hero_flat_passiv_atk = int(hero_Atreus[5]) + int(hero_Urasil[0]) + int(hero_Phoren[6]) + int(hero_Helix[5]) + int(hero_Meowgik[0]) + int(hero_Ayana[6]) + int(hero_Rolla[0]) + int(hero_Bonnie[5]) + int(hero_Shade[6]) + int(hero_Ophelia[0]) + int(hero_Ophelia[2]) + int(hero_Lina[0]) + int(hero_Lina[5]) + int(hero_Aquea[5]) + int(hero_Iris[5]) + int(hero_Melinda[6]) + int(hero_Iris[1]) + int(hero_Blazo[1]) + int(hero_Stella[0])
	cumul_hero_flat_passiv_hp = int(hero_Atreus[0]) + int(hero_Atreus[6]) + int(hero_Urasil[5]) + int(hero_Taranis[5]) + int(hero_Meowgik[6]) + int(hero_Shari[1]) + int(hero_Shari[5]) + int(hero_Onir[0]) + int(hero_Onir[5]) + int(hero_Bonnie[6]) + int(hero_Sylvan[0]) + int(hero_Lina[6]) + int(hero_Aquea[0]) + int(hero_Aquea[6]) + int(hero_Shingen[6]) + int(hero_Iris[0]) + int(hero_Blazo[6]) + int(hero_Elaine[5]) + int(hero_Elaine[6]) + int(hero_Bobo[5]) + int(hero_Bobo[6])
	cumul_skin_flat_passiv_atk = int(skin_atk_boost)
	cumul_skin_flat_passiv_hp = int(skin_health_boost)
	cumul_egg_flat_passiv_atk = int(egg_bomb_ghost_passiv[1]) + int(egg_green_bat_passiv[1]) + int(egg_piranha_passiv[1]) + int(egg_crazy_spider_passiv[1]) + int(egg_fire_mage_passiv[1]) + int(egg_skeleton_archer_passiv[1]) + int(egg_skeleton_soldier_passiv[1]) + int(egg_fire_element_passiv[1]) + int(egg_flame_ghost_passiv[1]) + int(egg_ice_mage_passiv[1]) + int(egg_pea_shooter_passiv[1]) + int(egg_shadow_assassin_passiv[1]) + int(egg_skull_wizard_passiv[1]) + int(egg_tornado_demon_passiv[1]) + int(egg_savage_spider_passiv[1]) + int(egg_flaming_bug_passiv[1]) + int(egg_one_eyed_bat_passiv[1]) + int(egg_elite_archer_passiv[1]) + int(egg_icefire_phantom_passiv[1]) + int(egg_purple_phantom_passiv[1]) + int(egg_scarlet_mage_passiv[1]) + int(egg_arch_leader_passiv[0]) + int(egg_crimson_witch_passiv[0]) + int(egg_medusa_boss_passiv[0]) + int(egg_ice_worm_passiv[0]) + int(egg_desert_goliath_passiv[0]) + int(egg_ice_demon_passiv[0]) + int(egg_fire_demon_passiv[1]) + int(egg_crimson_zombie_passiv[1]) + int(egg_scythe_pharoah_passiv[1]) + int(egg_infernal_demon_passiv[0]) + int(egg_fireworm_queen_passiv[0])
	cumul_egg_flat_passiv_hp = int(egg_green_bat_passiv[3]) + int(egg_party_tree_passiv[1]) + int(egg_rock_puppet_passiv[1]) +  int(egg_vase_passiv[1]) + int(egg_zombie_passiv[1]) + int(egg_fire_lizard_passiv[1]) + int(egg_long_dragon_passiv[1]) + int(egg_scarecrow_passiv[1]) + int(egg_skeleton_swordsman_passiv[1]) + int(egg_tornado_mage_passiv[1]) + int(egg_wasp_passiv[1]) + int(egg_cactus_passiv[1]) + int(egg_ice_golem_passiv[1]) + int(egg_scythe_mage_passiv[1]) + int(egg_skull_wizard_passiv[4]) + int(egg_fallen_bat_passiv[1]) + int(egg_nether_puppet_passiv[1]) + int(egg_psionic_scarecrow_passiv[1]) + int(egg_spitting_mushroom_passiv[1]) + int(egg_steel_dryad_passiv[1]) + int(egg_tundra_dragon_passiv[1]) +  int(egg_little_dragon_passiv[1]) + int(egg_rage_golem_passiv[1]) + int(egg_krab_boss_passiv[1]) + int(egg_skeleton_king_passiv[0]) + int(egg_queen_bee_passiv[0]) + int(egg_fire_demon_passiv[0]) + int(egg_plainswolf_passiv[1])
	cumul_altar_flat_passiv_atk = int(altar_stuff_atk) + int(altar_hero_atk)
	cumul_altar_flat_passiv_hp = int(altar_stuff_hp) + int(altar_hero_hp)
	cumul_jewel_flat_activ_atk = int(stats_jewel_dict['attack_ruby']) + int(stats_jewel_dict['attack_kunzite']) + int(stats_jewel_dict['attack_tourmaline']) + int(BonusSpe_jewel_weapon[0]) + int(BonusSpe_jewel_weapon[4]) + int(BonusSpe_jewel_bracelet[0]) + int(BonusSpe_jewel_bracelet[2]) + int(BonusSpe_jewel_bracelet[4])
	cumul_jewel_flat_activ_hp = int(stats_jewel_dict['pv_emerald']) + int(stats_jewel_dict['pv_lapis']) + int(stats_jewel_dict['pv_calaite']) + int(BonusSpe_jewel_armor[0]) + int(BonusSpe_jewel_armor[4]) + int(BonusSpe_jewel_bracelet[1]) + int(BonusSpe_jewel_locket[2]) + int(BonusSpe_jewel_locket[4])	
	cumul_old_flat_passiv_atk = int(cumul_talent_flat_passiv_atk) + int(cumul_runes_flat_passiv_atk) + int(cumul_hero_flat_passiv_atk) + int(cumul_skin_flat_passiv_atk) + int(cumul_egg_flat_passiv_atk)
	cumul_old_flat_passiv_hp = int(cumul_talent_flat_passiv_hp) + int(cumul_runes_flat_passiv_hp) + int(cumul_hero_flat_passiv_hp) + int(cumul_skin_flat_passiv_hp) + int(cumul_egg_flat_passiv_hp)
	cumul_refine_flat_activ_atk =  int(refine_weapon_atk) + int(refine_ring1_atk) + int(refine_ring2_atk) + int(refine_bracelet_atk)
	cumul_refine_flat_activ_hp = int(refine_armor_hp) + int(refine_locket_hp) + int(refine_book_hp)
	cumul_dragon_flat_activ_atk = int(dragon_1_stats_dict.get("Attack",0)) + int(dragon_2_stats_dict.get("Attack",0)) + int(dragon_3_stats_dict.get("Attack",0))
	cumul_dragon_flat_activ_hp = int(dragon_1_stats_dict.get("Max Hp",0)) + int(dragon_2_stats_dict.get("Max Hp",0)) + int(dragon_3_stats_dict.get("Max Hp",0))
	cumul_stuff_flat_activ_atk = round(stuff_activ_stats['weapon_total'] + stuff_activ_stats['bracelet_total'])
	cumul_stuff_flat_activ_hp = round(stuff_activ_stats['armor_total'] + stuff_activ_stats['locket_total'] + stuff_activ_stats['book_total'])

	cumul_runes_var_passiv_atk = float(runes_power_attack_var) + float(runes_courage_attack_var)
	cumul_runes_var_passiv_hp = float(runes_saviour_hp_var) + float(runes_luck_hp_var)
	cumul_heros_var_passiv_atk = float(hero_Taranis[2]) + float(hero_Meowgik[2]) + float(hero_Ayana[2]) + float(hero_Rolla[2]) + float(hero_Sylvan[2]) + float(hero_Aquea[2]) + float(hero_Iris[2]) + float(hero_Bonnie[4]) + float(hero_Shade[7]) + float(hero_Melinda[7]) + float(hero_Bobo[1]) + float(hero_Bobo[4]) + float(hero_Stella[2])
	cumul_heros_var_passiv_hp = float(hero_Atreus[2]) + float(hero_Helix[2]) + float(hero_Bonnie[2]) + float(hero_Shade[2]) + float(hero_Lina[2]) + float(hero_Shingen[2]) + float(hero_Blazo[2]) + float(hero_Ryan[4]) + float(hero_Gugu[4]) + float(hero_Blazo[4]) + float(hero_Atreus[7]) + float(hero_Rolla[7])  + float(hero_Elaine[7]) + float(hero_Elaine[2])
	cumul_heros_var_activ_atk = float(hero_Onir[3]) + float(hero_Bonnie[3])
	cumul_heros_var_activ_hp = float(hero_Urasil[3]) + float(hero_Sylvan[3]) + float(hero_Ophelia[3]) + float(hero_Ryan[1]) + float(hero_Elaine[1]) 
	cumul_altar_var_passiv_atk = float(altar_heros_ascension_atk) + float(altar_stuff_ascension_atk)
	cumul_altar_var_passiv_hp = float(altar_heros_ascension_hp) + float(altar_stuff_ascension_hp)
	cumul_privileges_var_passiv_atk = float(brave_privileges_stats['Attack Var'])
	cumul_privileges_var_passiv_hp = float(brave_privileges_stats['Hp Var'])
	cumul_jewel_var_activ_atk =  (float(BonusSpe_jewel_weapon[2]) + float(BonusSpe_jewel_ring1[5]) + float(BonusSpe_jewel_book[2]))/100
	cumul_jewel_var_activ_hp = (float(BonusSpe_jewel_book[3]) + float(BonusSpe_jewel_ring2[5]))/100
	cumul_stuff_var_activ_atk = (stuff_activ_stats['weapon_attack_var'] + stuff_activ_stats['bracelet_attack_var'] + stuff_activ_stats['ring1_atk_var'] + stuff_activ_stats['ring2_atk_var'])
	cumul_stuff_var_activ_hp = (stuff_activ_stats['armor_hp_var'] + stuff_activ_stats['book_hp_var'] + stuff_activ_stats['ring1_hp_var'] + stuff_activ_stats['ring2_hp_var'] + stuff_activ_stats['locket_hp_var'])

	cumul_heros_var_passiv_crit_dmg = float(hero_Urasil[2]) + float(hero_Taranis[3]) + float(hero_Helix[0]) + float(hero_Ayana[5]) + float(hero_Rolla[6]) + float(hero_Bonnie[0]) + float(hero_Shade[4])
	cumul_heros_var_passiv_crit_rate = float(hero_Elaine[3]) + float(hero_Melinda[3]) + float(hero_Shade[1]) + float(hero_Shade[5]) + float(hero_Shari[2]) + float(hero_Helix[3]) + float(hero_Taranis[0]) + float(hero_Phoren[0]) + float(hero_Phoren[2]) + float(hero_Phoren[3]) + float(hero_Urasil[6]) + float(hero_Stella[1])

	cumul_var_atk = (float(cumul_runes_var_passiv_atk) + float(cumul_heros_var_passiv_atk) + float(cumul_heros_var_activ_atk) + float(cumul_altar_var_passiv_atk) + float(cumul_privileges_var_passiv_atk) + float(medal_stats['attack_var']) + float(relics_stats['attack_var']))/100
	cumul_var_hp = (float(cumul_runes_var_passiv_hp) + float(cumul_heros_var_passiv_hp) + float(cumul_heros_var_activ_hp) + float(cumul_altar_var_passiv_hp) + float(cumul_privileges_var_passiv_hp) + float(medal_stats['hp_var']) + float(relics_stats['hp_var']))/100
	hero_modified_base_atk = (int(atk_base_hero_choosen) - int(rune_courage_hero['current_hero_atk_flat'])) * (float(rune_courage_hero['current_hero_atk_var']) + float(cumul_var_passiv_power_up_hero) + 1) + int(rune_courage_hero['current_hero_atk_flat'])
	hero_modified_base_hp = (int(health_base_hero_choosen) - int(rune_courage_hero['current_hero_hp_flat'])) * (float(rune_courage_hero['current_hero_hp_var']) + float(cumul_var_passiv_power_up_hero) + 1) + int(rune_courage_hero['current_hero_hp_flat'])
	############################################# RESULT #############################################
	global_critic_damage = 200 + float(dragons_skills.get("Crit Damage",0.0)) + float(rune_line_stats['var_crit_dmg']) + float(stats_jewel_dict['crit_dmg_topaz']) + float(stuff_raw_stats['weapon_crit_raw']) + float(stuff_raw_stats['ring1_crit_damage_raw']) + float(stuff_raw_stats['ring2_crit_damage_raw']) + float(stuff_raw_stats['bracelet_crit_raw']) + float(activ_egg_stats['Critic Damage']) + float(cumul_heros_var_passiv_crit_dmg) + float(BonusSpe_jewel_weapon[1])
	global_elemental_damage_flat = 0
	global_elemental_damage_var = float(rune_line_stats['var_elemental_dmg']) + float(relics_stats['elemental_damage_var']) + float(brave_privileges_stats['Elemental Damage']) + float(stats_jewel_dict['elementary_dmg_amber']) + float(hero_Sylvan[7])
	global_dodge_chance = 1 - (1-(float(dragons_skills.get("Dodge rate",0.0)))*1-(float(rune_line_stats['dodge']))*1-(float(relics_stats['dodge']))*1-(float(BonusSpe_jewel_ring1[4]))*1-(float(dragon_1_stats_dict.get("Dodge",0.0)))*1-(float(dragon_2_stats_dict.get("Dodge",0.0)))*1-(float(dragon_3_stats_dict.get("Dodge",0.0)))*1-(float(stuff_raw_stats['armor_dodge_raw']))*1-(float(stuff_raw_stats['locket_dodge_raw']))*1-(float(stuff_raw_stats['ring1_dodge_raw']))*1-(float(stuff_raw_stats['ring2_dodge_raw']))*1-(float(hero_Meowgik[4]))*1-(float(hero_Meowgik[7]))*1-(float(hero_Meowgik[1]))*1-(float(hero_Ayana[3]))*1-(float(hero_Rolla[3]))*1-(float(hero_Lina[1]))*1-(float(hero_Gugu[1]))*1-(float(hero_Iris[3])))
	global_crit_rate = float(15) + float(rune_line_stats['var_crit_rate']) + float(BonusSpe_jewel_weapon[5]) + float(relics_stats['crit_chance_var']) + float(brave_privileges_stats['Critic Rate']) + float(stuff_raw_stats['ring1_crit_chance_raw']) + float(stuff_raw_stats['ring2_crit_chance_raw']) + float(cumul_heros_var_passiv_crit_rate)
	global_boss_damage_flat = int(rune_line_stats['flat_dmg_boss']) + int(relics_stats['damage_bosses']) + int(activ_egg_stats['Damage To Bosses']) + int(stuff_activ_stats.get('boss units dmg',0)) + int(stuff_activ_stats.get('boss units dmg',0)) + int(stats_jewel_dict['dmg_to_boss'])
	global_boss_damage_var = float(stuff_activ_stats.get('boss units dmg var',0.0)) + float(rune_line_stats['var_dmg_boss']) + float(relics_stats['damage_bosses_var'])
	global_mobs_damage_flat = int(rune_line_stats['flat_dmg_mob']) + int(relics_stats['damage_mobs']) + int(dragon_1_stats_dict.get("Damage To Mobs",0)) + int(dragon_2_stats_dict.get("Damage To Mobs",0)) + int(dragon_3_stats_dict.get("Damage To Mobs",0)) + int(activ_egg_stats['Damage To Mobs']) + int(stuff_activ_stats.get('mobs units dmg',0)) + int(stuff_activ_stats.get('mobs units dmg',0)) + int(stats_jewel_dict['dmg_to_mobs']) + int(hero_Bobo[0])
	global_mobs_damage_var = float(stuff_activ_stats.get('mobs units dmg var',0.0)) + float(rune_line_stats['var_dmg_mob']) + float(relics_stats['damage_mobs_var'])
	global_ranged_damage_flat = int(rune_line_stats['flat_dmg_ranged']) + int(relics_stats['damage_ranged_units']) + int(dragon_1_stats_dict.get("Damage To Ranged Units",0)) + int(dragon_2_stats_dict.get("Damage To Ranged Units",0)) + int(dragon_3_stats_dict.get("Damage To Ranged Units",0)) + int(stuff_activ_stats.get('ranged units dmg',0)) + int(stuff_activ_stats.get('ranged units dmg',0)) + int(activ_egg_stats['Damage To Ranged Units']) + int(hero_Ryan[0]) + int(hero_Melinda[0]) + int(hero_Sylvan[5]) + int(hero_Ryan[5]) + int(hero_Melinda[5]) + int(hero_Helix[6]) + int(hero_Gugu[6])
	global_ranged_damage_var = float(stuff_activ_stats.get('ranged units dmg var',0.0)) + float(rune_line_stats['var_dmg_ranged']) + float(hero_Bobo[2]) + float(hero_Gugu[2]) + float(hero_Ayana[4]) + float(hero_Melinda[4]) + float(hero_Sylvan[4]) + float(hero_Phoren[4]) + float(hero_Atreus[1]) + float(hero_Ayana[1]) + float(hero_Sylvan[1])
	global_ground_damage_flat = int(rune_line_stats['flat_dmg_ground']) + int(relics_stats['damage_ground_units']) + int(dragon_1_stats_dict.get("Damage To Ground Units",0)) + int(dragon_2_stats_dict.get("Damage To Ground Units",0)) + int(dragon_3_stats_dict.get("Damage To Ground Units",0)) + int(stuff_activ_stats.get('ground units dmg',0)) + int(stuff_activ_stats.get('ground units dmg',0)) + int(activ_egg_stats['Damage To Ground Units']) + int(hero_Shade[0]) + int(hero_Ophelia[5]) + int(hero_Blazo[5]) + int(hero_Sylvan[6])
	global_ground_damage_var = float(stuff_activ_stats.get('ground units dmg var',0.0)) + float(rune_line_stats['var_dmg_ground']) + float(relics_stats['damage_ground_units_var']) + float(hero_Onir[4]) + float(hero_Shingen[4]) + float(hero_Phoren[7]) + float(hero_Onir[1]) + float(hero_Blazo[3])
	global_airborne_damage_flat = int(rune_line_stats['flat_dmg_airborne']) + int(relics_stats['damage_airborne_units']) + int(stuff_activ_stats.get('airborne units dmg',0)) + int(stuff_activ_stats.get('airborne units dmg',0)) + int(activ_egg_stats['Damage To Airborne Units']) + int(hero_Ayana[0]) + int(hero_Gugu[0]) + int(hero_Ryan[2]) + int(hero_Phoren[5]) + int(hero_Gugu[5]) + int(hero_Taranis[6]) + int(hero_Ryan[6]) + int(hero_Iris[6]) + int(hero_Elaine[0])
	global_airborne_damage_var = float(stuff_activ_stats.get('airborne units dmg var',0.0)) + float(rune_line_stats['var_dmg_airborne']) + float(relics_stats['damage_airborne_units_var']) + float(hero_Taranis[4]) + float(hero_Iris[4]) + float(hero_Taranis[1])
	global_melee_damage_flat = int(rune_line_stats['flat_dmg_melee']) + int(relics_stats['damage_melee_units']) + int(dragon_1_stats_dict.get("Damage To Melee Units",0)) + int(dragon_2_stats_dict.get("Damage To Melee Units",0)) + int(dragon_3_stats_dict.get("Damage To Melee Units",0)) + int(stuff_activ_stats.get('melee units dmg',0)) + int(stuff_activ_stats.get('melee units dmg',0)) + int(activ_egg_stats['Damage To Melee Units']) + int(hero_Shari[0]) + int(hero_Shingen[0]) + int(hero_Blazo[0]) + int(hero_Rolla[5]) + int(hero_Shingen[5]) + int(hero_Shari[6])
	global_melee_damage_var = float(stuff_activ_stats.get('melee units dmg var',0.0)) + float(dragons_skills.get("Damage VS melee units",0.0)) + float(rune_line_stats['var_dmg_melee']) + float(hero_Shari[3]) + float(hero_Melinda[2]) + float(hero_Urasil[4]) + float(hero_Ophelia[4]) + float(hero_Lina[4]) + float(hero_Urasil[1]) + float(hero_Ophelia[1]) + float(hero_Shingen[3]) + float(hero_Elaine[4])
	global_normal_damage_flat = int(stuff_activ_stats.get("non-elite mobs dmg",0))
	global_normal_damage_var = float(stuff_activ_stats.get("non-elite mobs dmg var",0))
	global_elite_damage_flat = int(stuff_activ_stats.get("elite mobs dmg",0))
	global_elite_damage_var = float(relics_stats.get("damage_elite_var",0.0)) + float(stuff_activ_stats.get("elite mobs dmg var",0)) + float(altar_heros_ascension_dmg_elite) ### RELICS damage_elite_var doesn't work because field isn't added in db and won't be added 
	global_all_damage_flat = 0
	global_all_damage_var = 0
	weapon_ranged_damage = float(stats_jewel_dict['weapon_ranged_damage']) + float(relics_stats.get("weapon_ranged_damage_var",0.0)) + float(hero_Iris[7])
	weapon_melee_damage = float(dragon_1_stats_dict.get("Weapon Melee Damage",0)) + float(dragon_2_stats_dict.get("Weapon Melee Damage",0)) + float(dragon_3_stats_dict.get("Weapon Melee Damage",0)) + float(relics_stats.get("weapon_melee_damage_var",0.0)) + float(hero_Shingen[7])
	weapon_damage = float(hero_Stella[7]) + float(stuff_raw_stats['weapon_damage_stats'])

	global_stats_atk_flat = hero_modified_base_atk + int(cumul_old_flat_passiv_atk) + int(cumul_stuff_flat_activ_atk) + int(activ_egg_stats["Attack"]) + int(cumul_altar_flat_passiv_atk) + int(cumul_dragon_flat_activ_atk) + int(brave_privileges_stats['Attack Flat']) + int(medal_stats['attack']) + int(relics_stats['attack'])
	global_stats_hp_flat = hero_modified_base_hp + int(cumul_old_flat_passiv_hp) + int(cumul_stuff_flat_activ_hp) + int(activ_egg_stats["Max Hp"]) + int(cumul_altar_flat_passiv_hp) + int(cumul_dragon_flat_activ_hp) + int(brave_privileges_stats['Hp Flat']) + int(medal_stats['hp']) + int(relics_stats['hp'])
	global_stats_atk = global_stats_atk_flat + (global_stats_atk_flat*float(cumul_var_atk)) + (global_stats_atk_flat*float(cumul_stuff_var_activ_atk)) + (global_stats_atk_flat*float(cumul_jewel_var_activ_atk)) + cumul_jewel_flat_activ_atk + cumul_refine_flat_activ_atk
	global_stats_hp = global_stats_hp_flat + (global_stats_hp_flat*float(cumul_var_hp)) + (global_stats_hp_flat*float(cumul_stuff_var_activ_hp)) + (global_stats_hp_flat*float(cumul_jewel_var_activ_hp)) + cumul_jewel_flat_activ_hp + cumul_refine_flat_activ_hp
	###################### CREATION IMAGE STUFF#############################################################
	create_image(pbid,str(stuff_table_stats.dictionnaire()['weapon_choosen'].lower().replace(" ","_")),
		str(stuff_table_stats.dictionnaire()['weapon_rarity'].lower().replace(" ","_")),int(stuff_table_stats.dictionnaire()['weapon_level']),
		str(stuff_table_stats.dictionnaire()['armor_choosen'].lower().replace(" ","_")),str(stuff_table_stats.dictionnaire()['armor_rarity'].lower().replace(" ","_")),int(stuff_table_stats.dictionnaire()['armor_level']),str(stuff_table_stats.dictionnaire()['ring1_choosen'].lower().replace(" ","_")),
		str(stuff_table_stats.dictionnaire()['ring1_rarity'].lower().replace(" ","_")),int(stuff_table_stats.dictionnaire()['ring1_level']),
		str(stuff_table_stats.dictionnaire()['ring2_choosen'].lower().replace(" ","_")),str(stuff_table_stats.dictionnaire()['ring2_rarity'].lower().replace(" ","_")),int(stuff_table_stats.dictionnaire()['ring2_level']),str(stuff_table_stats.dictionnaire()['pet1_choosen'].lower().replace(" ","_")),
		str(stuff_table_stats.dictionnaire()['pet1_rarity'].lower().replace(" ","_")),int(stuff_table_stats.dictionnaire()['pet1_level']),
		str(stuff_table_stats.dictionnaire()['pet2_choosen'].lower().replace(" ","_")),str(stuff_table_stats.dictionnaire()['pet2_rarity'].lower().replace(" ","_")),int(stuff_table_stats.dictionnaire()['pet2_level']),
		str(stuff_table_stats.dictionnaire()['bracelet_choosen'].lower().replace(" ","_")),str(stuff_table_stats.dictionnaire()['bracelet_rarity'].lower().replace(" ","_")),int(stuff_table_stats.dictionnaire()['bracelet_level']),
		str(stuff_table_stats.dictionnaire()['locket_choosen'].lower().replace(" ","_")),str(stuff_table_stats.dictionnaire()['locket_rarity'].lower().replace(" ","_")),int(stuff_table_stats.dictionnaire()['locket_level']),
		str(stuff_table_stats.dictionnaire()['book_choosen'].lower().replace(" ","_")),str(stuff_table_stats.dictionnaire()['book_rarity'].lower().replace(" ","_")),int(stuff_table_stats.dictionnaire()['book_level']),
		int(round(global_stats_atk)),int(round(global_stats_hp)),int(all_jewel_lvl_dict['jewel_lvl_weapon']),int(all_jewel_lvl_dict['jewel_lvl_armor']),int(all_jewel_lvl_dict['jewel_lvl_ring1']),int(all_jewel_lvl_dict['jewel_lvl_ring2']),int(all_jewel_lvl_dict['jewel_lvl_pet1']),
		int(all_jewel_lvl_dict['jewel_lvl_pet2']),int(all_jewel_lvl_dict['jewel_lvl_bracelet']),int(all_jewel_lvl_dict['jewel_lvl_locket']),int(all_jewel_lvl_dict['jewel_lvl_book']),str(user_stats.choosen_hero),str(dragon_1['dragon_type']),str(dragon_2['dragon_type']),
		str(dragon_3['dragon_type']),str(dragon_1['dragon_rarity']),str(dragon_2['dragon_rarity']),str(dragon_3['dragon_rarity']),weapon_skin_activ)

	user_stats.global_atk_save = int(global_stats_atk)
	user_stats.global_hp_save = int(global_stats_hp)
	user_stats.save()
	try:
		calc_user_dmg = dmg_calc_table.objects.get(user_profile=user_stats)
	except Exception:
		calc_user_dmg = dmg_calc_table()
		calc_user_dmg.user_profile = user_stats
	finally:
		calc_user_dmg.weapon_coeff = weapon_dmg_multiplier
		calc_user_dmg.flat_dmg_vs_ground = global_ground_damage_flat
		calc_user_dmg.flat_dmg_vs_airborne = global_airborne_damage_flat
		calc_user_dmg.flat_dmg_vs_melee = global_melee_damage_flat
		calc_user_dmg.flat_dmg_vs_range = global_ranged_damage_flat
		calc_user_dmg.flat_dmg_vs_mobs = global_mobs_damage_flat
		calc_user_dmg.flat_dmg_vs_boss = global_boss_damage_flat
		calc_user_dmg.flat_dmg_element = global_elemental_damage_flat
		calc_user_dmg.flat_dmg_all = global_all_damage_flat
		calc_user_dmg.flat_elite_dmg = global_elite_damage_flat
		calc_user_dmg.flat_normal_dmg = global_normal_damage_flat
		calc_user_dmg.var_dmg_vs_ground = global_ground_damage_var
		calc_user_dmg.var_dmg_vs_airborne = global_airborne_damage_var
		calc_user_dmg.var_dmg_vs_melee = global_melee_damage_var
		calc_user_dmg.var_dmg_vs_range = global_ranged_damage_var
		calc_user_dmg.var_dmg_vs_mobs = global_mobs_damage_var
		calc_user_dmg.var_dmg_vs_boss = global_boss_damage_var
		calc_user_dmg.var_dmg_element = global_elemental_damage_var
		calc_user_dmg.var_dmg_all = global_all_damage_var
		calc_user_dmg.var_normal_dmg = global_normal_damage_var
		calc_user_dmg.var_elite_dmg = global_elite_damage_var
		calc_user_dmg.crit_dmg = global_critic_damage
		calc_user_dmg.crit_rate = global_crit_rate
		calc_user_dmg.dodge_rate = global_dodge_chance
		calc_user_dmg.weapon_damage = weapon_damage
		calc_user_dmg.weapon_melee_damage = weapon_melee_damage
		calc_user_dmg.weapon_ranged_damage = weapon_ranged_damage

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
	messages.success(request=request,message=f"{ingame_name.capitalize()} updated with success")
	return HttpResponseRedirect(f'{dict_Link[redirectPath]}')

@login_required
def affiche_calc(request, pbid):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	user_credential = request.session['user_credential']
	darkmode = checkTheme_Request(request,user_credential)
	try: ## handle error if pbid doesn't exist
		user_stats = user.objects.get(public_id=pbid)
		try:
			dmg_calc_table_stats = dmg_calc_table.objects.get(user_profile=user_stats)
		except:
			return HttpResponseRedirect(f"/stats/calc/{pbid}/1/")
		if not os.path.exists(f"calculator/static/image/stuff_save/{pbid}.png"):
			return HttpResponseRedirect(f"/stats/calc/{pbid}/0/")
		valueError = "no"
		if dmg_calc_table_stats.missing_data != "" and dmg_calc_table_stats.missing_data != "none":
			valueError = "yes"
		ctx = {
			"pbid":pbid,
			"name":user_stats.ingame_name,
			"stats":user_stats,
			"global_stats_atk":user_stats.global_atk_save,
			"global_stats_hp":user_stats.global_hp_save,
			'global_critic_damage': dmg_calc_table_stats.crit_dmg,
			'global_crit_rate': dmg_calc_table_stats.crit_rate,
			'global_dodge_chance': dmg_calc_table_stats.dodge_rate,
			'global_boss_damage': dmg_calc_table_stats.flat_dmg_vs_boss,
			'global_boss_damage_var': dmg_calc_table_stats.var_dmg_vs_boss,
			'global_mobs_damage': dmg_calc_table_stats.flat_dmg_vs_mobs,
			'global_mobs_damage_var': dmg_calc_table_stats.var_dmg_vs_mobs,
			'global_ranged_damage': dmg_calc_table_stats.flat_dmg_vs_range,
			'global_ranged_damage_var': dmg_calc_table_stats.var_dmg_vs_range,
			'global_ground_damage': dmg_calc_table_stats.flat_dmg_vs_ground,
			'global_ground_damage_var': dmg_calc_table_stats.var_dmg_vs_ground,
			'global_airborne_damage': dmg_calc_table_stats.flat_dmg_vs_airborne,
			'global_airborne_damage_var': dmg_calc_table_stats.var_dmg_vs_airborne,
			'global_melee_damage': dmg_calc_table_stats.flat_dmg_vs_melee,
			'global_melee_damage_var': dmg_calc_table_stats.var_dmg_vs_melee,
			'global_elemental_damage': dmg_calc_table_stats.var_dmg_element,
			"global_elite_damage_flat": dmg_calc_table_stats.flat_elite_dmg,
			"global_normal_damage_flat": dmg_calc_table_stats.flat_normal_dmg,
			"global_normal_damage_var": dmg_calc_table_stats.var_normal_dmg,
			"global_elite_damage_var": dmg_calc_table_stats.var_elite_dmg,
			"weapon_damage": dmg_calc_table_stats.weapon_damage,
			"weapon_melee_damage": dmg_calc_table_stats.weapon_melee_damage,
			"weapon_ranged_damage": dmg_calc_table_stats.weapon_ranged_damage,
			"darkmode": darkmode,
			"header_msg": "Stats Calculator",
			"ValueError": valueError,
			"missing_data": dmg_calc_table_stats.missing_data,
			"lang":lang,
			"sidebarContent":SidebarContent,
			"cookieUsername":makeCookieheader(user_credential),
			'DEV_MODE':DEV_MODE
		}
		if request.user.is_superuser:
			ctx['DEV_MODE'] = True
		return render(request,'calculator/affiche.html',ctx)
	except Exception as e:
		messages.error(request,e)
		return HttpResponseRedirect("/")

@login_required
def index_calc(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	user_credential = request.session['user_credential']
	darkmode = checkTheme_Request(request,user_credential)
	try_access = False
	user_liste = list(user.objects.all().order_by('-global_atk_save'))
	user_stats = ""
	self_ingame_name = ""
	self_public_id = ""
	self_global_atk_save = ""
	self_global_hp_save = ""
	avatar_src = f"/static/image/hero_icon/icon_unknown.png"
	rank = "?"
	try:
		ingame_id_cookie = list(user_credential.values())[0]
		ingame_name_cookie = list(user_credential.keys())[0]
		if ingame_id_cookie == "0-000000" and ingame_name_cookie == "visitor":
			show_table = "visitor"
		else:
			user_stats = user.objects.get(ingame_id=ingame_id_cookie)
			self_ingame_name = user_stats.ingame_name
			self_ingame_hero = user_stats.choosen_hero
			if os.path.exists(f"calculator/static/image/hero_icon/icon_{self_ingame_hero}.png"):
				avatar_src = f"/static/image/hero_icon/icon_{self_ingame_hero}.png"
			self_public_id = user_stats.public_id
			self_global_atk_save = user_stats.global_atk_save
			self_global_hp_save = user_stats.global_hp_save
			resultSimilar = similar(self_ingame_name.lower(),str(ingame_name_cookie).lower())
			rank = user_liste.index(user_stats) + 1
			if resultSimilar >= 0.65:
				show_table = "yes"
			elif resultSimilar >= 0.65:
				show_table = "no_show"
			else:
				show_table = "visitor"
				try_access = True
				send_webhook(f"{str(ingame_name_cookie).lower()} tried to acces {self_ingame_name.lower()} and the similitude was at {similar(self_ingame_name.lower(),str(ingame_name_cookie).lower())}")
	except:
		show_table = "no_profile"
		self_ingame_hero = "unknown"
	number_user = len(user_liste)
	notuserlist = ['0-000001','0-000002','0-000003','0-000004'] ## pas besoin de mettre le user_init, il a déjà moins de 2800 atk
	notuserlist.extend(user.objects.filter(global_atk_save__lt=2800).values_list('ingame_id', flat=True))
	for i in notuserlist:
		profile = user.objects.get(ingame_id=i)
		user_liste.remove(profile)
	return render(request,"calculator/index.html",{
		"listALL": user_liste,
		"self_ingame_name":self_ingame_name,
		"self_global_atk_save":self_global_atk_save,
		"self_global_hp_save":self_global_hp_save,
		"self_public_id":self_public_id,
		"self_ingame_hero": avatar_src,
		"show_table": show_table,
		"rank": rank,
		"darkmode": darkmode,
		"header_msg": "Stats Calculator",
		"lang":lang,
		"number_user":number_user,
		"try_access":try_access,
		"ingame_name_cookie":ingame_name_cookie,
		"sidebarContent":SidebarContent,
		"cookieUsername":makeCookieheader(user_credential)
	})

@login_required
def formulaire_calc(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	user_credential = request.session['user_credential']
	darkmode = checkTheme_Request(request,user_credential)
	cookie_request_id = list(user_credential.values())[0]
	cookie_request_name = list(user_credential.keys())[0]
	try:
		profile = user.objects.get(ingame_id=cookie_request_id)
	except:
		profile = False
	if request.method == "POST" or profile != False:
		messages.info(request, f"{profile.ingame_name}'s Profile already exists")
		return HttpResponseRedirect("/calculator/index/", {"darkmode": darkmode,"header_msg":"Stats Calculator","lang":lang,"sidebarContent":SidebarContent})
	else :
		form_User = User()
		form_StuffTable = StuffTable()
		form_HeroTable = HeroTable()
		form_TalentTable = TalentTable()
		form_SkinTable = SkinTable()
		form_AltarTable = AltarTable()
		form_JewelTypeTable = JewelTypeTable()
		form_JewelLevelTable = JewelLevelTable()
		form_EggTable = EggTable()
		form_EggEquippedTable = EggEquippedTable()
		form_DragonTable = DragonTable()
		form_RunesTable = RunesTable()
		form_ReforgeTable = ReforgeTable()
		form_RefineTable = RefineTable()
		form_MedalTable = MedalsTable()
		form_RelicsTable = RelicsTable()
		form_WeaponSkinTable = WeaponSkinTable()
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
			"darkmode": darkmode,
			"header_msg": "Create Profile",
			"lang":lang,
			"pk_id":user_init.pk,
			"sidebarContent":SidebarContent,
			"cookieUsername":makeCookieheader(user_credential)
		}
	return render(request,"calculator/formulaire.html",ctx)

@login_required
def traitement_calc(request):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	user_credential = request.session['user_credential']
	darkmode = checkTheme_Request(request,user_credential)
	form_User = User(request.POST)
	form_StuffTable = StuffTable(request.POST)
	form_HeroTable = HeroTable(request.POST)
	form_TalentTable = TalentTable(request.POST)
	form_SkinTable = SkinTable(request.POST)
	form_AltarTable = AltarTable(request.POST)
	form_JewelTypeTable = JewelTypeTable(request.POST)
	form_JewelLevelTable = JewelLevelTable(request.POST)
	form_EggTable = EggTable(request.POST)
	form_EggEquippedTable = EggEquippedTable(request.POST)
	form_DragonTable = DragonTable(request.POST)
	form_RunesTable = RunesTable(request.POST)
	form_ReforgeTable = ReforgeTable(request.POST)
	form_RefineTable = RefineTable(request.POST)
	form_MedalTable = MedalsTable(request.POST)
	form_RelicsTable = RelicsTable(request.POST)
	form_WeaponSkinTable = WeaponSkinTable(request.POST)
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
		send_embed("Submit profile",f"{stats_User.ingame_name} | {stats_User.ingame_id}","",f"https://stats.wiki-archero.com/luhcaran/calculator/user/{stats_User.id}/change/\n[Profile](https://stats.wiki-archero.com/calculator/show/{stats_User.public_id}/) Stats : {stats_User.global_atk_save} | {stats_User.global_hp_save}","","A200FF", request,False)
		return HttpResponseRedirect(f"/stats/calc/{pbid_for_url}/0/")
	else:
		form_User = User(request.POST)
		form_StuffTable = StuffTable(request.POST)
		form_HeroTable = HeroTable(request.POST)
		form_TalentTable = TalentTable(request.POST)
		form_SkinTable = SkinTable(request.POST)
		form_AltarTable = AltarTable(request.POST)
		form_JewelTypeTable = JewelTypeTable(request.POST)
		form_JewelLevelTable = JewelLevelTable(request.POST)
		form_EggTable = EggTable(request.POST)
		form_EggEquippedTable = EggEquippedTable(request.POST)
		form_DragonTable = DragonTable(request.POST)
		form_RunesTable = RunesTable(request.POST)
		form_ReforgeTable = ReforgeTable(request.POST)
		form_RefineTable = RefineTable(request.POST)
		form_MedalTable = MedalsTable(request.POST)
		form_RelicsTable = RelicsTable(request.POST)
		form_WeaponSkinTable = WeaponSkinTable(request.POST)
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
			'form_WeaponSkinTable' :form_WeaponSkinTable,'darkmode': darkmode, 'header_msg': 'Create Profile','lang':lang, "public_id":pbid,"cookie_request_id":ingame_id,
			"cookie_request_name":ingame_name,"pk_id":pk_id,"sidebarContent":SidebarContent,"cookieUsername":makeCookieheader(user_credential)})

@login_required
def update_calc(request, pbid):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	user_credential = request.session['user_credential']
	darkmode = checkTheme_Request(request,user_credential)
	try:
		user_stats = user.objects.get(public_id=pbid)
	except:
		return HttpResponseRedirect("/")
	user_id = user_stats.ingame_id
	stuff_table_stats = stuff_table.objects.get(user_profile=user_stats)
	hero_table_stats = hero_table.objects.get(user_profile=user_stats)
	talent_table_stats = talent_table.objects.get(user_profile=user_stats)
	skin_table_stats = skin_table.objects.get(user_profile=user_stats)
	altar_table_stats = altar_table.objects.get(user_profile=user_stats)
	jewel_type_table_stats = jewel_type_table.objects.get(user_profile=user_stats)
	jewel_level_table_stats = jewel_level_table.objects.get(user_profile=user_stats)
	egg_table_stats = egg_table.objects.get(user_profile=user_stats)
	egg_equipped_table_stats = egg_equipped_table.objects.get(user_profile=user_stats)
	dragon_table_stats = dragon_table.objects.get(user_profile=user_stats)
	runes_table_stats = runes_table.objects.get(user_profile=user_stats)
	reforge_table_stats = reforge_table.objects.get(user_profile=user_stats)
	refine_table_stats = refine_table.objects.get(user_profile=user_stats)
	medal_table_stats = medals_table.objects.get(user_profile=user_stats)
	relics_table_stats = relics_table.objects.get(user_profile=user_stats)
	weapon_skins_table_stats = weapon_skins_table.objects.get(user_profile=user_stats)
	user_name = user_stats.ingame_name.lower()
	ingame_name_cookie = list(user_credential.keys())[0]
	ingame_id_cookie = list(user_credential.values())[0]
	if request.method == "GET" and similar(user_name,str(ingame_name_cookie).lower()) >= 0.65 and ingame_id_cookie == user_id:
		username_unlowered = user_stats.ingame_name
		public_id = user_stats.public_id
		form_User = User(user_stats.dictionnaire())
		form_StuffTable = StuffTable(stuff_table_stats.dictionnaire())
		form_HeroTable = HeroTable(hero_table_stats.dictionnaire())
		form_TalentTable = TalentTable(talent_table_stats.dictionnaire())
		form_SkinTable = SkinTable(skin_table_stats.dictionnaire())
		form_AltarTable = AltarTable(altar_table_stats.dictionnaire())
		form_JewelTypeTable = JewelTypeTable(jewel_type_table_stats.dictionnaire())
		form_JewelLevelTable = JewelLevelTable(jewel_level_table_stats.dictionnaire())
		form_EggTable = EggTable(egg_table_stats.dictionnaire())
		form_EggEquippedTable = EggEquippedTable(egg_equipped_table_stats.dictionnaire())
		form_DragonTable = DragonTable(dragon_table_stats.dictionnaire())
		form_RunesTable = RunesTable(runes_table_stats.dictionnaire())
		form_ReforgeTable = ReforgeTable(reforge_table_stats.dictionnaire())
		form_RefineTable = RefineTable(refine_table_stats.dictionnaire())
		form_MedalTable = MedalsTable(medal_table_stats.dictionnaire())
		form_RelicsTable = RelicsTable(relics_table_stats.dictionnaire())
		form_WeaponSkinTable = WeaponSkinTable(weapon_skins_table_stats.dictionnaire())
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
			"ingame_name": username_unlowered,
			"pk_id": user_stats.pk,
			"id_token": pbid,
			"form_dragon_1": dragon_table_stats.dragon1_type,
			"form_dragon_2": dragon_table_stats.dragon2_type,
			"form_dragon_3": dragon_table_stats.dragon3_type,
			"darkmode": darkmode,
			"header_msg": "Stats Calculator",
			"lang":lang,
			"sidebarContent":SidebarContent,
			"cookieUsername":makeCookieheader(user_credential)
		}
		return render(request,'calculator/formulaire.html',ctx)
	else:
		return HttpResponseRedirect("/calculator/index/")

@login_required
def updatetraitement_calc(request, pbid):
	with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
		local_data = json.load(f)
	SidebarContent = local_data['SidebarContent']
	user_ingame_id = user.objects.get(public_id=pbid)
	stuff_table_stats = stuff_table.objects.get(user_profile=user_ingame_id)
	hero_table_stats = hero_table.objects.get(user_profile=user_ingame_id)
	talent_table_stats = talent_table.objects.get(user_profile=user_ingame_id)
	skin_table_stats = skin_table.objects.get(user_profile=user_ingame_id)
	altar_table_stats = altar_table.objects.get(user_profile=user_ingame_id)
	jewel_type_table_stats = jewel_type_table.objects.get(user_profile=user_ingame_id)
	jewel_level_table_stats = jewel_level_table.objects.get(user_profile=user_ingame_id)
	egg_table_stats = egg_table.objects.get(user_profile=user_ingame_id)
	egg_equipped_table_stats = egg_equipped_table.objects.get(user_profile=user_ingame_id)
	dragon_table_stats = dragon_table.objects.get(user_profile=user_ingame_id)
	runes_table_stats = runes_table.objects.get(user_profile=user_ingame_id)
	reforge_table_stats = reforge_table.objects.get(user_profile=user_ingame_id)
	refine_table_stats = refine_table.objects.get(user_profile=user_ingame_id)
	medal_table_stats = medals_table.objects.get(user_profile=user_ingame_id)
	relics_table_stats = relics_table.objects.get(user_profile=user_ingame_id)
	weapon_skins_table_stats = weapon_skins_table.objects.get(user_profile=user_ingame_id)
	user_credential = request.session['user_credential']
	darkmode = checkTheme_Request(request,user_credential)
	form_User = User(request.POST,instance=user_ingame_id)
	form_StuffTable = StuffTable(request.POST,instance=stuff_table_stats)
	form_HeroTable = HeroTable(request.POST,instance=hero_table_stats)
	form_TalentTable = TalentTable(request.POST,instance=talent_table_stats)
	form_SkinTable = SkinTable(request.POST,instance=skin_table_stats)
	form_AltarTable = AltarTable(request.POST,instance=altar_table_stats)
	form_JewelTypeTable = JewelTypeTable(request.POST,instance=jewel_type_table_stats)
	form_JewelLevelTable = JewelLevelTable(request.POST,instance=jewel_level_table_stats)
	form_EggTable = EggTable(request.POST,instance=egg_table_stats)
	form_EggEquippedTable = EggEquippedTable(request.POST,instance=egg_equipped_table_stats)
	form_DragonTable = DragonTable(request.POST,instance=dragon_table_stats)
	form_RunesTable = RunesTable(request.POST,instance=runes_table_stats)
	form_ReforgeTable = ReforgeTable(request.POST,instance=reforge_table_stats)
	form_RefineTable = RefineTable(request.POST,instance=refine_table_stats)
	form_MedalTable = MedalsTable(request.POST,instance=medal_table_stats)
	form_RelicsTable = RelicsTable(request.POST,instance=relics_table_stats)
	form_WeaponSkinTable = WeaponSkinTable(request.POST,instance=weapon_skins_table_stats)
	form_validation = all_formIsValid(form_User.is_valid(),form_StuffTable.is_valid(),form_HeroTable.is_valid(),form_TalentTable.is_valid(),form_SkinTable.is_valid(),form_AltarTable.is_valid(),form_JewelTypeTable.is_valid(),form_JewelLevelTable.is_valid(),form_EggTable.is_valid(),form_EggEquippedTable.is_valid(),form_DragonTable.is_valid(),form_RunesTable.is_valid(),form_ReforgeTable.is_valid(),form_RefineTable.is_valid(), form_MedalTable.is_valid(), form_RelicsTable.is_valid(), form_WeaponSkinTable.is_valid())

	list_user = list(user.objects.all())
	list_user_ingame_id = []

	for i in list_user:
		iingame_id = i.ingame_id
		if iingame_id != user_ingame_id.ingame_id:
			user_id = iingame_id
			list_user_ingame_id.append(user_id)

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
		if stats_User.public_id != user_ingame_id.public_id:
			stats_User.public_id = user_ingame_id.public_id
		if stats_User.ingame_id != user_ingame_id.ingame_id:
			stats_User.ingame_id = user_ingame_id.ingame_id
		if stats_User.ingame_name != user_ingame_id.ingame_name:
			stats_User.ingame_name = user_ingame_id.ingame_name
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
		send_embed("Update profile",f"{stats_User.ingame_name} | {stats_User.ingame_id}","",f"https://stats.wiki-archero.com/luhcaran/calculator/user/{stats_User.id}/change/\n[Profile](https://stats.wiki-archero.com/calculator/show/{stats_User.public_id}/) Stats : {stats_User.global_atk_save} | {stats_User.global_hp_save}","","0096f9", request,False)
		return HttpResponseRedirect(f"/stats/calc/{user_ingame_id.public_id}/0/")
	else:
		form_User = User(request.POST)
		form_StuffTable = StuffTable(request.POST)
		form_HeroTable = HeroTable(request.POST)
		form_TalentTable = TalentTable(request.POST)
		form_SkinTable = SkinTable(request.POST)
		form_AltarTable = AltarTable(request.POST)
		form_JewelTypeTable = JewelTypeTable(request.POST)
		form_JewelLevelTable = JewelLevelTable(request.POST)
		form_EggTable = EggTable(request.POST)
		form_EggEquippedTable = EggEquippedTable(request.POST)
		form_DragonTable = DragonTable(request.POST)
		form_RunesTable = RunesTable(request.POST)
		form_ReforgeTable = ReforgeTable(request.POST)
		form_RefineTable = RefineTable(request.POST)
		form_MedalTable = MedalsTable(request.POST)
		form_RelicsTable = RelicsTable(request.POST)
		form_WeaponSkinTable = WeaponSkinTable(request.POST)
		form_error = findFormError(form_User, form_StuffTable, form_HeroTable, form_TalentTable, form_SkinTable, form_AltarTable, form_JewelTypeTable, form_JewelLevelTable, form_EggTable, form_EggEquippedTable, form_DragonTable, form_RunesTable, form_ReforgeTable, form_RefineTable, form_MedalTable, form_RelicsTable, form_WeaponSkinTable)
		value_error_msg = (str(form_error).split("'")[1].replace("_"," ") + ": " + str(form_error).split("'")[3]).title()
		ctx = {
			"ingame_id":user_ingame_id.ingame_id,
			"public_id":user_ingame_id.public_id,
			"ingame_name": user_ingame_id.ingame_name,
			"pk_id": user_ingame_id.pk,
			"form_dragon_1": dragon_table_stats.dragon1_type,
			"form_dragon_2": dragon_table_stats.dragon2_type,
			"form_dragon_3": dragon_table_stats.dragon3_type,
			'form_User': form_User,'form_StuffTable': form_StuffTable,
			'form_HeroTable' :form_HeroTable,'form_TalentTable' :form_TalentTable,'form_SkinTable' :form_SkinTable,'form_AltarTable' :form_AltarTable,
			'form_JewelTypeTable' :form_JewelTypeTable,'form_JewelLevelTable' :form_JewelLevelTable,'form_EggTable' :form_EggTable,
			'form_EggEquippedTable' :form_EggEquippedTable,'form_DragonTable' :form_DragonTable,'form_RunesTable' :form_RunesTable,
			'form_ReforgeTable' :form_ReforgeTable,'form_RefineTable' :form_RefineTable,"form_MedalTable":form_MedalTable,"form_RelicsTable":form_RelicsTable,
			"form_WeaponSkinTable":form_WeaponSkinTable,"id_token": pbid, "value_error": value_error_msg,"darkmode": darkmode,
			"header_msg": "Stats Calculator", "lang":lang,"sidebarContent":SidebarContent,"cookieUsername":makeCookieheader(user_credential)
		}
		return render(request,"calculator/formulaire.html",ctx)

def delete_user(request, pbid):
	user = user.objects.get(public_id=pbid)
	if request.user.is_superuser:
		user.delete()
		try:
			os.remove(f"calculator/static/image/stuff_save/stuff_{user.ingame_name}.png")
		except:
			pass
	else:
		cookie_value = checkCookie(request.COOKIES)
		try:
			ingame_name_cookie = list(cookie_value.keys())[0]
		except:
			ingame_name_cookie = "unknown"
		send_embed(ingame_name_cookie,user.ingame_name,f"{ingame_name_cookie} tried to delete {user.ingame_name}'s profile","","",'FF0000',request,True)
	return HttpResponseRedirect(f"/calculator/index")



def damage_calc(request, pbid):
	# one page request POST form
	return HttpResponseRedirect(f"/calculator/index")

def admin_reload_stats(request,pbid):
	os.remove(f"calculator/static/image/stuff_save/{pbid}.png")
	return HttpResponseRedirect(f"/calculator/show/{pbid}/")