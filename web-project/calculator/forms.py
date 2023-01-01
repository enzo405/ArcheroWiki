from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
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
)



class StuffTable(ModelForm):
	class Meta:
		model = models.stuff_table
		fields = (
				'ingame_id',
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
				'ingame_id',
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
)


class TalentTable(ModelForm):
	class Meta:
		model = models.talent_table
		fields = (
				'ingame_id',
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
				'ingame_id',
				'skin_health',
				'skin_attack',
)



class AltarTable(ModelForm):
	class Meta:
		model = models.altar_table
		fields = (
				'ingame_id',
				'stuff_altar_level', 
				'stuff_altar_ascension', 
				'heros_altar_level', 
				'heros_altar_ascension',
)


class JewelTypeTable(ModelForm):
	class Meta:
		model = models.jewel_type_table
		fields = (
				'ingame_id',
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
				'ingame_id',
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
				'ingame_id',
				'green_bat','vase','bomb_ghost','rock_puppet',
				'party_tree','wolfhound','skeleton_archer','skeleton_soldier',
				'wasp','fire_mage','medusa','ice_mage','fire_lizard',
				'flame_ghost','thorny_snake','tornado_demon','piranha',
				'zombie','scarecrow','long_dragon','skull_wizard','lava_golem','ice_golem',
				'cactus','crazy_spider','fire_element','skeleton_swordsman','scythe_mage',
				'pea_shooter','shadow_assassin','tornado_mage','spitting_mushroom',
				'rolling_mushroom','fallen_bat','one_eyed_bat','scarlet_mage',
				'icefire_phantom','purple_phantom','tundra_dragon','sandian',
				'nether_puppet','psionic_scarecrow','steel_dryad','savage_spider',
				'flaming_bug','elite_archer','little_dragon','arch_leader',
				'skeleton_king','crimson_witch','rage_golem','queen_bee',
				'ice_worm','medusa_boss','ice_demon','giant_owl',
				'fire_demon','krab_boss','desert_goliath',
)


class EggEquippedTable(ModelForm):
	class Meta:
		model = models.egg_equipped_table
		fields = (
				'ingame_id',
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
				'ingame_id',
				'dragon1_type',
				'dragon2_type',
				'dragon3_type',
				'dragon1_rarity',
				'dragon2_rarity',
				'dragon3_rarity',
				'dragon1_level',
				'dragon2_level',
				'dragon3_level',
				'dragon_1_boost_4_mythic',
				'dragon_2_boost_4_mythic',
				'dragon_3_boost_4_mythic',
)


class RunesTable(ModelForm):
	class Meta:
		model = models.runes_table
		fields = (
				'ingame_id',
				'power_attack_flat',
				'power_attack_var',
				'saviour_hp_flat',
				'saviour_hp_var',
				'recovery_hp_flat',
				'courage_attack_flat',
				'courage_attack_var',
				'courage_hero_attack_flat',
				'courage_hero_attack_var',
				'courage_hero_hp_flat',
				'courage_hero_hp_var',
				'luck_hp_flat',
				'luck_hp_var',
				'selected_hero_courage_attack_flat',
				'selected_hero_courage_attack_var',
				'selected_hero_courage_hp_flat',
				'selected_hero_courage_hp_var',
)


class ReforgeTable(ModelForm):
	class Meta:
		model = models.reforge_table
		fields = (
				"ingame_id",
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
				'ingame_id',
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