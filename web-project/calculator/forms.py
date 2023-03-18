from django.forms import ModelForm
from . import models



class User(ModelForm):
	class Meta:
		model = models.user
		fields = (
				'ingame_id',
				'ingame_name',
				'choosen_hero',
				'brave_privileges_level',
				'atk_base_stats_hero_choosen',
				'health_base_stats_hero_choosen',
				'public_id'
)



class StuffTable(ModelForm):
	class Meta:
		model = models.stuff_table
		fields = (
				'user_profile',
				"weapon_choosen","weapon_level" ,"weapon_rarity" ,
				"armor_choosen","armor_level" ,"armor_rarity" ,
				"ring1_choosen","ring1_level" ,"ring1_rarity" ,
				"ring2_choosen","ring2_level" ,"ring2_rarity" ,
				"pet1_choosen","pet1_level" ,"pet1_rarity" ,
				"pet2_choosen","pet2_level" ,"pet2_rarity" ,
				"bracelet_choosen","bracelet_level" ,"bracelet_rarity" ,
				"locket_choosen","locket_level" ,"locket_rarity" ,
				"book_choosen","book_level" ,"book_rarity" ,
		)


class HeroTable(ModelForm):
	class Meta:
		model = models.hero_table
		fields = (
				'user_profile',
				'atreus_level', 'atreus_star', 
				'urasil_level', 'urasil_star',
				'phoren_level', 'phoren_star',
				'taranis_level', 'taranis_star',
				'helix_level', 'helix_star', 
				'meowgik_level', 'meowgik_star',
				'shari_level', 'shari_star',
				'ayana_level', 'ayana_star',
				'onir_level', 'onir_star', 
				'rolla_level', 'rolla_star',
				'bonnie_level', 'bonnie_star',
				'sylvan_level', 'sylvan_star',
				'shade_level', 'shade_star', 
				'ophelia_level', 'ophelia_star',
				'ryan_level', 'ryan_star',
				'lina_level', 'lina_star',
				'aquea_level', 'aquea_star',
				'shingen_level', 'shingen_star', 
				'gugu_level', 'gugu_star',
				'iris_level', 'iris_star',
				'blazo_level', 'blazo_star',
				'melinda_level', 'melinda_star',
				'elaine_level', 'elaine_star',
				'bobo_level', 'bobo_star',
				'stella_level', 'stella_star',
)


class TalentTable(ModelForm):
	class Meta:
		model = models.talent_table
		fields = (
				'user_profile',
				'strength_level',
				'power_level',
				'recover_level',
				'block_level',
				'iron_bulwark_level',
				'enhanced_equipment_level',
				'hero_power_up_level',
				'runes_power_up_level',
)

class SkinTable(ModelForm):
	class Meta:
		model = models.skin_table
		fields = (
				'user_profile',
				'skin_health',
				'skin_attack',
)



class AltarTable(ModelForm):
	class Meta:
		model = models.altar_table
		fields = (
				'user_profile',
				'stuff_altar_level', 
				'stuff_altar_ascension', 
				'heros_altar_level', 
				'heros_altar_ascension',
)


class JewelTypeTable(ModelForm):
	class Meta:
		model = models.jewel_type_table
		fields = (
				'user_profile',
				'weapon_jewel1_type','weapon_jewel2_type','weapon_jewel3_type','weapon_jewel4_type',
				'armor_jewel1_type','armor_jewel2_type','armor_jewel3_type','armor_jewel4_type',
				'ring1_jewel1_type','ring1_jewel2_type','ring1_jewel3_type','ring1_jewel4_type', 
				'ring2_jewel1_type','ring2_jewel2_type','ring2_jewel3_type','ring2_jewel4_type', 
				'pet1_jewel1_type','pet1_jewel2_type','pet1_jewel3_type','pet1_jewel4_type',
				'pet2_jewel1_type','pet2_jewel2_type','pet2_jewel3_type','pet2_jewel4_type',
				'bracelet_jewel1_type','bracelet_jewel2_type','bracelet_jewel3_type','bracelet_jewel4_type',
				'locket_jewel1_type','locket_jewel2_type','locket_jewel3_type','locket_jewel4_type',
				'book_jewel1_type','book_jewel2_type','book_jewel3_type','book_jewel4_type',
)


class JewelLevelTable(ModelForm):
	class Meta:
		model = models.jewel_level_table
		fields = (
				'user_profile',
				'weapon_jewel1_level','weapon_jewel2_level','weapon_jewel3_level','weapon_jewel4_level',
				'armor_jewel1_level','armor_jewel2_level','armor_jewel3_level','armor_jewel4_level',
				'ring1_jewel1_level','ring1_jewel2_level','ring1_jewel3_level','ring1_jewel4_level',
				'ring2_jewel1_level','ring2_jewel2_level','ring2_jewel3_level','ring2_jewel4_level',
				'pet1_jewel1_level','pet1_jewel2_level','pet1_jewel3_level','pet1_jewel4_level',
				'pet2_jewel1_level','pet2_jewel2_level','pet2_jewel3_level','pet2_jewel4_level',
				'bracelet_jewel1_level','bracelet_jewel2_level','bracelet_jewel3_level','bracelet_jewel4_level',
				'locket_jewel1_level','locket_jewel2_level','locket_jewel3_level','locket_jewel4_level',
				'book_jewel1_level','book_jewel2_level','book_jewel3_level','book_jewel4_level',
)


class EggTable(ModelForm):
	class Meta:
		model = models.egg_table
		fields = (
				'user_profile','green_bat','vase','bomb_ghost','rock_puppet','party_tree','wolfhound',
				'skeleton_archer','skeleton_soldier','wasp','fire_mage','medusa','ice_mage',
				'fire_lizard','flame_ghost','thorny_snake','tornado_demon','piranha',
				'zombie','scarecrow','long_dragon','skull_wizard','lava_golem','ice_golem',
				'cactus','crazy_spider','fire_element','skeleton_swordsman','scythe_mage',
				'pea_shooter','shadow_assassin','tornado_mage','spitting_mushroom',
				'rolling_mushroom','fallen_bat','one_eyed_bat','scarlet_mage','icefire_phantom',
				'purple_phantom','tundra_dragon','sandian','nether_puppet','psionic_scarecrow',
				'steel_dryad','savage_spider','flaming_bug','shark_bro','crimson_zombie',
				'fat_bat','plainswolf','elite_archer','little_dragon','arch_leader','skeleton_king',
				'crimson_witch','rage_golem','queen_bee','ice_worm','medusa_boss','ice_demon',
				'giant_owl','fire_demon','krab_boss','desert_goliath','sinister_touch',
				'scythe_pharoah','fireworm_queen','infernal_demon',
)


class EggEquippedTable(ModelForm):
	class Meta:
		model = models.egg_equipped_table
		fields = (
				'user_profile',
				'egg_equipped1',
				'egg_equipped2',
				'egg_equipped3',
				'egg_equipped4',
				'egg_equipped5',
)

class DragonTable(ModelForm):
	class Meta:
		model = models.dragon_table
		fields = (
				'user_profile',
				'dragon1_type',
				'dragon2_type',
				'dragon3_type',
				'dragon1_rarity',
				'dragon2_rarity',
				'dragon3_rarity',
				'dragon1_level',
				'dragon2_level',
				'dragon3_level',
				'dragon_1_boost_1',
				'dragon_1_boost_2',
				'dragon_1_boost_3',
				'dragon_1_boost_4',
				'dragon_2_boost_1',
				'dragon_2_boost_2',
				'dragon_2_boost_3',
				'dragon_2_boost_4',
				'dragon_3_boost_1',
				'dragon_3_boost_2',
				'dragon_3_boost_3',
				'dragon_3_boost_4',
)


class RunesTable(ModelForm):
	class Meta:
		model = models.runes_table
		fields = (
				"user_profile",
				"power_attack_flat", 
				"power_attack_var", 
				"power_line_2", 
				"power_line_3", 
				"power_line_4", 
				"power_line_5", 
				"saviour_hp_flat", 
				"saviour_hp_var", 
				"saviour_line_2", 
				"saviour_line_3", 
				"saviour_line_4", 
				"saviour_line_5", 
				"recovery_hp_flat", 
				"recovery_line_2", 
				"recovery_line_3", 
				"recovery_line_4", 
				"recovery_line_5", 
				"courage_attack_flat", 
				"courage_attack_var", 
				"selected_hero_courage_attack_flat",
				"courage_hero_attack_flat", 
				"selected_hero_courage_attack_var",
				"courage_hero_attack_var",
				"selected_hero_courage_hp_flat",
				"courage_hero_hp_flat", 
				"selected_hero_courage_hp_var",
				"courage_hero_hp_var",
				"courage_line_2", 
				"courage_line_3", 
				"courage_line_4", 
				"courage_line_5", 
				"luck_hp_flat", 
				"luck_hp_var", 
				"luck_line_2", 
				"luck_line_3", 
				"luck_line_4", 
				"luck_line_5",
				"value_power_line_2",
				"value_power_line_3",
				"value_power_line_4",
				"value_power_line_5",
				"value_saviour_line_2",
				"value_saviour_line_3",
				"value_saviour_line_4",
				"value_saviour_line_5",
				"value_recovery_line_2",
				"value_recovery_line_3",
				"value_recovery_line_4",
				"value_recovery_line_5",
				"value_courage_line_2",
				"value_courage_line_3",
				"value_courage_line_4",
				"value_courage_line_5",
				"value_luck_line_2",
				"value_luck_line_3",
				"value_luck_line_4",
				"value_luck_line_5",
)


class ReforgeTable(ModelForm):
	class Meta:
		model = models.reforge_table
		fields = (
				"user_profile",
				'reforge_power',
				'reforge_saviour',
				'reforge_recovery',
				'reforge_courage',
				'reforge_luck',
		)


class RefineTable(ModelForm):
	class Meta:
		model = models.refine_table
		fields = (
				'user_profile',
				'weapon_refine_atk',
				'weapon_refine_basic_stats',
				'armor_refine_hp',
				'armor_refine_basic_stats',
				'ring1_refine_atk',
				'ring1_refine_basic_stats',
				'ring2_refine_atk',
				'ring2_refine_basic_stats',
				'bracelet_refine_atk',
				'bracelet_refine_basic_stats',
				'locket_refine_hp',
				'locket_refine_basic_stats',
				'book_refine_hp',
				'book_refine_basic_stats',
)


class MedalsTable(ModelForm):
	class Meta:
		model = models.medals_table
		fields = (
				'user_profile',
				'medals_01',
				'medals_02',
				'medals_03',
				'medals_04',
				'medals_05',
				'medals_06',
				# 'medals_07',
				'medals_08',
				'medals_09',
				'medals_10',
				'medals_11',
				'medals_12',
				'medals_13',
				'medals_14',
				'medals_15',
				'medals_16',
				'medals_17',
				'medals_18',
				'medals_19',
				'medals_20',
				'medals_21',
				'medals_22',
				'medals_23',
				'medals_24',
				'medals_25',
				'medals_26',
				'medals_27',
				'medals_28',
				'medals_29',
				'medals_30',
				'medals_31',
				'medals_32'
)



class RelicsTable(ModelForm):
	class Meta:
		model = models.relics_table
		fields = (
				"user_profile","wraith_mask",
				"clown_mask","princess_teddy_bear",
				"belt_of_might","beastmaster_whistle",
				"archmage_robe","shimmering_gem",
				"bloom_of_eternity","challenger_headband",
				"jade_gobelet","veteran_plate",
				"dragonscale","dragon_tooth",
				"scholar_telescope","pirate_shank",
				"giant_greatsword","healing_potion",
				"whirlwind_mauler","special_lance",
				"precision_slingshot","supreme_trinity_alpha",
				"golden_apple","ancient_stele",
				"philosopher_stone","dragon_heart",
				"spectral_duality","mystic_emblem",
				"immortal_brooch","golden_statue",
				"smilling_mask","unmerciful_mask",
				"holy_water","book_of_the_dead",
				"psionist_treasure","book_of_archery",
				"book_of_bravery","angelic_heart",
				"devil_whisper","stone_of_wisdom",
				"empyrean_mirror","fabled_archer_arrow",
				"shiny_gemmed_belt","mythril_flux_mail",
				"stealth_boots","assassin_dagger",
				"gold_bunny","genesis_staff",
				"bloodstained_sword","starcluster_rage",
				"elven_king_cape","spear_of_yggdrasil",
				"dragon_gem","life_crown",
				"sand_of_time","first_lightning",
				"oracle_quill","bloodthirsty_grail",
				"healing_grail","cupids_necklace",
)



class WeaponSkinTable(ModelForm):
	class Meta:
		model = models.weapon_skins_table
		fields = (
				"user_profile",
				"demon_blade_rain_1",
				"antiquated_sword_1",
				"gale_force_1",
				"death_scythe_1",
				"boomerang_1",
				"brightspear_1",
				"saw_blade_1",
				"brave_bow_1",
				"stalker_staff_1"
		)