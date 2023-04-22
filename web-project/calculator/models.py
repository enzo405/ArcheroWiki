from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime, math, json
from django.contrib.auth.models import User as BuiltinDjangoUser
from django.utils.crypto import get_random_string



class UserQueue(models.Model):
	username = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	is_validated = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)


class Token(models.Model):
	user = models.OneToOneField(BuiltinDjangoUser, on_delete=models.CASCADE)
	key = models.CharField(max_length=40, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	discord_acc_rely = models.CharField(max_length=40, default=" ", blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.key:
			self.key = self.generate_key()
		return super(Token, self).save(*args, **kwargs)

	def generate_key(self):
		return get_random_string(40)

	def __str__(self):
		return self.key

#(actual value, human readable name)
all_heros = (("Atreus","Atreus"),("Urasil","Urasil"),("Phoren","Phoren"),("Taranis","Taranis"),("Helix","Helix"),("Meowgik","Meowgik"),("Shari","Shari"),("Ayana","Ayana"),("Onir","Onir"),("Rolla","Rolla"),("Bonnie","Bonnie"),("Sylvan","Sylvan"),("Shade","Shade"),("Ophelia","Ophelia"),("Ryan","Ryan"),("Lina","Lina"),("Aquea","Aquea"),("Shingen","Shingen"),("Gugu","Gugu"),("Iris","Iris"),("Blazo","Blazo"),("Melinda","Melinda"),("Elaine","Elaine"),("Bobo","Bobo"),("Stella","Stella"))
stuff_weapon = (("None","None"),("Brave Bow","Brave Bow"),("Death Scythe","Death Scythe"),("Saw Blade","Saw Blade"),("Tornado","Tornado"),("Brightspear","Brightspear"),("Stalker Staff","Stalker Staff"),("Gale Force","Gale Force"),("Demon Blade Rain","Demon Blade Rain"),("Mini Atreus","Mini Atreus"),("Antiquated Sword","Antiquated Sword"))
stuff_armor = (("None","None"),("Phantom Cloak","Phantom Cloak"),("Vest of Dexterity","Vest of Dexterity"),("Golden Chestplate","Golden Chestplate"),("Void Robe","Void Robe"),("Bright Robe","Bright Robe"),("Shadow Robe","Shadow Robe"))
stuff_ring = (("None","None"),("Bear Ring","Bear Ring"),("Wolf Ring","Wolf Ring"),("Falcon Ring","Falcon Ring"),("Serpent Ring","Serpent Ring"),("Bull Ring","Bull Ring"),("Lion Ring","Lion Ring"),("Vilebat Ring","Vilebat Ring"),("Dragon Ring","Dragon Ring"))
stuff_pet = (("None","None"),("Laser Bat","Laser Bat"),("Scythe Mage","Scythe Mage"),("Elf","Elf"),("Living Bomb","Living Bomb"),("Noisy Owl","Noisy Owl"),("Flaming Ghost","Flaming Ghost"),("Bone Warrior","Bone Warrior"))
stuff_bracelet = (("None","None"),("Thunder Bracelet","Thunder Bracelet"),("Frozen Bracelet","Frozen Bracelet"),("Blazing Bracelet","Blazing Bracelet"),("Split Bracelet","Split Bracelet"),("Invincible Bracelet","Invincible Bracelet"),("Quickshot Bracelet","Quickshot Bracelet"),("Shield Bracelet","Shield Bracelet"))
stuff_locket = (("None","None"),("Agile Locket","Agile Locket"),("Iron Locket","Iron Locket"),("Angel Locket","Angel Locket"),("Bulletproof Locket","Bulletproof Locket"),("Piercer Locket","Piercer Locket"),("Bloodthirsty Locket","Bloodthirsty Locket"),("Counterattack Locket","Counterattack Locket"))
stuff_book = (("None","None"),("Arcane Archer","Arcane Archer"),("Art of Combat","Art of Combat"),("Ice Realm","Ice Realm"),("Enlightenment","Enlightenment"),("Giants Contract","Giants Contract"),("Spectre Book","Spectre Book"),("Arcanum of Time","Arcanum of Time"))
max_talent_level10 = ((10,"10"),(9,"9"),(8,"8"),(7,"7"),(6,"6"),(5,"5"),(4,"4"),(3,"3"),(2,"2"),(1,"1"),(0,"0"))
max_talent_level25 = ((25,"25"),(24,"24"),(23,"23"),(22,"22"),(21,"21"),(20,"20"),(19,"19"),(18,"18"),(17,"17"),(16,"16"),(15,"15"),(14,"14"),(13,"13"),(12,"12"),(11,"11"),(10,"10"),(9,"9"),(8,"8"),(7,"7"),(6,"6"),(5,"5"),(4,"4"),(3,"3"),(2,"2"),(1,"1"),(0,"0"))
max_talent_level15 = ((15,"15"),(14,"14"),(13,"13"),(12,"12"),(11,"11"),(10,"10"),(9,"9"),(8,"8"),(7,"7"),(6,"6"),(5,"5"),(4,"4"),(3,"3"),(2,"2"),(1,"1"),(0,'0'))
hero_level = ((120,"120"),(80,"80"),(60,"60"),(40,"40"),(20,"20"),(0,"0"))
star_hero = ((8,"8⭐"),(7,"7⭐"),(2,"2⭐"),(0,"0⭐"))
stuff_rarity = (("Common","Common"),("Great","Great"),("Rare","Rare"),("Epic","Epic"),("Perfect Epic","Perfect Epic"),("Legendary","Legendary"),("Ancient Legendary","Ancient Legendary"),("Mythic","Mythic"),("Mythic_1","Mythic+1"),("Mythic_2","Mythic+2"),("Titan Tales","Titan Tales"),("Titan Tales_1","Titan Tales+1"),("Titan Tales_2","Titan Tales+2"),("Titan Tales_3","Titan Tales+3"),("Chaos","Chaos"))
all_resistance_type = (("None","None"),("collision","collision"),("projectile","projectile"),("front","front"),("rear","rear"),("damage","damage"),("static","static"),("trap","trap"))
all_damage_type = (("None","None"),("ground","ground"),("airborn","airborn"),("ranged","ranged"),("melee","melee"),("boss","boss"),("mobs","mobs"),("elemental","elemental"),("all","all"))
atk_jewel = (("none","none"),("ruby","ruby"),("kunzite","kunzite"),("tourmaline","tourmaline"))
resistance_jewel = (("none","none"),("amber","amber"),("topaz","topaz"),("amethyst","amethyst"))
defense_jewel = (("none","none"),("lapis","lapis"),("emerald","emerald"),("calaite","calaite"))
mix_atk_defense = (("none","none"),("lapis","lapis"),("emerald","emerald"),("ruby","ruby"),("kunzite","kunzite"),("calaite","calaite"),("tourmaline","tourmaline"))
mix_atk_resistance = (("none","none"),("amber","amber"),("topaz","topaz"),("ruby","ruby"),("kunzite","kunzite"),("amethyst","amethyst"),("tourmaline","tourmaline"))
mix_defense_resistance = (("none","none"),("amber","amber"),("topaz","topaz"),("lapis","lapis"),("emerald","emerald"),("amethyst","amethyst"),("calaite","calaite"))
level_egg_boss = ((15,"15⭐"),(14,"14⭐"),(13,"13⭐"),(12,"12⭐"),(11,"11⭐"),(10,"10⭐"),(9,"9⭐"),(8,"8⭐"),(7,"7⭐"),(6,"6⭐"),(5,"5⭐"),(4,"4⭐"),(3,"3⭐"),(2,"2⭐"),(1,"1⭐"),(0,'0⭐'))
level_egg_mobs = ((20,"20⭐"),(19,"19⭐"),(18,"18⭐"),(17,"17⭐"),(16,"16⭐"),(15,"15⭐"),(14,"14⭐"),(13,"13⭐"),(12,"12⭐"),(11,"11⭐"),(10,"10⭐"),(9,"9⭐"),(8,"8⭐"),(7,"7⭐"),(6,"6⭐"),(5,"5⭐"),(4,"4⭐"),(3,"3⭐"),(2,"2⭐"),(1,"1⭐"),(0,"0⭐"))
all_dragon = (("None","None"),("Glacion","Glacion"),("Infernox","Infernox"),("Stormra","Stormra"),("Noxion","Noxion"),("Shadex","Shadex"),("Jadeon","Jadeon"),("Dominus","Dominus"),("Ferron","Ferron"),("Geogon","Geogon"),("Swordian","Swordian"),("Necrogon","Necrogon"),("Starrite","Starrite"),("Voideon","Voideon"))
dragon_rarity = (("Great","Great"),("Rare","Rare"),("Epic","Epic"),("Perfect Epic","Perfect Epic"),("Legendary","Legendary"),("Ancient Legendary","Ancient Legendary"),("Mythic","Mythic"))
reforge = ((0,0),(20,20),(40,40),(60,60),(80,80),(100,100),(120,120),(140,140),(160,160),(180,180),(200,200),(220,220),(240,240),(260,260),(280,280),(300,300),(320,320),(340,340),(360,360),(380,380),(400,400),(450,450),(500,500),(550,550),(600,600),(650,650),(700,700),(750,750),(800,800),(850,850),(900,900),(950,950),(1000,1000))
altar_ascension_level = ((12,12),(11,11),(10,10),(9,9),(8,8),(7,7),(6,6),(5,5),(4,4),(3,3),(2,2),(1,1),(0,0))
jewel_level = ((13,13),(12,12),(11,11),(10,10),(9,9),(8,8),(7,7),(6,6),(5,5),(4,4),(3,3),(2,2),(1,1))
dragon_skill_level = ((10,10),(9,9),(8,8),(7,7),(6,6),(5,5),(4,4),(3,3),(2,2),(1,1),(0,0))
brave_level_choice = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20))
type_reward = (("none","none"),("gem","gem"),("celestite_keys","celestite_keys"),("purple_ticket","purple_ticket"),("premium_ticket","premium_ticket"),("gold","gold"),("random_shards","random_shards"),("obsidian_keys","obsidian_keys"),("energy","energy"))
power_rune_all = (
	("none","None"),
	("flat_dmg_airborne","Damage to Airborne Units"),("var_dmg_airborne","Damage to Airborne Units %"),
	("flat_dmg_ground","Damage to Ground Units"),("var_dmg_ground","Damage to Ground Units %"),
	("flat_dmg_melee","Damage to Melee Units"),("var_dmg_melee","Damage to Melee Units %"),
	("flat_dmg_ranged","Damage to Ranged Units"),("var_dmg_ranged","Damage to Ranged Units %"),
	("flat_dmg_boss","Damage to Bosses Units"),("var_dmg_boss","Damage to Bosses Units %"),
	("flat_dmg_mob","Damage to Mobs Units"),("var_dmg_mob","Damage to Mobs Units %"),
	("var_dmg_hero","Damage to Heroes %"),
	("var_all_dmg","All Damage %"),
	("var_elemental_dmg","Elemental Damage %"),
	("var_atk_speed","Attack Speed %"),
	("var_crit_rate","Critic Chance %"),
	("var_crit_dmg","Critic Damage %")
)
saviour_rune_all = (
	("none","None"),
	("flat_trap_resistance","Trap Resistance"),("var_trap_resistance","Trap Resistance %"),
	("flat_projectile_resistance","Projectile Resistance"),("var_projectile_resistance","Projectile Resistance %"),
	("flat_collision_resistance","Collision Resistance"),("var_collision_resistance","Collision Resistance %"),
	("flat_static_resistance","Static Resistance"),("var_static_resistance","Static Resistance %"),
	("flat_front_resistance","Front Resistance"),("var_front_resistance","Front Resistance %"),
	("flat_rear_resistance","Rear Resistance"),("var_rear_resistance","Rear Resistance %"),
	("var_damage_resistance","Damage Resistance %"),
	("dodge","Dodge"),
	("var_elemental_resistance","Elemental Damage reduced"),
	("var_enhanced_eqpm","Enhance Equipment %"),
	("var_control_resistance","Control Resistance %"),
)
recovery_rune_all = (
	("none","None"),
	("flat_heal_red_heart","Healing Effect of Red Heart"),
	("var_heal_red_heart","Healing Effect of Red Heart %"),
	("flat_hp_drop","HP drops"),
	("var_hp_drop","HP drops %"),
	("var_atk_headshot","Attack Increased 3s within HeadShot")
)
courage_rune_all = (
	("none","None"),
	("flat_dmg_flame","Flame Damage"),("var_dmg_flame","Flame Damage %"),
	("flat_dmg_ice","Ice Damage"),("var_dmg_ice","Ice Damage %"),
	("flat_dmg_poison","Poison Damage"),("var_dmg_poison","Poison Damage %"),
	("flat_dmg_lightning","Lightning Damage"),("var_dmg_lightning","Lightning Damage %"),
	("flat_dmg_dark","Dark Touch Damage"),("var_dmg_dark","Dark Touch Damage %"),
)
luck_rune_all = (
	("none","None"),
	("counterattack_rate","Counterattack Rate"),("counterattack_dmg","Counterattack Damage"),
)

all_egg = (
	("Choose","Choose"),
	('Mobs', (("Vase","Vase"),("Green Bat","Green Bat"),("Rock Puppet","Rock Puppet"),("Bomb Ghost","Bomb Ghost"),("Piranha","Piranha"),("Skeleton Archer","Skeleton Archer"),("Tornado Demon","Tornado Demon"),("Party Tree","Party Tree"),("Wasp","Wasp"),("Wolfhound","Wolfhound"),("Scarecrow","Scarecrow"),("Tornado Mage","Tornado Mage"),("Lava Golem","Lava Golem"),("Skull Wizard","Skull Wizard"),("Cactus","Cactus"),("Ice Mage","Ice Mage"),("Shadow Assassin","Shadow Assassin"),("Fire Lizard","Fire Lizard"),("Fire Mage","Fire Mage"),("Fallen Bat","Fallen Bat"),("Steel Dryad","Steel Dryad"),("Ice Golem","Ice Golem"),("Medusa","Medusa"),("Nether Puppet","Nether Puppet"),("Spitting Mushroom","Spitting Mushroom"),("Psionic Scarecrow","Psionic Scarecrow"),("Pea Shooter","Pea Shooter"),("Scythe Mage","Scythe Mage"),("Rolling Mushroom","Rolling Mushroom"),("Skeleton Swordsman","Skeleton Swordsman"),("Sandian","Sandian"),("Savage Spider","Savage Spider"),("Scarlet Mage","Scarlet Mage"),("Thorny Snake","Thorny Snake"),("Long Dragon","Long Dragon"),("Purple Phantom","Purple Phantom"),("Elite Archer","Elite Archer"),("Flaming Bug","Flaming Bug"),("One-eyed Bat","One-eyed Bat"),("Tundra Dragon","Tundra Dragon"),("Zombie","Zombie"),("Crazy Spider","Crazy Spider"),("Icefire Phantom","Icefire Phantom"),("Skeleton Soldier","Skeleton Soldier"),("Flame Ghost","Flame Ghost"),("Fire Element","Fire Element"),("Shark Bro","Shark Bro"),("Crimson Zombie","Crimson Zombie"),("Fat Bat","Fat Bat"),("Plainswolf","Plainswolf"),)),
 	('Boss', (("Little Dragon","Little Dragon"),("Rage Golem","Rage Golem"),("Arch Leader","Arch Leader"),("Krab Boss","Krab Boss"),("Ice Demon","Ice Demon"),("Crimson Witch","Crimson Witch"),("Skeleton King","Skeleton King"),("Giant Owl","Giant Owl"),("Fire Demon","Fire Demon"),("Medusa-Boss","Medusa-Boss"),("Desert Goliath","Desert Goliath"),("Queen Bee","Queen Bee"),("Ice Worm","Ice Worm"),("Sinister Touch","Sinister Touch"),("Scythe Pharoah","Scythe Pharoah"),("Fireworm Queen","Fireworm Queen"),("Infernal Demon","Infernal Demon"),)),)

class parentModel():
	def __init__(self):
		with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
			local_data = json.load(f)
		self.local_data = local_data

class user(models.Model):
	ingame_id = models.CharField(max_length=20,blank=False,unique=True)
	ingame_name = models.CharField(max_length=30,blank=False)
	global_atk_save = models.IntegerField(blank=True, default=0)
	global_hp_save = models.IntegerField(blank=True, default=0)
	choosen_hero = models.CharField(max_length=30 ,choices=all_heros, default="Atreus")
	brave_privileges_level = models.IntegerField(choices=brave_level_choice, default=1)
	atk_base_stats_hero_choosen = models.BigIntegerField(default=100, validators=[MaxValueValidator(6000)])
	health_base_stats_hero_choosen = models.BigIntegerField(default=400, validators=[MaxValueValidator(20000)])
	public_id = models.BigIntegerField(default=0, blank=False)

	def getOtherModels(self):
			return {
				"stuff_table":self.stuff_table_set.get(),
				"hero_table":self.hero_table_set.get(),
				"talent_table":self.talent_table_set.get(),
				"skin_table":self.skin_table_set.get(),
				"altar_table":self.altar_table_set.get(),
				"jewel_type_table":self.jewel_type_table_set.get(),
				"jewel_level_table":self.jewel_level_table_set.get(),
				"egg_table":self.egg_table_set.get(),
				"egg_equipped_table":self.egg_equipped_table_set.get(),
				"dragon_table":self.dragon_table_set.get(),
				"runes_table":self.runes_table_set.get(),
				"reforge_table":self.reforge_table_set.get(),
				"refine_table":self.refine_table_set.get(),
				"medals_table":self.medals_table_set.get(),
				"relics_table":self.relics_table_set.get(),
				"weapon_skins_table":self.weapon_skins_table_set.get(),
			}

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

class stuff_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	weapon_choosen = models.CharField(max_length=20 ,choices=stuff_weapon, default="None")
	weapon_level = models.BigIntegerField(default=1, validators=[MaxValueValidator(170)]) 
	weapon_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	armor_choosen = models.CharField(max_length=20 ,choices=stuff_armor, default="None")
	armor_level = models.BigIntegerField(default=1, validators=[MaxValueValidator(170)]) 
	armor_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	ring1_choosen = models.CharField(max_length=20 ,choices=stuff_ring, default="None")
	ring1_level = models.BigIntegerField(default=1, validators=[MaxValueValidator(170)]) 
	ring1_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	ring2_choosen = models.CharField(max_length=20 ,choices=stuff_ring, default="None")
	ring2_level = models.BigIntegerField(default=1, validators=[MaxValueValidator(170)]) 
	ring2_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	pet1_choosen = models.CharField(max_length=20 ,choices=stuff_pet, default="None")
	pet1_level = models.BigIntegerField(default=1, validators=[MaxValueValidator(170)]) 
	pet1_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	pet2_choosen = models.CharField(max_length=20 ,choices=stuff_pet, default="None")
	pet2_level = models.BigIntegerField(default=1, validators=[MaxValueValidator(170)]) 
	pet2_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	bracelet_choosen = models.CharField(max_length=20 ,choices=stuff_bracelet, default="None")
	bracelet_level = models.BigIntegerField(default=1, validators=[MaxValueValidator(170)]) 
	bracelet_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	locket_choosen = models.CharField(max_length=20 ,choices=stuff_locket, default="None")
	locket_level = models.BigIntegerField(default=1, validators=[MaxValueValidator(170)]) 
	locket_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")
	book_choosen = models.CharField(max_length=20 ,choices=stuff_book, default="None")
	book_level = models.BigIntegerField(default=1, validators=[MaxValueValidator(170)]) 
	book_rarity = models.CharField(max_length=20 ,choices=stuff_rarity, default="Common")

	def dictionnaire(self):
			return {
					"user_profile": self.user_profile,
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
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine

	def getWeaponCoeff(self):
		return int(self.local_data["WeaponHiddenStats"][self.weapon_choosen.lower().replace(" ","_") + "_dmg_multiplier"])

	def GetRawStats(self):
		rarity_index = {
			"common":0,
			"great":1,
			"rare":2,
			"epic":3,
			"perfect_epic":4,
			"legendary":5,
			"ancient_legendary":6,
			"mythic":7,
			"mythic_1":8,
			"mythic_2":9,
			"titan_tales":10,
			"titan_tales_1":11,
			"titan_tales_2":12,
			"titan_tales_3":13,
			"chaos":14,
		}
		weapon_name = self.weapon_choosen.replace(" ","_").lower()
		armor_name = self.armor_choosen.replace(" ","_").lower()
		ring_1_name = self.ring1_choosen.replace(" ","_").lower()
		ring_2_name = self.ring2_choosen.replace(" ","_").lower()
		bracelet_name = self.bracelet_choosen.replace(" ","_").lower()
		locket_name = self.locket_choosen.replace(" ","_").lower()
		book_name = self.book_choosen.replace(" ","_").replace("'","").lower()
		weapon_rarity = self.weapon_rarity.replace(" ","_").lower()
		armor_rarity = self.armor_rarity.replace(" ","_").lower()
		ring1_rarity = self.ring1_rarity.replace(" ","_").lower()
		ring2_rarity = self.ring2_rarity.replace(" ","_").lower()
		bracelet_rarity = self.bracelet_rarity.replace(" ","_").lower()
		locket_rarity = self.locket_rarity.replace(" ","_").lower()
		book_rarity = self.book_rarity.replace(" ","_").lower()
		return {
			'weapon_inc_raw' : self.local_data["StatsWeapon"][str(weapon_name)]["inc"][rarity_index[str(weapon_rarity)]],
			'weapon_base_raw' : self.local_data["StatsWeapon"][str(weapon_name)]["base"][rarity_index[str(weapon_rarity)]],
			'weapon_var_raw' : self.local_data["StatsWeapon"][str(weapon_name)]["var_atk"][rarity_index[str(weapon_rarity)]],
			'weapon_crit_raw' : self.local_data["StatsWeapon"][str(weapon_name)]["crit"][rarity_index[str(weapon_rarity)]],
			'weapon_basic_stats' : self.local_data["StatsWeapon"][str(weapon_name)]["basic_stats"][rarity_index[str(weapon_rarity)]],
			'weapon_damage_stats' : self.local_data["StatsWeapon"][str(weapon_name)]["weapon_damage"][rarity_index[str(weapon_rarity)]],

			'armor_inc_raw' : self.local_data["StatsArmor"][str(armor_name)]["inc"][rarity_index[str(armor_rarity)]],
			'armor_base_raw' : self.local_data["StatsArmor"][str(armor_name)]["base"][rarity_index[str(armor_rarity)]],
			'armor_var_raw' : self.local_data["StatsArmor"][str(armor_name)]["var_hp"][rarity_index[str(armor_rarity)]],
			'armor_dodge_raw' : self.local_data["StatsArmor"][str(armor_name)]["dodge"][rarity_index[str(armor_rarity)]],
			'armor_resistance_raw' : self.local_data["StatsArmor"][str(armor_name)]["resistance"][rarity_index[str(armor_rarity)]],
			'armor_basic_stats' : self.local_data["StatsArmor"][str(armor_name)]["basic_stats"][rarity_index[str(armor_rarity)]],
			'armor_resistance_type_raw' : self.local_data["StatsArmor"][str(armor_name)]["resistance_type"],

			'ring1_inc_raw' : self.local_data["StatsRing"][str(ring_1_name)]["inc"][rarity_index[str(ring1_rarity)]],
			'ring1_base_raw' : self.local_data["StatsRing"][str(ring_1_name)]["base"][rarity_index[str(ring1_rarity)]],
			'ring1_hp_raw' : self.local_data["StatsRing"][str(ring_1_name)]["hp"][rarity_index[str(ring1_rarity)]],
			'ring1_atk_raw' : self.local_data["StatsRing"][str(ring_1_name)]["atk"][rarity_index[str(ring1_rarity)]],
			'ring1_dodge_raw' : self.local_data["StatsRing"][str(ring_1_name)]["dodge"][rarity_index[str(ring1_rarity)]],
			'ring1_resistance_raw' : self.local_data["StatsRing"][str(ring_1_name)]["resistance"][rarity_index[str(ring1_rarity)]],
			'ring1_crit_chance_raw' : self.local_data["StatsRing"][str(ring_1_name)]["crit_chance"][rarity_index[str(ring1_rarity)]],
			'ring1_crit_damage_raw' : self.local_data["StatsRing"][str(ring_1_name)]["crit_damage"][rarity_index[str(ring1_rarity)]],
			'ring1_mythic_raw' : self.local_data["StatsRing"][str(ring_1_name)]["mythic_boost"][rarity_index[str(ring1_rarity)]],
			'ring1_basic_stats' : self.local_data["StatsRing"][str(ring_1_name)]["basic_stats"][rarity_index[str(ring1_rarity)]],
			'ring1_titan_tales_boost': self.local_data["StatsRing"][str(ring_1_name)]["titan_tales_boost"][rarity_index[str(ring1_rarity)]],
			'ring1_chaos_boost': self.local_data["StatsRing"][str(ring_1_name)]["chaos_boost"][rarity_index[str(ring1_rarity)]],
			'ring1_resistance_type_raw' : self.local_data['StatsRing'][str(ring_1_name)]['resistance_type'],
			'ring1_mythic_type_raw' : self.local_data['StatsRing'][str(ring_1_name)]['mythic_type'],
			'ring1_damage_type_raw' : self.local_data['StatsRing'][str(ring_1_name)]['damage_type'],
			'ring1_titan_tales_type_raw': self.local_data['StatsRing'][str(ring_1_name)]['titan_tales_type'],
			'ring1_chaos_type_raw': self.local_data['StatsRing'][str(ring_1_name)]['chaos_type'],

			'ring2_inc_raw' : self.local_data["StatsRing"][str(ring_2_name)]["inc"][rarity_index[str(ring2_rarity)]],
			'ring2_base_raw' : self.local_data["StatsRing"][str(ring_2_name)]["base"][rarity_index[str(ring2_rarity)]],
			'ring2_hp_raw' : self.local_data["StatsRing"][str(ring_2_name)]["hp"][rarity_index[str(ring2_rarity)]],
			'ring2_atk_raw' : self.local_data["StatsRing"][str(ring_2_name)]["atk"][rarity_index[str(ring2_rarity)]],
			'ring2_dodge_raw' : self.local_data["StatsRing"][str(ring_2_name)]["dodge"][rarity_index[str(ring2_rarity)]],
			'ring2_resistance_raw' : self.local_data["StatsRing"][str(ring_2_name)]["resistance"][rarity_index[str(ring2_rarity)]],
			'ring2_crit_chance_raw' : self.local_data["StatsRing"][str(ring_2_name)]["crit_chance"][rarity_index[str(ring2_rarity)]],
			'ring2_crit_damage_raw' : self.local_data["StatsRing"][str(ring_2_name)]["crit_damage"][rarity_index[str(ring2_rarity)]],
			'ring2_mythic_raw' : self.local_data["StatsRing"][str(ring_2_name)]["mythic_boost"][rarity_index[str(ring2_rarity)]],
			'ring2_basic_stats' : self.local_data["StatsRing"][str(ring_2_name)]["basic_stats"][rarity_index[str(ring2_rarity)]],
			'ring2_titan_tales_boost': self.local_data["StatsRing"][str(ring_2_name)]["titan_tales_boost"][rarity_index[str(ring2_rarity)]],
			'ring2_chaos_boost': self.local_data["StatsRing"][str(ring_2_name)]["chaos_boost"][rarity_index[str(ring2_rarity)]],
			'ring2_resistance_type_raw' : self.local_data['StatsRing'][str(ring_2_name)]['resistance_type'],
			'ring2_mythic_type_raw' : self.local_data['StatsRing'][str(ring_2_name)]['mythic_type'],
			'ring2_damage_type_raw' : self.local_data['StatsRing'][str(ring_2_name)]['damage_type'],
			'ring2_titan_tales_type_raw': self.local_data['StatsRing'][str(ring_2_name)]['titan_tales_type'],
			'ring2_chaos_type_raw': self.local_data['StatsRing'][str(ring_2_name)]['chaos_type'],

			'bracelet_inc_raw' : self.local_data["StatsBracelet"][str(bracelet_name)]["inc"][rarity_index[str(bracelet_rarity)]],
			'bracelet_base_raw' : self.local_data["StatsBracelet"][str(bracelet_name)]["base"][rarity_index[str(bracelet_rarity)]],
			'bracelet_var_raw' : self.local_data["StatsBracelet"][str(bracelet_name)]["var_atk"][rarity_index[str(bracelet_rarity)]],
			'bracelet_crit_raw' : self.local_data["StatsBracelet"][str(bracelet_name)]["crit"][rarity_index[str(bracelet_rarity)]],
			'bracelet_basic_stats' : self.local_data["StatsBracelet"][str(bracelet_name)]["basic_stats"][rarity_index[str(bracelet_rarity)]],

			'locket_inc_raw' : self.local_data["StatsLocket"][str(locket_name)]["inc"][rarity_index[str(locket_rarity)]],
			'locket_base_raw' : self.local_data["StatsLocket"][str(locket_name)]["base"][rarity_index[str(locket_rarity)]],
			'locket_dodge_raw' : self.local_data["StatsLocket"][str(locket_name)]["dodge"][rarity_index[str(locket_rarity)]],
			'locket_var_raw' : self.local_data["StatsLocket"][str(locket_name)]["var_hp"][rarity_index[str(locket_rarity)]],
			'locket_resistance_raw' : self.local_data["StatsLocket"][str(locket_name)]["resistance"][rarity_index[str(locket_rarity)]],
			'locket_basic_stats' : self.local_data["StatsLocket"][str(locket_name)]["basic_stats"][rarity_index[str(locket_rarity)]],
			'locket_resistance_type_raw' : self.local_data["StatsLocket"][str(locket_name)]["resistance_type"],

			'book_inc_raw' : self.local_data["StatsBook"][str(book_name)]["inc"][rarity_index[str(book_rarity)]],
			'book_base_raw' : self.local_data["StatsBook"][str(book_name)]["base"][rarity_index[str(book_rarity)]],
			'book_var_raw' : self.local_data["StatsBook"][str(book_name)]["var_hp"][rarity_index[str(book_rarity)]],
			'book_resistance_raw' : self.local_data["StatsBook"][str(book_name)]["resistance"][rarity_index[str(book_rarity)]],
			'book_resistance2_raw' : self.local_data["StatsBook"][str(book_name)]["resistance2"][rarity_index[str(book_rarity)]],
			'book_basic_stats' : self.local_data["StatsBook"][str(book_name)]["basic_stats"][rarity_index[str(book_rarity)]],
			'book_enhance_eqm' : self.local_data["StatsBook"][str(book_name)]["enhance_eqm"][rarity_index[str(book_rarity)]],
			'book_resistance_type_raw' : self.local_data["StatsBook"][str(book_name)]["resistance_type"],
			'book_resistance2_type_raw' : self.local_data["StatsBook"][str(book_name)]["resistance2_type"]
		}

	def getStuffStats(self,enhanced_equipment_total,weapon_refine_basic_stats,armor_refine_basic_stats,ring1_refine_basic_stats,ring2_refine_basic_stats,bracelet_refine_basic_stats,locket_refine_basic_stats,book_refine_basic_stats,weapon_skin_stats):
		all_raw_stats = self.GetRawStats()
		global_enhance_eqm = enhanced_equipment_total + all_raw_stats['book_enhance_eqm']
		weapon_eh_eq = global_enhance_eqm + float(weapon_refine_basic_stats) + float(all_raw_stats["weapon_basic_stats"])
		weapon_base = math.floor((int(all_raw_stats['weapon_base_raw']) + int(all_raw_stats['weapon_inc_raw']) * ( self.weapon_level-1)) * (weapon_eh_eq))
		weapon_total = math.floor(weapon_base + math.floor(int(weapon_skin_stats['attack']) * (weapon_eh_eq)))

		armor_eh_eq = global_enhance_eqm + float(all_raw_stats["armor_basic_stats"]) + float(armor_refine_basic_stats)
		armor_base = math.floor((int(all_raw_stats['armor_base_raw']) + int(all_raw_stats['armor_inc_raw']) * ( self.armor_level-1)) * (armor_eh_eq))

		ring1_eh_eq = global_enhance_eqm + float(all_raw_stats["ring1_basic_stats"]) + float(ring1_refine_basic_stats)
		ring1_base = math.floor((int(all_raw_stats['ring1_base_raw']) + int(all_raw_stats['ring1_inc_raw']) * ( self.ring1_level-1)) * (ring1_eh_eq))
		
		ring2_eh_eq = global_enhance_eqm + float(all_raw_stats["ring2_basic_stats"]) + float(ring2_refine_basic_stats)
		ring2_base = math.floor((int(all_raw_stats['ring2_base_raw']) + int(all_raw_stats['ring2_inc_raw']) * ( self.ring2_level-1)) * (ring2_eh_eq))

		bracelet_eh_eq = global_enhance_eqm + float(all_raw_stats["bracelet_basic_stats"]) + float(bracelet_refine_basic_stats)
		bracelet_base = math.floor((int(all_raw_stats['bracelet_base_raw']) + int(all_raw_stats['bracelet_inc_raw']) * ( self.bracelet_level-1)) * (bracelet_eh_eq))

		locket_eh_eq = global_enhance_eqm + float(all_raw_stats["locket_basic_stats"]) + float(locket_refine_basic_stats)
		locket_base = math.floor((int(all_raw_stats['locket_base_raw']) + int(all_raw_stats['locket_inc_raw']) * ( self.locket_level-1)) * (locket_eh_eq))

		book_eh_eq = global_enhance_eqm + float(all_raw_stats["book_basic_stats"]) + float(book_refine_basic_stats)
		book_base = math.floor((int(all_raw_stats['book_base_raw']) + int(all_raw_stats['book_inc_raw']) * ( self.book_level-1)) * (book_eh_eq))
		return {
			"weapon_attack_var" : float(all_raw_stats['weapon_var_raw'])/100,
			"weapon_total" : weapon_total,
			"armor_hp_var" : float(all_raw_stats['armor_var_raw'])/100,
			"armor_total" : armor_base,
			"ring1_atk_var" : float(all_raw_stats['ring1_atk_raw'])/100,
			"ring1_hp_var" : float(all_raw_stats['ring1_hp_raw'])/100,
			"ring1_total" : ring1_base,
			"ring2_atk_var" : float(all_raw_stats['ring2_atk_raw'])/100,
			"ring2_hp_var" : float(all_raw_stats['ring2_hp_raw'])/100,
			"ring2_total" : ring2_base,
			"bracelet_attack_var" : float(all_raw_stats['bracelet_var_raw'])/100,
			"bracelet_total" : bracelet_base,
			"locket_hp_var" : float(all_raw_stats['locket_var_raw'])/100,
			"locket_total" : locket_base,
			"book_hp_var" : float(all_raw_stats['book_var_raw'])/100,
			"book_total" : book_base,
			## RING ADDIOTIONNAL STATS
			all_raw_stats['ring1_damage_type_raw']:ring1_base,
			all_raw_stats['ring1_titan_tales_type_raw']:all_raw_stats['ring1_titan_tales_boost'],
			all_raw_stats['ring1_chaos_type_raw']:all_raw_stats['ring1_chaos_boost'],
			all_raw_stats['ring2_damage_type_raw']:ring2_base,
			all_raw_stats['ring2_titan_tales_type_raw']:all_raw_stats['ring2_titan_tales_boost'],
			all_raw_stats['ring2_chaos_type_raw']:all_raw_stats['ring2_chaos_boost'],
		}


class hero_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	atreus_level = models.IntegerField(choices=hero_level, default=0)
	atreus_star = models.IntegerField(choices=star_hero, default=0) 
	urasil_level = models.IntegerField(choices=hero_level, default=0)
	urasil_star = models.IntegerField(choices=star_hero, default=0)
	phoren_level = models.IntegerField(choices=hero_level, default=0)
	phoren_star = models.IntegerField(choices=star_hero, default=0)
	taranis_level = models.IntegerField(choices=hero_level, default=0)
	taranis_star = models.IntegerField(choices=star_hero, default=0)
	helix_level = models.IntegerField(choices=hero_level, default=0)
	helix_star = models.IntegerField(choices=star_hero, default=0) 
	meowgik_level = models.IntegerField(choices=hero_level, default=0)
	meowgik_star = models.IntegerField(choices=star_hero, default=0)
	shari_level = models.IntegerField(choices=hero_level, default=0)
	shari_star = models.IntegerField(choices=star_hero, default=0)
	ayana_level = models.IntegerField(choices=hero_level, default=0)
	ayana_star = models.IntegerField(choices=star_hero, default=0)
	onir_level = models.IntegerField(choices=hero_level, default=0)
	onir_star = models.IntegerField(choices=star_hero, default=0)
	rolla_level = models.IntegerField(choices=hero_level, default=0)
	rolla_star = models.IntegerField(choices=star_hero, default=0)
	bonnie_level = models.IntegerField(choices=hero_level, default=0)
	bonnie_star = models.IntegerField(choices=star_hero, default=0)
	sylvan_level = models.IntegerField(choices=hero_level, default=0)
	sylvan_star = models.IntegerField(choices=star_hero, default=0)
	shade_level = models.IntegerField(choices=hero_level, default=0)
	shade_star = models.IntegerField(choices=star_hero, default=0) 
	ophelia_level = models.IntegerField(choices=hero_level, default=0)
	ophelia_star = models.IntegerField(choices=star_hero, default=0)
	ryan_level = models.IntegerField(choices=hero_level, default=0)
	ryan_star = models.IntegerField(choices=star_hero, default=0)
	lina_level = models.IntegerField(choices=hero_level, default=0)
	lina_star = models.IntegerField(choices=star_hero, default=0)
	aquea_level = models.IntegerField(choices=hero_level, default=0)
	aquea_star = models.IntegerField(choices=star_hero, default=0)
	shingen_level = models.IntegerField(choices=hero_level, default=0)
	shingen_star = models.IntegerField(choices=star_hero, default=0) 
	gugu_level = models.IntegerField(choices=hero_level, default=0)
	gugu_star = models.IntegerField(choices=star_hero, default=0)
	iris_level = models.IntegerField(choices=hero_level, default=0)
	iris_star = models.IntegerField(choices=star_hero, default=0)
	blazo_level = models.IntegerField(choices=hero_level, default=0)
	blazo_star = models.IntegerField(choices=star_hero, default=0)
	melinda_level = models.IntegerField(choices=hero_level, default=0)
	melinda_star = models.IntegerField(choices=star_hero, default=0)
	elaine_level = models.IntegerField(choices=hero_level, default=0)
	elaine_star = models.IntegerField(choices=star_hero, default=0)
	bobo_level = models.IntegerField(choices=hero_level, default=0)
	bobo_star = models.IntegerField(choices=star_hero, default=0)
	stella_level = models.IntegerField(choices=hero_level, default=0)
	stella_star = models.IntegerField(choices=star_hero, default=0)


	def dictionnaire(self):
			return {
					"user_profile": self.user_profile,
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
					'bobo_level': self.bobo_level, 'bobo_star': self.bobo_star,
					'stella_level': self.stella_level, 'stella_star': self.stella_star,
					}
	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine
	

	def HerosStatsRecup(self,hero):
		choosen_hero = user.objects.get(ingame_id=self.user_profile.ingame_id).choosen_hero
		heros_star = self.dictionnaire()
		hero_lower = str(hero).lower()
		stats_hero_star  = self.local_data["HerosStats"][hero_lower + "_star_" + str(heros_star[f"{hero_lower}_star"]).replace("","")]
		stats_hero_lvl  = self.local_data["HerosStats"][hero_lower + "_" + str(heros_star[f"{hero_lower}_level"])]
		if hero != "Shari":
			Blvl20 = stats_hero_lvl[0]
			Blvl60 = stats_hero_lvl[2]
			Blvl120 = stats_hero_lvl[4]
			Bs2 = stats_hero_star[0]
			Bs7 = stats_hero_star[1]
			Bs8 = stats_hero_star[2]
			if hero != choosen_hero:
				Blvl40 = 0
				Blvl80 = 0
			else:
				Blvl40 = stats_hero_lvl[1]
				Blvl80 = stats_hero_lvl[3]
		else:
			Blvl40 = stats_hero_lvl[1]
			Blvl80 = stats_hero_lvl[3]
			Blvl120 = stats_hero_lvl[4]
			Bs2 = stats_hero_star[0]
			Bs7 = stats_hero_star[1]
			Bs8 = stats_hero_star[2]
			if hero != choosen_hero:
				Blvl20 = 0
				Blvl60 = 0
			else:
				Blvl20 = stats_hero_lvl[0]
				Blvl60 = stats_hero_lvl[2]
		return Blvl20, Blvl40, Blvl60, Blvl80, Blvl120, Bs2, Bs7, Bs8


class talent_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	strength_level = models.IntegerField(validators=[MaxValueValidator(25)], default=1)
	power_level = models.IntegerField(validators=[MaxValueValidator(25)], default=1)
	recover_level = models.IntegerField(validators=[MaxValueValidator(25)], default=1)
	block_level = models.IntegerField(validators=[MaxValueValidator(25)], default=1)
	iron_bulwark_level = models.IntegerField(validators=[MaxValueValidator(25)], default=1)
	enhanced_equipment_level = models.IntegerField(validators=[MaxValueValidator(10)], default=1)
	hero_power_up_level = models.IntegerField(validators=[MaxValueValidator(10)], default=1)
	runes_power_up_level = models.IntegerField(validators=[MaxValueValidator(15)], default=1)

	def dictionnaire(self):
			return {
					"user_profile": self.user_profile,
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
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine
	
	def getTalentStats(self):
		TalentStats = self.local_data["TalentStats"]
		return {
			"talents_strength": TalentStats["strength_" + str(self.strength_level)],
			"talents_power": TalentStats["power_" + str(self.power_level)],
			"talents_recover": TalentStats["recover_" + str(self.recover_level)],
			"talents_block": TalentStats["block_" + str(self.block_level)],
			"talents_iron_bulwark": TalentStats["iron_bulwark_" + str(self.iron_bulwark_level)],
			"talents_enhanced_equipment": TalentStats["enhanced_equipment_" + str(self.enhanced_equipment_level)],
			"talents_hero_power_up": TalentStats["hero_power_up_" + str(self.hero_power_up_level)],
		}


class skin_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	skin_health = models.IntegerField(default=0)
	skin_attack = models.IntegerField(default=0)

	def dictionnaire(self):
			return {
					"user_profile": self.user_profile,
					'skin_health': self.skin_health,
					'skin_attack': self.skin_attack,
					}
	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine



class altar_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	stuff_altar_level = models.IntegerField(default=0, validators=[MaxValueValidator(120)]) 
	stuff_altar_ascension = models.IntegerField(choices=altar_ascension_level, default=0)
	heros_altar_level = models.IntegerField(default=0, validators=[MaxValueValidator(120)]) 
	heros_altar_ascension = models.IntegerField(choices=altar_ascension_level, default=0)
	
	def dictionnaire(self):
			return {
					"user_profile": self.user_profile,
					'stuff_altar_level': self.stuff_altar_level, 
					'stuff_altar_ascension': self.stuff_altar_ascension, 
					'heros_altar_level': self.heros_altar_level, 
					'heros_altar_ascension': self.heros_altar_ascension,
					}
	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine
	
	def RoundTen(self,x):
		if int(x) % 10==0:
			x = x
		else:
			while int(x) % 10>0:
				x=x-1
		return x

	def CalculAltar(self,type_altar,type_boost):
		if type_altar == "stuff":
			data = self.local_data["StuffAltar"]
		elif type_altar == "heros":
			data = self.local_data["HerosAltar"]
		base = int(data[str(self.RoundTen(self.dictionnaire()[type_altar+'_altar_level'])) + '_' + type_boost])
		level = int(self.dictionnaire()[type_altar+'_altar_level'])
		levelRoundTen = int(self.RoundTen(self.dictionnaire()[type_altar+'_altar_level']))
		inc = int(data[str(self.RoundTen(self.dictionnaire()[type_altar+'_altar_level'])) + '_inc_' + type_boost])
		diff = level - levelRoundTen
		if 1 <= diff <= 9:
			total = base+((level - levelRoundTen)*inc)
		else:
			total = base
		return total


class jewel_type_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	weapon_jewel1_type = models.CharField(max_length=10, choices=atk_jewel, default="none")
	weapon_jewel2_type = models.CharField(max_length=10, choices=atk_jewel, default="none")
	weapon_jewel3_type = models.CharField(max_length=10, choices=atk_jewel, default="none")
	weapon_jewel4_type = models.CharField(max_length=10, choices=atk_jewel, default="none")
	armor_jewel1_type = models.CharField(max_length=10, choices=defense_jewel, default="none")
	armor_jewel2_type = models.CharField(max_length=10, choices=defense_jewel, default="none")
	armor_jewel3_type = models.CharField(max_length=10, choices=defense_jewel, default="none")
	armor_jewel4_type = models.CharField(max_length=10, choices=defense_jewel, default="none")
	ring1_jewel1_type = models.CharField(max_length=10, choices=resistance_jewel, default="none")
	ring1_jewel2_type = models.CharField(max_length=10, choices=resistance_jewel, default="none")
	ring1_jewel3_type = models.CharField(max_length=10, choices=resistance_jewel, default="none")
	ring1_jewel4_type = models.CharField(max_length=10, choices=resistance_jewel, default="none") 
	ring2_jewel1_type = models.CharField(max_length=10, choices=resistance_jewel, default="none")
	ring2_jewel2_type = models.CharField(max_length=10, choices=resistance_jewel, default="none")
	ring2_jewel3_type = models.CharField(max_length=10, choices=resistance_jewel, default="none")
	ring2_jewel4_type = models.CharField(max_length=10, choices=resistance_jewel, default="none") 
	pet1_jewel1_type = models.CharField(max_length=10, choices=atk_jewel, default="none")
	pet1_jewel2_type = models.CharField(max_length=10, choices=atk_jewel, default="none")
	pet1_jewel3_type = models.CharField(max_length=10, choices=atk_jewel, default="none")
	pet1_jewel4_type = models.CharField(max_length=10, choices=atk_jewel, default="none")
	pet2_jewel1_type = models.CharField(max_length=10, choices=defense_jewel, default="none")
	pet2_jewel2_type = models.CharField(max_length=10, choices=defense_jewel, default="none")
	pet2_jewel3_type = models.CharField(max_length=10, choices=defense_jewel, default="none")
	pet2_jewel4_type = models.CharField(max_length=10, choices=defense_jewel, default="none")
	bracelet_jewel1_type = models.CharField(max_length=10, choices=mix_defense_resistance, default="none")
	bracelet_jewel2_type = models.CharField(max_length=10, choices=mix_defense_resistance, default="none")
	bracelet_jewel3_type = models.CharField(max_length=10, choices=mix_defense_resistance, default="none")
	bracelet_jewel4_type = models.CharField(max_length=10, choices=mix_defense_resistance, default="none")
	locket_jewel1_type = models.CharField(max_length=10, choices=mix_atk_resistance, default="none")
	locket_jewel2_type = models.CharField(max_length=10, choices=mix_atk_resistance, default="none")
	locket_jewel3_type = models.CharField(max_length=10, choices=mix_atk_resistance, default="none")
	locket_jewel4_type = models.CharField(max_length=10, choices=mix_atk_resistance, default="none")
	book_jewel1_type = models.CharField(max_length=10, choices=mix_atk_defense, default="none")
	book_jewel2_type = models.CharField(max_length=10, choices=mix_atk_defense, default="none")
	book_jewel3_type = models.CharField(max_length=10, choices=mix_atk_defense, default="none")
	book_jewel4_type = models.CharField(max_length=10, choices=mix_atk_defense, default="none")
	
	def dictionnaire(self):
			return {
					"user_profile": self.user_profile,
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
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine


class jewel_level_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	weapon_jewel1_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	weapon_jewel2_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	weapon_jewel3_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	weapon_jewel4_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	armor_jewel1_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	armor_jewel2_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	armor_jewel3_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	armor_jewel4_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	ring1_jewel1_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	ring1_jewel2_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	ring1_jewel3_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	ring1_jewel4_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)]) 
	ring2_jewel1_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	ring2_jewel2_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	ring2_jewel3_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	ring2_jewel4_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)]) 
	pet1_jewel1_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	pet1_jewel2_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	pet1_jewel3_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	pet1_jewel4_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	pet2_jewel1_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	pet2_jewel2_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	pet2_jewel3_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	pet2_jewel4_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	bracelet_jewel1_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	bracelet_jewel2_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	bracelet_jewel3_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	bracelet_jewel4_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	locket_jewel1_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	locket_jewel2_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	locket_jewel3_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	locket_jewel4_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	book_jewel1_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	book_jewel2_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	book_jewel3_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	book_jewel4_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(13)])
	
	def dictionnaire(self):
			return {
					"user_profile": self.user_profile,
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
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine

	def JewelStatsRecup(self,attack_jewel_base:float):
		jewel_type = list(jewel_type_table.objects.get(user_profile=self.user_profile).dictionnaire().values())
		jewel_level = list(self.dictionnaire().values())
		list_type = []
		JewelStats = self.local_data['JewelStats']
		for i in range(0,len(jewel_type)):
			list_type.append(str(jewel_type[i]) + "_" + str(jewel_level[i]))
		try:
			list_type.remove(str(self.user_profile.ingame_id)+"_"+str(self.user_profile.ingame_id))
		except:
			pass
		###### BONUS 1 ######
		atk_ruby = 0
		atk_kunzite = 0
		atk_tourmaline = 0
		pv_lapis = 0
		pv_emerald = 0
		proj_res_topaz = 0
		front_res_amber = 0
		collision_res_amethyst = 0
		pv_calaite = 0
		###### BONUS 2 ######
		dmg_to_boss = 0
		dmg_to_mobs = 0
		dmg_to_elite = 0
		red_he_lapis = 0
		drop_pv_emerald = 0
		crit_dmg_topaz = 0
		elementary_dmg_amber = 0
		pm_when_hurt_amethyst = 0
		mp_max_calaite = 0
		###### BONUS 3 ######
		weapon_ranged_damage = 0
		counterattack_rate = 0

		for x in list_type:
			a = x.split("_")[0]
			if a == "ruby":
				ruby_b1 = atk_ruby
				ruby_b2 = dmg_to_boss
				atk_ruby = int(JewelStats["ruby_lvl" + str(x.split("_")[1]) + "_bonus1"])
				dmg_to_boss = int(JewelStats["ruby_lvl" + str(x.split("_")[1]) + "_bonus2"])
				atk_ruby += ruby_b1
				dmg_to_boss +=  ruby_b2
			if a == "kunzite":
				kunzite_b1 = atk_kunzite
				kunzite_b2 = dmg_to_mobs
				atk_kunzite = int(JewelStats["kunzite_lvl" + str(x.split("_")[1]) + "_bonus1"])
				dmg_to_mobs = int(JewelStats["kunzite_lvl" + str(x.split("_")[1]) + "_bonus2"])
				atk_kunzite += kunzite_b1
				dmg_to_mobs +=  kunzite_b2
			if a == "tourmaline":
				tourmaline_b1 = atk_tourmaline
				tourmaline_b2 = dmg_to_elite
				tourmaline_b3 = weapon_ranged_damage
				atk_tourmaline = int(JewelStats["tourmaline_lvl" + str(x.split("_")[1]) + "_bonus1"])
				dmg_to_elite = int(JewelStats["tourmaline_lvl" + str(x.split("_")[1]) + "_bonus2"])
				weapon_ranged_damage = float(JewelStats["tourmaline_lvl" + str(x.split("_")[1]) + "_bonus3"])
				atk_tourmaline += tourmaline_b1
				dmg_to_elite +=  tourmaline_b2
				weapon_ranged_damage += tourmaline_b3
			if a == "lapis":
				lapis_b1 = pv_lapis
				lapis_b2 = red_he_lapis
				pv_lapis = int(JewelStats["lapis_lvl" + str(x.split("_")[1]) + "_bonus1"])
				red_he_lapis = int(JewelStats["lapis_lvl" + str(x.split("_")[1]) + "_bonus2"])
				pv_lapis += lapis_b1
				red_he_lapis +=  lapis_b2
			if a == "emerald":
				emerald_b1 = pv_emerald
				emerald_b2 = drop_pv_emerald
				pv_emerald = int(JewelStats["emerald_lvl" + str(x.split("_")[1]) + "_bonus1"])
				drop_pv_emerald = int(JewelStats["emerald_lvl" + str(x.split("_")[1]) + "_bonus2"])
				pv_emerald += emerald_b1
				drop_pv_emerald +=  emerald_b2
			if a == "topaz":
				topaz_b1 = proj_res_topaz
				topaz_b2 = crit_dmg_topaz
				proj_res_topaz = int(JewelStats["topaz_lvl" + str(x.split("_")[1]) + "_bonus1"])
				crit_dmg_topaz = int(JewelStats["topaz_lvl" + str(x.split("_")[1]) + "_bonus2"])
				proj_res_topaz += topaz_b1
				crit_dmg_topaz +=  topaz_b2
			if a == "amber":
				amber_b1 = front_res_amber
				amber_b2 = elementary_dmg_amber
				front_res_amber = int(JewelStats["amber_lvl" + str(x.split("_")[1]) + "_bonus1"])
				elementary_dmg_amber = float(JewelStats["amber_lvl" + str(x.split("_")[1]) + "_bonus2"])
				front_res_amber += amber_b1
				elementary_dmg_amber +=  amber_b2
			if a == "amethyst":
				amethyst_b1 = collision_res_amethyst
				amethyst_b2 = pm_when_hurt_amethyst
				amethyst_b3 = counterattack_rate
				collision_res_amethyst = int(JewelStats["amethyst_lvl" + str(x.split("_")[1]) + "_bonus1"])
				pm_when_hurt_amethyst = int(JewelStats["amethyst_lvl" + str(x.split("_")[1]) + "_bonus2"])
				counterattack_rate = float(JewelStats["amethyst_lvl" + str(x.split("_")[1]) + "_bonus3"])
				collision_res_amethyst += amethyst_b1
				pm_when_hurt_amethyst +=  amethyst_b2
				counterattack_rate +=  amethyst_b3
			if a == "calaite":
				calaite_b1 = pv_calaite
				calaite_b2 = mp_max_calaite
				pv_calaite = int(JewelStats["calaite_lvl" + str(x.split("_")[1]) + "_bonus1"])
				mp_max_calaite = int(JewelStats["calaite_lvl" + str(x.split("_")[1]) + "_bonus2"])
				pv_calaite += calaite_b1
				mp_max_calaite +=  calaite_b2
		return {
			'attack_ruby':math.floor(atk_ruby*(1+attack_jewel_base/100)),
			'attack_kunzite':math.floor(atk_kunzite*(1+attack_jewel_base/100)),
			'attack_tourmaline':math.floor(atk_tourmaline*(1+attack_jewel_base/100)),
			'pv_lapis':pv_lapis,
			'pv_emerald':pv_emerald,
			'proj_res_topaz':proj_res_topaz,
			'front_res_amber':front_res_amber,
			'collision_res_amethyst':collision_res_amethyst,
			'pv_calaite':pv_calaite,
			'dmg_to_boss':dmg_to_boss,
			'dmg_to_mobs':dmg_to_mobs,
			'dmg_to_elite':dmg_to_elite,
			'red_he_lapis':red_he_lapis,
			'drop_pv_emerald':drop_pv_emerald,
			'crit_dmg_topaz':crit_dmg_topaz,
			'elementary_dmg_amber':elementary_dmg_amber,
			'pm_when_hurt_amethyst':pm_when_hurt_amethyst,
			'mp_max_calaite':mp_max_calaite,
			'weapon_ranged_damage':weapon_ranged_damage,
			'counterattack_rate':counterattack_rate,
		}

	def JewelSpeBonusStatsRecup(self,type_jewel,brave_boost):
		JewelSpeBonus = self.local_data['JewelSpeBonus']
		jewel_type = jewel_type_table.objects.get(user_profile=self.user_profile).dictionnaire()
		jewel1_type = jewel_type[str(type_jewel)+"_jewel1_type"]
		jewel2_type = jewel_type[str(type_jewel)+"_jewel2_type"]
		jewel3_type = jewel_type[str(type_jewel)+"_jewel3_type"]
		jewel4_type = jewel_type[str(type_jewel)+"_jewel4_type"]
		jewel1_level = self.dictionnaire()[str(type_jewel)+"_jewel1_level"] if jewel1_type != "none" else 0
		jewel2_level = self.dictionnaire()[str(type_jewel)+"_jewel2_level"] if jewel2_type != "none" else 0
		jewel3_level = self.dictionnaire()[str(type_jewel)+"_jewel3_level"] if jewel3_type != "none" else 0
		jewel4_level = self.dictionnaire()[str(type_jewel)+"_jewel4_level"] if jewel4_type != "none" else 0

		result = int(jewel1_level) + int(jewel2_level) + int(jewel3_level) + int(jewel4_level) + int(brave_boost)
		if result >= 4:
			spe_bonus = JewelSpeBonus[str(type_jewel) + "_sb_lvl4"]
			if result >= 8:
				spe_bonus = JewelSpeBonus[str(type_jewel) + "_sb_lvl8"]
				if result >= 16:
					spe_bonus = JewelSpeBonus[str(type_jewel) + "_sb_lvl16"]
					if result >= 28:
						spe_bonus = JewelSpeBonus[str(type_jewel) + "_sb_lvl28"]
						if result >= 38:
							spe_bonus = JewelSpeBonus[str(type_jewel) + "_sb_lvl38"]
							if result >= 48:
								spe_bonus = JewelSpeBonus[str(type_jewel) + "_sb_lvl48"]
		else:
			spe_bonus = [0,0,0,0,0,0]
		return spe_bonus

	def allLevelForImage(self):
		jewel_type = jewel_type_table.objects.get(user_profile=self.user_profile).dictionnaire()
		weapon_jewel1_level = self.weapon_jewel1_level if jewel_type['weapon_jewel1_type'] != "none" else 0
		weapon_jewel2_level = self.weapon_jewel2_level if jewel_type['weapon_jewel2_type'] != "none" else 0
		weapon_jewel3_level = self.weapon_jewel3_level if jewel_type['weapon_jewel3_type'] != "none" else 0
		weapon_jewel4_level = self.weapon_jewel4_level if jewel_type['weapon_jewel4_type'] != "none" else 0
		armor_jewel1_level = self.armor_jewel1_level if jewel_type['armor_jewel1_type'] != "none" else 0
		armor_jewel2_level = self.armor_jewel2_level if jewel_type['armor_jewel2_type'] != "none" else 0
		armor_jewel3_level = self.armor_jewel3_level if jewel_type['armor_jewel3_type'] != "none" else 0
		armor_jewel4_level = self.armor_jewel4_level if jewel_type['armor_jewel4_type'] != "none" else 0
		ring1_jewel1_level = self.ring1_jewel1_level if jewel_type['ring1_jewel1_type'] != "none" else 0
		ring1_jewel2_level = self.ring1_jewel2_level if jewel_type['ring1_jewel2_type'] != "none" else 0
		ring1_jewel3_level = self.ring1_jewel3_level if jewel_type['ring1_jewel3_type'] != "none" else 0
		ring1_jewel4_level = self.ring1_jewel4_level if jewel_type['ring1_jewel4_type'] != "none" else 0
		ring2_jewel1_level = self.ring2_jewel1_level if jewel_type['ring2_jewel1_type'] != "none" else 0
		ring2_jewel2_level = self.ring2_jewel2_level if jewel_type['ring2_jewel2_type'] != "none" else 0
		ring2_jewel3_level = self.ring2_jewel3_level if jewel_type['ring2_jewel3_type'] != "none" else 0
		ring2_jewel4_level = self.ring2_jewel4_level if jewel_type['ring2_jewel4_type'] != "none" else 0
		pet1_jewel1_level = self.pet1_jewel1_level if jewel_type['pet1_jewel1_type'] != "none" else 0
		pet1_jewel2_level = self.pet1_jewel2_level if jewel_type['pet1_jewel2_type'] != "none" else 0
		pet1_jewel3_level = self.pet1_jewel3_level if jewel_type['pet1_jewel3_type'] != "none" else 0
		pet1_jewel4_level = self.pet1_jewel4_level if jewel_type['pet1_jewel4_type'] != "none" else 0
		pet2_jewel1_level = self.pet2_jewel1_level if jewel_type['pet2_jewel1_type'] != "none" else 0
		pet2_jewel2_level = self.pet2_jewel2_level if jewel_type['pet2_jewel2_type'] != "none" else 0
		pet2_jewel3_level = self.pet2_jewel3_level if jewel_type['pet2_jewel3_type'] != "none" else 0
		pet2_jewel4_level = self.pet2_jewel4_level if jewel_type['pet2_jewel4_type'] != "none" else 0
		bracelet_jewel1_level = self.bracelet_jewel1_level if jewel_type['bracelet_jewel1_type'] != "none" else 0
		bracelet_jewel2_level = self.bracelet_jewel2_level if jewel_type['bracelet_jewel2_type'] != "none" else 0
		bracelet_jewel3_level = self.bracelet_jewel3_level if jewel_type['bracelet_jewel3_type'] != "none" else 0
		bracelet_jewel4_level = self.bracelet_jewel4_level if jewel_type['bracelet_jewel4_type'] != "none" else 0
		locket_jewel1_level = self.locket_jewel1_level if jewel_type['locket_jewel1_type'] != "none" else 0
		locket_jewel2_level = self.locket_jewel2_level if jewel_type['locket_jewel2_type'] != "none" else 0
		locket_jewel3_level = self.locket_jewel3_level if jewel_type['locket_jewel3_type'] != "none" else 0
		locket_jewel4_level = self.locket_jewel4_level if jewel_type['locket_jewel4_type'] != "none" else 0
		book_jewel1_level = self.book_jewel1_level if jewel_type['book_jewel1_type'] != "none" else 0
		book_jewel2_level = self.book_jewel2_level if jewel_type['book_jewel2_type'] != "none" else 0
		book_jewel3_level = self.book_jewel3_level if jewel_type['book_jewel3_type'] != "none" else 0
		book_jewel4_level = self.book_jewel4_level if jewel_type['book_jewel4_type'] != "none" else 0
		return {
			"jewel_lvl_weapon":int(weapon_jewel1_level) + int(weapon_jewel2_level) + int(weapon_jewel3_level) + int(weapon_jewel4_level),
			"jewel_lvl_armor":int(armor_jewel1_level) + int(armor_jewel2_level) + int(armor_jewel3_level) + int(armor_jewel4_level),
			"jewel_lvl_ring1":int(ring1_jewel1_level) + int(ring1_jewel2_level) + int(ring1_jewel3_level) + int(ring1_jewel4_level),
			"jewel_lvl_ring2":int(ring2_jewel1_level) + int(ring2_jewel2_level) + int(ring2_jewel3_level) + int(ring2_jewel4_level),
			"jewel_lvl_pet1":int(pet1_jewel1_level) + int(pet1_jewel2_level) + int(pet1_jewel3_level) + int(pet1_jewel4_level),
			"jewel_lvl_pet2":int(pet2_jewel1_level) + int(pet2_jewel2_level) + int(pet2_jewel3_level) + int(pet2_jewel4_level),
			"jewel_lvl_bracelet":int(bracelet_jewel1_level) + int(bracelet_jewel2_level) + int(bracelet_jewel3_level) + int(bracelet_jewel4_level),
			"jewel_lvl_locket":int(locket_jewel1_level) + int(locket_jewel2_level) + int(locket_jewel3_level) + int(locket_jewel4_level),
			"jewel_lvl_book":int(book_jewel1_level) + int(book_jewel2_level) + int(book_jewel3_level) + int(book_jewel4_level),
		}




class egg_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	green_bat = models.IntegerField(choices=level_egg_mobs, default=0)
	vase = models.IntegerField(choices=level_egg_mobs, default=0)
	bomb_ghost = models.IntegerField(choices=level_egg_mobs, default=0)
	rock_puppet = models.IntegerField(choices=level_egg_mobs, default=0)
	party_tree = models.IntegerField(choices=level_egg_mobs, default=0)
	wolfhound = models.IntegerField(choices=level_egg_mobs, default=0)
	skeleton_archer = models.IntegerField(choices=level_egg_mobs, default=0)
	skeleton_soldier = models.IntegerField(choices=level_egg_mobs, default=0)
	wasp = models.IntegerField(choices=level_egg_mobs, default=0)
	fire_mage = models.IntegerField(choices=level_egg_mobs, default=0)
	medusa = models.IntegerField(choices=level_egg_mobs, default=0)
	ice_mage = models.IntegerField(choices=level_egg_mobs, default=0)
	fire_lizard = models.IntegerField(choices=level_egg_mobs, default=0)
	flame_ghost = models.IntegerField(choices=level_egg_mobs, default=0)
	thorny_snake = models.IntegerField(choices=level_egg_mobs, default=0)
	tornado_demon = models.IntegerField(choices=level_egg_mobs, default=0)
	piranha = models.IntegerField(choices=level_egg_mobs, default=0)
	zombie = models.IntegerField(choices=level_egg_mobs, default=0)
	scarecrow = models.IntegerField(choices=level_egg_mobs, default=0)
	long_dragon = models.IntegerField(choices=level_egg_mobs, default=0)
	skull_wizard = models.IntegerField(choices=level_egg_mobs, default=0)
	lava_golem = models.IntegerField(choices=level_egg_mobs, default=0)
	ice_golem = models.IntegerField(choices=level_egg_mobs, default=0)
	cactus = models.IntegerField(choices=level_egg_mobs, default=0)
	crazy_spider = models.IntegerField(choices=level_egg_mobs, default=0)
	fire_element = models.IntegerField(choices=level_egg_mobs, default=0)
	skeleton_swordsman = models.IntegerField(choices=level_egg_mobs, default=0)
	scythe_mage = models.IntegerField(choices=level_egg_mobs, default=0)
	pea_shooter = models.IntegerField(choices=level_egg_mobs, default=0)
	shadow_assassin = models.IntegerField(choices=level_egg_mobs, default=0)
	tornado_mage = models.IntegerField(choices=level_egg_mobs, default=0)
	spitting_mushroom = models.IntegerField(choices=level_egg_mobs, default=0)
	rolling_mushroom = models.IntegerField(choices=level_egg_mobs, default=0)
	fallen_bat = models.IntegerField(choices=level_egg_mobs, default=0)
	one_eyed_bat = models.IntegerField(choices=level_egg_mobs, default=0)
	scarlet_mage = models.IntegerField(choices=level_egg_mobs, default=0)
	icefire_phantom = models.IntegerField(choices=level_egg_mobs, default=0)
	purple_phantom = models.IntegerField(choices=level_egg_mobs, default=0)
	tundra_dragon = models.IntegerField(choices=level_egg_mobs, default=0)
	sandian = models.IntegerField(choices=level_egg_mobs, default=0)
	nether_puppet = models.IntegerField(choices=level_egg_mobs, default=0)
	psionic_scarecrow = models.IntegerField(choices=level_egg_mobs, default=0)
	steel_dryad = models.IntegerField(choices=level_egg_mobs, default=0)
	savage_spider = models.IntegerField(choices=level_egg_mobs, default=0)
	flaming_bug = models.IntegerField(choices=level_egg_mobs, default=0)
	shark_bro = models.IntegerField(choices=level_egg_mobs, default=0)
	crimson_zombie = models.IntegerField(choices=level_egg_mobs, default=0)
	fat_bat = models.IntegerField(choices=level_egg_mobs, default=0)
	plainswolf = models.IntegerField(choices=level_egg_mobs, default=0)
	elite_archer = models.IntegerField(choices=level_egg_mobs, default=0)
	little_dragon = models.IntegerField(choices=level_egg_boss, default=0)
	arch_leader = models.IntegerField(choices=level_egg_boss, default=0)
	skeleton_king = models.IntegerField(choices=level_egg_boss, default=0)
	crimson_witch = models.IntegerField(choices=level_egg_boss, default=0)
	rage_golem = models.IntegerField(choices=level_egg_boss, default=0)
	queen_bee = models.IntegerField(choices=level_egg_boss, default=0)
	ice_worm = models.IntegerField(choices=level_egg_boss, default=0)
	medusa_boss = models.IntegerField(choices=level_egg_boss, default=0)
	ice_demon = models.IntegerField(choices=level_egg_boss, default=0)
	giant_owl = models.IntegerField(choices=level_egg_boss, default=0)
	fire_demon = models.IntegerField(choices=level_egg_boss, default=0)
	krab_boss = models.IntegerField(choices=level_egg_boss, default=0)
	desert_goliath = models.IntegerField(choices=level_egg_boss, default=0)
	sinister_touch = models.IntegerField(choices=level_egg_boss, default=0)
	scythe_pharoah = models.IntegerField(choices=level_egg_boss, default=0)
	fireworm_queen = models.IntegerField(choices=level_egg_boss, default=0)
	infernal_demon = models.IntegerField(choices=level_egg_boss, default=0)

	def dictionnaire(self):
		return {
				"user_profile": self.user_profile,
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
				'shark_bro': self.shark_bro,
				'crimson_zombie': self.crimson_zombie,
				'fat_bat': self.fat_bat,
				'plainswolf': self.plainswolf,
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
				'sinister_touch': self.sinister_touch,
				'scythe_pharoah': self.scythe_pharoah,
				'fireworm_queen': self.fireworm_queen,
				'infernal_demon': self.infernal_demon,
				}
	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine
	
	def GetPassivEggStats1(self,egg,missing_data):
		egg_level = self.dictionnaire()[str(egg)]
		PassivMobsStats1 = self.local_data['PassivMobsStats1']
		passiv_stats = [0,0,0,0]
		if int(egg_level) >= 5:
			passiv_stats = PassivMobsStats1[str(egg) + "_5"]
			if int(egg_level) >= 10:
				passiv_stats = PassivMobsStats1[str(egg) + "_10"]
				if int(egg_level) >= 13:
					passiv_stats = PassivMobsStats1[str(egg) + "_13"]
					if int(egg_level) >= 17:
						passiv_stats = PassivMobsStats1[str(egg) + "_17"]
		try:
			for i in passiv_stats:
				int(i)
		except ValueError as e:
			missing_data.append(str(e).split("'")[1].replace("_"," "))
			passiv_stats = [0,0,0,0]
		return passiv_stats

	def GetPassivEggStats2(self,egg,missing_data):
		egg_level = self.dictionnaire()[str(egg)]
		PassivMobsStats2 = self.local_data['PassivMobsStats2']
		passiv_stats = [0,0,0,0,0]
		if int(egg_level) >= 4:
			passiv_stats = PassivMobsStats2[str(egg) + "_4"]
			if int(egg_level) >= 7:
				passiv_stats = PassivMobsStats2[str(egg) + "_7"]
				if int(egg_level) >= 10:
					passiv_stats = PassivMobsStats2[str(egg) + "_10"]
					if int(egg_level) >= 13:
						passiv_stats = PassivMobsStats2[str(egg) + "_13"]
						if int(egg_level) >= 17:
							passiv_stats = PassivMobsStats2[str(egg) + "_17"]
		try:
			for i in passiv_stats:
				int(i)
		except ValueError as e:
			missing_data.append(str(e).split("'")[1].replace("_"," "))
			passiv_stats = [0,0,0,0,0]
		return passiv_stats
	
	def GetPassivEggStats3(self,egg,missing_data):
		PassivMobsStats3 = self.local_data['PassivMobsStats3']
		egg_level = self.dictionnaire()[str(egg)]
		passiv_stats = [0,0,0,0,0]
		if int(egg_level) >= 3:
			passiv_stats = PassivMobsStats3[str(egg) + "_3"]
			if int(egg_level) >= 6:
				passiv_stats = PassivMobsStats3[str(egg) + "_6"]
				if int(egg_level) >= 8:
					passiv_stats = PassivMobsStats3[str(egg) + "_8"]
					if int(egg_level) >= 10:
						passiv_stats = PassivMobsStats3[str(egg) + "_10"]
						if int(egg_level) >= 13:
							passiv_stats = PassivMobsStats3[str(egg) + "_13"]
		try:
			for i in passiv_stats:
				int(i)
		except ValueError as e:
			missing_data.append(str(e).split("'")[1].replace("_"," "))
			passiv_stats = [0,0,0,0,0]
		return passiv_stats


class egg_equipped_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	egg_equipped1 = models.CharField(max_length=30, choices=all_egg, default="Choose")
	egg_equipped2 = models.CharField(max_length=30, choices=all_egg, default="Choose")
	egg_equipped3 = models.CharField(max_length=30, choices=all_egg, default="Choose")
	egg_equipped4 = models.CharField(max_length=30, choices=all_egg, default="Choose")
	egg_equipped5 = models.CharField(max_length=30, choices=all_egg, default="Choose")

	def dictionnaire(self):
			return {
					"user_profile": self.user_profile,
					'egg_equipped1': self.egg_equipped1,
					'egg_equipped2': self.egg_equipped2,
					'egg_equipped3': self.egg_equipped3,
					'egg_equipped4': self.egg_equipped4,
					'egg_equipped5': self.egg_equipped5,
					}
	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine
	
	def GetEggStats(self,missing_data):
		all_egg = egg_table.objects.get(user_profile=self.user_profile).dictionnaire()
		all_equipped = [self.egg_equipped1, self.egg_equipped2, self.egg_equipped3, self.egg_equipped4, self.egg_equipped5]
		dict_stats = {
					"none": 0,
					"Attack":0,
					"Critic Damage": 0,
					"Max Hp":0,
					"Damage To Bosses": 0,
					"Damage To Mobs": 0,
					"Damage To Ground Units": 0,
					"Damage To Ranged Units": 0,
					"Damage To Melee Units": 0,
					"Damage To Airborne Units": 0,
					"Projectile Resistance": 0,
					"Front Damage Resistance": 0,
					"Collision Damage Resistance": 0,
					"Blue Heart Recovery Effect": 0,
					"Rear Damage Resistance": 0,
					"Poison Damage": 0,
					"Damage To Normal Units": 0,
					"Damage To Human": 0,
					"Flame Damage": 0,
					"missing_data": "",
				}
		MobsStats = self.local_data["MobsStats"]
		for i in all_equipped:
			egg = str(i).lower().replace(" ","_").replace('-','_')
			if egg != "choose":
				egg_level = int(all_egg[egg])
				stats_type = MobsStats[str(egg) + "_stats_type"]
				mob_stat1 = MobsStats[str(egg)+"_boost_1"][egg_level] if len(MobsStats[str(egg)+"_boost_1"]) != 0 else 0
				mob_stat2 = MobsStats[str(egg)+"_boost_2"][egg_level] if len(MobsStats[str(egg)+"_boost_2"]) != 0 else 0
				mob_stat3 = MobsStats[str(egg)+"_boost_3"][egg_level] if len(MobsStats[str(egg)+"_boost_3"]) != 0 else 0
				stats_type = MobsStats[str(egg) + "_stats_type"]
				mob_stats = [mob_stat1,mob_stat2,mob_stat3]
				for stats in mob_stats:
					try:
						int(stats)
					except ValueError as e:
						missing_data.append(f"{i} {egg_level}")
						mob_stats[mob_stats.index(stats)] = 0
				new_value1 = int(dict_stats[stats_type[0]]) + int(mob_stats[0])
				new_value2 = int(dict_stats[stats_type[1]]) + int(mob_stats[1])
				new_value3 = int(dict_stats[stats_type[2]]) + int(mob_stats[2])
				dict_stats.update({
					"missing_data": missing_data,
					stats_type[0]: new_value1,
					stats_type[1]: new_value2,
					stats_type[2]: new_value3,
				})
		return dict_stats



class dragon_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	dragon1_type = models.CharField(max_length=30, choices=all_dragon, default="Glacion")
	dragon2_type = models.CharField(max_length=30, choices=all_dragon, default="Infernox")
	dragon3_type = models.CharField(max_length=30, choices=all_dragon, default="Stormra")
	dragon1_rarity = models.CharField(max_length=30, choices=dragon_rarity, default="Great")
	dragon2_rarity = models.CharField(max_length=30, choices=dragon_rarity, default="Great")
	dragon3_rarity = models.CharField(max_length=30, choices=dragon_rarity, default="Great")
	dragon1_level = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(120)]) 
	dragon2_level = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(120)]) 
	dragon3_level = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(120)])
	dragon_1_boost_1 = models.IntegerField(choices=dragon_skill_level, default=0)
	dragon_1_boost_2 = models.IntegerField(choices=dragon_skill_level, default=0)
	dragon_1_boost_3 = models.IntegerField(choices=dragon_skill_level, default=0)
	dragon_1_boost_4 = models.IntegerField(choices=dragon_skill_level, default=0)
	dragon_2_boost_1 = models.IntegerField(choices=dragon_skill_level, default=0)
	dragon_2_boost_2 = models.IntegerField(choices=dragon_skill_level, default=0)
	dragon_2_boost_3 = models.IntegerField(choices=dragon_skill_level, default=0)
	dragon_2_boost_4 = models.IntegerField(choices=dragon_skill_level, default=0)
	dragon_3_boost_1 = models.IntegerField(choices=dragon_skill_level, default=0)
	dragon_3_boost_2 = models.IntegerField(choices=dragon_skill_level, default=0)
	dragon_3_boost_3 = models.IntegerField(choices=dragon_skill_level, default=0)
	dragon_3_boost_4 = models.IntegerField(choices=dragon_skill_level, default=0)

	def dictionnaire(self):
		return {
				"user_profile": self.user_profile,
				'dragon1_type': self.dragon1_type,
				'dragon2_type': self.dragon2_type,
				'dragon3_type': self.dragon3_type,
				'dragon1_rarity': self.dragon1_rarity,
				'dragon2_rarity': self.dragon2_rarity,
				'dragon3_rarity': self.dragon3_rarity,
				'dragon1_level': self.dragon1_level,
				'dragon2_level': self.dragon2_level,
				'dragon3_level': self.dragon3_level,
				'dragon_1_boost_1': self.dragon_1_boost_1,
				'dragon_1_boost_2': self.dragon_1_boost_2,
				'dragon_1_boost_3': self.dragon_1_boost_3,
				'dragon_1_boost_4': self.dragon_1_boost_4,
				'dragon_2_boost_1': self.dragon_2_boost_1,
				'dragon_2_boost_2': self.dragon_2_boost_2,
				'dragon_2_boost_3': self.dragon_2_boost_3,
				'dragon_2_boost_4': self.dragon_2_boost_4,
				'dragon_3_boost_1': self.dragon_3_boost_1,
				'dragon_3_boost_2': self.dragon_3_boost_2,
				'dragon_3_boost_3': self.dragon_3_boost_3,
				'dragon_3_boost_4': self.dragon_3_boost_4,
				}
	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine
	
	def GetDragon(self,number:str):
		return {
			"dragon_type":self.dictionnaire()["dragon" + str(number) + "_type"],
			"dragon_rarity":self.dictionnaire()["dragon" + str(number) + "_rarity"].replace(' ','_'),
			"dragon_level":self.dictionnaire()["dragon" + str(number) + "_level"],
			"dragon_skill_1":self.dictionnaire()["dragon_" + str(number) + "_boost_1"],
			"dragon_skill_2":self.dictionnaire()["dragon_" + str(number) + "_boost_2"],
			"dragon_skill_3":self.dictionnaire()["dragon_" + str(number) + "_boost_3"],
			"dragon_skill_4":self.dictionnaire()["dragon_" + str(number) + "_boost_4"],
		}

	def DragonStatueStats(self,number):
		dragon_type = self.GetDragon(str(number))['dragon_type']
		dragon_rarity = self.GetDragon(str(number))['dragon_rarity'].replace(' ','_')
		dragon_level = self.GetDragon(str(number))['dragon_level']
		dragon_skill_4 = self.GetDragon(str(number))['dragon_skill_4']
		base_stats1 = self.local_data["DragonStats"][str(dragon_type).lower() + "_" + str(dragon_rarity).lower() + "_base_1"]
		base_stats2 = self.local_data["DragonStats"][str(dragon_type).lower() + "_" + str(dragon_rarity).lower() + "_base_2"]
		b1_type = self.local_data["DragonStats"][str(dragon_type).lower() + "_bonus1"]
		b2_type = self.local_data["DragonStats"][str(dragon_type).lower() + "_bonus2"]
		inc_stats1 = self.local_data["DragonStats"][str(dragon_type).lower() + "_" + str(dragon_rarity).lower() + "_inc_1"]
		inc_stats2 = self.local_data["DragonStats"][str(dragon_type).lower() + "_" + str(dragon_rarity).lower() + "_inc_2"]
		if dragon_rarity == "Mythic" and int(dragon_skill_4) > 0:
			inc_mythic_boost = self.local_data["DragonStats"][str(dragon_type).lower() + "_mythic_boost_inc"]
			inc_mythic_boost_float = float(inc_mythic_boost[0]) * (int(dragon_skill_4)-1) +int(inc_mythic_boost[1])
			inc_stats1_modified = round(float(inc_stats1) * (float(inc_mythic_boost_float)/100+1))
			inc_stats2_modified = round(float(inc_stats2) * (float(inc_mythic_boost_float)/100+1))
			result_stats1 = (float(base_stats1) + (float(dragon_level)-1)*inc_stats1_modified)*(float(inc_mythic_boost[1])/100+1)  ## c'est pas les bonnes formules mais 
			result_stats2 = (float(base_stats2) + (float(dragon_level)-1)*inc_stats2_modified)*(float(inc_mythic_boost[1])/100+1)  ## le résultat est proches de la réalité
		else:
			result_stats1 = int(base_stats1) + (int(dragon_level)-1)*int(inc_stats1)
			result_stats2 = int(base_stats2) + (int(dragon_level)-1)*int(inc_stats2)
			inc_stats1_modified = 0
			inc_stats2_modified = 0
		if dragon_rarity == "Mythic" or dragon_rarity == "Ancient Legendary":
			b3_type = self.local_data["DragonStats"][str(dragon_type).lower() + "_bonus3"]
			if dragon_rarity == "Ancient Legendary":
				b3_boost = self.local_data["DragonStats"][str(dragon_type).lower() + "_stats_boost3"][0]
			elif dragon_rarity == "Mythic":
				b3_boost = self.local_data["DragonStats"][str(dragon_type).lower() + "_stats_boost3"][1]
		else:
			b3_type = 0
			b3_boost = 0
		dict_result = {
			b1_type: round(result_stats1),
			b2_type: round(result_stats2),
			b3_type: float(b3_boost),
			"inc_stats1_modified":round(inc_stats1_modified),
			"inc_stats2_modified":round(inc_stats2_modified),
		}
		return dict_result


	def getPassivSkillDragon(self):
		dragon_1_skills = self.local_data["SkillPassivBonusDragon"][self.dragon1_type.lower()]
		dragon_2_skills = self.local_data["SkillPassivBonusDragon"][self.dragon2_type.lower()]
		dragon_3_skills = self.local_data["SkillPassivBonusDragon"][self.dragon3_type.lower()]
		return {
			dragon_1_skills["skill_2"]['line_1_txt']: int(dragon_1_skills["skill_2"]['line_1_value']) + int(dragon_1_skills["skill_2"]['line_1_inc'])* int(self.dragon_1_boost_2),
			dragon_1_skills["skill_2"]['line_5_txt']: int(dragon_1_skills["skill_2"]['line_5_value']),
			dragon_1_skills["skill_2"]['line_10_txt']: int(dragon_1_skills["skill_2"]['line_10_value']),

			dragon_2_skills["skill_2"]['line_1_txt']: int(dragon_2_skills["skill_2"]['line_1_value']) + int(dragon_2_skills["skill_2"]['line_1_inc'])* int(self.dragon_2_boost_2),
			dragon_2_skills["skill_2"]['line_5_txt']: int(dragon_2_skills["skill_2"]['line_5_value']),
			dragon_2_skills["skill_2"]['line_10_txt']: int(dragon_2_skills["skill_2"]['line_10_value']),

			dragon_3_skills["skill_2"]['line_1_txt']: int(dragon_3_skills["skill_2"]['line_1_value']) + int(dragon_3_skills["skill_2"]['line_1_inc'])* int(self.dragon_3_boost_2),
			dragon_3_skills["skill_2"]['line_5_txt']: int(dragon_3_skills["skill_2"]['line_5_value']),
			dragon_3_skills["skill_2"]['line_10_txt']: int(dragon_3_skills["skill_2"]['line_10_value']),
		}



class runes_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	power_attack_flat = models.BigIntegerField(default=0, validators=[MaxValueValidator(750)])
	power_attack_var = models.FloatField(default=0, validators=[MaxValueValidator(7)])
	power_line_2 = models.CharField(choices=power_rune_all,default="None", max_length=30)
	power_line_3 = models.CharField(choices=power_rune_all,default="None", max_length=30)
	power_line_4 = models.CharField(choices=power_rune_all,default="None", max_length=30)
	power_line_5 = models.CharField(choices=power_rune_all,default="None", max_length=30)
	saviour_hp_flat = models.BigIntegerField(default=0, validators=[MaxValueValidator(2800)])
	saviour_hp_var = models.FloatField(default=0, validators=[MaxValueValidator(7)])
	saviour_line_2 = models.CharField(choices=saviour_rune_all,default="None", max_length=30)
	saviour_line_3 = models.CharField(choices=saviour_rune_all,default="None", max_length=30)
	saviour_line_4 = models.CharField(choices=saviour_rune_all,default="None", max_length=30)
	saviour_line_5 = models.CharField(choices=saviour_rune_all,default="None", max_length=30)
	recovery_hp_flat = models.BigIntegerField(default=0, validators=[MaxValueValidator(2250)])
	recovery_line_2 = models.CharField(choices=recovery_rune_all,default="None", max_length=30)
	recovery_line_3 = models.CharField(choices=recovery_rune_all,default="None", max_length=30)
	recovery_line_4 = models.CharField(choices=recovery_rune_all,default="None", max_length=30)
	recovery_line_5 = models.CharField(choices=recovery_rune_all,default="None", max_length=30)
	courage_attack_flat = models.BigIntegerField(default=0, validators=[MaxValueValidator(750)])
	courage_attack_var = models.FloatField(default=0, validators=[MaxValueValidator(7)])
	selected_hero_courage_attack_flat = models.CharField(choices=all_heros,default="Atreus", max_length=15)
	courage_hero_attack_flat = models.BigIntegerField(default=0, validators=[MaxValueValidator(180)])
	selected_hero_courage_attack_var = models.CharField(choices=all_heros,default="Atreus", max_length=15)
	courage_hero_attack_var = models.FloatField(default=0, validators=[MaxValueValidator(12.5)])
	selected_hero_courage_hp_flat = models.CharField(choices=all_heros,default="Atreus", max_length=15)
	courage_hero_hp_flat = models.BigIntegerField(default=0, validators=[MaxValueValidator(900)])
	selected_hero_courage_hp_var = models.CharField(choices=all_heros,default="Atreus", max_length=15)
	courage_hero_hp_var = models.FloatField(default=0, validators=[MaxValueValidator(12.5)])
	courage_line_2 = models.CharField(choices=courage_rune_all,default="None", max_length=30)
	courage_line_3 = models.CharField(choices=courage_rune_all,default="None", max_length=30)
	courage_line_4 = models.CharField(choices=courage_rune_all,default="None", max_length=30)
	courage_line_5 = models.CharField(choices=courage_rune_all,default="None", max_length=30)
	luck_hp_flat = models.BigIntegerField(default=0, validators=[MaxValueValidator(2800)])
	luck_hp_var = models.FloatField(default=0, validators=[MaxValueValidator(7)])
	luck_line_2 = models.CharField(choices=luck_rune_all,default="None", max_length=30)
	luck_line_3 = models.CharField(choices=luck_rune_all,default="None", max_length=30)
	luck_line_4 = models.CharField(choices=luck_rune_all,default="None", max_length=30)
	luck_line_5 = models.CharField(choices=luck_rune_all,default="None", max_length=30)
	value_power_line_2 = models.FloatField(default=0, blank=False)
	value_power_line_3 = models.FloatField(default=0, blank=False)
	value_power_line_4 = models.FloatField(default=0, blank=False)
	value_power_line_5 = models.FloatField(default=0, blank=False)
	value_saviour_line_2 = models.FloatField(default=0, blank=False)
	value_saviour_line_3 = models.FloatField(default=0, blank=False)
	value_saviour_line_4 = models.FloatField(default=0, blank=False)
	value_saviour_line_5 = models.FloatField(default=0, blank=False)
	value_recovery_line_2 = models.FloatField(default=0, blank=False)
	value_recovery_line_3 = models.FloatField(default=0, blank=False)
	value_recovery_line_4 = models.FloatField(default=0, blank=False)
	value_recovery_line_5 = models.FloatField(default=0, blank=False)
	value_courage_line_2 = models.FloatField(default=0, blank=False)
	value_courage_line_3 = models.FloatField(default=0, blank=False)
	value_courage_line_4 = models.FloatField(default=0, blank=False)
	value_courage_line_5 = models.FloatField(default=0, blank=False)
	value_luck_line_2 = models.FloatField(default=0, blank=False)
	value_luck_line_3 = models.FloatField(default=0, blank=False)
	value_luck_line_4 = models.FloatField(default=0, blank=False)
	value_luck_line_5 = models.FloatField(default=0, blank=False)


	def dictionnaire(self):
			return {
				"user_profile": self.user_profile,
				"power_attack_flat": self.power_attack_flat, 
				"power_attack_var": self.power_attack_var, 
				"power_line_2": self.power_line_2, 
				"power_line_3": self.power_line_3, 
				"power_line_4": self.power_line_4, 
				"power_line_5": self.power_line_5, 
				"saviour_hp_flat": self.saviour_hp_flat, 
				"saviour_hp_var": self.saviour_hp_var, 
				"saviour_line_2": self.saviour_line_2, 
				"saviour_line_3": self.saviour_line_3, 
				"saviour_line_4": self.saviour_line_4, 
				"saviour_line_5": self.saviour_line_5, 
				"recovery_hp_flat": self.recovery_hp_flat, 
				"recovery_line_2": self.recovery_line_2, 
				"recovery_line_3": self.recovery_line_3, 
				"recovery_line_4": self.recovery_line_4, 
				"recovery_line_5": self.recovery_line_5, 
				"courage_attack_flat": self.courage_attack_flat, 
				"courage_attack_var": self.courage_attack_var, 
				"selected_hero_courage_attack_flat": self.selected_hero_courage_attack_flat,
				"courage_hero_attack_flat": self.courage_hero_attack_flat, 
				"selected_hero_courage_attack_var": self.selected_hero_courage_attack_var,
				"courage_hero_attack_var": self.courage_hero_attack_var,
				"selected_hero_courage_hp_flat": self.selected_hero_courage_hp_flat,
				"courage_hero_hp_flat": self.courage_hero_hp_flat, 
				"selected_hero_courage_hp_var": self.selected_hero_courage_hp_var,
				"courage_hero_hp_var": self.courage_hero_hp_var,
				"courage_line_2": self.courage_line_2, 
				"courage_line_3": self.courage_line_3, 
				"courage_line_4": self.courage_line_4, 
				"courage_line_5": self.courage_line_5, 
				"luck_hp_flat": self.luck_hp_flat, 
				"luck_hp_var": self.luck_hp_var, 
				"luck_line_2": self.luck_line_2, 
				"luck_line_3": self.luck_line_3, 
				"luck_line_4": self.luck_line_4, 
				"luck_line_5": self.luck_line_5,
				"value_power_line_2": self.value_power_line_2,
				"value_power_line_3": self.value_power_line_3,
				"value_power_line_4": self.value_power_line_4,
				"value_power_line_5": self.value_power_line_5,
				"value_saviour_line_2": self.value_saviour_line_2,
				"value_saviour_line_3": self.value_saviour_line_3,
				"value_saviour_line_4": self.value_saviour_line_4,
				"value_saviour_line_5": self.value_saviour_line_5,
				"value_recovery_line_2": self.value_recovery_line_2,
				"value_recovery_line_3": self.value_recovery_line_3,
				"value_recovery_line_4": self.value_recovery_line_4,
				"value_recovery_line_5": self.value_recovery_line_5,
				"value_courage_line_2": self.value_courage_line_2,
				"value_courage_line_3": self.value_courage_line_3,
				"value_courage_line_4": self.value_courage_line_4,
				"value_courage_line_5": self.value_courage_line_5,
				"value_luck_line_2": self.value_luck_line_2,
				"value_luck_line_3": self.value_luck_line_3,
				"value_luck_line_4": self.value_luck_line_4,
				"value_luck_line_5": self.value_luck_line_5,
			}
	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine

	def CourageBoostHero(self,heros_equipped):
		courage_hero = {
			"current_hero_atk_flat":str(self.courage_hero_attack_flat) + "_" + str(self.selected_hero_courage_attack_flat),
			"current_hero_atk_var":str(self.courage_hero_attack_var/100) + "_" + str(self.selected_hero_courage_attack_var),
			"current_hero_hp_flat":str(self.courage_hero_hp_flat) + "_" + str(self.selected_hero_courage_hp_flat),
			"current_hero_hp_var":str(self.courage_hero_hp_var/100) + "_" + str(self.selected_hero_courage_hp_var)
		}
		for k,v in courage_hero.items():
			hero = v.split("_")[1]
			boost = v.split("_")[0]
			if heros_equipped == hero:
				courage_hero.update({k:boost})
			else:
				courage_hero.update({k:0})
		return courage_hero
	
	def getRunesDmgCalc(self):
		return {
			"atk_power_flat": self.power_attack_flat,
			"atk_power_var": self.power_attack_var,
			"atk_courage_flat": self.courage_attack_flat,
			"atk_courage_var": self.courage_attack_var,
			"courage_hero_atk_flat": self.courage_hero_attack_flat,
			"courage_hero_atk_var": self.courage_hero_attack_var,
			"power_second_select": self.power_line_2,
			"power_second_input": self.value_power_line_2,
			"power_third_select": self.power_line_3,
			"power_third_input": self.value_power_line_3,
			"power_fourth_select": self.power_line_4,
			"power_fourth_input": self.value_power_line_4,
			"power_fifth_select": self.power_line_5,
			"power_fifth_input": self.value_power_line_5
		}

	def getValueLine(self):
		return {
			"flat_dmg_airborne":0,
			"var_dmg_airborne":0.0,
			"flat_dmg_ground":0,
			"var_dmg_ground":0.0,
			"flat_dmg_melee":0,
			"var_dmg_melee":0.0,
			"flat_dmg_ranged":0,
			"var_dmg_ranged":0.0,
			"flat_dmg_boss":0,
			"var_dmg_boss":0.0,
			"flat_dmg_mob":0,
			"var_dmg_mob":0.0,
			"var_dmg_hero":0.0,
			"var_all_dmg":0.0,
			"var_elemental_dmg":0.0,
			"var_crit_rate":0.0,
			"var_crit_dmg":0.0,
			"dodge":0.0,
			"var_enhanced_eqpm":0.0,
			"flat_heal_red_heart":0,
			"var_heal_red_heart":0.0,
			"flat_hp_drop":0,
			"var_hp_drop":0.0,
			## TODO dict.get("result_stats1","None")
			self.power_line_2: self.value_power_line_2,
			self.power_line_3: self.value_power_line_3,
			self.power_line_4: self.value_power_line_4,
			self.power_line_5: self.value_power_line_5,
			self.saviour_line_2: self.value_saviour_line_2,
			self.saviour_line_3: self.value_saviour_line_3,
			self.saviour_line_4: self.value_saviour_line_4,
			self.saviour_line_5: self.value_saviour_line_5,
			self.recovery_line_2: self.value_recovery_line_2,
			self.recovery_line_3: self.value_recovery_line_3,
			self.recovery_line_4: self.value_recovery_line_4,
			self.recovery_line_5: self.value_recovery_line_5,
			self.courage_line_2: self.value_courage_line_2,
			self.courage_line_3: self.value_courage_line_3,
			self.courage_line_4: self.value_courage_line_4,
			self.courage_line_5: self.value_courage_line_5,
			self.luck_line_2: self.value_luck_line_2,
			self.luck_line_3: self.value_luck_line_3,
			self.luck_line_4: self.value_luck_line_4,
			self.luck_line_5: self.value_luck_line_5,
		}


class reforge_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	reforge_power = models.IntegerField(choices=reforge, default=0)
	reforge_saviour = models.IntegerField(choices=reforge, default=0)
	reforge_recovery = models.IntegerField(choices=reforge, default=0)
	reforge_courage = models.IntegerField(choices=reforge, default=0)
	reforge_luck = models.IntegerField(choices=reforge, default=0)

	def dictionnaire(self):
			return {
					"user_profile": self.user_profile,
					'reforge_power': self.reforge_power,
					'reforge_saviour': self.reforge_saviour,
					'reforge_recovery': self.reforge_recovery,
					'reforge_courage': self.reforge_courage,
					'reforge_luck': self.reforge_luck,
					}
	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine
	
	def ReforgePowerCourage(self, type_runes):
		reforge_stats = self.dictionnaire()["reforge_" + str(type_runes)]
		if int(reforge_stats) <=400:
			stats_reforge = int(reforge_stats) 
		elif int(reforge_stats) > 400:
			stats_reforge = 400+(int(reforge_stats)-400)/50*30
		return stats_reforge

	def ReforgeSaviourRecoLuck(self, type_runes):
		reforge_stats = self.dictionnaire()["reforge_" + str(type_runes)]
		if int(reforge_stats) <=400:
			stats_reforge = (int(reforge_stats)/20)*60
		elif int(reforge_stats) > 400:
			stats_reforge = 1200+(int(reforge_stats)-400)/50*100
		return stats_reforge


class refine_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
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
				"user_profile": self.user_profile,
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
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine


class dmg_calc_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	hero_atk = models.JSONField(default=dict,blank=False)

	missing_data = models.CharField(max_length=20, default="none", blank=False,null=True)
	weapon_coeff = models.FloatField(default=1.0,blank=False)
	flat_dmg_vs_ground = models.IntegerField(default=0,blank=False)
	flat_dmg_vs_airborne = models.IntegerField(default=0,blank=False)
	flat_dmg_vs_melee = models.IntegerField(default=0,blank=False)
	flat_dmg_vs_range = models.IntegerField(default=0,blank=False)
	flat_dmg_vs_mobs = models.IntegerField(default=0,blank=False)
	flat_dmg_vs_boss = models.IntegerField(default=0,blank=False)
	flat_dmg_element = models.IntegerField(default=0,blank=False)
	flat_dmg_all = models.IntegerField(default=0,blank=False)
	flat_elite_dmg = models.IntegerField(default=0,blank=False)
	flat_normal_dmg = models.IntegerField(default=0,blank=False)
	var_dmg_vs_ground = models.FloatField(default=0,blank=False)
	var_dmg_vs_airborne = models.FloatField(default=0,blank=False)
	var_dmg_vs_melee = models.FloatField(default=0,blank=False)
	var_dmg_vs_range = models.FloatField(default=0,blank=False)
	var_dmg_vs_mobs = models.FloatField(default=0,blank=False)
	var_dmg_vs_boss = models.FloatField(default=0,blank=False)
	var_dmg_element = models.FloatField(default=0,blank=False)
	var_dmg_all = models.FloatField(default=0,blank=False)
	var_normal_dmg = models.FloatField(default=0,blank=False)
	var_elite_dmg = models.FloatField(default=0,blank=False)
	crit_dmg = models.IntegerField(default=0,blank=False)
	crit_rate = models.FloatField(default=0,blank=False)
	dodge_rate = models.FloatField(default=0,blank=False)
	weapon_damage = models.FloatField(default=0,blank=False)
	weapon_melee_damage = models.FloatField(default=0,blank=False)
	weapon_ranged_damage = models.FloatField(default=0,blank=False)

	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine

	def calculDamage(self, **kwargs):
		if len(list(kwargs)) == 0:
			crit_dmg = int(self.crit_dmg)/100
			crit_rate = self.crit_rate
			mob_ground_melee = round((int(self.user_profile.global_atk_save) + int(self.flat_dmg_vs_ground) + int(self.flat_dmg_vs_mobs) + int(self.flat_dmg_vs_melee) + int(self.flat_dmg_all))*(float(self.var_dmg_vs_melee/100) + float(self.var_dmg_vs_ground/100) + float(1))*(float(self.var_dmg_vs_mobs/100) + float(1))*(float(self.var_dmg_all/100) + float(1))*(float(self.weapon_coeff)))
			mob_ground_range = round((int(self.user_profile.global_atk_save) + int(self.flat_dmg_vs_ground) + int(self.flat_dmg_vs_mobs) + int(self.flat_dmg_vs_range) + int(self.flat_dmg_all))*(float(self.var_dmg_vs_range/100) + float(self.var_dmg_vs_ground/100) + float(1))*(float(self.var_dmg_vs_mobs/100) + float(1))*(float(self.var_dmg_all/100) + float(1))*(float(self.weapon_coeff)))
			mob_airborne_melee = round((int(self.user_profile.global_atk_save) + int(self.flat_dmg_vs_airborne) + int(self.flat_dmg_vs_mobs) + int(self.flat_dmg_vs_melee) + int(self.flat_dmg_all))*(float(self.var_dmg_vs_melee/100) + float(self.var_dmg_vs_airborne/100) + float(1))*(float(self.var_dmg_vs_mobs/100) + float(1))*(float(self.var_dmg_all/100) + float(1))*(float(self.weapon_coeff)))
			mob_airborne_range = round((int(self.user_profile.global_atk_save) + int(self.flat_dmg_vs_airborne) + int(self.flat_dmg_vs_mobs) + int(self.flat_dmg_vs_range) + int(self.flat_dmg_all))*(float(self.var_dmg_vs_range/100) + float(self.var_dmg_vs_airborne/100) + float(1))*(float(self.var_dmg_vs_mobs/100) + float(1))*(float(self.var_dmg_all/100) + float(1))*(float(self.weapon_coeff)))
			boss_ground_melee = round((int(self.user_profile.global_atk_save) + int(self.flat_dmg_vs_ground) + int(self.flat_dmg_vs_boss) + int(self.flat_dmg_vs_melee) + int(self.flat_dmg_all))*(float(self.var_dmg_vs_melee/100) + float(self.var_dmg_vs_ground/100) + float(1))*(float(self.var_dmg_vs_boss/100) + float(1))*(float(self.var_dmg_all/100) + float(1))*(float(self.weapon_coeff)))
			boss_ground_range = round((int(self.user_profile.global_atk_save) + int(self.flat_dmg_vs_ground) + int(self.flat_dmg_vs_boss) + int(self.flat_dmg_vs_range) + int(self.flat_dmg_all))*(float(self.var_dmg_vs_range/100) + float(self.var_dmg_vs_ground/100) + float(1))*(float(self.var_dmg_vs_boss/100) + float(1))*(float(self.var_dmg_all/100) + float(1))*(float(self.weapon_coeff)))
			boss_airborne_melee = round((int(self.user_profile.global_atk_save) + int(self.flat_dmg_vs_airborne) + int(self.flat_dmg_vs_boss) + int(self.flat_dmg_vs_melee) + int(self.flat_dmg_all))*(float(self.var_dmg_vs_melee/100) + float(self.var_dmg_vs_airborne/100) + float(1))*(float(self.var_dmg_vs_boss/100) + float(1))*(float(self.var_dmg_all/100) + float(1))*(float(self.weapon_coeff)))
			boss_airborne_range = round((int(self.user_profile.global_atk_save) + int(self.flat_dmg_vs_airborne) + int(self.flat_dmg_vs_boss) + int(self.flat_dmg_vs_range) + int(self.flat_dmg_all))*(float(self.var_dmg_vs_range/100) + float(self.var_dmg_vs_airborne/100) + float(1))*(float(self.var_dmg_vs_boss/100) + float(1))*(float(self.var_dmg_all/100) + float(1))*(float(self.weapon_coeff)))
		else:
			crit_dmg = int(kwargs['crit_dmg'])/100
			crit_rate = kwargs['crit_rate']
			mob_ground_melee = round((int(kwargs['global_atk_save']) + int(kwargs['flat_dmg_vs_ground']) + int(kwargs['flat_dmg_vs_mobs']) + int(kwargs['flat_dmg_vs_melee']) + int(kwargs['flat_dmg_all']))*(float(kwargs['var_dmg_vs_melee']/100) + float(kwargs['var_dmg_vs_ground']/100) + float(1))*(float(kwargs['var_dmg_vs_mobs']/100) + float(1))*(float(kwargs['var_dmg_all']/100) + float(1))*(float(self.weapon_coeff)))
			mob_ground_range = round((int(kwargs['global_atk_save']) + int(kwargs['flat_dmg_vs_ground']) + int(kwargs['flat_dmg_vs_mobs']) + int(kwargs['flat_dmg_vs_range']) + int(kwargs['flat_dmg_all']))*(float(kwargs['var_dmg_vs_range']/100) + float(kwargs['var_dmg_vs_ground']/100) + float(1))*(float(kwargs['var_dmg_vs_mobs']/100) + float(1))*(float(kwargs['var_dmg_all']/100) + float(1))*(float(self.weapon_coeff)))
			mob_airborne_melee = round((int(kwargs['global_atk_save']) + int(kwargs['flat_dmg_vs_airborne']) + int(kwargs['flat_dmg_vs_mobs']) + int(kwargs['flat_dmg_vs_melee']) + int(kwargs['flat_dmg_all']))*(float(kwargs['var_dmg_vs_melee']/100) + float(kwargs['var_dmg_vs_airborne']/100) + float(1))*(float(kwargs['var_dmg_vs_mobs']/100) + float(1))*(float(kwargs['var_dmg_all']/100) + float(1))*(float(self.weapon_coeff)))
			mob_airborne_range = round((int(kwargs['global_atk_save']) + int(kwargs['flat_dmg_vs_airborne']) + int(kwargs['flat_dmg_vs_mobs']) + int(kwargs['flat_dmg_vs_range']) + int(kwargs['flat_dmg_all']))*(float(kwargs['var_dmg_vs_range']/100) + float(kwargs['var_dmg_vs_airborne']/100) + float(1))*(float(kwargs['var_dmg_vs_mobs']/100) + float(1))*(float(kwargs['var_dmg_all']/100) + float(1))*(float(self.weapon_coeff)))
			boss_ground_melee = round((int(kwargs['global_atk_save']) + int(kwargs['flat_dmg_vs_ground']) + int(kwargs['flat_dmg_vs_boss']) + int(kwargs['flat_dmg_vs_melee']) + int(kwargs['flat_dmg_all']))*(float(kwargs['var_dmg_vs_melee']/100) + float(kwargs['var_dmg_vs_ground']/100) + float(1))*(float(kwargs['var_dmg_vs_boss']/100) + float(1))*(float(kwargs['var_dmg_all']/100) + float(1))*(float(self.weapon_coeff)))
			boss_ground_range = round((int(kwargs['global_atk_save']) + int(kwargs['flat_dmg_vs_ground']) + int(kwargs['flat_dmg_vs_boss']) + int(kwargs['flat_dmg_vs_range']) + int(kwargs['flat_dmg_all']))*(float(kwargs['var_dmg_vs_range']/100) + float(kwargs['var_dmg_vs_ground']/100) + float(1))*(float(kwargs['var_dmg_vs_boss']/100) + float(1))*(float(kwargs['var_dmg_all']/100) + float(1))*(float(self.weapon_coeff)))
			boss_airborne_melee = round((int(kwargs['global_atk_save']) + int(kwargs['flat_dmg_vs_airborne']) + int(kwargs['flat_dmg_vs_boss']) + int(kwargs['flat_dmg_vs_melee']) + int(kwargs['flat_dmg_all']))*(float(kwargs['var_dmg_vs_melee']/100) + float(kwargs['var_dmg_vs_airborne']/100) + float(1))*(float(kwargs['var_dmg_vs_boss']/100) + float(1))*(float(kwargs['var_dmg_all']/100) + float(1))*(float(self.weapon_coeff)))
			boss_airborne_range = round((int(kwargs['global_atk_save']) + int(kwargs['flat_dmg_vs_airborne']) + int(kwargs['flat_dmg_vs_boss']) + int(kwargs['flat_dmg_vs_range']) + int(kwargs['flat_dmg_all']))*(float(kwargs['var_dmg_vs_range']/100) + float(kwargs['var_dmg_vs_airborne']/100) + float(1))*(float(kwargs['var_dmg_vs_boss']/100) + float(1))*(float(kwargs['var_dmg_all']/100) + float(1))*(float(self.weapon_coeff)))
		mob_ground_melee_damage = [mob_ground_melee,int(mob_ground_melee*crit_dmg)]
		mob_ground_range_damage = [mob_ground_range,int(mob_ground_range*crit_dmg)]
		mob_airborne_melee_damage = [mob_airborne_melee,int(mob_airborne_melee*crit_dmg)]
		mob_airborne_range_damage = [mob_airborne_range,int(mob_airborne_range*crit_dmg)]
		boss_ground_melee_damage = [boss_ground_melee,int(boss_ground_melee*crit_dmg)]
		boss_ground_range_damage = [boss_ground_range,int(boss_ground_range*crit_dmg)]
		boss_airborne_melee_damage = [boss_airborne_melee,int(boss_airborne_melee*crit_dmg)]
		boss_airborne_range_damage = [boss_airborne_range,int(boss_airborne_range*crit_dmg)]
		averageDamage = round(
			int(mob_ground_melee_damage[0])+
			int(mob_ground_range_damage[0])+
			int(mob_airborne_melee_damage[0])+
			int(mob_airborne_range_damage[0])+
			int(boss_ground_melee_damage[0])+
			int(boss_ground_range_damage[0])+
			int(boss_airborne_melee_damage[0])+
			int(boss_airborne_range_damage[0])
		)/8
		averageDamageAll = round(averageDamage * (1 + (crit_rate/100) * (crit_dmg - 1)))
		return {
			"averageDamageAll": averageDamageAll,
			"mob_ground_melee_damage": [mob_ground_melee,int(mob_ground_melee*crit_dmg)],
			"mob_ground_range_damage": [mob_ground_range,int(mob_ground_range*crit_dmg)],
			"mob_airborne_melee_damage": [mob_airborne_melee,int(mob_airborne_melee*crit_dmg)],
			"mob_airborne_range_damage": [mob_airborne_range,int(mob_airborne_range*crit_dmg)],
			"boss_ground_melee_damage": [boss_ground_melee,int(boss_ground_melee*crit_dmg)],
			"boss_ground_range_damage": [boss_ground_range,int(boss_ground_range*crit_dmg)],
			"boss_airborne_melee_damage": [boss_airborne_melee,int(boss_airborne_melee*crit_dmg)],
			"boss_airborne_range_damage": [boss_airborne_range,int(boss_airborne_range*crit_dmg)],
			"crit_dmg": crit_dmg*100,
			"crit_rate": crit_rate,
		}


class medals_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	medals_01 = models.BooleanField(blank=True, default=False)
	medals_02 = models.BooleanField(blank=True, default=False)
	medals_03 = models.BooleanField(blank=True, default=False)
	medals_04 = models.BooleanField(blank=True, default=False)
	medals_05 = models.BooleanField(blank=True, default=False)
	medals_06 = models.BooleanField(blank=True, default=False)
	medals_07 = models.BooleanField(blank=True, default=False)
	medals_08 = models.BooleanField(blank=True, default=False)
	medals_09 = models.BooleanField(blank=True, default=False)
	medals_10 = models.BooleanField(blank=True, default=False)
	medals_11 = models.BooleanField(blank=True, default=False)
	medals_12 = models.BooleanField(blank=True, default=False)
	medals_13 = models.BooleanField(blank=True, default=False)
	medals_14 = models.BooleanField(blank=True, default=False)
	medals_15 = models.BooleanField(blank=True, default=False)
	medals_16 = models.BooleanField(blank=True, default=False)
	medals_17 = models.BooleanField(blank=True, default=False)
	medals_18 = models.BooleanField(blank=True, default=False)
	medals_19 = models.BooleanField(blank=True, default=False)
	medals_20 = models.BooleanField(blank=True, default=False)
	medals_21 = models.BooleanField(blank=True, default=False)
	medals_22 = models.BooleanField(blank=True, default=False)
	medals_23 = models.BooleanField(blank=True, default=False)
	medals_24 = models.BooleanField(blank=True, default=False)
	medals_25 = models.BooleanField(blank=True, default=False)
	medals_26 = models.BooleanField(blank=True, default=False)
	medals_27 = models.BooleanField(blank=True, default=False)
	medals_28 = models.BooleanField(blank=True, default=False)
	medals_29 = models.BooleanField(blank=True, default=False)
	medals_30 = models.BooleanField(blank=True, default=False)
	medals_31 = models.BooleanField(blank=True, default=False)
	medals_32 = models.BooleanField(blank=True, default=False)

	def dictionnaire(self):
		return {
				"user_profile": self.user_profile,
				"medals_01": self.medals_01,
				"medals_02": self.medals_02,
				"medals_03": self.medals_03,
				"medals_04": self.medals_04,
				"medals_05": self.medals_05,
				"medals_06": self.medals_06,
				"medals_07": self.medals_07,
				"medals_08": self.medals_08,
				"medals_09": self.medals_09,
				"medals_10": self.medals_10,
				"medals_11": self.medals_11,
				"medals_12": self.medals_12,
				"medals_13": self.medals_13,
				"medals_14": self.medals_14,
				"medals_15": self.medals_15,
				"medals_16": self.medals_16,
				"medals_17": self.medals_17,
				"medals_18": self.medals_18,
				"medals_19": self.medals_19,
				"medals_20": self.medals_20,
				"medals_21": self.medals_21,
				"medals_22": self.medals_22,
				"medals_23": self.medals_23,
				"medals_24": self.medals_24,
				"medals_25": self.medals_25,
				"medals_26": self.medals_26,
				"medals_27": self.medals_27,
				"medals_28": self.medals_28,
				"medals_29": self.medals_29,
				"medals_30": self.medals_30,
				"medals_31": self.medals_31,
				"medals_32": self.medals_32
			}

	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine
	
	def medal_calc(self):
		MedalsStats = self.local_data["MedalsStats"]
		medalsList = []
		for k,v in self.dictionnaire().items():
			medalsList.append(f"{v}-{k}")
		attack = 0
		attack_var = 0
		hp = 0
		hp_var = 0
		hero_base_enhanced = 0
		enhance_equipment = 0
		for i in medalsList:
			medal = i.split("-")
			if medal[0] == "True":
				type_medal_boost = MedalsStats["type_" + str(medal[1])]
				if type_medal_boost == "Attack":
					attack += MedalsStats["stats_" + str(medal[1])]
				elif type_medal_boost == "Attack%":
					attack_var += MedalsStats["stats_" + str(medal[1])]
				elif type_medal_boost == "Hp":
					hp += MedalsStats["stats_" + str(medal[1])]
				elif type_medal_boost == "Hp%":
					attack_var += MedalsStats["stats_" + str(medal[1])]
				elif type_medal_boost == "Hero Base Enhanced":
					hero_base_enhanced += MedalsStats["stats_" + str(medal[1])]
				elif type_medal_boost == "Enhance Equipment":
					enhance_equipment += MedalsStats["stats_" + str(medal[1])]
		return {
			"attack":attack,
			"attack_var":attack_var,
			"hp":hp,
			"hp_var":hp_var,
			"hero_base_enhanced":hero_base_enhanced,
			"enhance_equipment":enhance_equipment
		}

class relics_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	wraith_mask = models.CharField(max_length=15, blank=False, default="0-0-0")
	clown_mask = models.CharField(max_length=15, blank=False, default="0-0-0")
	princess_teddy_bear = models.CharField(max_length=10, blank=False, default="0-0")
	belt_of_might = models.CharField(max_length=15, blank=False, default="0-0-0")
	beastmaster_whistle = models.CharField(max_length=15, blank=False, default="0-0-0")
	archmage_robe = models.CharField(max_length=15, blank=False, default="0-0-0")
	shimmering_gem = models.CharField(max_length=10, blank=False, default="0-0")
	bloom_of_eternity = models.CharField(max_length=10, blank=False, default="0-0")
	challenger_headband = models.CharField(max_length=10, blank=False, default="0-0")
	jade_gobelet = models.CharField(max_length=10, blank=False, default="0-0")
	veteran_plate = models.CharField(max_length=10, blank=False, default="0-0")
	dragonscale = models.CharField(max_length=15, blank=False, default="0-0-0")
	dragon_tooth = models.CharField(max_length=10, blank=False, default="0-0")
	scholar_telescope = models.CharField(max_length=5, blank=False, default="0")
	pirate_shank = models.CharField(max_length=10, blank=False, default="0-0")
	giant_greatsword = models.CharField(max_length=15, blank=False, default="0-0-0")
	healing_potion = models.CharField(max_length=5, blank=False, default="0")
	whirlwind_mauler = models.CharField(max_length=10, blank=False, default="0-0")
	special_lance = models.CharField(max_length=15, blank=False, default="0-0-0")
	precision_slingshot = models.CharField(max_length=10, blank=False, default="0-0")
	supreme_trinity_alpha = models.CharField(max_length=15, blank=False, default="0-0-0")
	golden_apple = models.CharField(max_length=15, blank=False, default="0-0-0")
	ancient_stele = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	philosopher_stone = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	dragon_heart = models.CharField(max_length=15, blank=False, default="0-0-0")
	spectral_duality = models.CharField(max_length=15, blank=False, default="0-0-0")
	mystic_emblem = models.CharField(max_length=15, blank=False, default="0-0-0")
	immortal_brooch = models.CharField(max_length=15, blank=False, default="0-0-0")
	golden_statue = models.CharField(max_length=15, blank=False, default="0-0-0")
	smilling_mask = models.CharField(max_length=15, blank=False, default="0-0-0")
	unmerciful_mask = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	holy_water = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	book_of_the_dead = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	psionist_treasure = models.CharField(max_length=10, blank=False, default="0-0")
	book_of_archery = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	book_of_bravery = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	angelic_heart = models.CharField(max_length=10, blank=False, default="0-0")
	devil_whisper = models.CharField(max_length=15, blank=False, default="0-0-0")
	stone_of_wisdom = models.CharField(max_length=5, blank=False, default="0")
	empyrean_mirror = models.CharField(max_length=15, blank=False, default="0-0-0")
	fabled_archer_arrow = models.CharField(max_length=15, blank=False, default="0-0-0")
	shiny_gemmed_belt = models.CharField(max_length=10, blank=False, default="0-0")
	mythril_flux_mail = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	stealth_boots = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	assassin_dagger = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	gold_bunny = models.CharField(max_length=15, blank=False, default="0-0-0")
	genesis_staff = models.CharField(max_length=15, blank=False, default="0-0-0")
	bloodstained_sword = models.CharField(max_length=25, blank=False, default="0-0-0-0-0")
	starcluster_rage = models.CharField(max_length=25, blank=False, default="0-0-0-0-0")
	elven_king_cape = models.CharField(max_length=25, blank=False, default="0-0-0-0-0")
	spear_of_yggdrasil = models.CharField(max_length=25, blank=False, default="0-0-0-0-0")
	dragon_gem = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	life_crown = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	sand_of_time = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	first_lightning = models.CharField(max_length=15, blank=False, default="0-0-0")
	oracle_quill = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	bloodthirsty_grail = models.CharField(max_length=20, blank=False, default="0-0-0-0")
	healing_grail = models.CharField(max_length=15, blank=False, default="0-0-0")
	cupids_necklace = models.CharField(max_length=20, blank=False, default="0-0-0-0")


	def dictionnaire(self):
		return {
				"user_profile": self.user_profile,
				"wraith_mask": self.wraith_mask,
				"clown_mask": self.clown_mask,
				"princess_teddy_bear": self.princess_teddy_bear,
				"belt_of_might": self.belt_of_might,
				"beastmaster_whistle": self.beastmaster_whistle,
				"archmage_robe": self.archmage_robe,
				"shimmering_gem": self.shimmering_gem,
				"bloom_of_eternity": self.bloom_of_eternity,
				"challenger_headband": self.challenger_headband,
				"jade_gobelet": self.jade_gobelet,
				"veteran_plate": self.veteran_plate,
				"dragonscale": self.dragonscale,
				"dragon_tooth": self.dragon_tooth,
				"scholar_telescope": self.scholar_telescope,
				"pirate_shank": self.pirate_shank,
				"giant_greatsword": self.giant_greatsword,
				"healing_potion": self.healing_potion,
				"whirlwind_mauler": self.whirlwind_mauler,
				"special_lance": self.special_lance,
				"precision_slingshot": self.precision_slingshot,
				"supreme_trinity_alpha": self.supreme_trinity_alpha,
				"golden_apple": self.golden_apple,
				"ancient_stele": self.ancient_stele,
				"philosopher_stone": self.philosopher_stone,
				"dragon_heart": self.dragon_heart,
				"spectral_duality": self.spectral_duality,
				"mystic_emblem": self.mystic_emblem,
				"immortal_brooch": self.immortal_brooch,
				"golden_statue": self.golden_statue,
				"smilling_mask": self.smilling_mask,
				"unmerciful_mask": self.unmerciful_mask,
				"holy_water": self.holy_water,
				"book_of_the_dead": self.book_of_the_dead,
				"psionist_treasure": self.psionist_treasure,
				"book_of_archery": self.book_of_archery,
				"book_of_bravery": self.book_of_bravery,
				"angelic_heart": self.angelic_heart,
				"devil_whisper": self.devil_whisper,
				"stone_of_wisdom": self.stone_of_wisdom,
				"empyrean_mirror": self.empyrean_mirror,
				"fabled_archer_arrow": self.fabled_archer_arrow,
				"shiny_gemmed_belt": self.shiny_gemmed_belt,
				"mythril_flux_mail": self.mythril_flux_mail,
				"stealth_boots": self.stealth_boots,
				"assassin_dagger": self.assassin_dagger,
				"gold_bunny": self.gold_bunny,
				"genesis_staff": self.genesis_staff,
				"bloodstained_sword": self.bloodstained_sword,
				"starcluster_rage": self.starcluster_rage,
				"elven_king_cape": self.elven_king_cape,
				"spear_of_yggdrasil": self.spear_of_yggdrasil,
				"dragon_gem": self.dragon_gem,
				"life_crown": self.life_crown,
				"sand_of_time": self.sand_of_time,
				"first_lightning": self.first_lightning,
				"oracle_quill": self.oracle_quill,
				"bloodthirsty_grail": self.bloodthirsty_grail,
				"healing_grail": self.healing_grail,
				"cupids_necklace": self.cupids_necklace,
			}

	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine


	def relics_Stats(self):
		list_relic = []
		RelicLabel = self.local_data["RelicLabel"]
		for k,v in self.dictionnaire().items():
			if k != "user_profile":
				list_relic.append(v.split("-"))
		stats = {
			'':0,
			"attack": 0,
			"attack_var": 0,
			"hp": 0,
			"hp_var": 0,
			"enhance_equipment_var": 0,
			"hero_base_stats_increased_var": 0,
			"crit_chance_var": 0,
			"damage_ranged_units": 0,
			"damage_melee_units": 0,
			"damage_humanoid_enemies_var": 0,
			"damage_undead_var": 0,
			"damage_heroes_var": 0,
			"damage_elite_var": 0,
			"elemental_damage_var": 0,
			"damage_mobs": 0,
			"damage_mobs_var": 0,
			"damage_bosses": 0,
			"damage_bosses_var": 0,
			"damage_ground_units": 0,
			"damage_ground_units_var": 0,
			"damage_airborne_units": 0,
			"damage_airborne_units_var": 0,
			"weapon_melee_damage_var": 0,
			"weapon_ranged_damage_var": 0,
			"dodge":0,
			"attack_jewel_base":0,
		}
		relic_name = ["wraith_mask","clown_mask","princess_teddy_bear","belt_of_might","beastmaster_whistle","archmage_robe","shimmering_gem","bloom_of_eternity","challenger_headband","jade_gobelet","veteran_plate","dragonscale","dragon_tooth","scholar_telescope","pirate_shank","giant_greatsword","healing_potion","whirlwind_mauler","special_lance","precision_slingshot","supreme_trinity_alpha","golden_apple","ancient_stele","philosopher_stone","dragon_heart","spectral_duality","mystic_emblem","immortal_brooch","golden_statue","smilling_mask","unmerciful_mask","holy_water","book_of_the_dead","psionist_treasure","book_of_archery","book_of_bravery","angelic_heart","devil_whisper","stone_of_wisdom","empyrean_mirror","fabled_archer_arrow","shiny_gemmed_belt","mythril_flux_mail","stealth_boots","assassin_dagger","gold_bunny","genesis_staff","bloodstained_sword","starcluster_rage","elven_king_cape","spear_of_yggdrasil","dragon_gem","life_crown","sand_of_time","first_lightning","oracle_quill","bloodthirsty_grail","healing_grail","cupids_necklace"]
		for i in range(0,len(list_relic)):
			relic = relic_name[i]
			relic_boost = list_relic[i]
			for x in range(0,len(relic_boost)):
				search_data = RelicLabel[str(relic)+ "_" +str(x+1)]
				new_value = float(stats[search_data]) + float(relic_boost[x])
				stats.update({search_data:new_value})
				# if search_data != "":
				# 	print(f"{relic} | {relic_boost[x]} | {search_data} | {new_value}")
		return stats


class promo_code(models.Model,parentModel):
	code = models.CharField(max_length=30, blank=False)
	is_active = models.BooleanField(default=False)
	reward_1_type = models.CharField(max_length=20,choices= type_reward, default=" ")
	reward_1_amount = models.CharField(max_length=10, default=" ", blank=True, null=True)
	reward_2_type = models.CharField(max_length=20,choices= type_reward, default=" ")
	reward_2_amount = models.CharField(max_length=10, default=" ", blank=True, null=True)
	reward_3_type = models.CharField(max_length=20,choices= type_reward, default=" ")
	reward_3_amount = models.CharField(max_length=10, default=" ", blank=True, null=True)
	reward_4_type = models.CharField(max_length=20,choices= type_reward, default=" ")
	reward_4_amount = models.CharField(max_length=10, default=" ", blank=True, null=True)
	expire = models.DateField(blank=True, default=datetime.datetime.now, null=True)

	def __str__(self):
		return f"{self.code}"
	



class weapon_skins_table(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	demon_blade_rain_1 = models.BooleanField(blank=True, default=False)
	antiquated_sword_1 = models.BooleanField(blank=True, default=False)
	gale_force_1 = models.BooleanField(blank=True, default=False)
	death_scythe_1 = models.BooleanField(blank=True, default=False)
	boomerang_1 = models.BooleanField(blank=True, default=False)
	brightspear_1 = models.BooleanField(blank=True, default=False)
	saw_blade_1 = models.BooleanField(blank=True, default=False)
	brave_bow_1 = models.BooleanField(blank=True, default=False)
	stalker_staff_1 = models.BooleanField(blank=True, default=False)

	def dictionnaire(self):
		return {
				"user_profile": self.user_profile,
				"demon_blade_rain_1": self.demon_blade_rain_1,
				"antiquated_sword_1": self.antiquated_sword_1,
				"gale_force_1": self.gale_force_1,
				"death_scythe_1": self.death_scythe_1,
				"boomerang_1": self.boomerang_1,
				"brightspear_1": self.brightspear_1,
				"saw_blade_1": self.saw_blade_1,
				"brave_bow_1": self.brave_bow_1,
				"stalker_staff_1": self.stalker_staff_1
			}

	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine
	

	def equippedSkin(self):
		weapon_choosen = stuff_table.objects.get(user_profile=self.user_profile).weapon_choosen.replace(" ","_").lower()
		list_weapon_noskin = ['mini_atreus']
		## pour prochain skin faudra rajouter un moyen pour savoir quelle skin est équipé
		if weapon_choosen == "tornado":
			name_skin = "boomerang_1"
		elif weapon_choosen == "none" or weapon_choosen in list_weapon_noskin:
			return "None"
		else:
			name_skin = str(weapon_choosen) + "_1"
		if self.dictionnaire()[name_skin] == True:
			return name_skin
		else:
			return "None"
	
	def getWeaponSkinStats(self):
		WeaponSkinData = self.local_data["WeaponSkinData"]
		result = {
			"attack":0,
			"crit_rate":0,
			"none":0,
		}
		skin_equipped = self.equippedSkin()
		for k,v in self.dictionnaire().items():
			if v == True:
				skin_count = k.split("_")[-1]
				weapon_name = k.replace(f"_{skin_count}","") 
				all_hero_boost = WeaponSkinData[weapon_name][skin_count]["all_hero_type"]
				all_hero_value = WeaponSkinData[weapon_name][skin_count]["all_hero_value"] + result[all_hero_boost]
				result.update({all_hero_boost:all_hero_value})
				if skin_equipped == k:
					activ_type = WeaponSkinData[weapon_name][skin_count]["activ_type"]
					activ_boost = WeaponSkinData[weapon_name][skin_count]["activ_boost"] + result[activ_type]
					result.update({activ_type:activ_boost})
		return result