from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import datetime, math, json
from django.contrib.auth.models import User as BuiltinDjangoUser
from django.utils.crypto import get_random_string
from app.settings import DEBUG_STATS
from django.utils import timezone

class ServerManagement(models.Model):
	archeroVersion = models.CharField(max_length=20, default='Archero', blank=False, null=False)
	archeroIconLink = models.CharField(max_length=255, default='https://play-lh.googleusercontent.com/cMYvvKCxCnhIg0Gc4pbI0CgCqNw9l5lAFUAmAv4aXkK1nynqwiye8P8NxArULW9eMQ', blank=False, null=False)
	isMaintenance = models.BooleanField(default=False, blank=False)

class UserQueue(models.Model):
	username = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	is_validated = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

class Contributor(models.Model):
	label = models.CharField(max_length=40)
	
	def __str__(self):
		return self.label

class Token(models.Model):
	user = models.OneToOneField(BuiltinDjangoUser, on_delete=models.CASCADE)
	key = models.CharField(max_length=40, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	discord_acc_rely = models.CharField(max_length=40, default=" ", blank=True, null=True)
	discord_user_id = models.BigIntegerField(unique=True, blank=False, default=0)

	def save(self, *args, **kwargs):
		if not self.key:
			self.key = self.generate_key()
		return super(Token, self).save(*args, **kwargs)

	def generate_key(self):
		return get_random_string(40)

	def __str__(self):
		return self.key

# null=True sets NULL (versus NOT NULL) on the column in your DB.
# Blank values for Django field types such as DateTimeField or ForeignKey will be stored as NULL in the DB.
# blank determines whether the field will be required in forms.
# This includes the admin and your custom forms. If blank=True then the field will not be required, whereas if it's False the field cannot be blank.

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
dragon_rarity_index = {
	"Great":0,
	"Rare":1,
	"Epic":2,
	"Perfect_Epic":3,
	"Legendary":4,
	"Ancient_Legendary":5,
	"Mythic":6,
}

#(actual value, human readable name)
# default selected must be the value and not the human readable
# e.g : power_rune_all = (("none","None"),("attack_flat","Attack")) must be models.charField(.....default="none")
all_heros = (("Atreus","Atreus"),("Urasil","Urasil"),("Phoren","Phoren"),("Taranis","Taranis"),("Helix","Helix"),("Meowgik","Meowgik"),("Shari","Shari"),("Ayana","Ayana"),("Onir","Onir"),("Rolla","Rolla"),("Bonnie","Bonnie"),("Sylvan","Sylvan"),("Shade","Shade"),("Ophelia","Ophelia"),("Ryan","Ryan"),("Lina","Lina"),("Aquea","Aquea"),("Shingen","Shingen"),("Gugu","Gugu"),("Iris","Iris"),("Blazo","Blazo"),("Melinda","Melinda"),("Elaine","Elaine"),("Bobo","Bobo"),("Stella","Stella"),("Taiga","Taiga"))
stuff_weapon = (("None","None"),("Brave Bow","Brave Bow"),("Death Scythe","Death Scythe"),("Saw Blade","Saw Blade"),("Tornado","Tornado"),("Brightspear","Brightspear"),("Stalker Staff","Stalker Staff"),("Gale Force","Gale Force"),("Demon Blade Rain","Demon Blade Rain"),("Mini Atreus","Mini Atreus"),("Antiquated Sword","Antiquated Sword"),("Expedition Fist","Expedition Fist"))
stuff_armor = (("None","None"),("Phantom Cloak","Phantom Cloak"),("Vest of Dexterity","Vest of Dexterity"),("Golden Chestplate","Golden Chestplate"),("Void Robe","Void Robe"),("Bright Robe","Bright Robe"),("Shadow Robe","Shadow Robe"),("Expedition Plate","Expedition Plate"))
stuff_ring = (("None","None"),("Bear Ring","Bear Ring"),("Wolf Ring","Wolf Ring"),("Falcon Ring","Falcon Ring"),("Serpent Ring","Serpent Ring"),("Bull Ring","Bull Ring"),("Lion Ring","Lion Ring"),("Vilebat Ring","Vilebat Ring"),("Dragon Ring","Dragon Ring"),("Expedition Ring","Expedition Ring"))
stuff_pet = (("None","None"),("Laser Bat","Laser Bat"),("Scythe Mage","Scythe Mage"),("Elf","Elf"),("Living Bomb","Living Bomb"),("Noisy Owl","Noisy Owl"),("Flaming Ghost","Flaming Ghost"),("Bone Warrior","Bone Warrior"))
stuff_bracelet = (("None","None"),("Thunder Bracelet","Thunder Bracelet"),("Frozen Bracelet","Frozen Bracelet"),("Blazing Bracelet","Blazing Bracelet"),("Split Bracelet","Split Bracelet"),("Invincible Bracelet","Invincible Bracelet"),("Quickshot Bracelet","Quickshot Bracelet"),("Shield Bracelet","Shield Bracelet"),("Expedition Bracelet","Expedition Bracelet"))
stuff_locket = (("None","None"),("Agile Locket","Agile Locket"),("Iron Locket","Iron Locket"),("Angel Locket","Angel Locket"),("Bulletproof Locket","Bulletproof Locket"),("Piercer Locket","Piercer Locket"),("Bloodthirsty Locket","Bloodthirsty Locket"),("Counterattack Locket","Counterattack Locket"),("Expedition Locket","Expedition Locket"))
stuff_book = (("None","None"),("Arcane Archer","Arcane Archer"),("Art of Combat","Art of Combat"),("Ice Realm","Ice Realm"),("Enlightenment","Enlightenment"),("Giants Contract","Giants Contract"),("Spectre Book","Spectre Book"),("Arcanum of Time","Arcanum of Time"),("Expedition Spellbook","Expedition Spellbook"))
hero_level = ((120,"120"),(80,"80"),(60,"60"),(40,"40"),(20,"20"),(0,"0"))
star_hero = ((8,"8⭐"),(7,"7⭐"),(6,"6⭐"),(5,"5⭐"),(4,"4⭐"),(3,"3⭐"),(2,"2⭐"),(1,"1⭐"),(0,"0⭐"))
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
all_dragon = (("None","None"),("Glacion","Glacion"),("Infernox","Infernox"),("Stormra","Stormra"),("Noxion","Noxion"),("Shadex","Shadex"),("Jadeon","Jadeon"),("Dominus","Dominus"),("Ferron","Ferron"),("Geogon","Geogon"),("Swordian","Swordian"),("Necrogon","Necrogon"),("Starrite","Starrite"),("Voideon","Voideon"),("Magmar","Magmar"))
dragon_rarity = (("Great","Great"),("Rare","Rare"),("Epic","Epic"),("Perfect Epic","Perfect Epic"),("Legendary","Legendary"),("Ancient Legendary","Ancient Legendary"),("Mythic","Mythic"))
reforge = ((0,0),(20,20),(40,40),(60,60),(80,80),(100,100),(120,120),(140,140),(160,160),(180,180),(200,200),(220,220),(240,240),(260,260),(280,280),(300,300),(320,320),(340,340),(360,360),(380,380),(400,400),(450,450),(500,500),(550,550),(600,600),(650,650),(700,700),(750,750),(800,800),(850,850),(900,900),(950,950),(1000,1000))
altar_ascension_level = ((12,12),(11,11),(10,10),(9,9),(8,8),(7,7),(6,6),(5,5),(4,4),(3,3),(2,2),(1,1),(0,0))
jewel_level = ((13,13),(12,12),(11,11),(10,10),(9,9),(8,8),(7,7),(6,6),(5,5),(4,4),(3,3),(2,2),(1,1))
dragon_skill_level = ((10,10),(9,9),(8,8),(7,7),(6,6),(5,5),(4,4),(3,3),(2,2),(1,1),(0,0))
brave_level_choice = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20))
relics_level = ((0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20),(21,21),(22,22),(23,23),(24,24),(25,25),(26,26),(27,27),(28,28),(29,29),(30,30))
rare_relics_star = ((0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8))
radiant_relics_star = ((0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6))
holy_relics_star = ((0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6))
power_rune_all = (
	("none","None"),("attack_flat","Attack"),("attack_var","Attack %"),
	("flat_dmg_airborne","Damage to Airborne Units"),("var_dmg_airborne","Damage to Airborne Units %"),
	("flat_dmg_ground","Damage to Ground Units"),("var_dmg_ground","Damage to Ground Units %"),
	("flat_dmg_melee","Damage to Melee Units"),("var_dmg_melee","Damage to Melee Units %"),
	("flat_dmg_ranged","Damage to Ranged Units"),("var_dmg_ranged","Damage to Ranged Units %"),
	("flat_dmg_boss","Damage to Bosses Units"),("var_dmg_boss","Damage to Bosses Units %"),
	("flat_dmg_mob","Damage to Mobs Units"),("var_dmg_mob","Damage to Mobs Units %"),
	("var_dmg_hero","Damage to Heroes %"),("var_all_dmg","All Damage %"),
	("var_elemental_dmg","Elemental Damage %"),("var_atk_speed","Attack Speed %"),
	("var_crit_rate","Critic Chance %"),("var_crit_dmg","Critic Damage %")
)
saviour_rune_all = (
	("none","None"),
	("hp_flat","Max Hp"),
	("hp_var","Max Hp %"),
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
	("hp_flat","Max Hp"),
	("flat_heal_red_heart","Healing Effect of Red Heart"),
	("var_heal_red_heart","Healing Effect of Red Heart %"),
	("flat_hp_drop","HP drops"),
	("var_hp_drop","HP drops %"),
	("var_atk_headshot","Attack Increased 3s within HeadShot")
)
courage_rune_all = (
	("none","None"),("attack_flat","Attack"),("attack_var","Attack %"),
	("courage_hero_attack_flat","Current Hero Attack"),
	("courage_hero_attack_var","Current Hero Attack %"),
	("courage_hero_hp_flat","Current Hero Hp"),
	("courage_hero_hp_var","Current Hero Hp %"),
	("flat_dmg_flame","Flame Damage"),("var_dmg_flame","Flame Damage %"),
	("flat_dmg_ice","Ice Damage"),("var_dmg_ice","Ice Damage %"),
	("flat_dmg_poison","Poison Damage"),("var_dmg_poison","Poison Damage %"),
	("flat_dmg_lightning","Lightning Damage"),("var_dmg_lightning","Lightning Damage %"),
	("flat_dmg_dark","Dark Touch Damage"),("var_dmg_dark","Dark Touch Damage %"),
)
luck_rune_all = (
	("none","None"),
	("hp_flat","Max Hp"),
	("hp_var","Max Hp %"),
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
	public_profile = models.BooleanField(default=True, blank=False)

	def getOtherModels(self)->dict:
			return {
				"StuffTable": self.stufftable_set.get(),
				"HeroTable":self.herotable_set.get(),
				"TalentTable":self.talenttable_set.get(),
				"SkinTable":self.skintable_set.get(),
				"AltarTable":self.altartable_set.get(),
				"JewelTypeTable":self.jeweltypetable_set.get(),
				"JewelLevelTable":self.jewelleveltable_set.get(),
				"EggTable":self.eggtable_set.get(),
				"EggEquippedTable":self.eggequippedtable_set.get(),
				"DragonTable":self.dragontable_set.get(),
				"RunesTable":self.runestable_set.get(),
				"ReforgeTable":self.reforgetable_set.get(),
				"RefineTable":self.refinetable_set.get(),
				"MedalsTable":self.medalstable_set.get(),
				"RelicsTable":self.relicstable_set.get(),
				"WeaponSkinsTable":self.weaponskinstable_set.get(),
			}

	def duplicate(self, new_Userusername, new_Useringameid):
		from .function import create_unique_id
		target = user.objects.get(pk=self.pk)
		self.pk = None
		self.ingame_id = new_Useringameid
		self.ingame_name = new_Userusername
		self.public_id = create_unique_id()
		self.save()
		for childTarget in target.getOtherModels().values():
			childTarget.pk = None
			childTarget.user_profile = self
			childTarget.save()

	def __str__(self):
		chaine = f"{self.ingame_name}'s stats ({self.ingame_id})"
		return chaine

	def dictionnaire(self):
			return {
					"ingame_id": self.ingame_id,
					"ingame_name": self.ingame_name,
					'choosen_hero': self.choosen_hero,
					'brave_privileges_level': self.brave_privileges_level,
					'atk_base_stats_hero_choosen': self.atk_base_stats_hero_choosen,
					'health_base_stats_hero_choosen': self.health_base_stats_hero_choosen,
					}

class StuffTable(models.Model,parentModel):
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
			'weapon_critdmg_raw' : self.local_data["StatsWeapon"][str(weapon_name)]["crit"][rarity_index[str(weapon_rarity)]],
			'weapon_critrate_raw' : self.local_data["StatsWeapon"][str(weapon_name)]["crit_rate"][rarity_index[str(weapon_rarity)]],
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

	def getStuffStats(self,enhanced_equipment_total,weapon_refine_basic_stats,armor_refine_basic_stats,ring1_refine_basic_stats,ring2_refine_basic_stats,bracelet_refine_basic_stats,locket_refine_basic_stats,book_refine_basic_stats,weapon_skin_stats,relic_ring_stats):
		all_raw_stats = self.GetRawStats()
		global_enhance_eqm = enhanced_equipment_total + all_raw_stats['book_enhance_eqm']
		weapon_eh_eq = global_enhance_eqm + float(weapon_refine_basic_stats) + float(all_raw_stats["weapon_basic_stats"])
		weapon_base = math.floor((int(all_raw_stats['weapon_base_raw']) + int(all_raw_stats['weapon_inc_raw']) * ( self.weapon_level-1)) * (weapon_eh_eq))
		weapon_total = math.floor(weapon_base + math.floor(int(weapon_skin_stats['attack']) * (weapon_eh_eq)))

		armor_eh_eq = global_enhance_eqm + float(all_raw_stats["armor_basic_stats"]) + float(armor_refine_basic_stats)
		armor_base = math.floor((int(all_raw_stats['armor_base_raw']) + int(all_raw_stats['armor_inc_raw']) * ( self.armor_level-1)) * (armor_eh_eq))

		ring1_eh_eq = global_enhance_eqm + float(all_raw_stats["ring1_basic_stats"]) + float(ring1_refine_basic_stats) + float(relic_ring_stats)
		ring1_base = math.floor((int(all_raw_stats['ring1_base_raw']) + int(all_raw_stats['ring1_inc_raw']) * ( self.ring1_level-1)) * (ring1_eh_eq))
		
		ring2_eh_eq = global_enhance_eqm + float(all_raw_stats["ring2_basic_stats"]) + float(ring2_refine_basic_stats) + float(relic_ring_stats)
		ring2_base = math.floor((int(all_raw_stats['ring2_base_raw']) + int(all_raw_stats['ring2_inc_raw']) * ( self.ring2_level-1)) * (ring2_eh_eq))

		bracelet_eh_eq = global_enhance_eqm + float(all_raw_stats["bracelet_basic_stats"]) + float(bracelet_refine_basic_stats)
		bracelet_base = math.floor((int(all_raw_stats['bracelet_base_raw']) + int(all_raw_stats['bracelet_inc_raw']) * ( self.bracelet_level-1)) * (bracelet_eh_eq))

		locket_eh_eq = global_enhance_eqm + float(all_raw_stats["locket_basic_stats"]) + float(locket_refine_basic_stats)
		locket_base = math.floor((int(all_raw_stats['locket_base_raw']) + int(all_raw_stats['locket_inc_raw']) * ( self.locket_level-1)) * (locket_eh_eq))

		book_eh_eq = global_enhance_eqm + float(all_raw_stats["book_basic_stats"]) + float(book_refine_basic_stats)
		book_base = math.floor((int(all_raw_stats['book_base_raw']) + int(all_raw_stats['book_inc_raw']) * ( self.book_level-1)) * (book_eh_eq))
		result = {
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
		if DEBUG_STATS:
			print(f"\ngetStuffStats :{result}\n")
		return result


class HeroTable(models.Model,parentModel):
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
	taiga_level = models.IntegerField(choices=hero_level, default=0)
	taiga_star = models.IntegerField(choices=star_hero, default=0)


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
					'taiga_level': self.taiga_level, 'taiga_star': self.taiga_star,
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


class TalentTable(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	strength_level = models.IntegerField(validators=[MaxValueValidator(25)], default=0)
	power_level = models.IntegerField(validators=[MaxValueValidator(25)], default=0)
	recover_level = models.IntegerField(validators=[MaxValueValidator(25)], default=0)
	block_level = models.IntegerField(validators=[MaxValueValidator(25)], default=0)
	iron_bulwark_level = models.IntegerField(validators=[MaxValueValidator(25)], default=0)
	enhanced_equipment_level = models.IntegerField(validators=[MaxValueValidator(10)], default=0)
	hero_power_up_level = models.IntegerField(validators=[MaxValueValidator(10)], default=0)
	runes_power_up_level = models.IntegerField(validators=[MaxValueValidator(15)], default=0)

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


class SkinTable(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	skin_health = models.IntegerField(default=0, validators=[MaxValueValidator(18000)])
	skin_attack = models.IntegerField(default=0, validators=[MaxValueValidator(3800)])

	def dictionnaire(self):
			return {
					"user_profile": self.user_profile,
					'skin_health': self.skin_health,
					'skin_attack': self.skin_attack,
					}
	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine



class AltarTable(models.Model,parentModel):
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
	
	def RoundTen(self,x) -> int:
		if int(x) % 10==0:
			pass
		else:
			while int(x) % 10>0:
				x=x-1
		return x

	def CalculAltar(self,type_altar,type_boost,stuff_altar_boost_relic):
		if type_altar == "stuff":
			data = self.local_data["StuffAltar"]
			altar_var_stats = stuff_altar_boost_relic
		elif type_altar == "heros":
			data = self.local_data["HerosAltar"]
			altar_var_stats = 0
		level = self.dictionnaire()[type_altar + '_altar_level']
		levelRoundTen = int(self.RoundTen(level) / 10)
		base = int(data[type_boost][levelRoundTen]) * float(1+altar_var_stats/100)
		inc = int(data['inc_' + type_boost][int(levelRoundTen)]) * float(1+altar_var_stats/100)
		diff = level - levelRoundTen
		if 1 <= diff <= 9:
			total = base+((level - levelRoundTen)*inc)
		else:
			total = base
		if DEBUG_STATS:
			print(f"\nCalculAltar :{total}\n")
		return total


class JewelTypeTable(models.Model,parentModel):
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


class JewelLevelTable(models.Model,parentModel):
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

	def JewelStatsRecup(self,attack_jewel_base:float,hp_jewel_base:float):
		jewels_type = list(JewelTypeTable.objects.get(user_profile=self.user_profile).dictionnaire().values())
		jewels_level = list(self.dictionnaire().values())
		list_type = []
		result =  {}
		JewelStats = self.local_data['JewelStats']
		for i in range(1,len(jewels_type)): # 1 car l'index 0 = user_profile
			list_type.append(str(jewels_type[i]) + "_" + str(jewels_level[i]))
		try:
			list_type.remove(str(self.user_profile.ingame_id)+"_"+str(self.user_profile.ingame_id))
		except ValueError:
			pass
		for jewel in list_type:
			jewel_type = jewel.split("_")[0]
			jewel_level = jewel.split("_")[1]
			for v in dict(JewelStats[jewel_type]).values():
				value = int(result.get(v['label'],0)) + int(v['value'][int(jewel_level)-1])
				result.update({v['label']: value})
		result_jewel_attack = result.get("attack_flat",0)
		result_jewel_hp = result.get("hp_flat",0)
		result.update({
			"attack":math.floor(math.floor(result_jewel_attack)*(1+attack_jewel_base/100)),
			"hp":math.floor(math.floor(result_jewel_hp)*(1+hp_jewel_base/100))
		})
		
		if DEBUG_STATS:
			print(f"\nJewelStatsRecup :{result}\n")
		return result

	def JewelSpeBonusStatsRecup(self,type_jewel,brave_boost,relic_jewel_base=0)->dict:
		result = {}
		JewelSpeBonus = self.local_data['JewelSpeBonus']
		jewel_type = JewelTypeTable.objects.get(user_profile=self.user_profile).dictionnaire()
		jewel1_type = jewel_type[str(type_jewel)+"_jewel1_type"]
		jewel2_type = jewel_type[str(type_jewel)+"_jewel2_type"]
		jewel3_type = jewel_type[str(type_jewel)+"_jewel3_type"]
		jewel4_type = jewel_type[str(type_jewel)+"_jewel4_type"]
		jewel1_level = self.dictionnaire()[str(type_jewel)+"_jewel1_level"] if jewel1_type != "none" else 0
		jewel2_level = self.dictionnaire()[str(type_jewel)+"_jewel2_level"] if jewel2_type != "none" else 0
		jewel3_level = self.dictionnaire()[str(type_jewel)+"_jewel3_level"] if jewel3_type != "none" else 0
		jewel4_level = self.dictionnaire()[str(type_jewel)+"_jewel4_level"] if jewel4_type != "none" else 0
		sum_lvl = int(jewel1_level) + int(jewel2_level) + int(jewel3_level) + int(jewel4_level) + int(brave_boost)
		if sum_lvl >= 4:
			value_4 = result.get(JewelSpeBonus[type_jewel]["4"]["label"],0) + int(JewelSpeBonus[type_jewel]["4"]["value"])
			result.update({JewelSpeBonus[type_jewel]["4"]["label"]:value_4})
			if sum_lvl >= 8:
				value_8 = result.get(JewelSpeBonus[type_jewel]["8"]["label"],0) + int(JewelSpeBonus[type_jewel]["8"]["value"])
				result.update({JewelSpeBonus[type_jewel]["8"]["label"]:value_8})
				if sum_lvl >= 16:
					value_16 = result.get(JewelSpeBonus[type_jewel]["16"]["label"],0) + int(JewelSpeBonus[type_jewel]["16"]["value"])
					result.update({JewelSpeBonus[type_jewel]["16"]["label"]:value_16})
					if sum_lvl >= 28:
						value_28 = result.get(JewelSpeBonus[type_jewel]["28"]["label"],0) + int(JewelSpeBonus[type_jewel]["28"]["value"])
						result.update({JewelSpeBonus[type_jewel]["28"]["label"]:value_28})
						if sum_lvl >= 38:
							value_38 = result.get(JewelSpeBonus[type_jewel]["38"]["label"],0) + int(JewelSpeBonus[type_jewel]["38"]["value"])
							result.update({JewelSpeBonus[type_jewel]["38"]["label"]:value_38})
							if sum_lvl >= 48:
								value_48 = result.get(JewelSpeBonus[type_jewel]["48"]["label"],0) + int(JewelSpeBonus[type_jewel]["48"]["value"])
								result.update({JewelSpeBonus[type_jewel]["48"]["label"]:value_48})		
		result['attack_flat'] = result.get('attack_flat',0) * (1+relic_jewel_base/100)
		result['hp_flat'] = result.get('hp_flat',0) * (1+relic_jewel_base/100)
		if DEBUG_STATS:
			print(f"\nJewelSpeBonusStatsRecup :{result}\n")
		return result

	def allLevelForImage(self):
		jewel_type = JewelTypeTable.objects.get(user_profile=self.user_profile).dictionnaire()
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




class EggTable(models.Model,parentModel):
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


class EggEquippedTable(models.Model,parentModel):
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
		all_egg = EggTable.objects.get(user_profile=self.user_profile).dictionnaire()
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
		if DEBUG_STATS:
			print(f"\nGetEggStats :{dict_stats}\n")
		return dict_stats



class DragonTable(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	dragon1_type = models.CharField(max_length=30, choices=all_dragon, default="None")
	dragon2_type = models.CharField(max_length=30, choices=all_dragon, default="None")
	dragon3_type = models.CharField(max_length=30, choices=all_dragon, default="None")
	dragon1_rarity = models.CharField(max_length=30, choices=dragon_rarity, default="Great")
	dragon2_rarity = models.CharField(max_length=30, choices=dragon_rarity, default="Great")
	dragon3_rarity = models.CharField(max_length=30, choices=dragon_rarity, default="Great")
	dragon1_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(120)]) 
	dragon2_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(120)]) 
	dragon3_level = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(120)])
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

	def DragonStatueStats(self,relic_dragon_boost):
		dict_result = {}
		for i in range(1,4):
			dragon_type = self.GetDragon(str(i))['dragon_type']
			dragon_rarity = dragon_rarity_index[self.GetDragon(str(i))['dragon_rarity']]
			dragon_level = self.GetDragon(str(i))['dragon_level']
			dragon_skill_4 = self.GetDragon(str(i))['dragon_skill_4']
			base_stats1 = self.local_data["DragonStats"][dragon_type.lower()]["base_1"][dragon_rarity]
			base_stats2 = self.local_data["DragonStats"][dragon_type.lower()]["base_2"][dragon_rarity]
			b1_type = self.local_data["DragonStats"][dragon_type.lower()]["bonus1"]
			b2_type = self.local_data["DragonStats"][dragon_type.lower()]["bonus2"]
			inc_stats1 = self.local_data["DragonStats"][dragon_type.lower()]["inc_1"][dragon_rarity]
			inc_stats2 = self.local_data["DragonStats"][dragon_type.lower()]["inc_2"][dragon_rarity]

			dragon_base_stats_inc = 1
			dragon_base_stats_base = relic_dragon_boost
			if dragon_rarity == "Mythic" and int(dragon_skill_4) > 0:
				dragon_base_stats_values = self.local_data["DragonStats"][dragon_type.lower()]["mythic_boost_inc"]
				dragon_base_stats_inc = math.floor(dragon_base_stats_inc + dragon_base_stats_values[0])
				dragon_base_stats_base = math.floor(dragon_base_stats_base + dragon_base_stats_values[1])
				dragon_base_stats = (float(dragon_base_stats_inc) * (int(dragon_skill_4)-1)) + int(dragon_base_stats_base)
			else:
				dragon_base_stats = int(dragon_base_stats_base)
			inc_stats1_modified = math.floor(float(inc_stats1) * (float(dragon_base_stats)/100+1))
			inc_stats2_modified = math.floor(float(inc_stats2) * (float(dragon_base_stats)/100+1))
			result_stats1 = (float(base_stats1) + (float(dragon_level)-1)*inc_stats1_modified)*(float(dragon_base_stats_base)/100+1)  ## c'est pas les bonnes formules mais 
			result_stats2 = (float(base_stats2) + (float(dragon_level)-1)*inc_stats2_modified)*(float(dragon_base_stats_base)/100+1)  ## le résultat est proches de la réalité
			
			if dragon_rarity == "Mythic" or dragon_rarity == "Ancient Legendary":
				b3_type = self.local_data["DragonStats"][str(dragon_type).lower() + "_bonus3"]
				if dragon_rarity == "Ancient Legendary":
					b3_boost = self.local_data["DragonStats"][str(dragon_type).lower() + "_stats_boost3"][0]
				elif dragon_rarity == "Mythic":
					b3_boost = self.local_data["DragonStats"][str(dragon_type).lower() + "_stats_boost3"][1]
			else:
				b3_type = 0
				b3_boost = 0
			a_value = dict_result.get(b1_type,0) + math.floor(result_stats1)
			b_value = dict_result.get(b2_type,0) + math.floor(result_stats2)
			c_value = dict_result.get(b3_type,0) + float(b3_boost)
			dict_result.update({b1_type: a_value,b2_type: b_value,b3_type: c_value})
		if DEBUG_STATS:
			print(f"\nDragonStatueStats :{dict_result}\n")
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



class RunesTable(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	power_line_1 = models.CharField(choices=power_rune_all,default="none", max_length=30)
	power_line_2 = models.CharField(choices=power_rune_all,default="none", max_length=30)
	power_line_3 = models.CharField(choices=power_rune_all,default="none", max_length=30)
	power_line_4 = models.CharField(choices=power_rune_all,default="none", max_length=30)
	power_line_5 = models.CharField(choices=power_rune_all,default="none", max_length=30)
	saviour_line_1 = models.CharField(choices=saviour_rune_all,default="none", max_length=30)
	saviour_line_2 = models.CharField(choices=saviour_rune_all,default="none", max_length=30)
	saviour_line_3 = models.CharField(choices=saviour_rune_all,default="none", max_length=30)
	saviour_line_4 = models.CharField(choices=saviour_rune_all,default="none", max_length=30)
	saviour_line_5 = models.CharField(choices=saviour_rune_all,default="none", max_length=30)
	recovery_line_1 = models.CharField(choices=recovery_rune_all,default="none", max_length=30)
	recovery_line_2 = models.CharField(choices=recovery_rune_all,default="none", max_length=30)
	recovery_line_3 = models.CharField(choices=recovery_rune_all,default="none", max_length=30)
	recovery_line_4 = models.CharField(choices=recovery_rune_all,default="none", max_length=30)
	recovery_line_5 = models.CharField(choices=recovery_rune_all,default="none", max_length=30)
	courage_line_1 = models.CharField(choices=courage_rune_all,default="none", max_length=30)
	courage_line_2 = models.CharField(choices=courage_rune_all,default="none", max_length=30)
	courage_line_3 = models.CharField(choices=courage_rune_all,default="none", max_length=30)
	courage_line_4 = models.CharField(choices=courage_rune_all,default="none", max_length=30)
	courage_line_5 = models.CharField(choices=courage_rune_all,default="none", max_length=30)
	luck_line_1 = models.CharField(choices=luck_rune_all,default="none", max_length=30)
	luck_line_2 = models.CharField(choices=luck_rune_all,default="none", max_length=30)
	luck_line_3 = models.CharField(choices=luck_rune_all,default="none", max_length=30)
	luck_line_4 = models.CharField(choices=luck_rune_all,default="none", max_length=30)
	luck_line_5 = models.CharField(choices=luck_rune_all,default="none", max_length=30)
	value_power_line_1 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(750)])
	value_power_line_2 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(750)])
	value_power_line_3 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(750)])
	value_power_line_4 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(750)])
	value_power_line_5 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(750)])
	value_saviour_line_1 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2800)])
	value_saviour_line_2 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2800)])
	value_saviour_line_3 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2800)])
	value_saviour_line_4 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2800)])
	value_saviour_line_5 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2800)])
	value_recovery_line_1 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2250)])
	value_recovery_line_2 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2250)])
	value_recovery_line_3 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2250)])
	value_recovery_line_4 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2250)])
	value_recovery_line_5 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2250)])
	value_courage_line_1 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(750)])
	value_courage_line_2 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(750)])
	value_courage_line_3 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(750)])
	value_courage_line_4 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(750)])
	value_courage_line_5 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(750)])
	value_luck_line_1 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2800)])
	value_luck_line_2 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2800)])
	value_luck_line_3 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2800)])
	value_luck_line_4 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2800)])
	value_luck_line_5 = models.FloatField(default=0, blank=False, validators=[MaxValueValidator(2800)])


	def dictionnaire(self):
			return {
				"user_profile": self.user_profile,
				"power_line_1":self.power_line_1,
				"power_line_2":self.power_line_2,
				"power_line_3":self.power_line_3,
				"power_line_4":self.power_line_4,
				"power_line_5":self.power_line_5,
				"saviour_line_1":self.saviour_line_1,
				"saviour_line_2":self.saviour_line_2,
				"saviour_line_3":self.saviour_line_3,
				"saviour_line_4":self.saviour_line_4,
				"saviour_line_5":self.saviour_line_5,
				"recovery_line_1":self.recovery_line_1,
				"recovery_line_2":self.recovery_line_2,
				"recovery_line_3":self.recovery_line_3,
				"recovery_line_4":self.recovery_line_4,
				"recovery_line_5":self.recovery_line_5,
				"courage_line_1":self.courage_line_1,
				"courage_line_2":self.courage_line_2,
				"courage_line_3":self.courage_line_3,
				"courage_line_4":self.courage_line_4,
				"courage_line_5":self.courage_line_5,
				"luck_line_1":self.luck_line_1,
				"luck_line_2":self.luck_line_2,
				"luck_line_3":self.luck_line_3,
				"luck_line_4":self.luck_line_4,
				"luck_line_5":self.luck_line_5,
				"value_power_line_1":self.value_power_line_1,
				"value_power_line_2":self.value_power_line_2,
				"value_power_line_3":self.value_power_line_3,
				"value_power_line_4":self.value_power_line_4,
				"value_power_line_5":self.value_power_line_5,
				"value_saviour_line_1":self.value_saviour_line_1,
				"value_saviour_line_2":self.value_saviour_line_2,
				"value_saviour_line_3":self.value_saviour_line_3,
				"value_saviour_line_4":self.value_saviour_line_4,
				"value_saviour_line_5":self.value_saviour_line_5,
				"value_recovery_line_1":self.value_recovery_line_1,
				"value_recovery_line_2":self.value_recovery_line_2,
				"value_recovery_line_3":self.value_recovery_line_3,
				"value_recovery_line_4":self.value_recovery_line_4,
				"value_recovery_line_5":self.value_recovery_line_5,
				"value_courage_line_1":self.value_courage_line_1,
				"value_courage_line_2":self.value_courage_line_2,
				"value_courage_line_3":self.value_courage_line_3,
				"value_courage_line_4":self.value_courage_line_4,
				"value_courage_line_5":self.value_courage_line_5,
				"value_luck_line_1":self.value_luck_line_1,
				"value_luck_line_2":self.value_luck_line_2,
				"value_luck_line_3":self.value_luck_line_3,
				"value_luck_line_4":self.value_luck_line_4,
				"value_luck_line_5":self.value_luck_line_5,
			}
	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine

	
	def getRunesDmgCalc(self):
		return {
			"courage_first_select": self.courage_line_1,
			"courage_first_input": self.value_courage_line_1,
			"courage_second_select": self.courage_line_2,
			"courage_second_input": self.value_courage_line_2,
			"courage_third_select": self.courage_line_3,
			"courage_third_input": self.value_courage_line_3,
			"courage_fourth_select": self.courage_line_4,
			"courage_fourth_input": self.value_courage_line_4,
			"courage_fifth_select": self.courage_line_5,
			"courage_fifth_input": self.value_courage_line_5,
			"power_first_select": self.power_line_1,
			"power_first_input": self.value_power_line_1,
			"power_second_select": self.power_line_2,
			"power_second_input": self.value_power_line_2,
			"power_third_select": self.power_line_3,
			"power_third_input": self.value_power_line_3,
			"power_fourth_select": self.power_line_4,
			"power_fourth_input": self.value_power_line_4,
			"power_fifth_select": self.power_line_5,
			"power_fifth_input": self.value_power_line_5
		}

	def getValueLinePower(self):
		return {
			self.power_line_1: self.value_power_line_1,
			self.power_line_2: self.value_power_line_2,
			self.power_line_3: self.value_power_line_3,
			self.power_line_4: self.value_power_line_4,
			self.power_line_5: self.value_power_line_5
		}
	def getValueLineSaviour(self):
		return {
			self.saviour_line_1: self.value_saviour_line_1,
			self.saviour_line_2: self.value_saviour_line_2,
			self.saviour_line_3: self.value_saviour_line_3,
			self.saviour_line_4: self.value_saviour_line_4,
			self.saviour_line_5: self.value_saviour_line_5,
		}
	def getValueLineRecovery(self):
		return {
			self.recovery_line_1: self.value_recovery_line_1,
			self.recovery_line_2: self.value_recovery_line_2,
			self.recovery_line_3: self.value_recovery_line_3,
			self.recovery_line_4: self.value_recovery_line_4,
			self.recovery_line_5: self.value_recovery_line_5,
		}
	def getValueLineCourage(self):
		return {
			self.courage_line_1: self.value_courage_line_1,
			self.courage_line_2: self.value_courage_line_2,
			self.courage_line_3: self.value_courage_line_3,
			self.courage_line_4: self.value_courage_line_4,
			self.courage_line_5: self.value_courage_line_5,
		}
	def getValueLineLuck(self):
		return {
			self.luck_line_1: self.value_luck_line_1,
			self.luck_line_2: self.value_luck_line_2,
			self.luck_line_3: self.value_luck_line_3,
			self.luck_line_4: self.value_luck_line_4,
			self.luck_line_5: self.value_luck_line_5
		}


class ReforgeTable(models.Model,parentModel):
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


class RefineTable(models.Model,parentModel):
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


class DamageCalcTable(models.Model,parentModel):
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

	def calculDamage(self, **kwargs) -> dict:
		crit_dmg = float(kwargs.get("crit_dmg",self.crit_dmg))/100
		crit_rate = kwargs.get("crit_rate",self.crit_rate)
		mob_ground_melee = round((int(kwargs.get("global_atk_save",self.user_profile.global_atk_save)) + int(kwargs.get("flat_dmg_vs_ground",self.flat_dmg_vs_ground)) + int(kwargs.get("flat_dmg_vs_mobs",self.flat_dmg_vs_mobs)) + int(kwargs.get("flat_dmg_vs_melee",self.flat_dmg_vs_melee)) + int(kwargs.get("flat_dmg_all",self.flat_dmg_all)))*(float(kwargs.get("var_dmg_vs_melee",self.var_dmg_vs_melee)/100) + float(kwargs.get("var_dmg_vs_ground",self.var_dmg_vs_ground)/100) + float(1))*(float(kwargs.get("var_dmg_vs_mobs",self.var_dmg_vs_mobs)/100) + float(1))*(float(kwargs.get("var_dmg_all",self.var_dmg_all)/100) + float(1))*(float(kwargs.get("weapon_coeff",self.weapon_coeff))))
		mob_ground_range = round((int(kwargs.get("global_atk_save",self.user_profile.global_atk_save)) + int(kwargs.get("flat_dmg_vs_ground",self.flat_dmg_vs_ground)) + int(kwargs.get("flat_dmg_vs_mobs",self.flat_dmg_vs_mobs)) + int(kwargs.get("flat_dmg_vs_range",self.flat_dmg_vs_range)) + int(kwargs.get("flat_dmg_all",self.flat_dmg_all)))*(float(kwargs.get("var_dmg_vs_range",self.var_dmg_vs_range)/100) + float(kwargs.get("var_dmg_vs_ground",self.var_dmg_vs_ground)/100) + float(1))*(float(kwargs.get("var_dmg_vs_mobs",self.var_dmg_vs_mobs)/100) + float(1))*(float(kwargs.get("var_dmg_all",self.var_dmg_all)/100) + float(1))*(float(kwargs.get("weapon_coeff",self.weapon_coeff))))
		mob_airborne_melee = round((int(kwargs.get("global_atk_save",self.user_profile.global_atk_save)) + int(kwargs.get("flat_dmg_vs_airborne",self.flat_dmg_vs_airborne)) + int(kwargs.get("flat_dmg_vs_mobs",self.flat_dmg_vs_mobs)) + int(kwargs.get("flat_dmg_vs_melee",self.flat_dmg_vs_melee)) + int(kwargs.get("flat_dmg_all",self.flat_dmg_all)))*(float(kwargs.get("var_dmg_vs_melee",self.var_dmg_vs_melee)/100) + float(kwargs.get("var_dmg_vs_airborne",self.var_dmg_vs_airborne)/100) + float(1))*(float(kwargs.get("var_dmg_vs_mobs",self.var_dmg_vs_mobs)/100) + float(1))*(float(kwargs.get("var_dmg_all",self.var_dmg_all)/100) + float(1))*(float(kwargs.get("weapon_coeff",self.weapon_coeff))))
		mob_airborne_range = round((int(kwargs.get("global_atk_save",self.user_profile.global_atk_save)) + int(kwargs.get("flat_dmg_vs_airborne",self.flat_dmg_vs_airborne)) + int(kwargs.get("flat_dmg_vs_mobs",self.flat_dmg_vs_mobs)) + int(kwargs.get("flat_dmg_vs_range",self.flat_dmg_vs_range)) + int(kwargs.get("flat_dmg_all",self.flat_dmg_all)))*(float(kwargs.get("var_dmg_vs_range",self.var_dmg_vs_range)/100) + float(kwargs.get("var_dmg_vs_airborne",self.var_dmg_vs_airborne)/100) + float(1))*(float(kwargs.get("var_dmg_vs_mobs",self.var_dmg_vs_mobs)/100) + float(1))*(float(kwargs.get("var_dmg_all",self.var_dmg_all)/100) + float(1))*(float(kwargs.get("weapon_coeff",self.weapon_coeff))))
		boss_ground_melee = round((int(kwargs.get("global_atk_save",self.user_profile.global_atk_save)) + int(kwargs.get("flat_dmg_vs_ground",self.flat_dmg_vs_ground)) + int(kwargs.get("flat_dmg_vs_boss",self.flat_dmg_vs_boss)) + int(kwargs.get("flat_dmg_vs_melee",self.flat_dmg_vs_melee)) + int(kwargs.get("flat_dmg_all",self.flat_dmg_all)))*(float(kwargs.get("var_dmg_vs_melee",self.var_dmg_vs_melee)/100) + float(kwargs.get("var_dmg_vs_ground",self.var_dmg_vs_ground)/100) + float(1))*(float(kwargs.get("var_dmg_vs_boss",self.var_dmg_vs_boss)/100) + float(1))*(float(kwargs.get("var_dmg_all",self.var_dmg_all)/100) + float(1))*(float(kwargs.get("weapon_coeff",self.weapon_coeff))))
		boss_ground_range = round((int(kwargs.get("global_atk_save",self.user_profile.global_atk_save)) + int(kwargs.get("flat_dmg_vs_ground",self.flat_dmg_vs_ground)) + int(kwargs.get("flat_dmg_vs_boss",self.flat_dmg_vs_boss)) + int(kwargs.get("flat_dmg_vs_range",self.flat_dmg_vs_range)) + int(kwargs.get("flat_dmg_all",self.flat_dmg_all)))*(float(kwargs.get("var_dmg_vs_range",self.var_dmg_vs_range)/100) + float(kwargs.get("var_dmg_vs_ground",self.var_dmg_vs_ground)/100) + float(1))*(float(kwargs.get("var_dmg_vs_boss",self.var_dmg_vs_boss)/100) + float(1))*(float(kwargs.get("var_dmg_all",self.var_dmg_all)/100) + float(1))*(float(kwargs.get("weapon_coeff",self.weapon_coeff))))
		boss_airborne_melee = round((int(kwargs.get("global_atk_save",self.user_profile.global_atk_save)) + int(kwargs.get("flat_dmg_vs_airborne",self.flat_dmg_vs_airborne)) + int(kwargs.get("flat_dmg_vs_boss",self.flat_dmg_vs_boss)) + int(kwargs.get("flat_dmg_vs_melee",self.flat_dmg_vs_melee)) + int(kwargs.get("flat_dmg_all",self.flat_dmg_all)))*(float(kwargs.get("var_dmg_vs_melee",self.var_dmg_vs_melee)/100) + float(kwargs.get("var_dmg_vs_airborne",self.var_dmg_vs_airborne)/100) + float(1))*(float(kwargs.get("var_dmg_vs_boss",self.var_dmg_vs_boss)/100) + float(1))*(float(kwargs.get("var_dmg_all",self.var_dmg_all)/100) + float(1))*(float(kwargs.get("weapon_coeff",self.weapon_coeff))))
		boss_airborne_range = round((int(kwargs.get("global_atk_save",self.user_profile.global_atk_save)) + int(kwargs.get("flat_dmg_vs_airborne",self.flat_dmg_vs_airborne)) + int(kwargs.get("flat_dmg_vs_boss",self.flat_dmg_vs_boss)) + int(kwargs.get("flat_dmg_vs_range",self.flat_dmg_vs_range)) + int(kwargs.get("flat_dmg_all",self.flat_dmg_all)))*(float(kwargs.get("var_dmg_vs_range",self.var_dmg_vs_range)/100) + float(kwargs.get("var_dmg_vs_airborne",self.var_dmg_vs_airborne)/100) + float(1))*(float(kwargs.get("var_dmg_vs_boss",self.var_dmg_vs_boss)/100) + float(1))*(float(kwargs.get("var_dmg_all",self.var_dmg_all)/100) + float(1))*(float(kwargs.get("weapon_coeff",self.weapon_coeff))))
		averageDamage = round(
			int(mob_ground_melee)+
			int(mob_ground_range)+
			int(mob_airborne_melee)+
			int(mob_airborne_range)+
			int(boss_ground_melee)+
			int(boss_ground_range)+
			int(boss_airborne_melee)+
			int(boss_airborne_range)
		)/8
		averageDamageAll = round(averageDamage * (1 + (crit_rate/100) * (crit_dmg - 1)))
		result = {
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
		return result


class MedalsTable(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	medals_1001 = models.BooleanField(blank=True, default=False)
	medals_1002 = models.BooleanField(blank=True, default=False)
	medals_1003 = models.BooleanField(blank=True, default=False)
	medals_1004 = models.BooleanField(blank=True, default=False)
	medals_1005 = models.BooleanField(blank=True, default=False)
	medals_1006 = models.BooleanField(blank=True, default=False)
	medals_1008 = models.BooleanField(blank=True, default=False)
	medals_1009 = models.BooleanField(blank=True, default=False)
	medals_1010 = models.BooleanField(blank=True, default=False)
	medals_1011 = models.BooleanField(blank=True, default=False)
	medals_1012 = models.BooleanField(blank=True, default=False)
	medals_2001 = models.BooleanField(blank=True, default=False)
	medals_2002 = models.BooleanField(blank=True, default=False)
	medals_2003 = models.BooleanField(blank=True, default=False)
	medals_2004 = models.BooleanField(blank=True, default=False)
	medals_2005 = models.BooleanField(blank=True, default=False)
	medals_2006 = models.BooleanField(blank=True, default=False)
	medals_2007 = models.BooleanField(blank=True, default=False)
	medals_2008 = models.BooleanField(blank=True, default=False)
	medals_2009 = models.BooleanField(blank=True, default=False)
	medals_2010 = models.BooleanField(blank=True, default=False)
	medals_2011 = models.BooleanField(blank=True, default=False)
	medals_2012 = models.BooleanField(blank=True, default=False)
	medals_2013 = models.BooleanField(blank=True, default=False)
	medals_2014 = models.BooleanField(blank=True, default=False)
	medals_3001 = models.BooleanField(blank=True, default=False)
	medals_3002 = models.BooleanField(blank=True, default=False)
	medals_3003 = models.BooleanField(blank=True, default=False)
	medals_3004 = models.BooleanField(blank=True, default=False)
	medals_3005 = models.BooleanField(blank=True, default=False)
	medals_3006 = models.BooleanField(blank=True, default=False)
	medals_3007 = models.BooleanField(blank=True, default=False)
	medals_3008 = models.BooleanField(blank=True, default=False)
	medals_3009 = models.BooleanField(blank=True, default=False)
	medals_3010 = models.BooleanField(blank=True, default=False)
	medals_3019 = models.BooleanField(blank=True, default=False)
	medals_3020 = models.BooleanField(blank=True, default=False)
	medals_3021 = models.BooleanField(blank=True, default=False)
	medals_3022 = models.BooleanField(blank=True, default=False)
	medals_3023 = models.BooleanField(blank=True, default=False)
	medals_3024 = models.BooleanField(blank=True, default=False)
	medals_3025 = models.BooleanField(blank=True, default=False)
	medals_3026 = models.BooleanField(blank=True, default=False)
	medals_3027 = models.BooleanField(blank=True, default=False)
	medals_3028 = models.BooleanField(blank=True, default=False)
	medals_3029 = models.BooleanField(blank=True, default=False)
	medals_3030 = models.BooleanField(blank=True, default=False)
	medals_3034 = models.BooleanField(blank=True, default=False)
	medals_3035 = models.BooleanField(blank=True, default=False)
	medals_3036 = models.BooleanField(blank=True, default=False)

	def dictionnaire(self):
		return {
				"user_profile": self.user_profile,
				"medals_1001": self.medals_1001,
				"medals_1002": self.medals_1002,
				"medals_1003": self.medals_1003,
				"medals_1004": self.medals_1004,
				"medals_1005": self.medals_1005,
				"medals_1006": self.medals_1006,
				"medals_1008": self.medals_1008,
				"medals_1009": self.medals_1009,
				"medals_1010": self.medals_1010,
				"medals_1011": self.medals_1011,
				"medals_1012": self.medals_1012,
				"medals_2001": self.medals_2001,
				"medals_2002": self.medals_2002,
				"medals_2003": self.medals_2003,
				"medals_2004": self.medals_2004,
				"medals_2005": self.medals_2005,
				"medals_2006": self.medals_2006,
				"medals_2007": self.medals_2007,
				"medals_2008": self.medals_2008,
				"medals_2009": self.medals_2009,
				"medals_2010": self.medals_2010,
				"medals_2011": self.medals_2011,
				"medals_2012": self.medals_2012,
				"medals_2013": self.medals_2013,
				"medals_2014": self.medals_2014,
				"medals_3001": self.medals_3001,
				"medals_3002": self.medals_3002,
				"medals_3003": self.medals_3003,
				"medals_3004": self.medals_3004,
				"medals_3005": self.medals_3005,
				"medals_3006": self.medals_3006,
				"medals_3007": self.medals_3007,
				"medals_3008": self.medals_3008,
				"medals_3009": self.medals_3009,
				"medals_3010": self.medals_3010,
				"medals_3019": self.medals_3019,
				"medals_3020": self.medals_3020,
				"medals_3021": self.medals_3021,
				"medals_3022": self.medals_3022,
				"medals_3023": self.medals_3023,
				"medals_3024": self.medals_3024,
				"medals_3025": self.medals_3025,
				"medals_3026": self.medals_3026,
				"medals_3027": self.medals_3027,
				"medals_3028": self.medals_3028,
				"medals_3029": self.medals_3029,
				"medals_3030": self.medals_3030,
				"medals_3034": self.medals_3034,
				"medals_3035": self.medals_3035,
				"medals_3036": self.medals_3036,
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
					hp_var += MedalsStats["stats_" + str(medal[1])]
				elif type_medal_boost == "Hero Base Enhanced":
					hero_base_enhanced += MedalsStats["stats_" + str(medal[1])]
				elif type_medal_boost == "Enhance Equipment":
					enhance_equipment += MedalsStats["stats_" + str(medal[1])]
		result = {
			"attack":attack,
			"attack_var":attack_var,
			"hp":hp,
			"hp_var":hp_var,
			"hero_base_enhanced":hero_base_enhanced,
			"enhance_equipment":enhance_equipment
		}
		if DEBUG_STATS:
			print(f"\nMedals Stats :{result}\n")
		return result

class RelicsTable(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	wraith_mask_level = models.IntegerField(default=0, choices=relics_level)
	wraith_mask_star = models.IntegerField(default=0, choices=rare_relics_star)
	wraith_mask_effective = models.FloatField(default=0,validators=[MaxValueValidator(420)])
	clown_mask_level = models.IntegerField(default=0, choices=relics_level)
	clown_mask_star = models.IntegerField(default=0, choices=rare_relics_star)
	clown_mask_effective = models.FloatField(default=0,validators=[MaxValueValidator(420)])
	princess_teddy_bear_level = models.IntegerField(default=0, choices=relics_level)
	princess_teddy_bear_star = models.IntegerField(default=0, choices=rare_relics_star)
	princess_teddy_bear_effective = models.FloatField(default=0,validators=[MaxValueValidator(1600)])
	belt_of_might_level = models.IntegerField(default=0, choices=relics_level)
	belt_of_might_star = models.IntegerField(default=0, choices=rare_relics_star)
	belt_of_might_effective = models.FloatField(default=0,validators=[MaxValueValidator(1600)])
	beastmaster_whistle_level = models.IntegerField(default=0, choices=relics_level)
	beastmaster_whistle_star = models.IntegerField(default=0, choices=rare_relics_star)
	beastmaster_whistle_effective = models.FloatField(default=0,validators=[MaxValueValidator(1600)])
	archmage_robe_level = models.IntegerField(default=0, choices=relics_level)
	archmage_robe_star = models.IntegerField(default=0, choices=rare_relics_star)
	archmage_robe_effective = models.FloatField(default=0,validators=[MaxValueValidator(1600)])
	shimmering_gem_level = models.IntegerField(default=0, choices=relics_level)
	shimmering_gem_star = models.IntegerField(default=0, choices=rare_relics_star)
	bloom_of_eternity_level = models.IntegerField(default=0, choices=relics_level)
	bloom_of_eternity_star = models.IntegerField(default=0, choices=rare_relics_star)
	bloom_of_eternity_effective = models.FloatField(default=0,validators=[MaxValueValidator(1600)])
	challenger_headband_level = models.IntegerField(default=0, choices=relics_level)
	challenger_headband_star = models.IntegerField(default=0, choices=rare_relics_star)
	jade_gobelet_level = models.IntegerField(default=0, choices=relics_level)
	jade_gobelet_star = models.IntegerField(default=0, choices=rare_relics_star)
	jade_gobelet_effective = models.FloatField(default=0,validators=[MaxValueValidator(1600)])
	veteran_plate_level = models.IntegerField(default=0, choices=relics_level)
	veteran_plate_star = models.IntegerField(default=0, choices=rare_relics_star)
	dragonscale_level = models.IntegerField(default=0, choices=relics_level)
	dragonscale_star = models.IntegerField(default=0, choices=rare_relics_star)
	dragonscale_effective = models.FloatField(default=0,validators=[MaxValueValidator(1600)])
	dragon_tooth_level = models.IntegerField(default=0, choices=relics_level)
	dragon_tooth_star = models.IntegerField(default=0, choices=rare_relics_star)
	dragon_tooth_effective = models.FloatField(default=0,validators=[MaxValueValidator(420)])
	scholar_telescope_level = models.IntegerField(default=0, choices=relics_level)
	scholar_telescope_star = models.IntegerField(default=0, choices=rare_relics_star)
	pirate_shank_level = models.IntegerField(default=0, choices=relics_level)
	pirate_shank_star = models.IntegerField(default=0, choices=rare_relics_star)
	giant_greatsword_level = models.IntegerField(default=0, choices=relics_level)
	giant_greatsword_star = models.IntegerField(default=0, choices=rare_relics_star)
	giant_greatsword_effective = models.FloatField(default=0,validators=[MaxValueValidator(420)])
	healing_potion_level = models.IntegerField(default=0, choices=relics_level)
	healing_potion_star = models.IntegerField(default=0, choices=rare_relics_star)
	whirlwind_mauler_level = models.IntegerField(default=0, choices=relics_level)
	whirlwind_mauler_star = models.IntegerField(default=0, choices=rare_relics_star)
	whirlwind_mauler_effective = models.FloatField(default=0,validators=[MaxValueValidator(420)])
	special_lance_level = models.IntegerField(default=0, choices=relics_level)
	special_lance_star = models.IntegerField(default=0, choices=rare_relics_star)
	special_lance_effective = models.FloatField(default=0,validators=[MaxValueValidator(420)])
	precision_slingshot_level = models.IntegerField(default=0, choices=relics_level)
	precision_slingshot_star = models.IntegerField(default=0, choices=rare_relics_star)
	maidens_pearl_earring_level = models.IntegerField(default=0, choices=relics_level)
	maidens_pearl_earring_star = models.IntegerField(default=0, choices=rare_relics_star)
	ancient_shield_level = models.IntegerField(default=0, choices=relics_level)
	ancient_shield_star = models.IntegerField(default=0, choices=rare_relics_star)
	ancient_shield_effective = models.FloatField(default=0,validators=[MaxValueValidator(200)])
	supreme_trinity_alpha_level = models.IntegerField(default=0, choices=relics_level)
	supreme_trinity_alpha_star = models.IntegerField(default=0, choices=radiant_relics_star)
	supreme_trinity_alpha_effective = models.FloatField(default=0,validators=[MaxValueValidator(500)])
	golden_apple_level = models.IntegerField(default=0, choices=relics_level)
	golden_apple_star = models.IntegerField(default=0, choices=radiant_relics_star)
	golden_apple_effective = models.FloatField(default=0,validators=[MaxValueValidator(2200)])
	ancient_stele_level = models.IntegerField(default=0, choices=relics_level)
	ancient_stele_star = models.IntegerField(default=0, choices=radiant_relics_star)
	ancient_stele_effective = models.FloatField(default=0,validators=[MaxValueValidator(500)])
	philosopher_stone_level = models.IntegerField(default=0, choices=relics_level)
	philosopher_stone_star = models.IntegerField(default=0, choices=radiant_relics_star)
	philosopher_stone_effective = models.FloatField(default=0,validators=[MaxValueValidator(2200)])
	dragon_heart_level = models.IntegerField(default=0, choices=relics_level)
	dragon_heart_star = models.IntegerField(default=0, choices=radiant_relics_star)
	dragon_heart_effective = models.FloatField(default=0,validators=[MaxValueValidator(2200)])
	spectral_duality_level = models.IntegerField(default=0, choices=relics_level)
	spectral_duality_star = models.IntegerField(default=0, choices=radiant_relics_star)
	spectral_duality_effective = models.FloatField(default=0,validators=[MaxValueValidator(500)])
	mystic_emblem_level = models.IntegerField(default=0, choices=relics_level)
	mystic_emblem_star = models.IntegerField(default=0, choices=radiant_relics_star)
	immortal_brooch_level = models.IntegerField(default=0, choices=relics_level)
	immortal_brooch_star = models.IntegerField(default=0, choices=radiant_relics_star)
	golden_statue_level = models.IntegerField(default=0, choices=relics_level)
	golden_statue_star = models.IntegerField(default=0, choices=radiant_relics_star)
	golden_statue_effective = models.FloatField(default=0,validators=[MaxValueValidator(2200)])
	smilling_mask_level = models.IntegerField(default=0, choices=relics_level)
	smilling_mask_star = models.IntegerField(default=0, choices=radiant_relics_star)
	unmerciful_mask_level = models.IntegerField(default=0, choices=relics_level)
	unmerciful_mask_star = models.IntegerField(default=0, choices=radiant_relics_star)
	unmerciful_mask_effective = models.FloatField(default=0,validators=[MaxValueValidator(500)])
	holy_water_level = models.IntegerField(default=0, choices=relics_level)
	holy_water_star = models.IntegerField(default=0, choices=radiant_relics_star)
	holy_water_effective = models.FloatField(default=0,validators=[MaxValueValidator(2200)])
	book_of_the_dead_level = models.IntegerField(default=0, choices=relics_level)
	book_of_the_dead_star = models.IntegerField(default=0, choices=radiant_relics_star)
	book_of_the_dead_effective = models.FloatField(default=0,validators=[MaxValueValidator(500)])
	psionist_treasure_level = models.IntegerField(default=0, choices=relics_level)
	psionist_treasure_star = models.IntegerField(default=0, choices=radiant_relics_star)
	book_of_archery_level = models.IntegerField(default=0, choices=relics_level)
	book_of_archery_star = models.IntegerField(default=0, choices=radiant_relics_star)
	book_of_archery_effective = models.FloatField(default=0,validators=[MaxValueValidator(500)])
	book_of_bravery_level = models.IntegerField(default=0, choices=relics_level)
	book_of_bravery_star = models.IntegerField(default=0, choices=radiant_relics_star)
	book_of_bravery_effective = models.FloatField(default=0,validators=[MaxValueValidator(500)])
	angelic_heart_level = models.IntegerField(default=0, choices=relics_level)
	angelic_heart_star = models.IntegerField(default=0, choices=radiant_relics_star)
	angelic_heart_effective = models.FloatField(default=0,validators=[MaxValueValidator(2200)])
	devil_whisper_level = models.IntegerField(default=0, choices=relics_level)
	devil_whisper_star = models.IntegerField(default=0, choices=radiant_relics_star)
	devil_whisper_effective = models.FloatField(default=0,validators=[MaxValueValidator(2200)])
	stone_of_wisdom_level = models.IntegerField(default=0, choices=relics_level)
	stone_of_wisdom_star = models.IntegerField(default=0, choices=radiant_relics_star)
	empyrean_mirror_level = models.IntegerField(default=0, choices=relics_level)
	empyrean_mirror_star = models.IntegerField(default=0, choices=radiant_relics_star)
	empyrean_mirror_effective = models.FloatField(default=0,validators=[MaxValueValidator(2200)])
	fabled_archer_arrow_level = models.IntegerField(default=0, choices=relics_level)
	fabled_archer_arrow_star = models.IntegerField(default=0, choices=radiant_relics_star)
	fabled_archer_arrow_effective = models.FloatField(default=0,validators=[MaxValueValidator(10)])
	shiny_gemmed_belt_level = models.IntegerField(default=0, choices=relics_level)
	shiny_gemmed_belt_star = models.IntegerField(default=0, choices=radiant_relics_star)
	mythril_flux_mail_level = models.IntegerField(default=0, choices=relics_level)
	mythril_flux_mail_star = models.IntegerField(default=0, choices=radiant_relics_star)
	mythril_flux_mail_effective = models.FloatField(default=0,validators=[MaxValueValidator(8)])
	stealth_boots_level = models.IntegerField(default=0, choices=relics_level)
	stealth_boots_star = models.IntegerField(default=0, choices=radiant_relics_star)
	stealth_boots_effective = models.FloatField(default=0,validators=[MaxValueValidator(2200)])
	assassin_dagger_level = models.IntegerField(default=0, choices=relics_level)
	assassin_dagger_star = models.IntegerField(default=0, choices=radiant_relics_star)
	assassin_dagger_effective = models.FloatField(default=0,validators=[MaxValueValidator(500)])
	gold_bunny_level = models.IntegerField(default=0, choices=relics_level)
	gold_bunny_star = models.IntegerField(default=0, choices=radiant_relics_star)
	lucky_coin_level = models.IntegerField(default=0, choices=relics_level)
	lucky_coin_star = models.IntegerField(default=0, choices=radiant_relics_star)
	dusken_cask_level = models.IntegerField(default=0, choices=relics_level)
	dusken_cask_star = models.IntegerField(default=0, choices=radiant_relics_star)
	dragon_eye_level = models.IntegerField(default=0, choices=relics_level)
	dragon_eye_star = models.IntegerField(default=0, choices=radiant_relics_star)
	dragon_eye_effective = models.FloatField(default=0,validators=[MaxValueValidator(10)])
	ring_of_greed_level = models.IntegerField(default=0, choices=relics_level)
	ring_of_greed_star = models.IntegerField(default=0, choices=radiant_relics_star)
	genesis_staff_level = models.IntegerField(default=0, choices=relics_level)
	genesis_staff_star = models.IntegerField(default=0, choices=holy_relics_star)
	bloodstained_sword_level = models.IntegerField(default=0, choices=relics_level)
	bloodstained_sword_star = models.IntegerField(default=0, choices=holy_relics_star)
	bloodstained_sword_effective = models.FloatField(default=0,validators=[MaxValueValidator(9)])
	starcluster_rage_level = models.IntegerField(default=0, choices=relics_level)
	starcluster_rage_star = models.IntegerField(default=0, choices=holy_relics_star)
	starcluster_rage_effective = models.FloatField(default=0,validators=[MaxValueValidator(10)])
	elven_king_cape_level = models.IntegerField(default=0, choices=relics_level)
	elven_king_cape_star = models.IntegerField(default=0, choices=holy_relics_star)
	elven_king_cape_effective = models.FloatField(default=0,validators=[MaxValueValidator(600)])
	spear_of_yggdrasil_level = models.IntegerField(default=0, choices=relics_level)
	spear_of_yggdrasil_star = models.IntegerField(default=0, choices=holy_relics_star)
	spear_of_yggdrasil_effective = models.FloatField(default=0,validators=[MaxValueValidator(600)])
	dragon_gem_level = models.IntegerField(default=0, choices=relics_level)
	dragon_gem_star = models.IntegerField(default=0, choices=holy_relics_star)
	dragon_gem_effective = models.FloatField(default=0,validators=[MaxValueValidator(600)])
	life_crown_level = models.IntegerField(default=0, choices=relics_level)
	life_crown_star = models.IntegerField(default=0, choices=holy_relics_star)
	life_crown_effective = models.FloatField(default=0,validators=[MaxValueValidator(2720)])
	sand_of_time_level = models.IntegerField(default=0, choices=relics_level)
	sand_of_time_star = models.IntegerField(default=0, choices=holy_relics_star)
	sand_of_time_effective = models.FloatField(default=0,validators=[MaxValueValidator(10)])
	first_lightning_level = models.IntegerField(default=0, choices=relics_level)
	first_lightning_star = models.IntegerField(default=0, choices=holy_relics_star)
	oracle_quill_level = models.IntegerField(default=0, choices=relics_level)
	oracle_quill_star = models.IntegerField(default=0, choices=holy_relics_star)
	oracle_quill_effective = models.FloatField(default=0,validators=[MaxValueValidator(10)])
	bloodthirsty_grail_level = models.IntegerField(default=0, choices=relics_level)
	bloodthirsty_grail_star = models.IntegerField(default=0, choices=holy_relics_star)
	bloodthirsty_grail_effective = models.FloatField(default=0,validators=[MaxValueValidator(2720)])
	healing_grail_level = models.IntegerField(default=0, choices=relics_level)
	healing_grail_star = models.IntegerField(default=0, choices=holy_relics_star)
	healing_grail_effective = models.FloatField(default=0,validators=[MaxValueValidator(2720)])
	cupids_necklace_level = models.IntegerField(default=0, choices=relics_level)
	cupids_necklace_star = models.IntegerField(default=0, choices=holy_relics_star)
	life_staff_level = models.IntegerField(default=0, choices=relics_level)
	life_staff_star = models.IntegerField(default=0, choices=holy_relics_star)
	life_staff_effective = models.FloatField(default=0,validators=[MaxValueValidator(2000)])
	light_grail_level = models.IntegerField(default=0, choices=relics_level)
	light_grail_star = models.IntegerField(default=0, choices=holy_relics_star)
	primal_fire_level = models.IntegerField(default=0, choices=relics_level)
	primal_fire_star = models.IntegerField(default=0, choices=holy_relics_star)
	primal_fire_effective = models.FloatField(default=0,validators=[MaxValueValidator(600)])
	
	def dictionnaire(self):
		return {
				"user_profile": self.user_profile,
				"wraith_mask_level": self.wraith_mask_level,"wraith_mask_star": self.wraith_mask_star,"wraith_mask_effective": self.wraith_mask_effective, 
				"clown_mask_level": self.clown_mask_level,"clown_mask_star": self.clown_mask_star,"clown_mask_effective": self.clown_mask_effective, 
				"princess_teddy_bear_level": self.princess_teddy_bear_level,"princess_teddy_bear_star": self.princess_teddy_bear_star,"princess_teddy_bear_effective": self.princess_teddy_bear_effective, 
				"belt_of_might_level": self.belt_of_might_level,"belt_of_might_star": self.belt_of_might_star,"belt_of_might_effective": self.belt_of_might_effective, 
				"beastmaster_whistle_level": self.beastmaster_whistle_level,"beastmaster_whistle_star": self.beastmaster_whistle_star,"beastmaster_whistle_effective": self.beastmaster_whistle_effective, 
				"archmage_robe_level": self.archmage_robe_level,"archmage_robe_star": self.archmage_robe_star,"archmage_robe_effective": self.archmage_robe_effective, 
				"shimmering_gem_level": self.shimmering_gem_level,"shimmering_gem_star": self.shimmering_gem_star, 
				"bloom_of_eternity_level": self.bloom_of_eternity_level,"bloom_of_eternity_star": self.bloom_of_eternity_star,"bloom_of_eternity_effective": self.bloom_of_eternity_effective, 
				"challenger_headband_level": self.challenger_headband_level,"challenger_headband_star": self.challenger_headband_star,
				"jade_gobelet_level": self.jade_gobelet_level,"jade_gobelet_star": self.jade_gobelet_star,"jade_gobelet_effective": self.jade_gobelet_effective, 
				"veteran_plate_level": self.veteran_plate_level,"veteran_plate_star": self.veteran_plate_star,
				"dragonscale_level": self.dragonscale_level,"dragonscale_star": self.dragonscale_star,"dragonscale_effective": self.dragonscale_effective, 
				"dragon_tooth_level": self.dragon_tooth_level,"dragon_tooth_star": self.dragon_tooth_star,"dragon_tooth_effective": self.dragon_tooth_effective, 
				"scholar_telescope_level": self.scholar_telescope_level,"scholar_telescope_star": self.scholar_telescope_star,
				"pirate_shank_level": self.pirate_shank_level,"pirate_shank_star": self.pirate_shank_star,
				"giant_greatsword_level": self.giant_greatsword_level,"giant_greatsword_star": self.giant_greatsword_star,"giant_greatsword_effective": self.giant_greatsword_effective, 
				"healing_potion_level": self.healing_potion_level,"healing_potion_star": self.healing_potion_star,
				"whirlwind_mauler_level": self.whirlwind_mauler_level,"whirlwind_mauler_star": self.whirlwind_mauler_star,"whirlwind_mauler_effective": self.whirlwind_mauler_effective, 
				"special_lance_level": self.special_lance_level,"special_lance_star": self.special_lance_star,"special_lance_effective": self.special_lance_effective, 
				"precision_slingshot_level": self.precision_slingshot_level,"precision_slingshot_star": self.precision_slingshot_star,
				"maidens_pearl_earring_level": self.maidens_pearl_earring_level,"maidens_pearl_earring_star": self.maidens_pearl_earring_star,
				"ancient_shield_level": self.ancient_shield_level,"ancient_shield_star": self.ancient_shield_star,"ancient_shield_effective": self.ancient_shield_effective, 
				"supreme_trinity_alpha_level": self.supreme_trinity_alpha_level,"supreme_trinity_alpha_star": self.supreme_trinity_alpha_star,"supreme_trinity_alpha_effective": self.supreme_trinity_alpha_effective, 
				"golden_apple_level": self.golden_apple_level,"golden_apple_star": self.golden_apple_star,"golden_apple_effective": self.golden_apple_effective, 
				"ancient_stele_level": self.ancient_stele_level,"ancient_stele_star": self.ancient_stele_star,"ancient_stele_effective": self.ancient_stele_effective, 
				"philosopher_stone_level": self.philosopher_stone_level,"philosopher_stone_star": self.philosopher_stone_star,"philosopher_stone_effective": self.philosopher_stone_effective, 
				"dragon_heart_level": self.dragon_heart_level,"dragon_heart_star": self.dragon_heart_star,"dragon_heart_effective": self.dragon_heart_effective, 
				"spectral_duality_level": self.spectral_duality_level,"spectral_duality_star": self.spectral_duality_star,"spectral_duality_effective": self.spectral_duality_effective, 
				"mystic_emblem_level": self.mystic_emblem_level,"mystic_emblem_star": self.mystic_emblem_star,
				"immortal_brooch_level": self.immortal_brooch_level,"immortal_brooch_star": self.immortal_brooch_star,
				"golden_statue_level": self.golden_statue_level,"golden_statue_star": self.golden_statue_star,"golden_statue_effective": self.golden_statue_effective, 
				"smilling_mask_level": self.smilling_mask_level,"smilling_mask_star": self.smilling_mask_star,
				"unmerciful_mask_level": self.unmerciful_mask_level,"unmerciful_mask_star": self.unmerciful_mask_star,"unmerciful_mask_effective": self.unmerciful_mask_effective, 
				"holy_water_level": self.holy_water_level,"holy_water_star": self.holy_water_star,"holy_water_effective": self.holy_water_effective, 
				"book_of_the_dead_level": self.book_of_the_dead_level,"book_of_the_dead_star": self.book_of_the_dead_star,"book_of_the_dead_effective": self.book_of_the_dead_effective, 
				"psionist_treasure_level": self.psionist_treasure_level,"psionist_treasure_star": self.psionist_treasure_star,
				"book_of_archery_level": self.book_of_archery_level,"book_of_archery_star": self.book_of_archery_star,"book_of_archery_effective": self.book_of_archery_effective, 
				"book_of_bravery_level": self.book_of_bravery_level,"book_of_bravery_star": self.book_of_bravery_star,"book_of_bravery_effective": self.book_of_bravery_effective, 
				"angelic_heart_level": self.angelic_heart_level,"angelic_heart_star": self.angelic_heart_star,"angelic_heart_effective": self.angelic_heart_effective, 
				"devil_whisper_level": self.devil_whisper_level,"devil_whisper_star": self.devil_whisper_star,"devil_whisper_effective": self.devil_whisper_effective,
				"stone_of_wisdom_level": self.stone_of_wisdom_level,"stone_of_wisdom_star": self.stone_of_wisdom_star,
				"empyrean_mirror_level": self.empyrean_mirror_level,"empyrean_mirror_star": self.empyrean_mirror_star,"empyrean_mirror_effective": self.empyrean_mirror_effective, 
				"fabled_archer_arrow_level": self.fabled_archer_arrow_level,"fabled_archer_arrow_star": self.fabled_archer_arrow_star,"fabled_archer_arrow_effective": self.fabled_archer_arrow_effective, 
				"shiny_gemmed_belt_level": self.shiny_gemmed_belt_level,"shiny_gemmed_belt_star": self.shiny_gemmed_belt_star,
				"mythril_flux_mail_level": self.mythril_flux_mail_level,"mythril_flux_mail_star": self.mythril_flux_mail_star,"mythril_flux_mail_effective": self.mythril_flux_mail_effective, 
				"stealth_boots_level": self.stealth_boots_level,"stealth_boots_star": self.stealth_boots_star,"stealth_boots_effective": self.stealth_boots_effective, 
				"assassin_dagger_level": self.assassin_dagger_level,"assassin_dagger_star": self.assassin_dagger_star,"assassin_dagger_effective": self.assassin_dagger_effective, 
				"gold_bunny_level": self.gold_bunny_level,"gold_bunny_star": self.gold_bunny_star,
				"lucky_coin_level": self.lucky_coin_level,"lucky_coin_star": self.lucky_coin_star,
				"dusken_cask_level": self.dusken_cask_level,"dusken_cask_star": self.dusken_cask_star,
				"dragon_eye_level": self.dragon_eye_level,"dragon_eye_star": self.dragon_eye_star,"dragon_eye_effective": self.dragon_eye_effective, 
				"ring_of_greed_level": self.ring_of_greed_level,"ring_of_greed_star": self.ring_of_greed_star,
				"genesis_staff_level": self.genesis_staff_level,"genesis_staff_star": self.genesis_staff_star,
				"bloodstained_sword_level": self.bloodstained_sword_level,"bloodstained_sword_star": self.bloodstained_sword_star,"bloodstained_sword_effective": self.bloodstained_sword_effective, 
				"starcluster_rage_level": self.starcluster_rage_level,"starcluster_rage_star": self.starcluster_rage_star,"starcluster_rage_effective": self.starcluster_rage_effective, 
				"elven_king_cape_level": self.elven_king_cape_level,"elven_king_cape_star": self.elven_king_cape_star,"elven_king_cape_effective": self.elven_king_cape_effective, 
				"spear_of_yggdrasil_level": self.spear_of_yggdrasil_level,"spear_of_yggdrasil_star": self.spear_of_yggdrasil_star,"spear_of_yggdrasil_effective": self.spear_of_yggdrasil_effective, 
				"dragon_gem_level": self.dragon_gem_level,"dragon_gem_star": self.dragon_gem_star,"dragon_gem_effective": self.dragon_gem_effective, 
				"life_crown_level": self.life_crown_level,"life_crown_star": self.life_crown_star,"life_crown_effective": self.life_crown_effective, 
				"sand_of_time_level": self.sand_of_time_level,"sand_of_time_star": self.sand_of_time_star,"sand_of_time_effective": self.sand_of_time_effective, 
				"first_lightning_level": self.first_lightning_level,"first_lightning_star": self.first_lightning_star,
				"oracle_quill_level": self.oracle_quill_level,"oracle_quill_star": self.oracle_quill_star,"oracle_quill_effective": self.oracle_quill_effective, 
				"bloodthirsty_grail_level": self.bloodthirsty_grail_level,"bloodthirsty_grail_star": self.bloodthirsty_grail_star,"bloodthirsty_grail_effective": self.bloodthirsty_grail_effective, 
				"healing_grail_level": self.healing_grail_level,"healing_grail_star": self.healing_grail_star,"healing_grail_effective": self.healing_grail_effective, 
				"cupids_necklace_level": self.cupids_necklace_level,"cupids_necklace_star": self.cupids_necklace_star,
				"life_staff_level": self.life_staff_level,"life_staff_star": self.life_staff_star,"life_staff_effective": self.life_staff_effective, 
				"light_grail_level": self.light_grail_level,"light_grail_star": self.light_grail_star,
				"primal_fire_level": self.primal_fire_level,"primal_fire_star": self.primal_fire_star,"primal_fire_effective": self.primal_fire_effective, 
			}

	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine


	def relics_Stats(self):
		result = {}
		RelicLabel:dict = self.local_data["RelicLabel"]
		star_multiplier = [1,1.1,1.21,1.34,1.48,1.62,1.78,1.96,2.16]
		user_data = self.dictionnaire()
		for relic,value in RelicLabel.items():
			if RelicLabel[relic]['type'] == 1:
				level_multiplier = [1,1.1,1.2336,1.3336,1.4336,1.5336,1.6672,1.7672,1.8672,1.9672,2.1008,2.2008,2.3008,2.4008,2.5344,2.6344,2.7344,2.8344,2.968,3.068,3.168,3.268,3.4016,3.5016,3.6016,3.7016,3.8352,3.9352,4.0352,4.1352,4.2688]
			elif RelicLabel[relic]['type'] == 2:
				level_multiplier = [1,1.08,1.18,1.26,1.34,1.42,1.52,1.60,1.68,1.76,1.86,1.94,2.02,2.10,2.20,2.28,2.36,2.44,2.54,2.62,2.70,2.78,2.88,2.96,3.04,3.12,3.22,3.30,3.38,3.46,3.56]
			elif RelicLabel[relic]['type'] == 3:
				level_multiplier =  [1,1.0625,1.125,1.1875,1.25,1.3125,1.375,1.4375,1.5,1.5625,1.625,1.6875,1.75,1.8125,1.875,1.9375,2,2.0625,2.125,2.1875,2.25,2.3125,2.375,2.4375,2.5,2.5625,2.625,2.6875,2.75,2.8125,2.875]
			relic_lv = user_data[str(relic) + "_level"]
			relic_star = user_data[str(relic) + "_star"]
			relic_eff = user_data.get(str(relic) + "_effective",0)
			if not (int(relic_star) == 0 and int(relic_lv) == 0 and int(relic_eff) == 0):
				exclusive_label = RelicLabel[relic]['exclusive_label']
				for boost in RelicLabel[relic]["boost"]:
					old_value = result.get(boost['label'],0)
					if isinstance(boost['value'],list):
						value = float(boost['value'][int(relic_star)]) + float(old_value)
						result.update({boost['label']:value})
					elif isinstance(boost['value'],(int,float)):
						value = math.floor(math.floor(int(boost['value']) * level_multiplier[relic_lv]) * float(star_multiplier[relic_star])) + float(old_value)
						result.update({boost['label']:value})
				if exclusive_label != False and relic_eff != 0:
					old_value = result.get(exclusive_label,0)
					value = float(relic_eff) + float(old_value)
					result.update({exclusive_label:value})
		if DEBUG_STATS:
			print(f"\nrelics_Stats :{result}\n")
		return result


class PromoCode(models.Model,parentModel):
	code = models.CharField(max_length=30, blank=False)
	is_active = models.BooleanField(default=False)
	expire = models.DateField(blank=True, default=datetime.datetime.now, null=True)

	def __str__(self):
		return f"{self.code}"

	def deactivateIfExpired(self) -> bool:
		if self.expire < timezone.now().date():
			self.is_active = False
			self.save()
			return True
		return False


class PromoCodeReward(models.Model):
	promocodeId = models.ForeignKey(PromoCode, blank=False, null=True, on_delete=models.CASCADE)
	reward_type = models.CharField(max_length=20, default="", help_text="Write down the name of the image of the reward (gem,celestite_keys,purple_ticket,premium_ticket,gold,random_shards,obsidian_keys,energy,gold_keys)")
	reward_amount = models.CharField(max_length=10, default="", help_text="Write down the amount of reward", blank=True, null=True)

	def __str__(self):
		return f"{self.promocodeId.code} |  {self.reward_type} x{self.reward_amount}"

class WeaponSkinsTable(models.Model,parentModel):
	user_profile = models.ForeignKey(user,blank=False, on_delete=models.CASCADE, null=True)
	demon_blade_rain_1 = models.BooleanField(blank=True, default=False)
	demon_blade_rain_2 = models.BooleanField(blank=True, default=False)
	antiquated_sword_1 = models.BooleanField(blank=True, default=False)
	antiquated_sword_2 = models.BooleanField(blank=True, default=False)
	gale_force_1 = models.BooleanField(blank=True, default=False)
	gale_force_2 = models.BooleanField(blank=True, default=False)
	death_scythe_1 = models.BooleanField(blank=True, default=False)
	death_scythe_2 = models.BooleanField(blank=True, default=False)
	boomerang_1 = models.BooleanField(blank=True, default=False)
	boomerang_2 = models.BooleanField(blank=True, default=False)
	brightspear_1 = models.BooleanField(blank=True, default=False)
	brightspear_2 = models.BooleanField(blank=True, default=False)
	saw_blade_1 = models.BooleanField(blank=True, default=False)
	saw_blade_2 = models.BooleanField(blank=True, default=False)
	brave_bow_1 = models.BooleanField(blank=True, default=False)
	brave_bow_2 = models.BooleanField(blank=True, default=False)
	stalker_staff_1 = models.BooleanField(blank=True, default=False)
	stalker_staff_2 = models.BooleanField(blank=True, default=False)

	def dictionnaire(self):
		return {
				"user_profile": self.user_profile,
				"demon_blade_rain_1": self.demon_blade_rain_1,
				"demon_blade_rain_2": self.demon_blade_rain_2,
				"antiquated_sword_1": self.antiquated_sword_1,
				"antiquated_sword_2": self.antiquated_sword_2,
				"gale_force_1": self.gale_force_1,
				"gale_force_2": self.gale_force_2,
				"death_scythe_1": self.death_scythe_1,
				"death_scythe_2": self.death_scythe_2,
				"boomerang_1": self.boomerang_1,
				"boomerang_2": self.boomerang_2,
				"brightspear_1": self.brightspear_1,
				"brightspear_2": self.brightspear_2,
				"saw_blade_1": self.saw_blade_1,
				"saw_blade_2": self.saw_blade_2,
				"brave_bow_1": self.brave_bow_1,
				"brave_bow_2": self.brave_bow_2,
				"stalker_staff_1": self.stalker_staff_1,
				"stalker_staff_2": self.stalker_staff_2
			}

	def __str__(self):
		chaine = f"{self.user_profile.ingame_id} | {self.user_profile.ingame_name}"
		return chaine


	def equippedSkin(self):
		weapon_choosen = StuffTable.objects.get(user_profile=self.user_profile).weapon_choosen.replace(" ","_").lower()
		list_weapon_noskin = ['mini_atreus']
		## pour prochain skin faudra rajouter un moyen pour savoir quelle skin est équipé
		if weapon_choosen == "tornado":
			name_skin = "boomerang"
		elif weapon_choosen == "none" or weapon_choosen in list_weapon_noskin:
			return "None"
		name_skin = str(weapon_choosen)
		for k,v in self.dictionnaire().items():
			if v == True and k[0:int(k.index(k.split("_")[-1]))-1] == name_skin:
				return k
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
		if DEBUG_STATS:
			print(f"\ngetWeaponSkinStats :{result}\n")
		return result

isImage = RegexValidator(r"([-\w]+\.(?:png))", "Your string need to be an image.")

class ArticleMenu(models.Model):
	title = models.CharField(max_length=255)
	intro = models.TextField()
	body = models.TextField()
	image_label = models.CharField(max_length=255, default=None, validators=[isImage], blank=True, null=True)
	last_change = models.CharField(max_length=55, default=f"Created on {datetime.datetime.now().strftime('%m/%d/%Y')}")
	is_new = models.BooleanField(default=True)
	display = models.BooleanField(default=True)
	index = models.IntegerField(null=True, blank=True)
	titre_description = models.CharField(max_length=255, default=None, blank=True, null=True)
	meta_description = models.CharField(max_length=255, default=None, blank=True, null=True)

	def save(self, *args, **kwargs):
		pk_article = self.pk
		try:
			ArticleMenu.objects.get(pk=pk_article)
			self.last_change = f"Updated on {datetime.datetime.now().strftime('%m/%d/%Y')}"
		except:
			# article being created
			pass
		super(ArticleMenu, self).save(*args, **kwargs)

	def __str__(self):
		chaine = f"{self.title} | display {self.display} | is_new {self.is_new}"
		return chaine