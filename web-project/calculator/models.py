from django.db import models
from django.core.validators import MaxValueValidator


all_heros = (("Atreus","Atreus"),("Urasil","Urasil"),("Phoren","Phoren"),("Taranis","Taranis"),("Helix","Helix"),("Meowgik","Meowgik"),("Shari","Shari"),("Ayana","Ayana"),("Onir","Onir"),("Rolla","Rolla"),("Bonnie","Bonnie"),("Sylvan","Sylvan"),("Shade","Shade"),("Ophelia","Ophelia"),("Ryan","Ryan"),("Lina","Lina"),("Aquea","Aquea"),("Shingen","Shingen"),("Gugu","Gugu"),("Iris","Iris"),("Blazo","Blazo"),("Melinda","Melinda"),("Elaine","Elaine"))
stuff_weapon = (("None","None"),("Brave Bow","Brave Bow"),("Death Scythe","Death Scythe"),("Saw Blade","Saw Blade"),("Tornado","Tornado"),("Brightspear","Brightspear"),("Stalker Staff","Stalker Staff"),("Gale Force","Gale Force"),("Demon Blade Rain","Demon Blade Rain"),("Mini Atreus","Mini Atreus"),("Antiquated Sword","Antiquated Sword"))
stuff_armor = (("None","None"),("Phantom Cloak","Phantom Cloak"),("Vest of Dexterity","Vest of Dexterity"),("Golden Chestplate","Golden Chestplate"),("Void Robe","Void Robe"),("Bright Robe","Bright Robe"),("Shadow Robe","Shadow Robe"))
stuff_ring = (("None","None"),("Bear Ring","Bear Ring"),("Wolf Ring","Wolf Ring"),("Falcon Ring","Falcon Ring"),("Serpent Ring","Serpent Ring"),("Bull Ring","Bull Ring"),("Lion Ring","Lion Ring"),("Vilebat Ring","Vilebat Ring"),("Dragon Ring","Dragon Ring"))
stuff_pet = (("None","None"),("Laser Bat","Laser Bat"),("Scythe Mage","Scythe Mage"),("Elf","Elf"),("Living Bomb","Living Bomb"),("Noisy Owl","Noisy Owl"),("Flaming Ghost","Flaming Ghost"),("Bone Warrior","Bone Warrior"))
stuff_bracelet = (("None","None"),("Thunder Bracelet","Thunder Bracelet"),("Frozen Bracelet","Frozen Bracelet"),("Blazing Bracelet","Blazing Bracelet"),("Split Bracelet","Split Bracelet"),("Invincible Bracelet","Invincible Bracelet"),("Quickshot Bracelet","Quickshot Bracelet"),("Shield Bracelet","Shield Bracelet"))
stuff_locket = (("None","None"),("Agile Locket","Agile Locket"),("Iron Locket","Iron Locket"),("Angel Locket","Angel Locket"),("Bulletproof Locket","Bulletproof Locket"),("Piercer Locket","Piercer Locket"),("Bloodthirsty Locket","Bloodthirsty Locket"),("Counterattack Locket","Counterattack Locket"))
stuff_book = (("None","None"),("Arcane Archer","Arcane Archer"),("Art of Combat","Art of Combat"),("Ice Realm","Ice Realm"),("Enlightenment","Enlightenment"),("Giants Contract","Giants Contract"),("Spectre Book","Spectre Book"),("Arcanum of Time","Arcanum of Time"))
max_talent_level10 = (("10","10"),("9","9"),("8","8"),("7","7"),("6","6"),("5","5"),("4","4"),("3","3"),("2","2"),("1","1"),("0","0"))
max_talent_level25 = (("25","25"),("24","24"),("23","23"),("22","22"),("21","21"),("20","20"),("19","19"),("18","18"),("17","17"),("16","16"),("15","15"),("14","14"),("13","13"),("12","12"),("11","11"),("10","10"),("9","9"),("8","8"),("7","7"),("6","6"),("5","5"),("4","4"),("3","3"),("2","2"),("1","1"),("0","0"))
max_talent_level15 = (("15","15"),("14","14"),("13","13"),("12","12"),("11","11"),("10","10"),("9","9"),("8","8"),("7","7"),("6","6"),("5","5"),("4","4"),("3","3"),("2","2"),("1","1"),("0",'0'))
hero_level = (("120","120"),("80","80"),("60","60"),("40","40"),("20","20"),("0","0"))
star_hero = (("8⭐","8⭐"),("7⭐","7⭐"),("2⭐","2⭐"),("0⭐","0⭐"))
stuff_rarity = (("Common","Common"),("Great","Great"),("Rare","Rare"),("Epic","Epic"),("Perfect Epic","Perfect Epic"),("Legendary","Legendary"),("Ancient Legendary","Ancient Legendary"),("Mythic","Mythic"))
all_resistance_type = (("None","None"),("collision","collision"),("projectile","projectile"),("front","front"),("rear","rear"),("damage","damage"),("static","static"),("trap","trap"))
all_damage_type = (("None","None"),("ground","ground"),("airborn","airborn"),("ranged","ranged"),("melee","melee"),("boss","boss"),("mobs","mobs"),("elemental","elemental"),("all","all"))
atk_jewel = (("none","none"),("ruby","ruby"),("kunzite","kunzite"),("tourmaline","tourmaline"))
resistance_jewel = (("none","none"),("amber","amber"),("topaz","topaz"),("amethyst","amethyst"))
defense_jewel = (("none","none"),("lapis","lapis"),("emerald","emerald"),("calaite","calaite"))
mix_atk_defense = (("none","none"),("lapis","lapis"),("emerald","emerald"),("ruby","ruby"),("kunzite","kunzite"),("calaite","calaite"),("tourmaline","tourmaline"))
mix_atk_resistance = (("none","none"),("amber","amber"),("topaz","topaz"),("ruby","ruby"),("kunzite","kunzite"),("amethyst","amethyst"),("tourmaline","tourmaline"))
mix_defense_resistance = (("none","none"),("amber","amber"),("topaz","topaz"),("lapis","lapis"),("emerald","emerald"),("amethyst","amethyst"),("calaite","calaite"))
level_egg_boss = (("15⭐","15⭐"),("14⭐","14⭐"),("13⭐","13⭐"),("12⭐","12⭐"),("11⭐","11⭐"),("10⭐","10⭐"),("9⭐","9⭐"),("8⭐","8⭐"),("7⭐","7⭐"),("6⭐","6⭐"),("5⭐","5⭐"),("4⭐","4⭐"),("3⭐","3⭐"),("2⭐","2⭐"),("1⭐","1⭐"),("0⭐",'0⭐'))
level_egg_mobs = (("20⭐","20⭐"),("19⭐","19⭐"),("18⭐","18⭐"),("17⭐","17⭐"),("16⭐","16⭐"),("15⭐","15⭐"),("14⭐","14⭐"),("13⭐","13⭐"),("12⭐","12⭐"),("11⭐","11⭐"),("10⭐","10⭐"),("9⭐","9⭐"),("8⭐","8⭐"),("7⭐","7⭐"),("6⭐","6⭐"),("5⭐","5⭐"),("4⭐","4⭐"),("3⭐","3⭐"),("2⭐","2⭐"),("1⭐","1⭐"),("0⭐","0⭐"))
all_egg = (("Choose","Choose"),("Vase","Vase"),("Green Bat","Green Bat"),("Rock Puppet","Rock Puppet"),("Bomb Ghost","Bomb Ghost"),("Piranha","Piranha"),("Skeleton Archer","Skeleton Archer"),("Tornado Demon","Tornado Demon"),("Party Tree","Party Tree"),("Wasp","Wasp"),("Wolfhound","Wolfhound"),("Scarecrow","Scarecrow"),("Tornado Mage","Tornado Mage"),("Lava Golem","Lava Golem"),("Skull Wizard","Skull Wizard"),("Cactus","Cactus"),("Ice Mage","Ice Mage"),("Shadow Assassin","Shadow Assassin"),("Fire Lizard","Fire Lizard"),("Fire Mage","Fire Mage"),("Fallen Bat","Fallen Bat"),("Steel Dryad","Steel Dryad"),("Ice Golem","Ice Golem"),("Medusa","Medusa"),("Nether Puppet","Nether Puppet"),("Spitting Mushroom","Spitting Mushroom"),("Psionic Scarecrow","Psionic Scarecrow"),("Pea Shooter","Pea Shooter"),("Scythe Mage","Scythe Mage"),("Rolling Mushroom","Rolling Mushroom"),("Skeleton Swordsman","Skeleton Swordsman"),("Sandian","Sandian"),("Savage Spider","Savage Spider"),("Scarlet Mage","Scarlet Mage"),("Thorny Snake","Thorny Snake"),("Long Dragon","Long Dragon"),("Purple Phantom","Purple Phantom"),("Elite Archer","Elite Archer"),("Flaming Bug","Flaming Bug"),("One-eyed Bat","One-eyed Bat"),("Tundra Dragon","Tundra Dragon"),("Zombie","Zombie"),("Crazy Spider","Crazy Spider"),("Icefire Phantom","Icefire Phantom"),("Skeleton Soldier","Skeleton Soldier"),("Flame Ghost","Flame Ghost"),("Fire Element","Fire Element"),("Little Dragon","Little Dragon"),("Rage Golem","Rage Golem"),("Arch Leader","Arch Leader"),("Krab Boss","Krab Boss"),("Ice Demon","Ice Demon"),("Crimson Witch","Crimson Witch"),("Skeleton King","Skeleton King"),("Giant Owl","Giant Owl"),("Fire Demon","Fire Demon"),("Medusa-Boss","Medusa-Boss"),("Desert Goliath","Desert Goliath"),("Queen Bee","Queen Bee"),("Ice Worm","Ice Worm"))
all_dragon = (("None","None"),("Glacion","Glacion"),("Infernox","Infernox"),("Stormra","Stormra"),("Noxion","Noxion"),("Shadex","Shadex"),("Jadeon","Jadeon"),("Dominus","Dominus"),("Ferron","Ferron"),("Geogon","Geogon"),("Swordian","Swordian"),("Necrogon","Necrogon"),("Starrite","Starrite"),("Voideon","Voideon"))
dragon_rarity = (("Great","Great"),("Rare","Rare"),("Epic","Epic"),("Perfect Epic","Perfect Epic"),("Legendary","Legendary"),("Ancient Legendary","Ancient Legendary"),("Mythic","Mythic"))
reforge = (("0","0"),("20","20"),("40","40"),("60","60"),("80","80"),("100","100"),("120","120"),("140","140"),("160","160"),("180","180"),("200","200"),("220","220"),("240","240"),("260","260"),("280","280"),("300","300"),("320","320"),("340","340"),("360","360"),("380","380"),("400","400"),("450","450"),("500","500"),("550","550"),("600","600"),("650","650"),("700","700"),("750","750"),("800","800"),("850","850"),("900","900"),("950","950"),("1000","1000"),)
altar_ascension_level = (("12","12"),("11","11"),("10","10"),("9","9"),("8","8"),("7","7"),("6","6"),("5","5"),("4","4"),("3","3"),("2","2"),("1","1"),("0","0"))
jewel_level = (("13","13"),("12","12"),("11","11"),("10","10"),("9","9"),("8","8"),("7","7"),("6","6"),("5","5"),("4","4"),("3","3"),("2","2"),("1","1"))
mythic_boost_dragon = (("10","10"),("9","9"),("8","8"),("7","7"),("6","6"),("5","5"),("4","4"),("3","3"),("2","2"),("1","1"),("0","0"))
brave_level_choice = (("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),("11","11"),("12","12"),("13","13"),("14","14"),("15","15"),("16","16"),("17","17"),("18","18"),("19","19"),("20","20"))



#	nom = models.CharField(max_length=50, validators=[RegexValidator(r'^([A-Z]([a-z- ])+)+$')])
#	star_stats1 = models.CharField(max_length=8, blank=True, validators=[RegexValidator(r'^([+-]([0-9-x]){1,4}\%?)?$')])
#	stats3_10 = models.CharField(max_length=4 ,blank=True,default="-", validators=[RegexValidator(r'^(([0-9 -])+)?$')])
#	chapterR = models.CharField(max_length=30 ,blank=True, validators=[RegexValidator(r'^(([0-9]{1,2})(( - )[0-9-A-Z]{1,2})*)?$')])



class user(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	ingame_name = models.CharField(max_length=30,blank=False)
	global_atk_save = models.IntegerField(blank=True, default=0)
	global_hp_save = models.IntegerField(blank=True, default=0)
	choosen_hero = models.CharField(max_length=30 ,choices=all_heros, default="Atreus")
	brave_privileges_level = models.CharField(max_length=10, choices=brave_level_choice, default="1")
	atk_base_stats_hero_choosen = models.BigIntegerField(default="100", validators=[MaxValueValidator(6000)])
	health_base_stats_hero_choosen = models.BigIntegerField(default="400", validators=[MaxValueValidator(20000)])
		
	def __str__(self):
		chaine = f"{self.ingame_name}'s stats ({self.ingame_id})"
		return chaine

	def dictionnaire(self):
			return {
					"ingame_id": self.ingame_id,
					"ingame_name": self.ingame_name,
					"ingame_id": self.ingame_id,
					'choosen_hero': self.choosen_hero,
					'brave_privileges_level': self.brave_privileges_level,
					'atk_base_stats_hero_choosen': self.atk_base_stats_hero_choosen,
					'health_base_stats_hero_choosen': self.health_base_stats_hero_choosen,
					}

class stuff_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	weapon_choosen = models.CharField(max_length=20 ,choices=stuff_weapon, default="None")
	weapon_level = models.BigIntegerField(default="1", validators=[MaxValueValidator(120)]) 
	weapon_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	armor_choosen = models.CharField(max_length=20 ,choices=stuff_armor, default="None")
	armor_level = models.BigIntegerField(default="1", validators=[MaxValueValidator(120)]) 
	armor_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	ring1_choosen = models.CharField(max_length=20 ,choices=stuff_ring, default="None")
	ring1_level = models.BigIntegerField(default="1", validators=[MaxValueValidator(120)]) 
	ring1_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	ring2_choosen = models.CharField(max_length=20 ,choices=stuff_ring, default="None")
	ring2_level = models.BigIntegerField(default="1", validators=[MaxValueValidator(120)]) 
	ring2_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	pet1_choosen = models.CharField(max_length=20 ,choices=stuff_pet, default="None")
	pet1_level = models.BigIntegerField(default="1", validators=[MaxValueValidator(120)]) 
	pet1_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	pet2_choosen = models.CharField(max_length=20 ,choices=stuff_pet, default="None")
	pet2_level = models.BigIntegerField(default="1", validators=[MaxValueValidator(120)]) 
	pet2_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	bracelet_choosen = models.CharField(max_length=20 ,choices=stuff_bracelet, default="None")
	bracelet_level = models.BigIntegerField(default="1", validators=[MaxValueValidator(120)]) 
	bracelet_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	locket_choosen = models.CharField(max_length=20 ,choices=stuff_locket, default="None")
	locket_level = models.BigIntegerField(default="1", validators=[MaxValueValidator(120)]) 
	locket_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	book_choosen = models.CharField(max_length=20 ,choices=stuff_book, default="None")
	book_level = models.BigIntegerField(default="1", validators=[MaxValueValidator(120)]) 
	book_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	
	def dictionnaire(self):
			return {
					"ingame_id": self.ingame_id,
					"weapon_choosen":self.weapon_choosen,"weapon_level" : self.weapon_level,"weapon_rarity" : self.weapon_rarity,
					"armor_choosen":self.armor_choosen,"armor_level" : self.armor_level,"armor_rarity" : self.armor_rarity,
					"ring1_choosen":self.ring1_choosen,"ring1_level" : self.ring1_level,"ring1_rarity" : self.ring1_rarity,
					"ring2_choosen":self.ring2_choosen,"ring2_level" : self.ring2_level,"ring2_rarity" : self.ring2_rarity,
					"pet1_choosen":self.pet1_choosen,"pet1_level" : self.pet1_level,"pet1_rarity" : self.pet1_rarity,
					"pet2_choosen":self.pet2_choosen,"pet2_level" : self.pet2_level,"pet2_rarity" : self.pet2_rarity,
					"bracelet_choosen":self.bracelet_choosen,"bracelet_level" : self.bracelet_level,"bracelet_rarity" : self.bracelet_rarity,
					"locket_choosen":self.locket_choosen,"locket_level" : self.locket_level,"locket_rarity" : self.locket_rarity,
					"book_choosen":self.book_choosen,"book_level" : self.book_level,"book_rarity" : self.book_rarity,
					}

	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine

class hero_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	atreus_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	atreus_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐") 
	urasil_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	urasil_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	phoren_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	phoren_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	taranis_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	taranis_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	helix_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	helix_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐") 
	meowgik_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	meowgik_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	shari_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	shari_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	ayana_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	ayana_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	onir_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	onir_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐") 
	rolla_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	rolla_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	bonnie_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	bonnie_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	sylvan_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	sylvan_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	shade_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	shade_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐") 
	ophelia_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	ophelia_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	ryan_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	ryan_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	lina_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	lina_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	aquea_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	aquea_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	shingen_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	shingen_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐") 
	gugu_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	gugu_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	iris_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	iris_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	blazo_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	blazo_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	melinda_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	melinda_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")
	elaine_level = models.CharField(max_length=10 ,choices=hero_level, default="60")
	elaine_star = models.CharField(max_length=10 ,choices=star_hero, default="2⭐")

	def dictionnaire(self):
			return {
					"ingame_id": self.ingame_id,
					'atreus_level': self.atreus_level, 'atreus_star': self.atreus_star, 
					'urasil_level': self.urasil_level, 'urasil_star': self.urasil_star,
					'phoren_level': self.phoren_level, 'phoren_star': self.phoren_star,
					'taranis_level': self.taranis_level, 'taranis_star': self.taranis_star,
					'helix_level': self.helix_level, 'helix_star': self.helix_star, 
					'meowgik_level': self.meowgik_level, 'meowgik_star': self.meowgik_star,
					'shari_level': self.shari_level, 'shari_star': self.shari_star,
					'ayana_level': self.ayana_level, 'ayana_star': self.ayana_star,
					'onir_level': self.onir_level, 'onir_star': self.onir_star, 
					'rolla_level': self.rolla_level, 'rolla_star': self.rolla_star,
					'bonnie_level': self.bonnie_level, 'bonnie_star': self.bonnie_star,
					'sylvan_level': self.sylvan_level, 'sylvan_star': self.sylvan_star,
					'shade_level': self.shade_level, 'shade_star': self.shade_star, 
					'ophelia_level': self.ophelia_level, 'ophelia_star': self.ophelia_star,
					'ryan_level': self.ryan_level, 'ryan_star': self.ryan_star,
					'lina_level': self.lina_level, 'lina_star': self.lina_star,
					'aquea_level': self.aquea_level, 'aquea_star': self.aquea_star,
					'shingen_level': self.shingen_level, 'shingen_star': self.shingen_star, 
					'gugu_level': self.gugu_level, 'gugu_star': self.gugu_star,
					'iris_level': self.iris_level, 'iris_star': self.iris_star,
					'blazo_level': self.blazo_level, 'blazo_star': self.blazo_star,
					'melinda_level': self.melinda_level, 'melinda_star': self.melinda_star,
					'elaine_level': self.elaine_level, 'elaine_star': self.elaine_star,
					}
	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine


class talent_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	strength_level = models.IntegerField(validators=[MaxValueValidator(25)], default="1")
	power_level = models.IntegerField(validators=[MaxValueValidator(25)], default="1")
	recover_level = models.IntegerField(validators=[MaxValueValidator(25)], default="1")
	block_level = models.IntegerField(validators=[MaxValueValidator(25)], default="1")
	iron_bulwark_level = models.IntegerField(validators=[MaxValueValidator(25)], default="1")
	enhanced_equipment_level = models.IntegerField(validators=[MaxValueValidator(10)], default="1")
	hero_power_up_level = models.IntegerField(validators=[MaxValueValidator(10)], default="1")
	runes_power_up_level = models.IntegerField(validators=[MaxValueValidator(15)], default="1")

	def dictionnaire(self):
			return {
					"ingame_id": self.ingame_id,
					'strength_level': self.strength_level,
					'power_level': self.power_level,
					'recover_level': self.recover_level,
					'block_level': self.block_level,
					'iron_bulwark_level': self.iron_bulwark_level,
					'enhanced_equipment_level': self.enhanced_equipment_level,
					'hero_power_up_level': self.hero_power_up_level,
					'runes_power_up_level': self.runes_power_up_level,
					}
	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine

class skin_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	skin_health = models.IntegerField(default="1", validators=[MaxValueValidator(10595)])
	skin_attack = models.IntegerField(default="1", validators=[MaxValueValidator(2355)])

	def dictionnaire(self):
			return {
					"ingame_id": self.ingame_id,
					'skin_health': self.skin_health,
					'skin_attack': self.skin_attack,
					}
	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine



class altar_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	stuff_altar_level = models.IntegerField(default="1", validators=[MaxValueValidator(120)]) 
	stuff_altar_ascension = models.CharField(max_length=5 ,choices=altar_ascension_level, default="1")
	heros_altar_level = models.IntegerField(default="1", validators=[MaxValueValidator(120)]) 
	heros_altar_ascension = models.CharField(max_length=5 ,choices=altar_ascension_level, default="1")
	
	def dictionnaire(self):
			return {
					"ingame_id": self.ingame_id,
					'stuff_altar_level': self.stuff_altar_level, 
					'stuff_altar_ascension': self.stuff_altar_ascension, 
					'heros_altar_level': self.heros_altar_level, 
					'heros_altar_ascension': self.heros_altar_ascension,
					}
	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine


class jewel_type_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	weapon_jewel1_type = models.CharField(max_length=10, choices=atk_jewel, default="ruby")
	weapon_jewel2_type = models.CharField(max_length=10, choices=atk_jewel, default="ruby")
	weapon_jewel3_type = models.CharField(max_length=10, choices=atk_jewel, default="ruby")
	weapon_jewel4_type = models.CharField(max_length=10, choices=atk_jewel, default="ruby")
	armor_jewel1_type = models.CharField(max_length=10, choices=defense_jewel, default="lapis")
	armor_jewel2_type = models.CharField(max_length=10, choices=defense_jewel, default="lapis")
	armor_jewel3_type = models.CharField(max_length=10, choices=defense_jewel, default="lapis")
	armor_jewel4_type = models.CharField(max_length=10, choices=defense_jewel, default="lapis")
	ring1_jewel1_type = models.CharField(max_length=10, choices=resistance_jewel, default="amber")
	ring1_jewel2_type = models.CharField(max_length=10, choices=resistance_jewel, default="amber")
	ring1_jewel3_type = models.CharField(max_length=10, choices=resistance_jewel, default="amber")
	ring1_jewel4_type = models.CharField(max_length=10, choices=resistance_jewel, default="amber") 
	ring2_jewel1_type = models.CharField(max_length=10, choices=resistance_jewel, default="amber")
	ring2_jewel2_type = models.CharField(max_length=10, choices=resistance_jewel, default="amber")
	ring2_jewel3_type = models.CharField(max_length=10, choices=resistance_jewel, default="amber")
	ring2_jewel4_type = models.CharField(max_length=10, choices=resistance_jewel, default="amber") 
	pet1_jewel1_type = models.CharField(max_length=10, choices=atk_jewel, default="ruby")
	pet1_jewel2_type = models.CharField(max_length=10, choices=atk_jewel, default="ruby")
	pet1_jewel3_type = models.CharField(max_length=10, choices=atk_jewel, default="ruby")
	pet1_jewel4_type = models.CharField(max_length=10, choices=atk_jewel, default="ruby")
	pet2_jewel1_type = models.CharField(max_length=10, choices=defense_jewel, default="lapis")
	pet2_jewel2_type = models.CharField(max_length=10, choices=defense_jewel, default="lapis")
	pet2_jewel3_type = models.CharField(max_length=10, choices=defense_jewel, default="lapis")
	pet2_jewel4_type = models.CharField(max_length=10, choices=defense_jewel, default="lapis")
	bracelet_jewel1_type = models.CharField(max_length=10, choices=mix_defense_resistance, default="emerald")
	bracelet_jewel2_type = models.CharField(max_length=10, choices=mix_defense_resistance, default="emerald")
	bracelet_jewel3_type = models.CharField(max_length=10, choices=mix_defense_resistance, default="emerald")
	bracelet_jewel4_type = models.CharField(max_length=10, choices=mix_defense_resistance, default="emerald")
	locket_jewel1_type = models.CharField(max_length=10, choices=mix_atk_resistance, default="ruby")
	locket_jewel2_type = models.CharField(max_length=10, choices=mix_atk_resistance, default="ruby")
	locket_jewel3_type = models.CharField(max_length=10, choices=mix_atk_resistance, default="ruby")
	locket_jewel4_type = models.CharField(max_length=10, choices=mix_atk_resistance, default="ruby")
	book_jewel1_type = models.CharField(max_length=10, choices=mix_atk_defense, default="lapis")
	book_jewel2_type = models.CharField(max_length=10, choices=mix_atk_defense, default="lapis")
	book_jewel3_type = models.CharField(max_length=10, choices=mix_atk_defense, default="lapis")
	book_jewel4_type = models.CharField(max_length=10, choices=mix_atk_defense, default="lapis")
	
	def dictionnaire(self):
			return {
					"ingame_id": self.ingame_id,
					'weapon_jewel1_type': self.weapon_jewel1_type,
					'weapon_jewel2_type': self.weapon_jewel2_type,
					'weapon_jewel3_type': self.weapon_jewel3_type,
					'weapon_jewel4_type': self.weapon_jewel4_type,
					'armor_jewel1_type': self.armor_jewel1_type,
					'armor_jewel2_type': self.armor_jewel2_type,
					'armor_jewel3_type': self.armor_jewel3_type,
					'armor_jewel4_type': self.armor_jewel4_type,
					'ring1_jewel1_type': self.ring1_jewel1_type,
					'ring1_jewel2_type': self.ring1_jewel2_type,
					'ring1_jewel3_type': self.ring1_jewel3_type,
					'ring1_jewel4_type': self.ring1_jewel4_type, 
					'ring2_jewel1_type': self.ring2_jewel1_type,
					'ring2_jewel2_type': self.ring2_jewel2_type,
					'ring2_jewel3_type': self.ring2_jewel3_type,
					'ring2_jewel4_type': self.ring2_jewel4_type, 
					'pet1_jewel1_type': self.pet1_jewel1_type,
					'pet1_jewel2_type': self.pet1_jewel2_type,
					'pet1_jewel3_type': self.pet1_jewel3_type,
					'pet1_jewel4_type': self.pet1_jewel4_type,
					'pet2_jewel1_type': self.pet2_jewel1_type,
					'pet2_jewel2_type': self.pet2_jewel2_type,
					'pet2_jewel3_type': self.pet2_jewel3_type,
					'pet2_jewel4_type': self.pet2_jewel4_type,
					'bracelet_jewel1_type': self.bracelet_jewel1_type,
					'bracelet_jewel2_type': self.bracelet_jewel2_type,
					'bracelet_jewel3_type': self.bracelet_jewel3_type,
					'bracelet_jewel4_type': self.bracelet_jewel4_type,
					'locket_jewel1_type': self.locket_jewel1_type,
					'locket_jewel2_type': self.locket_jewel2_type,
					'locket_jewel3_type': self.locket_jewel3_type,
					'locket_jewel4_type': self.locket_jewel4_type,
					'book_jewel1_type': self.book_jewel1_type,
					'book_jewel2_type': self.book_jewel2_type,
					'book_jewel3_type': self.book_jewel3_type,
					'book_jewel4_type': self.book_jewel4_type,
					}
	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine


class jewel_level_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	weapon_jewel1_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	weapon_jewel2_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	weapon_jewel3_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	weapon_jewel4_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	armor_jewel1_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	armor_jewel2_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	armor_jewel3_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	armor_jewel4_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	ring1_jewel1_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	ring1_jewel2_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	ring1_jewel3_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	ring1_jewel4_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)]) 
	ring2_jewel1_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	ring2_jewel2_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	ring2_jewel3_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	ring2_jewel4_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)]) 
	pet1_jewel1_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	pet1_jewel2_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	pet1_jewel3_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	pet1_jewel4_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	pet2_jewel1_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	pet2_jewel2_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	pet2_jewel3_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	pet2_jewel4_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	bracelet_jewel1_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	bracelet_jewel2_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	bracelet_jewel3_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	bracelet_jewel4_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	locket_jewel1_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	locket_jewel2_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	locket_jewel3_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	locket_jewel4_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	book_jewel1_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	book_jewel2_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	book_jewel3_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	book_jewel4_level = models.IntegerField(default=1, validators=[MaxValueValidator(13)])
	
	def dictionnaire(self):
			return {
					"ingame_id": self.ingame_id,
					'weapon_jewel1_level': self.weapon_jewel1_level,
					'weapon_jewel2_level': self.weapon_jewel2_level,
					'weapon_jewel3_level': self.weapon_jewel3_level,
					'weapon_jewel4_level': self.weapon_jewel4_level,
					'armor_jewel1_level': self.armor_jewel1_level,
					'armor_jewel2_level': self.armor_jewel2_level,
					'armor_jewel3_level': self.armor_jewel3_level,
					'armor_jewel4_level': self.armor_jewel4_level,
					'ring1_jewel1_level': self.ring1_jewel1_level,
					'ring1_jewel2_level': self.ring1_jewel2_level,
					'ring1_jewel3_level': self.ring1_jewel3_level,
					'ring1_jewel4_level': self.ring1_jewel4_level, 
					'ring2_jewel1_level': self.ring2_jewel1_level,
					'ring2_jewel2_level': self.ring2_jewel2_level,
					'ring2_jewel3_level': self.ring2_jewel3_level,
					'ring2_jewel4_level': self.ring2_jewel4_level, 
					'pet1_jewel1_level': self.pet1_jewel1_level,
					'pet1_jewel2_level': self.pet1_jewel2_level,
					'pet1_jewel3_level': self.pet1_jewel3_level,
					'pet1_jewel4_level': self.pet1_jewel4_level,
					'pet2_jewel1_level': self.pet2_jewel1_level,
					'pet2_jewel2_level': self.pet2_jewel2_level,
					'pet2_jewel3_level': self.pet2_jewel3_level,
					'pet2_jewel4_level': self.pet2_jewel4_level,
					'bracelet_jewel1_level': self.bracelet_jewel1_level,
					'bracelet_jewel2_level': self.bracelet_jewel2_level,
					'bracelet_jewel3_level': self.bracelet_jewel3_level,
					'bracelet_jewel4_level': self.bracelet_jewel4_level,
					'locket_jewel1_level': self.locket_jewel1_level,
					'locket_jewel2_level': self.locket_jewel2_level,
					'locket_jewel3_level': self.locket_jewel3_level,
					'locket_jewel4_level': self.locket_jewel4_level,
					'book_jewel1_level': self.book_jewel1_level,
					'book_jewel2_level': self.book_jewel2_level,
					'book_jewel3_level': self.book_jewel3_level,
					'book_jewel4_level': self.book_jewel4_level,
					}
	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine


class egg_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	green_bat = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	vase = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	bomb_ghost = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	rock_puppet = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	party_tree = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	wolfhound = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	skeleton_archer = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	skeleton_soldier = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	wasp = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	fire_mage = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	medusa = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	ice_mage = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	fire_lizard = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	flame_ghost = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	thorny_snake = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	tornado_demon = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	piranha = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	zombie = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	scarecrow = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	long_dragon = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	skull_wizard = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	lava_golem = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	ice_golem = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	cactus = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	crazy_spider = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	fire_element = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	skeleton_swordsman = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	scythe_mage = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	pea_shooter = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	shadow_assassin = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	tornado_mage = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	spitting_mushroom = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	rolling_mushroom = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	fallen_bat = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	one_eyed_bat = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	scarlet_mage = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	icefire_phantom = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	purple_phantom = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	tundra_dragon = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	sandian = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	nether_puppet = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	psionic_scarecrow = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	steel_dryad = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	savage_spider = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	flaming_bug = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	elite_archer = models.CharField(max_length=10, choices=level_egg_mobs, default="0⭐")
	little_dragon = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")
	arch_leader = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")
	skeleton_king = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")
	crimson_witch = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")
	rage_golem = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")
	queen_bee = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")
	ice_worm = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")
	medusa_boss = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")
	ice_demon = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")
	giant_owl = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")
	fire_demon = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")
	krab_boss = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")
	desert_goliath = models.CharField(max_length=10, choices=level_egg_boss, default="0⭐")

	def dictionnaire(self):
		return {
				"ingame_id": self.ingame_id,
				'green_bat': self.green_bat,
				'vase': self.vase,
				'bomb_ghost': self.bomb_ghost,
				'rock_puppet': self.rock_puppet,
				'party_tree': self.party_tree,
				'wolfhound': self.wolfhound,
				'skeleton_archer': self.skeleton_archer,
				'skeleton_soldier': self.skeleton_soldier,
				'wasp': self.wasp,
				'fire_mage': self.fire_mage,
				'medusa': self.medusa,
				'ice_mage': self.ice_mage,
				'fire_lizard': self.fire_lizard,
				'flame_ghost': self.flame_ghost,
				'thorny_snake': self.thorny_snake,
				'tornado_demon': self.tornado_demon,
				'piranha': self.piranha,
				'zombie': self.zombie,
				'scarecrow': self.scarecrow,
				'long_dragon': self.long_dragon,
				'skull_wizard': self.skull_wizard,
				'lava_golem': self.lava_golem,
				'ice_golem': self.ice_golem,
				'cactus': self.cactus,
				'crazy_spider': self.crazy_spider,
				'fire_element': self.fire_element,
				'skeleton_swordsman': self.skeleton_swordsman,
				'scythe_mage': self.scythe_mage,
				'pea_shooter': self.pea_shooter,
				'shadow_assassin': self.shadow_assassin,
				'tornado_mage': self.tornado_mage,
				'spitting_mushroom': self.spitting_mushroom,
				'rolling_mushroom': self.rolling_mushroom,
				'fallen_bat': self.fallen_bat,
				'one_eyed_bat': self.one_eyed_bat,
				'scarlet_mage': self.scarlet_mage,
				'icefire_phantom': self.icefire_phantom,
				'purple_phantom': self.purple_phantom,
				'tundra_dragon': self.tundra_dragon,
				'sandian': self.sandian,
				'nether_puppet': self.nether_puppet,
				'psionic_scarecrow': self.psionic_scarecrow,
				'steel_dryad': self.steel_dryad,
				'savage_spider': self.savage_spider,
				'flaming_bug': self.flaming_bug,
				'elite_archer': self.elite_archer,
				'little_dragon': self.little_dragon,
				'arch_leader': self.arch_leader,
				'skeleton_king': self.skeleton_king,
				'crimson_witch': self.crimson_witch,
				'rage_golem': self.rage_golem,
				'queen_bee': self.queen_bee,
				'ice_worm': self.ice_worm,
				'medusa_boss': self.medusa_boss,
				'ice_demon': self.ice_demon,
				'giant_owl': self.giant_owl,
				'fire_demon': self.fire_demon,
				'krab_boss': self.krab_boss,
				'desert_goliath': self.desert_goliath,
				}
	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine


class egg_equipped_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	egg_equipped1 = models.CharField(max_length=30, choices=all_egg, default="Choose")
	egg_equipped2 = models.CharField(max_length=30, choices=all_egg, default="Choose")
	egg_equipped3 = models.CharField(max_length=30, choices=all_egg, default="Choose")
	egg_equipped4 = models.CharField(max_length=30, choices=all_egg, default="Choose")
	egg_equipped5 = models.CharField(max_length=30, choices=all_egg, default="Choose")

	def dictionnaire(self):
			return {
					"ingame_id": self.ingame_id,
					'egg_equipped1': self.egg_equipped1,
					'egg_equipped2': self.egg_equipped2,
					'egg_equipped3': self.egg_equipped3,
					'egg_equipped4': self.egg_equipped4,
					'egg_equipped5': self.egg_equipped5,
					}
	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine



class dragon_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	dragon1_type = models.CharField(max_length=30, choices=all_dragon, default="Glacion")
	dragon2_type = models.CharField(max_length=30, choices=all_dragon, default="Infernox")
	dragon3_type = models.CharField(max_length=30, choices=all_dragon, default="Stormra")
	dragon1_rarity = models.CharField(max_length=30, choices=dragon_rarity, default="Great")
	dragon2_rarity = models.CharField(max_length=30, choices=dragon_rarity, default="Great")
	dragon3_rarity = models.CharField(max_length=30, choices=dragon_rarity, default="Great")
	dragon1_level = models.IntegerField(default="1", validators=[MaxValueValidator(120)]) 
	dragon2_level = models.IntegerField(default="1", validators=[MaxValueValidator(120)]) 
	dragon3_level = models.IntegerField(default="1", validators=[MaxValueValidator(120)]) 
	dragon_1_boost_4_mythic = models.CharField(max_length=3, choices=mythic_boost_dragon, default="0")
	dragon_2_boost_4_mythic = models.CharField(max_length=3, choices=mythic_boost_dragon, default="0")
	dragon_3_boost_4_mythic = models.CharField(max_length=3, choices=mythic_boost_dragon, default="0")

	def dictionnaire(self):
		return {
				"ingame_id": self.ingame_id,
				'dragon1_type': self.dragon1_type,
				'dragon2_type': self.dragon2_type,
				'dragon3_type': self.dragon3_type,
				'dragon1_rarity': self.dragon1_rarity,
				'dragon2_rarity': self.dragon2_rarity,
				'dragon3_rarity': self.dragon3_rarity,
				'dragon1_level': self.dragon1_level,
				'dragon2_level': self.dragon2_level,
				'dragon3_level': self.dragon3_level,
				'dragon_1_boost_4_mythic': self.dragon_1_boost_4_mythic,
				'dragon_2_boost_4_mythic': self.dragon_2_boost_4_mythic,
				'dragon_3_boost_4_mythic': self.dragon_3_boost_4_mythic,
				}
	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine



class runes_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	power_attack_flat = models.BigIntegerField(default="0", validators=[MaxValueValidator(750)])
	power_attack_var = models.FloatField(default="0", validators=[MaxValueValidator(7)])
	saviour_hp_flat = models.BigIntegerField(default="0", validators=[MaxValueValidator(2800)])
	saviour_hp_var = models.FloatField(default="0", validators=[MaxValueValidator(7)])
	recovery_hp_flat = models.BigIntegerField(default="0", validators=[MaxValueValidator(2250)])
	courage_attack_flat = models.BigIntegerField(default="0", validators=[MaxValueValidator(750)])
	courage_attack_var = models.FloatField(default="0", validators=[MaxValueValidator(7)])
	selected_hero_courage_attack_flat = models.CharField(choices=all_heros,default="Atreus", max_length=15)
	courage_hero_attack_flat = models.BigIntegerField(default="0", validators=[MaxValueValidator(180)])
	selected_hero_courage_attack_var = models.CharField(choices=all_heros,default="Atreus", max_length=15)
	courage_hero_attack_var = models.FloatField(default="0", validators=[MaxValueValidator(12.5)])
	selected_hero_courage_hp_flat = models.CharField(choices=all_heros,default="Atreus", max_length=15)
	courage_hero_hp_flat = models.BigIntegerField(default="0", validators=[MaxValueValidator(900)])
	selected_hero_courage_hp_var = models.CharField(choices=all_heros,default="Atreus", max_length=15)
	courage_hero_hp_var = models.FloatField(default="0", validators=[MaxValueValidator(12.5)])
	luck_hp_flat = models.BigIntegerField(default="0", validators=[MaxValueValidator(2800)])
	luck_hp_var = models.FloatField(default="0", validators=[MaxValueValidator(7)])

	def dictionnaire(self):
			return {
					"ingame_id": self.ingame_id,
					'power_attack_flat': self.power_attack_flat,
					'power_attack_var': self.power_attack_var,
					'saviour_hp_flat': self.saviour_hp_flat,
					'saviour_hp_var': self.saviour_hp_var,
					'recovery_hp_flat': self.recovery_hp_flat,
					'courage_attack_flat': self.courage_attack_flat,
					'courage_attack_var': self.courage_attack_var,
					'courage_hero_attack_flat': self.courage_hero_attack_flat,
					'courage_hero_attack_var': self.courage_hero_attack_var,
					'courage_hero_hp_flat': self.courage_hero_hp_flat,
					'courage_hero_hp_var': self.courage_hero_hp_var,
					'luck_hp_flat': self.luck_hp_flat,
					'luck_hp_var': self.luck_hp_var,
					'selected_hero_courage_attack_flat': self.selected_hero_courage_attack_flat,
					'selected_hero_courage_attack_var': self.selected_hero_courage_attack_var,
					'selected_hero_courage_hp_flat': self.selected_hero_courage_hp_flat,
					'selected_hero_courage_hp_var': self.selected_hero_courage_hp_var,
					}
	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine



class reforge_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	reforge_power = models.CharField(max_length=10, choices=reforge, default="0")
	reforge_saviour = models.CharField(max_length=10, choices=reforge, default="0")
	reforge_recovery = models.CharField(max_length=10, choices=reforge, default="0")
	reforge_courage = models.CharField(max_length=10, choices=reforge, default="0")
	reforge_luck = models.CharField(max_length=10, choices=reforge, default="0")

	def dictionnaire(self):
			return {
					"ingame_id": self.ingame_id,
					'reforge_power': self.reforge_power,
					'reforge_saviour': self.reforge_saviour,
					'reforge_recovery': self.reforge_recovery,
					'reforge_courage': self.reforge_courage,
					'reforge_luck': self.reforge_luck,
					}
	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine


class refine_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	weapon_refine_atk = models.IntegerField(default=0, validators=[MaxValueValidator(8000)])
	weapon_refine_basic_stats = models.FloatField(default=0, validators=[MaxValueValidator(100)])
	armor_refine_hp = models.IntegerField(default=0, validators=[MaxValueValidator(25000)])
	armor_refine_basic_stats = models.FloatField(default=0, validators=[MaxValueValidator(100)])
	ring1_refine_atk = models.IntegerField(default=0, validators=[MaxValueValidator(8000)])
	ring1_refine_basic_stats = models.FloatField(default=0, validators=[MaxValueValidator(100)])
	ring2_refine_atk = models.IntegerField(default=0, validators=[MaxValueValidator(8000)])
	ring2_refine_basic_stats = models.FloatField(default=0, validators=[MaxValueValidator(100)])
	bracelet_refine_atk = models.IntegerField(default=0, validators=[MaxValueValidator(8000)])
	bracelet_refine_basic_stats = models.FloatField(default=0, validators=[MaxValueValidator(100)])
	locket_refine_hp = models.IntegerField(default=0, validators=[MaxValueValidator(25000)])
	locket_refine_basic_stats = models.FloatField(default=0, validators=[MaxValueValidator(100)])
	book_refine_hp = models.IntegerField(default=0, validators=[MaxValueValidator(25000)])
	book_refine_basic_stats = models.FloatField(default=0, validators=[MaxValueValidator(100)])

	def dictionnaire(self):
		return {
				"ingame_id": self.ingame_id,
				'weapon_refine_atk': self.weapon_refine_atk,
				'weapon_refine_basic_stats': self.weapon_refine_basic_stats,
				'armor_refine_hp': self.armor_refine_hp,
				'armor_refine_basic_stats': self.armor_refine_basic_stats,
				'ring1_refine_atk': self.ring1_refine_atk,
				'ring1_refine_basic_stats': self.ring1_refine_basic_stats,
				'ring2_refine_atk': self.ring2_refine_atk,
				'ring2_refine_basic_stats': self.ring2_refine_basic_stats,
				'bracelet_refine_atk': self.bracelet_refine_atk,
				'bracelet_refine_basic_stats': self.bracelet_refine_basic_stats,
				'locket_refine_hp': self.locket_refine_hp,
				'locket_refine_basic_stats': self.locket_refine_basic_stats,
				'book_refine_hp': self.book_refine_hp,
				'book_refine_basic_stats': self.book_refine_basic_stats,
				}
	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine


class dmg_calc_table(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False)
	hero_atk = models.JSONField(default=dict,blank=False)
	weapon_coeff = models.CharField(max_length=20,blank=False)

	flat_dmg_vs_ground = models.IntegerField(default=0,blank=False)
	flat_dmg_vs_airborne = models.IntegerField(default=0,blank=False)
	flat_dmg_vs_melee = models.IntegerField(default=0,blank=False)
	flat_dmg_vs_range = models.IntegerField(default=0,blank=False)
	flat_dmg_vs_mobs = models.IntegerField(default=0,blank=False)
	flat_dmg_vs_boss = models.IntegerField(default=0,blank=False)
	flat_dmg_element = models.IntegerField(default=0,blank=False)
	flat_dmg_all = models.IntegerField(default=0,blank=False)

	var_dmg_vs_ground = models.FloatField(default=0,blank=False)
	var_dmg_vs_airborne = models.FloatField(default=0,blank=False)
	var_dmg_vs_melee = models.FloatField(default=0,blank=False)
	var_dmg_vs_range = models.FloatField(default=0,blank=False)
	var_dmg_vs_mobs = models.FloatField(default=0,blank=False)
	var_dmg_vs_boss = models.FloatField(default=0,blank=False)
	var_dmg_element = models.FloatField(default=0,blank=False)
	var_dmg_all = models.FloatField(default=0,blank=False)

	crit_dmg = models.IntegerField(default=0,blank=False)


	def dictionnaire(self):
		return {
				"ingame_id": self.ingame_id,
				"hero_atk": self.hero_atk,
				"weapon_coeff": self.weapon_coeff,
				"flat_dmg_vs_ground": self.flat_dmg_vs_ground,
				"flat_dmg_vs_airborne": self.flat_dmg_vs_airborne,
				"flat_dmg_vs_melee": self.flat_dmg_vs_melee,
				"flat_dmg_vs_range": self.flat_dmg_vs_range,
				"flat_dmg_vs_mobs": self.flat_dmg_vs_mobs,
				"flat_dmg_vs_boss": self.flat_dmg_vs_boss,
				"flat_dmg_element": self.flat_dmg_element,
				"flat_dmg_all": self.flat_dmg_all,
				"var_dmg_vs_ground": self.var_dmg_vs_ground,
				"var_dmg_vs_airborne": self.var_dmg_vs_airborne,
				"var_dmg_vs_melee": self.var_dmg_vs_melee,
				"var_dmg_vs_range": self.var_dmg_vs_range,
				"var_dmg_vs_mobs": self.var_dmg_vs_mobs,
				"var_dmg_vs_boss": self.var_dmg_vs_boss,
				"var_dmg_element": self.var_dmg_element,
				"var_dmg_all": self.var_dmg_all,
				"crit_dmg": self.crit_dmg,
			}

	def __str__(self):
		chaine = f"{self.ingame_id}"
		return chaine