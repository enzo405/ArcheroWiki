from django.forms import ModelForm, widgets
from .models import UserQueue,user,StuffTable,HeroTable,TalentTable,SkinTable,AltarTable,JewelTypeTable,JewelLevelTable,EggTable,EggEquippedTable,DragonTable,RunesTable,ReforgeTable,RefineTable,MedalsTable,RelicsTable,WeaponSkinsTable
from django import forms



class UserForm(ModelForm):
	class Meta:
		model = user
		fields = (
				'ingame_id',
				'ingame_name',
				'choosen_hero',
				'brave_privileges_level',
				'atk_base_stats_hero_choosen',
				'health_base_stats_hero_choosen',
				'public_id'
)



class StuffForm(ModelForm):
	class Meta:
		model = StuffTable
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


class HeroForm(ModelForm):
	class Meta:
		model = HeroTable
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
				'taiga_level', 'taiga_star',
)


class TalentForm(ModelForm):
	class Meta:
		model = TalentTable
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

class SkinForm(ModelForm):
	class Meta:
		model = SkinTable
		fields = (
				'user_profile',
				'skin_health',
				'skin_attack',
)



class AltarForm(ModelForm):
	class Meta:
		model = AltarTable
		fields = (
				'user_profile',
				'stuff_altar_level', 
				'stuff_altar_ascension', 
				'heros_altar_level', 
				'heros_altar_ascension',
)


class JewelTypeForm(ModelForm):
	class Meta:
		model = JewelTypeTable
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


class JewelLevelForm(ModelForm):
	class Meta:
		model = JewelLevelTable
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


class EggForm(ModelForm):
	class Meta:
		model = EggTable
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


class EggEquippedForm(ModelForm):
	class Meta:
		model = EggEquippedTable
		fields = (
				'user_profile',
				'egg_equipped1',
				'egg_equipped2',
				'egg_equipped3',
				'egg_equipped4',
				'egg_equipped5',
)

class DragonForm(ModelForm):
	class Meta:
		model = DragonTable
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


class RunesForm(ModelForm):
	class Meta:
		model = RunesTable
		fields = (
				"user_profile",
				"power_line_1",
				"power_line_2",
				"power_line_3",
				"power_line_4",
				"power_line_5",
				"saviour_line_1",
				"saviour_line_2",
				"saviour_line_3",
				"saviour_line_4",
				"saviour_line_5",
				"recovery_line_1",
				"recovery_line_2",
				"recovery_line_3",
				"recovery_line_4",
				"recovery_line_5",
				"courage_line_1",
				"courage_line_2",
				"courage_line_3",
				"courage_line_4",
				"courage_line_5",
				"luck_line_1",
				"luck_line_2",
				"luck_line_3",
				"luck_line_4",
				"luck_line_5",
				"value_power_line_1",
				"value_power_line_2",
				"value_power_line_3",
				"value_power_line_4",
				"value_power_line_5",
				"value_saviour_line_1",
				"value_saviour_line_2",
				"value_saviour_line_3",
				"value_saviour_line_4",
				"value_saviour_line_5",
				"value_recovery_line_1",
				"value_recovery_line_2",
				"value_recovery_line_3",
				"value_recovery_line_4",
				"value_recovery_line_5",
				"value_courage_line_1",
				"value_courage_line_2",
				"value_courage_line_3",
				"value_courage_line_4",
				"value_courage_line_5",
				"value_luck_line_1",
				"value_luck_line_2",
				"value_luck_line_3",
				"value_luck_line_4",
				"value_luck_line_5",
)


class ReforgeForm(ModelForm):
	class Meta:
		model = ReforgeTable
		fields = (
				"user_profile",
				'reforge_power',
				'reforge_saviour',
				'reforge_recovery',
				'reforge_courage',
				'reforge_luck',
		)


class RefineForm(ModelForm):
	class Meta:
		model = RefineTable
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


class MedalsForm(ModelForm):
	class Meta:
		model = MedalsTable
		fields = (
				'user_profile','medals_1001','medals_1002','medals_1003','medals_1004',
				'medals_1005','medals_1006','medals_1008','medals_1009','medals_1010',
				'medals_1011','medals_1012','medals_2001','medals_2002','medals_2003',
				'medals_2004','medals_2005','medals_2006','medals_2007','medals_2008',
				'medals_2009','medals_2010','medals_2011','medals_2012','medals_2013',
				'medals_2014','medals_3001','medals_3002','medals_3003','medals_3004',
				'medals_3005','medals_3006','medals_3007','medals_3008','medals_3009',
				'medals_3010','medals_3019','medals_3020','medals_3021','medals_3022',
				'medals_3023','medals_3024','medals_3025','medals_3026','medals_3027',
				'medals_3028','medals_3029','medals_3030','medals_3034','medals_3035',
				'medals_3036',
)



class RelicsForm(ModelForm):
	class Meta:
		model = RelicsTable
		fields = (
				"user_profile",
				"wraith_mask_level","wraith_mask_star","wraith_mask_effective", 
				"clown_mask_level","clown_mask_star","clown_mask_effective",
				"princess_teddy_bear_level","princess_teddy_bear_star","princess_teddy_bear_effective",
				"belt_of_might_level","belt_of_might_star","belt_of_might_effective",
				"beastmaster_whistle_level","beastmaster_whistle_star","beastmaster_whistle_effective",
				"archmage_robe_level","archmage_robe_star","archmage_robe_effective",
				"shimmering_gem_level","shimmering_gem_star",
				"bloom_of_eternity_level","bloom_of_eternity_star","bloom_of_eternity_effective",
				"challenger_headband_level","challenger_headband_star",
				"jade_gobelet_level","jade_gobelet_star","jade_gobelet_effective",
				"veteran_plate_level","veteran_plate_star",
				"dragonscale_level","dragonscale_star","dragonscale_effective",
				"dragon_tooth_level","dragon_tooth_star","dragon_tooth_effective",
				"scholar_telescope_level","scholar_telescope_star",
				"pirate_shank_level","pirate_shank_star",
				"giant_greatsword_level","giant_greatsword_star","giant_greatsword_effective",
				"healing_potion_level","healing_potion_star",
				"whirlwind_mauler_level","whirlwind_mauler_star","whirlwind_mauler_effective",
				"special_lance_level","special_lance_star","special_lance_effective",
				"precision_slingshot_level","precision_slingshot_star",
				"maidens_pearl_earring_level","maidens_pearl_earring_star",
				"ancient_shield_level","ancient_shield_star","ancient_shield_effective",
				"supreme_trinity_alpha_level","supreme_trinity_alpha_star","supreme_trinity_alpha_effective",
				"golden_apple_level","golden_apple_star","golden_apple_effective",
				"ancient_stele_level","ancient_stele_star","ancient_stele_effective",
				"philosopher_stone_level","philosopher_stone_star","philosopher_stone_effective",
				"dragon_heart_level","dragon_heart_star","dragon_heart_effective",
				"spectral_duality_level","spectral_duality_star","spectral_duality_effective",
				"mystic_emblem_level","mystic_emblem_star",
				"immortal_brooch_level","immortal_brooch_star",
				"golden_statue_level","golden_statue_star","golden_statue_effective",
				"smilling_mask_level","smilling_mask_star",
				"unmerciful_mask_level","unmerciful_mask_star","unmerciful_mask_effective",
				"holy_water_level","holy_water_star","holy_water_effective",
				"book_of_the_dead_level","book_of_the_dead_star","book_of_the_dead_effective",
				"psionist_treasure_level","psionist_treasure_star",
				"book_of_archery_level","book_of_archery_star","book_of_archery_effective",
				"book_of_bravery_level","book_of_bravery_star","book_of_bravery_effective",
				"angelic_heart_level","angelic_heart_star","angelic_heart_effective",
				"devil_whisper_level","devil_whisper_star","devil_whisper_effective",
				"stone_of_wisdom_level","stone_of_wisdom_star",
				"empyrean_mirror_level","empyrean_mirror_star","empyrean_mirror_effective",
				"fabled_archer_arrow_level","fabled_archer_arrow_star","fabled_archer_arrow_effective",
				"shiny_gemmed_belt_level","shiny_gemmed_belt_star",
				"mythril_flux_mail_level","mythril_flux_mail_star","mythril_flux_mail_effective",
				"stealth_boots_level","stealth_boots_star","stealth_boots_effective",
				"assassin_dagger_level","assassin_dagger_star","assassin_dagger_effective",
				"gold_bunny_level","gold_bunny_star",
				"lucky_coin_level","lucky_coin_star",
				"dusken_cask_level","dusken_cask_star",
				"dragon_eye_level","dragon_eye_star","dragon_eye_effective",
				"ring_of_greed_level","ring_of_greed_star",
				"genesis_staff_level","genesis_staff_star",
				"bloodstained_sword_level","bloodstained_sword_star","bloodstained_sword_effective",
				"starcluster_rage_level","starcluster_rage_star","starcluster_rage_effective",
				"elven_king_cape_level","elven_king_cape_star","elven_king_cape_effective",
				"spear_of_yggdrasil_level","spear_of_yggdrasil_star","spear_of_yggdrasil_effective",
				"dragon_gem_level","dragon_gem_star","dragon_gem_effective",
				"life_crown_level","life_crown_star","life_crown_effective",
				"sand_of_time_level","sand_of_time_star","sand_of_time_effective",
				"first_lightning_level","first_lightning_star",
				"oracle_quill_level","oracle_quill_star","oracle_quill_effective",
				"bloodthirsty_grail_level","bloodthirsty_grail_star","bloodthirsty_grail_effective",
				"healing_grail_level","healing_grail_star","healing_grail_effective",
				"cupids_necklace_level","cupids_necklace_star",
				"life_staff_level","life_staff_star","life_staff_effective",
				"light_grail_level","light_grail_star",
				"primal_fire_level","primal_fire_star","primal_fire_effective"
)



class WeaponSkinForm(ModelForm):
	class Meta:
		model = WeaponSkinsTable
		fields = (
				"user_profile",
				"demon_blade_rain_1",
				"demon_blade_rain_2",
				"antiquated_sword_1",
				"antiquated_sword_2",
				"gale_force_1",
				"gale_force_2",
				"death_scythe_1",
				"death_scythe_2",
				"boomerang_1",
				"boomerang_2",
				"brightspear_1",
				"brightspear_2",
				"saw_blade_1",
				"saw_blade_2",
				"brave_bow_1",
				"brave_bow_2",
				"stalker_staff_1",
				"stalker_staff_2"
		)


RUNE_CHOICES = [('power', 'Power'), ('courage', 'Courage')]
class DamageCalculatorForm(forms.Form):
	runes = forms.ChoiceField(choices=RUNE_CHOICES, widget=forms.RadioSelect)
	firstInput = forms.DecimalField(max_digits=6, decimal_places=2)
	secondInput = forms.DecimalField(max_digits=6, decimal_places=2)
	thirdInput = forms.DecimalField(max_digits=6, decimal_places=2)
	fourthInput = forms.DecimalField(max_digits=6, decimal_places=2)
	fifthInput = forms.DecimalField(max_digits=6, decimal_places=2)


class UserQueueForm(forms.ModelForm):
    class Meta:
        model = UserQueue
        fields = ['username', 'email', 'password']