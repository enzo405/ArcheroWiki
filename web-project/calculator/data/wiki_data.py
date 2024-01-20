from django.utils.translation import gettext_lazy as _


LocalDataContentWiki = {
  "SkillData": {
    "Absolute_Strike": {
      "displayName": _("Absolute Strike"),
      "description": _("After moving some distance, the next attack's damage is doubled"),
      "requirement": _("Requirement : clear Chapter 21"),
      "stats": ""
    },
    "Agility": {
      "displayName": _("Agility"),
      "description": _("Your Dodge chance increase the lower your HP is"),
      "requirement": "",
      "stats": _("+0.3% chance to dodge each 1% of life missing. (Additive)")
    },
    "Attack_Boost": {
      "displayName": _("Attack Boost"),
      "description": _("Increase your damage"),
      "requirement": "",
      "stats": _("[Major] Damage +30%<br>[Minor] Damage +15%<br>Additive")
    },
    "Attack_Plus": {
      "displayName": _("Attack Plus"),
      "description": _("Increases your attack when you don't take damage in a stage"),
      "requirement": "",
      "stats": _("Increases your attack by 2.25% when you don't take damage in a room.<br>18 times max [40%]")
    },
    "Attack_Speed_Boost": {
      "displayName": _("Attack Speed Boost"),
      "description": _("Increase your attack speed"),
      "requirement": "",
      "stats": _("• [Major] Attack Speed +25%<br>• [Minor] Attack Speed +12.5%<br>• Additive")
    },
    "Angelic_Blessing": {
      "displayName": _("Angelic Blessing"),
      "description": _("Angel room has chance to heal 2x 4x HP"),
      "requirement": "",
      "stats": ""
    },
    "Blade_Storm": {
      "displayName": _("Blade Storm"),
      "description": _("Whirldwind storm of blades that blocks projectiles."),
      "requirement": _("Only available while using <a class='styled_a' href='/wiki/item/Antiquated_Sword/'>Antiquated Sword</a>"),
      "stats": ""
    },
    "Blaze": {
      "displayName": _("Blaze"),
      "description": _("Your attacks cause a Flame effect"),
      "requirement": "",
      "stats": _("Deals 18% equipment damage every 0.25s to enemies hit by weapon projectile after initial hit up to 7 ticks (2s)")
    },
    "Blazing_Meteor": {
      "displayName": _("Blazing Meteor"),
      "description": _("Summon a flame meteor to attack enemies"),
      "requirement": _("Requirement : clear Chapter 9"),
      "stats": _("Burn chips off enemy HP for 2 seconds.<br>225% modifiable damage, Partial hit: 80% damage.<br>Not affected by Rage ability.")
    },
    "Blazing_Star": {
      "displayName": _("Blazing Star"),
      "description": _("Summon a flame star to attack enemies"),
      "requirement": "",
      "stats": _("Burn chips off enemy HP for 2 seconds.<br>90% modifiable damage. <br>Not affected by Rage ability.<br>Stars are affected by ricochet and will bounce between enemies just like ricochet.")
    },
    "Blazing_Strike": {
      "displayName": _("Blazing Strike"),
      "description": _("Summon a flame sword to attack enemies"),
      "requirement": "",
      "stats": _("Burn chips off enemy HP for 2 seconds.<br>165% modifiable damage.<br>Not affected by Rage ability.<br>The faster the attack speed, the shorter the summoning time.")
    },
    "Blazing_Sword": {
      "displayName": _("Blazing Sword"),
      "description": _("Summons 2 flame swords to spin around you"),
      "requirement": _("Requirement : clear Chapter 2"),
      "stats": _("Burn chips off enemy HP for 2 seconds.<br>132% modifiable damage.<br><b>Notes</b><br>Spins much faster after receiving attack speed boosts.")
    },
    "Bloodthirst": {
      "displayName": _("Bloodthirst"),
      "description": _("Restores HP when you kill enemies!"),
      "requirement": "",
      "stats": _("Gain 1.5% of base Max HP on enemy kills.")
    },
    "Bolt": {
      "displayName": _("Bolt"),
      "description": _("Your attacks cause Lightning effect"),
      "requirement": "",
      "stats": _("Deal 25% equipment damage to enemies within a few tiles of enemies hit by weapon projectile.<br>Deals 30% (Up to 45%) damage to the initial target, with an additional 5% damage per enemy chained by the lightning bolt.<br>Works well with Ricochet<br>Maximum of one spark per enemy per tick.<br>i.e. doesn't hit twice with Front Arrow or extremely high attack speed.")
    },
    "Bolt_Circle": {
      "displayName": _("Bolt Circle"),
      "description": _("Two lightning orbs circle around you"),
      "requirement": "",
      "stats": _("The shocks from the lightning bolts quickly chips off enemy HP, and bounces to other nearby enemies.<br>Deals 85% modifiable damage.<br>Proportional to damage of a single projectile.<br>Affected by rage.<br>Spins faster with attack speed boosts.")
    },
    "Bolt_Meteor": {
      "displayName": _("Bolt Meteor"),
      "description": _("Summon a bolt meteor to attack enemies"),
      "requirement": _("Requirement : clear Chapter 9"),
      "stats": _("The shocks from the lightning bolts quickly chips off enemy HP, and bounces to other nearby enemies.<br>225% modifiable damage, Partial hit: 80% damage.<br>Not affected by Rage ability.")
    },
    "Bolt_Star": {
      "displayName": _("Bolt Star"),
      "description": _("Summon a bolt star to attack enemies"),
      "requirement": "",
      "stats": _("The shocks from the lightning bolts quickly chips off enemy HP, and bounces to other nearby enemies.<br>90% modifiable damage.<br>Not affected by Rage ability.<br>Stars are affected by ricochet and will bounce between enemies just like ricochet.")
    },
    "Bolt_Strike": {
      "displayName": _("Bolt Strike"),
      "description": _("Summon a bolt sword to attack enemies"),
      "requirement": "",
      "stats": _("The shocks from the lightning bolts quickly chips off enemy HP, and bounces to other nearby enemies.<br>165% modifiable damage.<br>Not affected by Rage ability.<br>The faster the attack speed, the shorter the summoning time.")
    },
    "Bolt_Sword": {
      "displayName": _("Bolt Sword"),
      "description": _("Summons 2 bolt swords to spin around you"),
      "requirement": _("Requirement : clear Chapter 2"),
      "stats": _("The shocks from the lightning bolts quickly chips off enemy HP, and bounces to other nearby enemies.<br>132% modifiable damage.<br><b>Notes</b><br>Spins much faster after receiving attack speed boosts.")
    },
    "Bouncy_Wall": {
      "displayName": _("Bouncy Wall"),
      "description": _("Your arrows bounce up to 2 times against walls."),
      "requirement": "",
      "stats": _("-50% damage for each bounce")
    },
    "Burst_Punch": {
      "displayName": _("Burst Punch"),
      "description": _("Chance to trigger explosion when enemies are hit. Melee attack chance is 2x of ranged attack chance (Melee attacks chance of triggering explosions is 2x higher than Ranged attacks)"),
      "requirement": _("Only available while using <a class='a_styled' href='/wiki/item/Expedition_Fist/'>Expedition Weapon</a>"),
      "stats": ""
    },
    "Chilling_Blast": {
      "displayName": _("Chilling Blast"),
      "description": _("Enemies blast a cold wave on death"),
      "requirement": _("Requirement : clear Chapter 3"),
      "stats": _("Enemies explode on death causing an explosive ice effect.")
    },
    "Crit_Aura": {
      "displayName": _("Crit Aura"),
      "description": _("Increases Crit Chance for a short time"),
      "requirement": "",
      "stats": _("Increases your crit chance by 47.5% for 2 seconds.<br>8 second cooldown")
    },
    "Crit_Master": {
      "displayName": _("Crit Master"),
      "description": _("Increase your critical damage & chance"),
      "requirement": "",
      "stats": _("[Major] Crit Damage +40% & Crit chance +10%<br>[Minor] Crit Damage +20% & Crit chance +5%<br>Additive")
    },
    "Crit_Plus": {
      "displayName": _("Crit Plus"),
      "description": _("Increases your crit chance when you don't take damage in a stage"),
      "requirement": "",
      "stats": _("Increases your crit chance by 0.9% when you don't take damage in a room.<br>20 times max [18%]")
    },
    "Dauntless_Greatsword": {
      "displayName": _("Dauntless Greatsword"),
      "description": _("Reduced greatsword rage cost. Forms can be freely changed."),
      "requirement": _("Only available while using <a class='styled_a' href='/wiki/item/Antiquated_Sword/'>Antiquated Sword</a>"),
      "stats": ""
    },
    "Dark_Touch": {
      "displayName": _("Dark Touch"),
      "description": _("Your attacks cause a Dark effect"),
      "requirement": "",
      "stats": _("Dark touch places a bomb on a struck target for 1 second, the explosion deals 90% of modified damage from ATK boosts in an area of effect around the targeted mob.<br>Base damage does not affect damage.<br>Multiple darks will not stack on an enemy.")
    },
    "Death_Axe": {
      "displayName": _("Death Axe"),
      "description": _("Summmons 6 axes when an enemy is defeated"),
      "requirement": _("Requirement : clear Chapter 13"),
      "stats": ""
    },
    "Death_Bomb": {
      "displayName": _("Death Bomb"),
      "description": _("Cause enemies to explode on death"),
      "requirement": _("Requirement : clear Chapter 3"),
      "stats": _("Enemies explode on death causing an area of effect damage (66% of base damage).")
    },
    "Death_Nova": {
      "displayName": _("Death Nova"),
      "description": _("Enemies explode into lightning bolts upon death"),
      "requirement": "",
      "stats": _("When an enemy is killed, enemies create holy projectiles, shooting out in 8 equidistant directions dealing 30% current damage on contact.")
    },
    "Diagonal_Arrows": {
      "displayName": _("Diagonal Arrows"),
      "description": _("Fire 2 additional projectile diagonally."),
      "requirement": "",
      "stats": _("You fire an additional projectile diagonally forward to the left and right.<br>You can get up to 3 diagonal arrow.<br><br><b>-20% Damage per arrow in Melee Attack</b><br><b>100% of Damage per arrow in Range Attack</b>")
    },
    "Dodge_Aura": {
      "displayName": _("Dodge Aura"),
      "description": _("Greatly increases Dodge once in a while."),
      "requirement": "",
      "stats": ""
    },
    "Dodge_Burst": {
      "displayName": _("Dodge Burst"),
      "description": _("Greatly increases Attack once in a while after dodging."),
      "requirement": "",
      "stats": ""
    },
    "Dodge_Challenge": {
      "displayName": _("Dodge Challenge"),
      "description": _("Increases Dodge if no damage taken when clearing a room."),
      "requirement": "",
      "stats": ""
    },
    "Dodge_Master": {
      "displayName": _("Dodge Master"),
      "description": _("Your Dodge Chance is increased"),
      "requirement": "",
      "stats": _("Dodge Chance +20%<br>Dodge is multiplicative when combining dodge from different items and abilities")
    },
    "Double_Payback": {
      "displayName": _("Double Payback"),
      "description": _("Chance to summon twice the summoned objects"),
      "requirement": _("Requirement : clear Chapter 17"),
      "stats": ""
    },
    "Dwarf": {
      "displayName": _("Dwarf"),
      "description": _("Transform into a dwarf with a smaller body"),
      "requirement": _("Requirement : clear Chapter 10"),
      "stats": _("Reduces your hitbox by 15%.<br>Crit Chance +12%.")
    },
    "Enhanced_Summon": {
      "displayName": _("Enhanced Summon"),
      "description": _("Greatly increases summoned creature duration and attack"),
      "requirement": "",
      "stats": ""
    },
    "Element_Burst": {
      "displayName": _("Element Burst"),
      "description": _("Various elemental stats, elemental damage has chance for Crit."),
      "requirement": "",
      "stats": _("Elemental damage crit chance/damage TBC")
    },
    "Element_Upgrade": {
      "displayName": _("Element Upgrade"),
      "description": _("Elemental damage increased greatly."),
      "requirement": "",
      "stats": _("Freeze Damage +100%<br>Bolt Damage +150%<br>Poison Damage +250%<br>Blaze Damage +100%<br>Dark Touch Damage +100%")
    },
    "Eye_For_An_Eye": {
      "displayName": _("Eye For An Eye"),
      "description": _("When summoned object disappears, it has a chance to drop HP and MP items (red & blue hearts)"),
      "requirement": _("Requirement : clear Chapter 17"),
      "stats": ""
    },
    "Explosive_Arrow": {
      "displayName": _("Explosive Arrow"),
      "description": _("Store explosive arrow when moving.<br>Explodes when enemies or walls are hit"),
      "requirement": "",
      "stats": _("Can stack up to 4 explosive arrow.<br>Each explosion does x1.5 damage to mobs close to the wall")
    },
    "Extra_Life": {
      "displayName": _("Extra Life"),
      "description": _("Provides you an automatic free revival after death"),
      "requirement": "",
      "stats": _("Revives you once after death.<br>Reduces your Max HP by 30% (Devil Tax).<br>Can only be recieved by the devil<br>There is no invincibility when reviving from the extra life', Does not use up your revive.<br>When you exclude reviving, Extra Life provides you with 40% more HP overall. However if you choose to revive, Extra Life only provides you with a 5% increase overall in HP compared to if you didn't accept the deal from the Devil")
    },
    "Fatal_Excitement": {
      "displayName": _("Fatal Excitement"),
      "description": _("The lower your HP, the faster circling objects spin"),
      "requirement": "",
      "stats": ""
    },
    "Fire_Circle": {
      "displayName": _("Fire Circle"),
      "description": _("Two flame orbs circle around you"),
      "requirement": "",
      "stats": _("Burn chips off enemy HP for 2 seconds.<br>Deals 85% modifiable damage.<br>Proportional to damage of a single projectile.<br>Affected by rage.<br>Spins faster with attack speed boosts.")
    },
    "Firepower_Boost": {
      "displayName": _("Firepower Boost"),
      "description": _("Summoned object gets a front arrow"),
      "requirement": _("Requirement : clear Chapter 17"),
      "stats": ""
    },
    "Freeze": {
      "displayName": _("Freeze"),
      "description": _("Slows enemies down"),
      "requirement": "",
      "stats": _("Freezes enemies until attacked or for 2 seconds.<br>Only freezes enemies; does not slow enemies. Mobs will be unfrozen by next hit, including pets hits. Freeze changes the behavior of mobs")
    },
    "Front_Arrow": {
      "displayName": _("Front Arrow"),
      "description": _("Shoot 2 arrows in one shot."),
      "requirement": "",
      "stats": _("Additional Front Arrow.<br>-25% damage per arrow<br><br>Devil Stats<br>Additional Front Arrow.<br>-20% damage per arrow")
    },
    "Frost_Meteor": {
      "displayName": _("Frost Meteor"),
      "description": _("Summon a frost meteor to attack enemies"),
      "requirement": _("Requirement : clear Chapter 7"),
      "stats": _("Freeze or slows enemies for 2 seconds.<br>225% modifiable damage, Partial hit: 80% damage.<br>Not affected by Rage ability.")
    },
    "Frost_Star": {
      "displayName": _("Frost Star"),
      "description": _("Summon a frost star to attack enemies"),
      "requirement": "",
      "stats": _("Freeze or slows enemies for 2 seconds.<br>90% modifiable damage.<br>Not affected by Rage ability.<br>Stars are affected by ricochet and will bounce between enemies just like ricochet.")
    },
    "Frost_Strike": {
      "displayName": _("Frost Strike"),
      "description": _("Summon a frost sword to attack enemies"),
      "requirement": "",
      "stats": _("Freeze or slows enemies for 2 seconds.<br>165% modifiable damage.<br>Not affected by Rage ability.<br>The faster the attack speed, the shorter the summoning time.")
    },
    "Frost_Sword": {
      "displayName": _("Frost Sword"),
      "description": _("Summons 2 frost swords to spin around you"),
      "requirement": _("Requirement : clear Chapter 2"),
      "stats": _("Freeze or slows enemies for 2 seconds.<br>132% modifiable damage.<br><b>Notes</b><br>Spins much faster after receiving attack speed boosts.")
    },
    "Furious": {
      "displayName": _("Furious"),
      "description": _("When wielding the Broadsword, it deals more damage at higher Fury."),
      "requirement": _("Only available while using <a class='styled_a' href='/wiki/item/Antiquated_Sword/'>Antiquated Sword</a>"),
      "stats": ""
    },
    "Fury": {
      "displayName": _("Fury"),
      "description": _("Your Attack Speed increase the lower your HP is"),
      "requirement": "",
      "stats": _("+0.4% Attack Speed per 1% of life missing. (Additive)")
    },
    "Fury_Command": {
      "displayName": _("Fury Command"),
      "description": _("Spirits enters a fury state within 5s of entering a room"),
      "requirement": "",
      "stats": ""
    },
    "Giant": {
      "displayName": _("Giant"),
      "description": _("Transform into a giant with increased damage"),
      "requirement": _("Requirement : clear Chapter 11"),
      "stats": _("Increases your hitbox by 10%.<br>Attack +40%<br>Max HP +5%")
    },
    "Grace": {
      "displayName": _("Grace"),
      "description": _("Heal from red heart increase the lower your HP is"),
      "requirement": "",
      "stats": _("+0.6% of heal for red heart each 1% of life missing. (Additive)")
    },
    "Greed": {
      "displayName": _("Greed"),
      "description": _("Collect more coins, but also receive more damage"),
      "requirement": "",
      "stats": _("Coin drop chance +25%<br>Enemy damage +20%")
    },
    "Headshot": {
      "displayName": _("Headshot"),
      "description": _("Small chance to kill mobs instantly"),
      "requirement": "",
      "stats": _("12% chance to kill mobs instantly<br>Ricochet, pierce, and spirit shots can trigger the effect.")
    },
    "Heal": {
      "displayName": _("Heal"),
      "description": _("Restores HP partially"),
      "requirement": "",
      "stats": _("Restores 40% of your HP<br><b>Notes</b><br>Can only be recieved via an Angel and lucky wheel")
    },
    "Hermes_Shoes": {
      "displayName": _("Hermes Shoes"),
      "description": _("Increases movement speed and some dodge rate."),
      "requirement": "",
      "stats": _("Movement Speed +12%<br>Dodge Chance +15%")
    },
    "Heal_Overflow": {
      "displayName": _("Heal Overflow"),
      "description": _("Excess healing increases Max HP"),
      "requirement": "",
      "stats": ""
    },
    "Heroic_Fightback": {
      "displayName": _("Heroic Fightback"),
      "description": _("Once the hero falls, huge amounts of damage is dealt to all enemies"),
      "requirement": "",
      "stats": ""
    },
    "Holy_Touch": {
      "displayName": _("Holy Touch"),
      "description": _("Your attacks cause Holy effect"),
      "requirement": "",
      "stats": _("All arrows that hit an enemy create two perpendicular holy projectiles that deals 70% of your modified projectile damage each.<br>Piercing.")
    },
    "HP_Boost": {
      "displayName": _("HP Boost"),
      "description": _("Max HP increased!"),
      "requirement": "",
      "stats": _("Increases HP by 20% of base max HP")
    },
    "Bloodthirst_Aura": {
      "displayName": _("Bloodthirst Aura"),
      "description": _("Bloodthirst Aura increases health once in a while (cooldown of 8s)"),
      "requirement": "",
      "stats": _("Mob/Boss kill heal 15% of Max HP.")
    },
    "HP_Plus": {
      "displayName": _("HP Plus"),
      "description": _("Increases your Max HP when you don't take damage in a stage"),
      "requirement": "",
      "stats": _("Increases your max HP by 2.2% when you don't take damage in a room.<br>14 times max [30%]")
    },
    "Hurling_Axe": {
      "displayName": _("Hurling Axe"),
      "description": _("Chance to hurl an axe with each attack. Axe count increases with shot count."),
      "requirement": _("Requirement : clear Chapter 13"),
      "stats": ""
    },
    "Ice_Circle": {
      "displayName": _("Ice Circle"),
      "description": _("Two ice orbs circle around you"),
      "requirement": "",
      "stats": _("Freeze or slows enemies for 2 seconds.<br>Deals 85% modifiable damage.<br>Proportional to damage of a single projectile.<br>Affected by rage.<br>Spins faster with attack speed boosts.")
    },
    "Inherited_Summon": {
      "displayName": _("Inherited Summon"),
      "description": _("Summon creature inherits portion of own stats"),
      "requirement": "",
      "stats": ""
    },
    "Inspire": {
      "displayName": _("Inspire"),
      "description": _("Increases attack speed and effect is doubled once enemy is killed."),
      "requirement": "",
      "stats": _("Attack Speed +25% (Effect doubled when enemy killed)")
    },
    "Invincibility_Star": {
      "displayName": _("Invincibility Star"),
      "description": _("Become invincible for 2 seconds once a while"),
      "requirement": "",
      "stats": _("Become invincible for 2 seconds every 10 seconds (1/6th of total time)")
    },
    "Monkey_Offspring": {
      "displayName": _("Monkey Offspring"),
      "description": _("On each attack, chance to turn monkey hairs into Monkey Offspring that perform powerfull attacks"),
      "requirement": "",
      "stats": _("Only available while using <a class='a_styled' href='/wiki/heroes/Wukong/'>Wukong</a> and unlocked the Heavenly Havoc skill")
    },
    "Mirror_Punch": {
      "displayName": _("Mirror Punch"),
      "description": _("When Melee attacks deal critical hits, they leave behind 1-2 melee range Shadow Clones"),
      "requirement": "",
      "stats": _("Only available while using <a class='a_styled' href='/wiki/item/Expedition_Fist/'>Fist Expedition Weapon</a>")
    },
    "Multishot": {
      "displayName": _("Multishot"),
      "description": _("Shoot 2 consecutive arrows in a row."),
      "requirement": "",
      "stats": _("-10% damage per arrow (range)<br>-5% damage per arrow (melee)<br>-15% attack speed<br><br><b>Devil Stats</b><br>-10% damage per arrow (range)<br>-5% damage per arrow (melee)<br>-10% attack speed")
    },
    "Obsidian_Circle": {
      "displayName": _("Obsidian Circle"),
      "description": _("Two dark orbs circle around you"),
      "requirement": "",
      "stats": _("Deals 85% modifiable damage.<br>Proportional to damage of a single projectile.<br>Affected by rage.<br>Spins faster with attack speed boosts.")
    },
    "One_Punch": {
      "displayName": _("One Punch"),
      "description": _("Max Attack Speed is 60%. Additional Attack Speed is converted to 2x weapon damage."),
      "requirement": "",
      "stats": _("Only available while using <a class='a_styled' href='/wiki/item/Expedition_Fist/'>Fist Expedition Weapon</a>")
    },
    "Overdraft": {
      "displayName": _("Overdraft"),
      "description": _("Massive boost to attack speed, but gain experience slower."),
      "requirement": "",
      "stats": _("Attack Speed +45%<br>XP gain -20%.")
    },
    "Pain_Suppression": {
      "displayName": _("Pain Suppression"),
      "description": _("Greatly reduces damage taken during attack action"),
      "requirement": _("Requirement : clear Chapter 21"),
      "stats": ""
    },
    "Phantom_Sword": {
      "displayName": _("Phantom Sword"),
      "description": _("Melee attacks will split the sword into two"),
      "requirement": _("Only available while using <a class='a_styled' href='/wiki/item/Demon_Blade_Rain/'>Demon Blade Rain</a>"),
      "stats": ""
    },
    "Piercing_Shot": {
      "displayName": _("Piercing Shot"),
      "description": _("Your arrows pierce enemies."),
      "requirement": "",
      "stats": _("-33% damage after each enemy pierced")
    },
    "Poison_Circle": {
      "displayName": _("Poison Circle"),
      "description": _("Two poisonous orbs circle around you"),
      "requirement": "",
      "stats": _("Poison slowly chips off enemy HP till it dies<br>Deals 90% modifiable damage.<br>Proportional to damage of a single projectile.<br>Affected by rage.<br>Spins faster with attack speed boosts.")
    },
    "Poisoned_Touch": {
      "displayName": _("Poisoned Touch"),
      "description": _("Your attacks cause Poison effect"),
      "requirement": "",
      "stats": _("Poison deals 30% equipment damage per sec utill mob dies.<br>Works well with Ricochet.<br>Does not stack.")
    },
    "Price_of_Strength": {
      "displayName": _("Price of Strength"),
      "description": _("Get greatly enhanced when entering a room.<br>Weakened for a time when durations ends"),
      "requirement": "",
      "stats": _("8sec :  10% movespeed, 40% atk, regular dmg taken, 10% size, normal atkspd, 10% melee damage boost, 15% crit rate<br>2sec : -5% movespeed, 28% atk, 1.1x dmg taken, 5% size, -15% atkspd, 10% melee damage boost<br>6sec : -15% movespeed, -12% atk, 1.2x dmg taken, -5% size, -15% atkspd")
    },
    "Radiant_Star": {
      "displayName": _("Radiant Star"),
      "description": _("All Stars attacks trigger radiance when enemies are hit."),
      "requirement": _("Requirement : clear Chapter 11"),
      "stats": ""
    },
    "Rage": {
      "displayName": _("Rage"),
      "description": _("Your Attack Speed increase the lower your HP is"),
      "requirement": "",
      "stats": _("+1% Damage each 1% of life missing. (Additive)<br>At 20% of your HP you'll have +80% damage (multiplicative with the other abilities)")
    },
    "Red-Hearted_Grace": {
      "displayName": _("Red-Hearted Grace"),
      "description": _("Chance for enemies to drop a heart when they are hit."),
      "requirement": "",
      "stats": ""
    },
    "Rear_Arrow": {
      "displayName": _("Rear Arrow"),
      "description": _("Fire 1 additional projectile backward."),
      "requirement": "",
      "stats": _("You fire an additional projectile backwards<br>Deal 100% of damage per projectile")
    },
    "Ricochet": {
      "displayName": _("Ricochet"),
      "description": _("Your arrows bounce up to 3 times between nearby enemies."),
      "requirement": "",
      "stats": _("You fire an additional projectile to the left and right<br>-30% damage after each bounce<br>Allows your shot to rebound between enemies up to 3 times in total")
    },
    "Sated": {
      "displayName": _("Sated"),
      "description": _("When HP is full, damage +60%"),
      "requirement": _("Requirement : clear Chapter 19"),
      "stats": ""
    },
    "Side_Arrow": {
      "displayName": _("Side Arrow"),
      "description": _("Fire 2 additional projectile on your both sides."),
      "requirement": "",
      "stats": _("You fire an additional projectile to the left and right <br><br><b>-20% Damage per arrow in Melee Attack</b><br><b>100% of Damage per arrow in Range Attack</b>")
    },
    "Shadow_Samurai": {
      "displayName": _("Shadow Samurai"),
      "description": _("Summon a Samurai to help you in Melee attacks."),
      "requirement": _("Only available while using <a class='a_styled' href='/wiki/item/Demon_Blade_Rain/'>Demon Blade Rain</a>"),
      "stats": ""
    },
    "Shadow_Clone": {
      "displayName": _("Shadow Clone"),
      "description": _("Summons a shadow clone of yours."),
      "requirement": _("Requirement : clear Chapter 2"),
      "stats": _("15% chance to spawn.<br>Max 1 per enemy.<br>Max 3 per boss.<br>Up to 15 clones can be spawned at once.<br>Lasts up to 8 seconds.<br>Deals 100% equipment damage every second.")
    },
    "Shield_Guard": {
      "displayName": _("Shield Guard"),
      "description": _("A shield circles around you"),
      "requirement": "",
      "stats": _("Two shields rotate around you, blocking incoming projectiles<br>Up to 3 shield rotating")
    },
    "Slow_Projectile": {
      "displayName": _("Slow Projectile"),
      "description": _("Slow enemy projectiles"),
      "requirement": "",
      "stats": _("Effect : -50% projectile speed")
    },
    "Smart": {
      "displayName": _("Smart"),
      "description": _("Level-up faster, Max level increased by 2."),
      "requirement": "",
      "stats": _("30% increased experience (XP).<br>2 Additional levels<br>This ability does not appear in hero adventure.<br>The extra level provides you with only 1 additional extra skill besides smart.<br>Chapters where there are only 10 stages (chapterd 7 and 14) don't give much xp. On these stages you don't usually recieve enough xp to get anywhere close to max level.")
    },
    "Speed_Aura": {
      "displayName": _("Speed Aura"),
      "description": _("Increases Attack Speed for a short time"),
      "requirement": "",
      "stats": _("+62.5% Attack Speed for 2s.<br>8 second cooldown")
    },
    "Speed_Plus": {
      "displayName": _("Speed Plus"),
      "description": _("Increases speed by a small percent if no damage is taken"),
      "requirement": "",
      "stats": _("Increases your attack speed by 2.1% when you don't take damage in a room.<br>17 times max [35%]")
    },
    "Spirit_Blaze": {
      "displayName": _("Spirit Blaze"),
      "description": _("Your spirit's attacks cause a flame effect"),
      "requirement": _("Requirement : clear Chapter 8"),
      "stats": _("Hero Attack +22%.")
    },
    "Spirit_Bolt": {
      "displayName": _("Spirit Bolt"),
      "description": _("Your spirit's attacks cause a lightning effect"),
      "requirement": _("Requirement : clear Chapter 8"),
      "stats": _("Hero Crit Chance +3%")
    },
    "Spirit_Freeze": {
      "displayName": _("Spirit Freeze"),
      "description": _("Your spirit's attacks slows enemies down"),
      "requirement": _("Requirement : clear Chapter 8"),
      "stats": _("Hero Attack Speed +18%")
    },
    "Spirit_Front_Arrow": {
      "displayName": _("Spirit Front Arrow"),
      "description": _("Your spirit Front Arrow +1"),
      "requirement": "",
      "stats": _("Scales with hero attack and crit damage.<br>Your spirit's attack can receive a maximum of 80% in boosts, whereas the spirit's crit damage can receive a maximum of 200%. Does not boost your hero, in-game description is incorrect.")
    },
    "Spirit_Multishot": {
      "displayName": _("Spirit Multishot"),
      "description": _("Your spirit fire one more arrow"),
      "requirement": "",
      "stats": _("Scales with hero attack speed and crit rate.<br>Your spirit's attack speed can receive a maximum of 95% in boosts, whereas the spirit's crit rate can receive a maximum of 30%. Does not boost your hero, in-game description is incorrect.")
    },
    "Spirit_Poisoned_Touch": {
      "displayName": _("Spirit Poisoned Touch"),
      "description": _("Your spirit's attacks cause a poison effect"),
      "requirement": _("Requirement : clear Chapter 7"),
      "stats": _("Hero HP Boost +15%<br>Unlocks in Chapter 8.")
    },
    "Strong_Heart": {
      "displayName": _("Strong Heart"),
      "description": _("You restore more HP when healed"),
      "requirement": "",
      "stats": _("Increases red heart heal power by 40% of the base heal.<br>40% more red hearts spawn<br>When receiving this ability from the Angel, heal power of heart crystal is only increased by 20%. (Half the strength of the regular Strong Heart ability)")
    },
    "Strong_Strong_Heart": {
      "displayName": _("Strong Strong Heart"),
      "description": _("Strong Heart increases attack speed and can be stacked"),
      "requirement": _("Requirement : <a href='/wiki/skill/Strong_Heart/' class='styled_a'>Strong Heart</a>"),
      "stats": _("Attack Speed +2% every time you get a crystal heart (Max 60%)")
    },
    "Summon_Bone_Warrior": {
      "displayName": _("Summon Bone Warrior"),
      "description": _("Chance to summon bone warrior when attacking enemies"),
      "requirement": "",
      "stats": ""
    },
    "Summon_One_Eyed_Bat": {
      "displayName": _("Summon One Eyed Bat"),
      "description": _("Summon a One-Eyed Bat"),
      "requirement": _("Requirement : clear Chapter 2"),
      "stats": _("15% chance to spawn<br>Max 1 per enemy<br>Max 3 per boss<br>Up to 15 clones can be spawned at once.<br>Lasts up to 8 seconds.<br>Each bat shoots 1 laser per second dealing 65% of player damage.")
    },
    "Summon_Wolfhound": {
      "displayName": _("Summon Wolfhound"),
      "description": _("Chance to summon wolfhound when attacking enemies"),
      "requirement": "",
      "stats": ""
    },
    "Toxic_Meteor": {
      "displayName": _("Toxic Meteor"),
      "description": _("Summon a toxic meteor to attack enemies"),
      "requirement": "",
      "stats": _("Poison slowly chips off enemy HP till it dies<br>225% modifiable damage, Partial hit: 80% damage.<br>Unlocks in Chapter 9.<br>Not affected by Rage ability.")
    },
    "Toxic_Star": {
      "displayName": _("Toxic Star"),
      "description": _("Summon a toxic star to attack enemies"),
      "requirement": "",
      "stats": _("Poison slowly chips off enemy HP until it dies<br>95% modifiable damage.<br>Not affected by Rage ability.<br>Stars are affected by ricochet and will bounce between enemies just like ricochet.")
    },
    "Toxic_Strike": {
      "displayName": _("Toxic Strike"),
      "description": _("Summon a toxic sword to attack enemies"),
      "requirement": "",
      "stats": _("Poison slowly chips off enemy HP till it dies<br>168% modifiable damage.<br>Not affected by Rage ability.<br>The faster the attack speed, the shorter the summoning time.")
    },
    "Toxic_Sword": {
      "displayName": _("Toxic Sword"),
      "description": _("Summons 2 toxic swords to spin around you"),
      "requirement": _("Requirement : clear Chapter 1"),
      "stats": _("Poison slowly chips off enemy HP till it dies<br>132% modifiable damage.<br><b>Notes</b><br>Spins much faster after receiving attack speed boosts.")
    },
    "Through_The_Wall": {
      "displayName": _("Through The Wall"),
      "description": _("Allows the player to walk through walls"),
      "requirement": "",
      "stats": _("Increases attack damage by 15%")
    },
    "Water_Walker": {
      "displayName": _("Water Walker"),
      "description": _("Allows the player to walk across water"),
      "requirement": "",
      "stats": _("Increases attack damage by 15%")
    },
    "Whirlwind_Axe": {
      "displayName": _("Whirlwind Axe"),
      "description": _("Summons a random number of axes at intervals"),
      "requirement": _("Requirement : clear Chapter 13"),
      "stats": ""
    },
    "Wingman": {
      "displayName": _("Wingman"),
      "description": _("Your spirit can block projectiles for you."),
      "requirement": _("Requirement : clear Chapter 4"),
      "stats": _("Pets block projectiles.")
    }
  },
  "ItemData": {
    "Expedition_Fist": {
      "displayName": _("Expedition Fist"),
      "description": _("Unbreakable gauntlet that blows through mountains with a single punch"),
      "hidden_stats": {
        "1": _("Damage Multiplier<br>x1.6 (Ranged)<br>x1.7 & x2.1 (2 Melee hits)")
      },
      "image": "image/items/expedition_fist_mythic_s.png",
      "rarity": {
        "base": _("Fast Attack Speed, short distance. Hits twice in melee range<br>Attack +[x]<br>Crit Chance +8%"),
        "common": "",
        "great": "",
        "rare": "",
        "epic": _("[Epic] Active skill: Power Punch - Slide the joystick to quickly move and attack<br>[Epic] Combo attacks gradually increase Attack Speed and Movement Speed"),
        "perfect_epic": _("[Perfect Epic] Chance to ignore projectile damage when moving. The faster you move, the higher the chance"),
        "legendary": _("[Legendary] 2nd hit in melee range has slightly higher Crit Rate"),
        "ancient_legendary": _("[Ancient Legendary] Attack +15%"),
        "mythic": _("[Mythic] The lower you HP, the higher your Attack"),
        "mythic+1": _("[Mythic+1] Weapon Basic Stats +10%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Weapon damage : +15%"),
        "titan_tales+1": _("[Titan Tales+1] Weapon Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Weapon Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Total HP restored is converted into Attack and Elemental damage")
      }
    },
    "Expedition_Plate": {
      "displayName": _("Expedition Plate"),
      "description": _("Possesses impenetrable defense and restorative effects."),
      "hidden_stats": {
        "1": _("Note that [Legendary] effect works only once per life")
      },
      "image": "image/items/expedition_plate_s.png",
      "rarity": {
        "base": _("Max HP +[x]<br>Max HP +10%.<br>HP Drops +25%"),
        "common": "",
        "great": "",
        "rare": "",
        "epic": _("[Epic] When attacking, reduces own damage taken."),
        "perfect_epic": "",
        "legendary": _("[Legendary] When healing, gain 2x healing effect until max healing is reached"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] When looting a Red Heart, slightly higher chance to gain invincibility shield for 2s"),
        "mythic+1": _("[Mythic+1] Armor Basic Stats +10%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Max Hp : +18%"),
        "titan_tales+1": _("[Titan Tales+1] Armor Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Armor Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Max Battle Level +1")
      }
    },
    "Expedition_Ring": {
      "displayName": _("Expedition Ring"),
      "description": _("Symbolizes the expeditionary force's unwavering glory"),
      "hidden_stats": {},
      "image": "image/items/expedition_ring_s.png",
      "rarity": {
        "base": _("Attack +[x]<br>Movement Speed +4%"),
        "common": "",
        "great": "",
        "rare": "",
        "epic": _("[Epic] Damage on enemies with full HP +15%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Crit Chance +7%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Damage to Bosses +9%"),
        "mythic+1": _("[Mythic+1] Ring Basic Stats +10%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+20%)"),
        "titan_tales": _("[Titan Tales] Battle XP Gain +4%"),
        "titan_tales+1": _("[Titan Tales+1] Ring Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Ring Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (+13%)"),
        "chaos": _("[Chaos] Knockback +7%")
      }
    },
    "Expedition_Locket": {
      "displayName": _("Expedition Locket"),
      "description": _("Increases leveling speed and healing when equipped"),
      "hidden_stats": {},
      "image": "image/items/expedition_locket_s.png",
      "rarity": {
        "base": _("Max HP +[x]<br>Battle XP Gain +15%"),
        "common": "",
        "great": "",
        "rare": "",
        "epic": _("[Epic] When HP is below 25%, heal for [x]% HP. Only triggers 1 time"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Increased Attack after looting Hearts +25%"),
        "ancient_legendary": _("[Ancient Legendary] Max HP +7%"),
        "mythic": _("[Mythic] Additionnaly restores some HP with each level up"),
        "mythic+1": _("[Mythic+1] Locket Basic Stats +10%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Max Hp +15%"),
        "titan_tales+1": _("[Titan Tales+1] Locket Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Locket Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] When healing in Angel Room, 40% chance to gain angel's other skill")
      }
    },
    "Expedition_Bracelet": {
      "displayName": _("Expedition Bracelet"),
      "description": _("Increase archery proficiency when equipped"),
      "hidden_stats": {},
      "image": "image/items/expedition_bracelet_s.png",
      "rarity": {
        "base": _("Attack +[x]<br>Upon encountering enemy, +1 Front Arrow with 3 random elements for 2s"),
        "common": "",
        "great": "",
        "rare": "",
        "epic": _("[Epic] 2x Crit Rate on enemies with slightly more HP"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Crit Damage +40%"),
        "ancient_legendary": _("Attack +7%"),
        "mythic": _("[Mythic] Weapon damage increases with level. Higher levels deals more damage"),
        "mythic+1": _("[Mythic+1] Bracelet Basic Stats +10%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Attack +15%"),
        "titan_tales+1": _("[Titan Tales+1] Bracelet Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Bracelet Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] For every 100 enemies defeated, projectiles bounce +1 (Max 2)")
      }
    },
    "Expedition_Spellbook": {
      "displayName": _("Expedition Spellbook"),
      "description": _("Lets you gain an angel's blessing. Gain 1 auto-cast Ult. when equipped."),
      "hidden_stats": {},
      "image": "image/items/expedition_spellbook_s.png",
      "rarity": {
        "base": _("When meter is full, instantly gain 1-3 special Red Hearts that heal and increase battle power<br>Max HP +[x]<br>(ULT.) Attack +[x]<br>(ULT.) Attack Speed +10%"),
        "common": "",
        "great": "",
        "rare": "",
        "epic": _("[Epic] (ULT.) Red Hearts can temporarily raise Attack and Crit Rate. Can be stacked"),
        "perfect_epic": _("[Perfect Epic] (ULT.) Each Red Heart spawns +1 Shadow Clone"),
        "legendary": _("[Legendary] (ULT.) Max Red Hearts +1"),
        "ancient_legendary": _("[Ancient Legendary] (ULT.) Red Hearts can temporarily raise Movement Speed and Damage Reduction. Can be stacked"),
        "mythic": _("[Mythic] (ULT.) For every 15 Expedition book's Red Hearts obtained, summon +1 Angel"),
        "mythic+1": _("[Mythic+1] Spellbook Basic Stats +10%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Enhance equipment +12%"),
        "titan_tales+1": _("[Titan Tales+1] Spellbook Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Spellbook Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Red Hearts dropped by enemies raise Spellbook charge speed")
      }
    },
    "Brave_Bow": {
      "displayName": _("Brave Bow"),
      "description": _("Only the worthly can use this bow, with balanced performance."),
      "hidden_stats": {
        "1": _("Damage Multiplier x1"),
        "2": _("Base Attack Speed x1.73")
      },
      "image": "image/items/brave_bow_mythic.png",
      "rarity": {
        "common": _("A well-balanced weapon<br>Attack +[x]"),
        "great": "",
        "rare": _("[Rare] Attack +5%"),
        "epic": _("[Epic] Crit Damage +50%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] When HP is lower, next attack has a chance to fire consecutive shots after moving for a short distance."),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Attack increased temporarily after moving"),
        "mythic+1": _("[Mythic+1] Weapon Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (50% → 75%)"),
        "titan_tales": _("[Titan Tales] Weapon damage : +8%"),
        "titan_tales+1": _("[Titan Tales+1] Weapon Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Weapon Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Increases Critic chance by +5%. Increase attack speed upon critical hit")
      }
    },
    "Brightspear": {
      "displayName": _("Brightspear"),
      "description": _("Contains immense energy, you're defeated before you know it!"),
      "hidden_stats": {
        "1": _("Damage Multiplier x1.2"),
        "2": _("Base Attack Speed x1.63")
      },
      "image": "image/items/brightspear_mythic.png",
      "rarity": {
        "common": _("Can suddenly attack enemies<br>Attack +[x]"),
        "great": "",
        "rare": _("[Rare] Attack +5%"),
        "epic": _("[Epic] When attacking a similar target (same mob), damage dealt will increase."),
        "perfect_epic": "",
        "legendary": _("[Legendary] Shot damage increased each time it bounces off wall. Also increases max wall bounces."),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Landing crits increases Attack Speed"),
        "mythic+1": _("[Mythic+1] Weapon Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Weapon damage : +9%"),
        "titan_tales+1": _("[Titan Tales+1] Weapon Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Weapon Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Your arrows pierce enemies")
      }
    },
    "Death_Scythe": {
      "displayName": _("Death Scythe"),
      "description": _("Powerful scythe, very heavy with slow attack speed."),
      "hidden_stats": {
        "1": _("Damage Multiplier x1.45"),
        "2": _("Base Attack Speed x0.85"),
        "3": _("50% chance to kill enemies under 30% Hp")
      },
      "image": "image/items/death_scythe_mythic.png",
      "rarity": {
        "common": _("High attack with low speed<br>Attack +[x]"),
        "great": "",
        "rare": _("[Rare] Attack +5%"),
        "epic": _("[Epic] High chance to kill mobs with less than 30% of HP"),
        "perfect_epic": "",
        "legendary": _("[Legendary] After instakilling lower HP minions, increase own Attack Speed for a short time."),
        "ancient_legendary": "",
        "mythic": _("[Mythic] The closer, the higher the damage"),
        "mythic+1": _("[Mythic+1] Weapon Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (30% → 35%)"),
        "titan_tales": _("[Titan Tales] Weapon damage : +8%"),
        "titan_tales+1": _("[Titan Tales+1] Weapon Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Weapon Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] After headshot, increase atk and there is a chance it cause explosion")
      }
    },
    "Demon_Blade_Rain": {
      "displayName": _("Demon Blade Rain"),
      "description": _("Legendary demon blade can devour the soul of the enemy."),
      "hidden_stats": {
        "1": _("Damage Multiplier<br>x1.5 (Ranged)<br>x1.85 (Melee)"),
        "2": _("Base Attack Speed x?"),
        "3": _("During Melee attack +100% Front Collision Resistance"),
        "4": _("[Epic] +x1.18% Damage to enemies above 8% HP")
      },
      "image": "image/items/demon_blade_rain_mythic.png",
      "rarity": {
        "common": _("Unsheathing deals melee damage, also deals long-range damage.<br>Attack +[x]<br>Immune to front collision damage in melee attacks"),
        "great": _("[Great] When low HP, kill enemies in melee can recover HP"),
        "rare": _("[Rare] Attack +5%"),
        "epic": _("[Epic] The higher the enemy's HP, the more damage dealt"),
        "perfect_epic": _("[Perfect Epic] Lost HP will increase Crit damage"),
        "legendary": _("[Legendary] When moving, dodge rate slightly increased"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Taking damage increases Crit Chance temporarily"),
        "mythic+1": _("[Mythic+1] Weapon Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Weapon damage : +11%"),
        "titan_tales+1": _("[Titan Tales+1] Weapon Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Weapon Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] The less health, the higher dodge rate and movement speed")
      }
    },
    "Antiquated_Sword": {
      "displayName": _("Antiquated Sword"),
      "description": _("Ancient Sword that becomes bigger when empowered. Named 'Giantkiller' for its history of slaying titans."),
      "hidden_stats": {
        "1": _("Damage Multiplier<br>x1.5 (Ranged)<br>x1.85 (Melee)<br>x2.02 (2 hands)"),
        "2": _("Base Attack Speed x?")
      },
      "image": "image/items/antiquated_sword_mythic.png",
      "rarity": {
        "common": _("Allows change of forms: one-handed swords attack faster; increases two-handed sword attack range<br>Attack +[x]<br>Broadsword deals more damage to bigger enemies"),
        "great": _("[Great] Broadsword bullets can go through enemies"),
        "rare": _("[Rare] Attack +5%"),
        "epic": _("[Epic] Unlock active skill: Whirlwind<br>[Epic] Upon hitting an enemy, Attack Speed becomes higher"),
        "perfect_epic": _("[Perfect Epic] Upon killing an enemy, Attack becomes higher."),
        "legendary": _("[Legendary] Increases Max HP and reduces Whirlwind cost. At low HP, Fury cost is significantly reduced"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Upon taking damage, increases Attack Speed and Crit Chance"),
        "mythic+1": _("[Mythic+1] Weapon Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Weapon damage : +12%"),
        "titan_tales+1": _("[Titan Tales+1] Weapon Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Weapon Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] When in dual form, a 3rd attack is added to successive ranged attacks")
      }
    },
    "Gale_Force": {
      "displayName": _("Gale Force"),
      "description": _("A crossbow infused with the power of the wind, shooting out charged arrows."),
      "hidden_stats": {
        "1": _("Damage Multiplier x1.55"),
        "2": _("Base Attack Speed x0.75"),
        "3": _("Charged Attack x2"),
        "4": _("Penetrating Attack x1.35")
      },
      "image": "image/items/gale_force_mythic.png",
      "rarity": {
        "common": _("High attack, slow attack speed. It automatically reloads and shoots a charged arrow.<br>Attack +[x]"),
        "great": _("[Great] Attack +5%"),
        "rare": _("[Rare] Charged attacks carry a penetrating effect."),
        "epic": _("[Epic] Penetrating attacks have multiple damage effects, normal attack crit rate increases over distance."),
        "perfect_epic": "",
        "legendary": _("[Legendary] After a Crit attack, charging speed can be increased."),
        "ancient_legendary": _("[Ancient Legendary] After a Crit Attack, charging speed can be increased."),
        "mythic": _("[Mythic] Charged attacks deal increased damage and slow enemies."),
        "mythic+1": _("[Mythic+1] Weapon Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Weapon damage : +10%"),
        "titan_tales+1": _("[Titan Tales+1] Weapon Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Weapon Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] When a charged attack lands critical hit, increases hero's Attack for a while (~2s)")
      }
    },
    "Mini_Atreus": {
      "displayName": _("Mini Atreus"),
      "description": _("An exquisite Atreus puppet that can be used for battle in times of danger."),
      "hidden_stats": {
        "1": _("Damage Multiplier x1.25"),
        "2": _("Base Attack Speed x?")
      },
      "image": "image/items/mini_atreus.png",
      "rarity": {
        "common": _("Slows enemies on hit<br>Attack +[x]"),
        "great": _("[Great] Attack +5%"),
        "rare": "",
        "epic": _("[Epic] Hitting the enemy has a chance to summon an Atreus to assist in battle"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Chance to summon 2 Atreus Rotating Shields after hitting an enemy"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Coins from Battle +10%"),
        "mythic+1": _("[Mythic+1] Weapon Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Weapon damage : +12%"),
        "titan_tales+1": _("[Titan Tales+1] Weapon Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Weapon Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (+22%)"),
        "chaos": _("[Chaos] Deals more damage to enemies that slow you down or have freeze effect")
      }
    },
    "Saw_Blade": {
      "displayName": _("Saw Blade"),
      "description": _("A serrated throwing knife from the mysterious Orient."),
      "hidden_stats": {
        "1": _("Damage Multiplier x0.8"),
        "2": _("Base Attack Speed x2.6")
      },
      "image": "image/items/saw_blade_mythic.png",
      "rarity": {
        "common": _("Low Attack with high speed<br>Attack +[x]"),
        "great": "",
        "rare": _("[Rare] Attack +5%"),
        "epic": _("[Epic] Increases your Attack Speed for 3 sec after entering a room"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Reduces Elemental Resistance after hitting an enemy. Can be stacked"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Hitting enemies has a chance to increase Dodge and Attack (Stackable)"),
        "mythic+1": _("[Mythic+1] Weapon Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (3s → 5s)"),
        "titan_tales": _("[Titan Tales] Weapon damage : +8%"),
        "titan_tales+1": _("[Titan Tales+1] Weapon Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Weapon Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] After hitting enemy, there is a chance to increase the damage of bullet (stackable)")
      }
    },
    "Stalker_Staff": {
      "displayName": _("Stalker Staff"),
      "description": _("The staff of all staffs, no one can escape!"),
      "hidden_stats": {
        "1": _("Damage Multiplier x1<br>Base Attack Speed x2")
      },
      "image": "image/items/stalker_staff_mythic.png",
      "rarity": {
        "common": _("The Bullets will follow enemies and attack<br>Attack +[x]"),
        "great": "",
        "rare": _("[Rare] Attack +5%"),
        "epic": _("[Epic] The lower the target's HP, the higher the Crit rate."),
        "perfect_epic": "",
        "legendary": _("[Legendary] Chance to split into an extra shot after defeating an enemy."),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Projectile charge time -50%"),
        "mythic+1": _("[Mythic+1] Weapon Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Weapon damage : +9%"),
        "titan_tales+1": _("[Titan Tales+1] Weapon Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Weapon Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (-70%)"),
        "chaos": _("[Chaos] The bigger the turn radius of own projectile, the higher the damage")
      }
    },
    "Tornado": {
      "displayName": _("Tornado"),
      "description": _("A sharp boomerang that can fly back and forth."),
      "hidden_stats": {
        "1": _("Damage Multiplier x0.8 (and x0.536 for the return)<br>Base Attack Speed x1.73")
      },
      "image": "image/items/tornado_mythic.png",
      "rarity": {
        "common": _("It returns to your hand<br>Attack +[x]"),
        "great": "",
        "rare": _("[Rare] Attack +5%"),
        "epic": _("[Epic] Boomerang deals increased damage when it returns"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Tornado damage increased. Tornado return speed is faster"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] The further projectiles travel, the higher the damage"),
        "mythic+1": _("[Mythic+1] Weapon Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Weapon damage : +8%"),
        "titan_tales+1": _("[Titan Tales+1] Weapon Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Weapon Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] The more enemies hit by the boomerang, the higher bullet damage")
      }
    },
    "Phantom_Cloak": {
      "displayName": _("Phantom Cloak"),
      "description": _("An awesome-looking cloak."),
      "hidden_stats": {
        "1": _("[Epic] Thorn attacks are x2 your base damage"),
        "2": _("[Mythic] Frozen enemy takes +10% base damage"),
        "3": _("[Mythic+2] Thorns attack are x2.8 your base damage"),
        "4": _("[Titan Tales+3] Frozen enemy takes +15% base damage")
      },
      "image": "image/items/phantom_cloak.png",
      "rarity": {
        "base": _("Max HP +[x]"),
        "common": _("[Common] Projectile Resistance +10%"),
        "great": "",
        "rare": _("[Rare] Healing from red hearts +20%"),
        "epic": _("[Epic] Freezes enemies who hit you for 1-2s and deal thorn damage"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Increases Attack upon revival"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Enemies frozen by Phantom Cloak take more damage"),
        "mythic+1": _("[Mythic+1] Armor Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Max Hp : +10%"),
        "titan_tales+1": _("[Titan Tales+1] Armor Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Armor Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Chance to drop a Hearts when taking projectile damage")
      }
    },
    "Golden_Chestplate": {
      "displayName": _("Golden Chestplate"),
      "description": _("A chestplate made of pure gold. It's as solid as a rock."),
      "hidden_stats": {
        "1": _("[Epic] Fire Damage +10%"),
        "2": _("[Mythic] Damage reduction = 25%"),
        "3": _("[Mythic+2] Fire Damage +13%"),
        "4": _("[Titan Tales+3]Damage reduction = 27.5%")
      },
      "image": "image/items/golden_chestplate.png",
      "rarity": {
        "base": _("Max HP +[x]"),
        "common": _("[Common] Damage Resistance +5%"),
        "great": "",
        "rare": _("[Rare] Healing from red hearts +20%"),
        "epic": _("[Epic] Deals 8% of base damage per tick as flame damage to close enemies"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Increases Max HP upon revival"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Damage taken is greatly reduced for 2s after taking damage "),
        "mythic+1": _("[Mythic+1] Armor Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Max Hp : +10%"),
        "titan_tales+1": _("[Titan Tales+1] Armor Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Armor Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] The lower your health the higher the recovery")
      }
    },
    "Vest_of_Dexterity": {
      "displayName": _("Vest of Dexterity"),
      "description": _("Light and durable. Wear it to dodge enemy attacks."),
      "hidden_stats": {
        "1": _("[Epic] Lightning Damage 80%"),
        "2": _("[Mythic+2] Lightning Damage 110%")
      },
      "image": "image/items/vest_of_dexterity.png",
      "rarity": {
        "base": _("Max HP +[x]"),
        "common": _("[Common] Dodge Chance +7%"),
        "great": "",
        "rare": _("[Rare] Healing from red hearts +20%"),
        "epic": _("[Epic] Deals 80% base damage (affected by attack boost) and applies Lightning effect to nearest enemy"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Increases Attack upon revival"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Increased Dodge while moving"),
        "mythic+1": _("[Mythic+1] Armor Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Max Hp : +10%"),
        "titan_tales+1": _("[Titan Tales+1] Armor Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Armor Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Chance to gain blessing 1 time when obtaining a heart. (shield that block projectile, can stack up to 2)")
      }
    },
    "Void_Robe": {
      "displayName": _("Void Robe"),
      "description": _("A robe from a demonic realm."),
      "hidden_stats": {
        "1": _("[Epic] : Poison Damage = 40%"),
        "2": _("[Mythic+2] : Poison Damage = 56%")
      },
      "image": "image/items/void_robe.png",
      "rarity": {
        "base": _("Max HP +[x]"),
        "common": _("[Common] Collision Resistance +10%"),
        "great": "",
        "rare": _("[Rare] Healing from red hearts +20%"),
        "epic": _("[Epic] Poisons all enemies in the room."),
        "perfect_epic": "",
        "legendary": _("[Legendary] Increases Max HP upon revival"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Dropped Hearts restore more HP"),
        "mythic+1": _("[Mythic+1] Armor Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Max Hp : +10%"),
        "titan_tales+1": _("[Titan Tales+1] Armor Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Armor Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Chance of dropping a heart when taking collision Damage")
      }
    },
    "Bright_Robe": {
      "displayName": _("Bright Robe"),
      "description": _("A robe that's full of light, reduces front damage during battle."),
      "hidden_stats": {
        "1": _("[Epic] HP limit increases by +2.5% per skill/ability received from levelling up"),
        "2": _("[Mythic+2] HP limit increases by +3% per skill/ability received from levelling up"),
        "3": _("[Chaos] Red Heart : +0.4% Max Health & 0.15% damage reduction (stackable)")
      },
      "image": "image/items/bright_robe.png",
      "rarity": {
        "base": _("Max HP +[x]"),
        "common": _("[Common] Front Damage Resistance +12%"),
        "great": "",
        "rare": _("[Rare] Battle XP Gain +25%"),
        "epic": _("[Epic] Each upgrade will increase HP limit."),
        "perfect_epic": "",
        "legendary": _("[Legendary] Increases Attack upon revival"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] HP Drops +10%"),
        "mythic+1": _("[Mythic+1] Armor Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Max Hp : +12%"),
        "titan_tales+1": _("[Titan Tales+1] Armor Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Armor Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Obtained Hearts increase Max Hp and Damage reduction")
      }
    },
    "Shadow_Robe": {
      "displayName": _("Shadow Robe"),
      "description": _("An assassin's special robe, reduces rear damage during battle."),
      "hidden_stats": {
        "1": _("[Epic] Deals 135% modifiable base damage"),
        "2": _("[Mythic] 10% Resistance when there are 5 enemies or more"),
        "3": _("[Mythic+2] Deals 165% modifiable base damage"),
        "4": _("[Titan Tales+3] 16% Resistance when there are 5 enemies or more")
      },
      "image": "image/items/shadow_robe.png",
      "rarity": {
        "base": _("Max HP +[x]"),
        "common": _("[Common] Rear Damage Resistance +20%"),
        "great": "",
        "rare": _("[Rare] Max HP +7%"),
        "epic": _("[Epic] Causes strong dark damage (Dark Touch) to nearby enemies."),
        "perfect_epic": "",
        "legendary": _("[Legendary] Increases Max HP upon revival"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] In case of many enemies, damage taken is reduced"),
        "mythic+1": _("[Mythic+1] Armor Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Max Hp : +12%"),
        "titan_tales+1": _("[Titan Tales+1] Armor Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Armor Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] The more nearby enemies inflected with Dark, the higher Hero's Attack")
      }
    },
    "Laser_Bat": {
      "displayName": _("Laser Bat"),
      "description": _("Bat from a mysterious cave. Its laser could easily penetrate obsticles."),
      "hidden_stats": {
        "1": _("[Mythic] Enemies take 7% more damage when hit by Pets"),
        "3": _("[Titan Tales+3] Enemies take 10% more damage when hit by Pets")
      },
      "image": "image/items/laser_bat.png",
      "rarity": {
        "common": _("Own Attack +[x]"),
        "great": _("[Great] Own Attack Speed +10%"),
        "rare": _("[Rare] Own crit +20%"),
        "epic": _("[Epic] 50% chance for new ability after adventure level-up"),
        "perfect_epic": _("[Perfect Epic] Inherit Leader's attack +10%"),
        "legendary": _("[Legendary] Attacked enemies will be poisoned"),
        "ancient_legendary": _("[Ancient Legendary] 80% chance for new ability after adventure level-up"),
        "mythic": _("[Mythic] Enemies hit lose more HP when taking damage"),
        "mythic+1": _("[Mythic+1] Pets Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] For every 5 spirit level they gain 1% of Hero's attack"),
        "titan_tales+1": _("[Titan Tales+1] Pets Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Pets Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Gain hero's attack speed")
      }
    },
    "Scythe_Mage": {
      "displayName": _("Scythe Mage"),
      "description": _("Like the Grim Reaper, he can slice through enemies with his sharpened scythe."),
      "hidden_stats": {
        "1": _("[Mythic] Enemies take 7% more damage when hit by Pets"),
        "3": _("[Titan Tales+3] Enemies take 10% more damage when hit by Pets")
      },
      "image": "image/items/scythe_mage.png",
      "rarity": {
        "common": _("Own Attack +[x]"),
        "great": _("[Great] Own Attack Speed +10%"),
        "rare": _("[Rare] Own crit +20%"),
        "epic": _("[Epic] 50% chance for new ability after adventure level-up"),
        "perfect_epic": _("[Perfect Epic] Inherit Leader's Attack +10%"),
        "legendary": _("[Legendary] Crit Damage increased greatly"),
        "ancient_legendary": _("[Ancient Legendary] 80% chance for new ability after adventure level-up"),
        "mythic": _("[Mythic] Enemies hit lose more HP when taking damage"),
        "mythic+1": _("[Mythic+1] Pets Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] For every 5 spirit level they gain 1% of Hero's attack"),
        "titan_tales+1": _("[Titan Tales+1] Pets Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Pets Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Gain hero's attack speed")
      }
    },
    "Elf": {
      "displayName": _("Elf"),
      "description": _("Elf of the Dark Forest. Fires projectiles."),
      "hidden_stats": {
        "1": _("[Mythic] Enemies take 7% more damage when hit by Pets"),
        "3": _("[Titan Tales+3] Enemies take 10% more damage when hit by Pets")
      },
      "image": "image/items/elf.png",
      "rarity": {
        "common": _("Own Attack +[x]"),
        "great": _("[Great] Own Attack Speed +10%"),
        "rare": _("[Rare] Own crit +20%"),
        "epic": _("[Epic] 50% chance for new ability after adventure level-up"),
        "perfect_epic": _("[Perfect Epic] Inherit Leader's Attack +10%"),
        "legendary": _("[Legendary] Attack Speed increased greatly from time to time"),
        "ancient_legendary": _("[Ancient Legendary] 80% chance for new ability after adventure level-up"),
        "mythic": _("[Mythic] Enemies hit lose more HP when taking damage"),
        "mythic+1": _("[Mythic+1] Pets Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] For every 5 spirit level they gain 1% of Hero's attack"),
        "titan_tales+1": _("[Titan Tales+1] Pets Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Pets Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Gain hero's attack speed")
      }
    },
    "Bone_Warrior": {
      "displayName": _("Bone Warrior"),
      "description": _("Once a powerful warrior, now it pledges its blade to you"),
      "hidden_stats": {
        "1": _("[Mythic] Enemies take 7% more damage when hit by Pets"),
        "3": _("[Titan Tales+3] Enemies take 10% more damage when hit by Pets")
      },
      "image": "image/items/bone_warrior.png",
      "rarity": {
        "common": _("Own Attack +[x]"),
        "great": _("[Great] Own Attack Speed +10%"),
        "rare": _("[Rare] Own Crit +20%"),
        "epic": _("[Epic] 50% chance for new ability after adventure level-up"),
        "perfect_epic": _("[Perfect Epic] Inherit Leader's attack +10%"),
        "legendary": _("[Legendary] Trigger Fury State for a short duration after a Crit"),
        "ancient_legendary": _("[Ancient Legendary] Chance to block a lethal attack and die for Hero 1 time"),
        "mythic": _("[Mythic] Enemies hit lose more HP when taking damage"),
        "mythic+1": _("[Mythic+1] Pets Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] For every 5 spirit level they gain 1% of Hero's attack"),
        "titan_tales+1": _("[Titan Tales+1] Pets Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Pets Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Gain hero's attack speed")
      }
    },
    "Living_Bomb": {
      "displayName": _("Living Bomb"),
      "description": _("Keeps throwing bombs that deal splash damage."),
      "hidden_stats": {
        "1": _("[Mythic] Enemies take 7% more damage when hit by Pets"),
        "3": _("[Titan Tales+3] Enemies take 10% more damage when hit by Pets")
      },
      "image": "image/items/living_bomb.png",
      "rarity": {
        "common": _("Own Attack +[x]"),
        "great": _("[Great] Own Attack Speed +10%"),
        "rare": _("[Rare] Own crit +20%"),
        "epic": _("[Epic] 50% chance for new ability after adventure level-up"),
        "perfect_epic": _("[Perfect Epic] Inherit Leader's Attack +10%"),
        "legendary": _("[Legendary] The bomb will split into 3 mini bombs once it hits the floor"),
        "ancient_legendary": _("[Ancient Legendary] 80% chance for new ability after adventure level-up"),
        "mythic": _("[Mythic] Enemies hit lose more HP when taking damage"),
        "mythic+1": _("[Mythic+1] Pets Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] For every 5 spirit level they gain 1% of Hero's attack"),
        "titan_tales+1": _("[Titan Tales+1] Pets Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Pets Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Gain hero's attack speed")
      }
    },
    "Noisy_Owl": {
      "displayName": _("Noisy Owl"),
      "description": _("Part of the gale force, this owl can summon a strong gale which can knockback enemies."),
      "hidden_stats": {
        "1": _("Sends 2 forward-facing tornado projectiles that can knockback enemies"),
        "2": _("[Mythic] Enemies take 7% more damage when hit by Pets"),
        "3": _("[Titan Tales+3] Enemies take 10% more damage when hit by Pets")
      },
      "image": "image/items/noisy_owl.png",
      "rarity": {
        "common": _("Own Attack +[x]"),
        "great": _("[Great] Own Attack Speed +10%"),
        "rare": _("[Rare] Own crit +20%"),
        "epic": _("[Epic] 50% chance for new ability after adventure level-up"),
        "perfect_epic": _("[Perfect Epic] Inherit Leader's Attack +10%"),
        "legendary": _("[Legendary] Projectiles split into 2 after some distance"),
        "ancient_legendary": _("[Ancient Legendary] 80% chance for new ability after adventure level-up"),
        "mythic": _("[Mythic] Enemies hit lose more HP when taking damage"),
        "mythic+1": _("[Mythic+1] Pets Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] For every 5 spirit level they gain 1% of Hero's attack"),
        "titan_tales+1": _("[Titan Tales+1] Pets Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Pets Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Gain hero's attack speed")
      }
    },
    "Flaming_Ghost": {
      "displayName": _("Flaming Ghost"),
      "description": _("A ghost burning with blue flames that can shoot fireballs which split."),
      "hidden_stats": {
        "1": _("Sends a single forward-facing projectile that splits into two, similar to the purple ghost projectile"),
        "2": _("[Mythic] Enemies take 7% more damage when hit by Pets"),
        "3": _("[Titan Tales+3] Enemies take 10% more damage when hit by Pets")
      },
      "image": "image/items/flaming_ghost.png",
      "rarity": {
        "common": _("Own Attack +[x]"),
        "great": _("[Great] Own Attack Speed +10%"),
        "rare": _("[Rare] Own crit +20%"),
        "epic": _("[Epic] 50% chance for new ability after adventure level-up"),
        "perfect_epic": _("[Perfect Epic] Inherit Leader's Attack +10%"),
        "legendary": _("[Legendary] Projectiles rebound once"),
        "ancient_legendary": _("[Ancient Legendary] 80% chance for new ability after adventure level-up"),
        "mythic": _("[Mythic] Enemies hit lose more HP when taking damage"),
        "mythic+1": _("[Mythic+1] Pets Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] For every 5 spirit level they gain 1% of Hero's attack"),
        "titan_tales+1": _("[Titan Tales+1] Pets Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Pets Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Gain hero's attack speed")
      }
    },
    "Bear_Ring": {
      "displayName": _("Bear Ring"),
      "description": _("Bestowed with the Power of a Bear."),
      "hidden_stats": {
        "1": _("[Chaos] Fire Damage +5%")
      },
      "image": "image/items/bear_ring_epic.png",
      "rarity": {
        "common": _("Increases damage to ground units +[x]"),
        "great": "",
        "rare": _("[Rare] Max HP +5%"),
        "epic": _("[Epic] Coins From Battle +10%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Ice Damage +8%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Ground Units damage reduced +7%"),
        "mythic+1": _("[Mythic+1] Ring Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+15%)"),
        "titan_tales": _("[Titan Tales] Damage Ground Units +10%"),
        "titan_tales+1": _("[Titan Tales+1] Ring Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Ring Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (+12%)"),
        "chaos": _("[Chaos] Greatly Increases fire Damage.")
      }
    },
    "Wolf_Ring": {
      "displayName": _("Wolf Ring"),
      "description": _("Bestowed with the Power of a Wolf."),
      "hidden_stats": {
        "1": _("[Chaos] Lightning Damage +15%")
      },
      "image": "image/items/wolf_ring_epic.png",
      "rarity": {
        "common": _("Increases damage to melee units +[x]"),
        "great": "",
        "rare": _("[Rare] Crit Chance +5%"),
        "epic": _("[Epic] Coins From Battle +10%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Flame Damage +5%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Melee Units damage reduced+7%"),
        "mythic+1": _("[Mythic+1] Ring Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+15%)"),
        "titan_tales": _("[Titan Tales] Damage Melee Units +10%"),
        "titan_tales+1": _("[Titan Tales+1] Ring Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Ring Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (+12%)"),
        "chaos": _("[Chaos] Greatly Increases lightning Damage")
      }
    },
    "Falcon_Ring": {
      "displayName": _("Falcon Ring"),
      "description": _("Bestowed with the Power of a Falcon."),
      "hidden_stats": {
        "1": _("[Chaos] Ice Damage +40%")
      },
      "image": "image/items/falcon_ring_epic.png",
      "rarity": {
        "common": _("Increases damage to airborne units +[x]"),
        "great": "",
        "rare": _("[Rare] Attack Speed +5%"),
        "epic": _("[Epic] Coins From Battle +10%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Dark Touch Damage +6%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Airborne damage resistance +7%"),
        "mythic+1": _("[Mythic+1] Ring Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+15%)"),
        "titan_tales": _("[Titan Tales] Damage Airborne Units +10%"),
        "titan_tales+1": _("[Titan Tales+1] Ring Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Ring Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (+12%)"),
        "chaos": _("[Chaos] Greatly increases ice damage.")
      }
    },
    "Serpent_Ring": {
      "displayName": _("Serpent Ring"),
      "description": _("Bestowed with the Power of a Serpent."),
      "hidden_stats": {
        "1": _("[Chaos] Poison Damage +20%")
      },
      "image": "image/items/serpent_ring_epic.png",
      "rarity": {
        "common": _("Increases damage to ranged units +[x]"),
        "great": "",
        "rare": _("[Rare] Dodge +7%"),
        "epic": _("[Epic] Coins From Battle +10%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Poison Damage +7%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Ranged Units damage reduced +7%"),
        "mythic+1": _("[Mythic+1] Ring Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+15%)"),
        "titan_tales": _("[Titan Tales] Damage Range Units +10%"),
        "titan_tales+1": _("[Titan Tales+1] Ring Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Ring Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (+12%)"),
        "chaos": _("[Chaos] Greatly increases poison damage.")
      }
    },
    "Bull_Ring": {
      "displayName": _("Bull Ring"),
      "description": _("Contains the power of bulls, use it to increase attacks on all mobs."),
      "hidden_stats": {
        "1": _("[Chaos] Damage to Melee Units +3%")
      },
      "image": "image/items/bull_ring_epic.png",
      "rarity": {
        "common": _("Increases damage to mobs +[x]"),
        "great": "",
        "rare": _("[Rare] Damage Resistance +10%"),
        "epic": _("[Epic] Coins From Battle +10%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Lightning Damage +7%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Mobs damage resistance +5%"),
        "mythic+1": _("[Mythic+1] Ring Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+15%)"),
        "titan_tales": _("[Titan Tales] Damage Mob Units +10%"),
        "titan_tales+1": _("[Titan Tales+1] Ring Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Ring Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (+7%)"),
        "chaos": _("[Chaos] Increase Melee Damage")
      }
    },
    "Lion_Ring": {
      "displayName": _("Lion Ring"),
      "description": _("Contains the power of a berserk lion, use it to increase attacks on boss monsters."),
      "hidden_stats": {
        "1": _("[Chaos] Damage to Ranged Units +4%")
      },
      "image": "image/items/lion_ring_epic.png",
      "rarity": {
        "common": _("Increases damage to bosses +[x]"),
        "great": "",
        "rare": _("[Rare] Crit Damage +20%"),
        "epic": _("[Epic] Attack +5%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Holy Touch' Damage +8%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Boss Damage Resistance +5%"),
        "mythic+1": _("[Mythic+1] Ring Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Damage Boss Units +10%"),
        "titan_tales+1": _("[Titan Tales+1] Ring Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Ring Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (+7%)"),
        "chaos": _("[Chaos] Increases ranged damage")
      }
    },
    "Dragon_Ring": {
      "displayName": _("Dragon Ring"),
      "description": _("Contains draconic power, and increases attack effects on Hero Mode monsters."),
      "hidden_stats": {},
      "image": "image/items/dragon_ring_epic.png",
      "rarity": {
        "common": _("Deals damage to elite enemies +[x]"),
        "great": "",
        "rare": _("[Rare] Projectile Resistance +12%"),
        "epic": _("[Epic] Crit Chance +6%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] MP Strength +20%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Damage dealt to Humanoid enemies +15%"),
        "mythic+1": _("[Mythic+1] Ring Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+8%)"),
        "titan_tales": _("[Titan Tales] Damage Elite Units +12%"),
        "titan_tales+1": _("[Titan Tales+1] Ring Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Ring Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (+22%)"),
        "chaos": _("[Chaos] Increases Movement Speed")
      }
    },
    "Vilebat_Ring": {
      "displayName": _("Vilebat Ring"),
      "description": _("Contains the ability of vampiric bats, and increases attack effects on Normal Mode monsters."),
      "hidden_stats": {
        "1": _("[Epic] Heals 0.7% HP per mob kill and 7% per boss kill"),
        "2": _("[Mythic+2] Heals 0.9% HP per mob kill and 10% per boss kill"),
        "3": _("[Chaos] Heals 1.2% HP per mob kill and 13.3% per boss kill")
      },
      "image": "image/items/vilebat_ring_epic.png",
      "rarity": {
        "common": _("Increases damage to normal enemies +[x]"),
        "great": "",
        "rare": _("[Rare] Healing Effect of Red Heart +20%"),
        "epic": _("[Epic] Killing enemies restores HP. Heal is stronger for boss kills"),
        "perfect_epic": "",
        "legendary": _("[Legendary] HP drops +20%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Collision Damage Resistance +15%"),
        "mythic+1": _("[Mythic+1] Ring Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Damage Normal Units +10%"),
        "titan_tales+1": _("[Titan Tales+1] Ring Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Ring Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (+22%)"),
        "chaos": _("[Chaos] HP Gain's Healing is more effective.")
      }
    },
    "Agile_Locket": {
      "displayName": _("Agile Locket"),
      "description": _("Locket created with agility to dodge enemies easily."),
      "hidden_stats": {},
      "image": "image/items/agile_locket.png",
      "rarity": {
        "common": _("Max HP +[x]<br>When HP is lower than 20%, Dodge increases by y %."),
        "great": "",
        "rare": "",
        "epic": _("[Epic] Chance of Angel's Healing x2 +30%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Max HP +4%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Dodge +6%"),
        "mythic+1": _("[Mythic+1] Locket Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+40%)"),
        "titan_tales": _("[Titan Tales] Angel HP restored +30%"),
        "titan_tales+1": _("[Titan Tales+1] Locket Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Locket Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] While moving, increases self Dodge.")
      }
    },
    "Iron_Locket": {
      "displayName": _("Iron Locket"),
      "description": _("Locket engraved with iron to reduce damage from contact with enemies."),
      "hidden_stats": {},
      "image": "image/items/iron_locket.png",
      "rarity": {
        "common": _("Max HP +[x]<br>When HP is lower than 20%, Damage dealt by bumping into enemies is reduced by y %."),
        "great": "",
        "rare": "",
        "epic": _("[Epic] Chance of Angel's Healing x2 +30%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Max HP +4%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Collision damage resistance +8%"),
        "mythic+1": _("[Mythic+1] Locket Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+40%)"),
        "titan_tales": _("[Titan Tales] Angel HP restored +30%"),
        "titan_tales+1": _("[Titan Tales+1] Locket Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Locket Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Gain Attack for a short duration when taking Collision Damage")
      }
    },
    "Angel_Locket": {
      "displayName": _("Angel Locket"),
      "description": _("Locket blessed by the angels to be invincible in times of dispair."),
      "hidden_stats": {},
      "image": "image/items/angel_locket.png",
      "rarity": {
        "common": _("Max HP +[x]<br>There's a y% chance to revive and be invincible for t seconds when dying; available once only."),
        "great": "",
        "rare": "",
        "epic": _("[Epic] Chance of Angel's Healing x2 +30%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Max HP +4%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Chance to Revive +5%"),
        "mythic+1": _("[Mythic+1] Locket Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+40%)"),
        "titan_tales": _("[Titan Tales] Angel HP restored +30%"),
        "titan_tales+1": _("[Titan Tales+1] Locket Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Locket Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Chance to get a random number of Red Hearts when angel restores your HP.")
      }
    },
    "Bulletproof_Locket": {
      "displayName": _("Bulletproof Locket"),
      "description": _("Locket crafted with bulletproof in mind to reduce projectile damage."),
      "hidden_stats": {},
      "image": "image/items/bulletproof_locket.png",
      "rarity": {
        "common": _("Max HP +[x]<br>Projectile damage decreased y % when HP is lower than 20%."),
        "great": "",
        "rare": "",
        "epic": _("[Epic] Chance of Angel's Healing x2 +30%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Max HP +4%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Projectile Resistance +8%"),
        "mythic+1": _("[Mythic+1] Locket Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+40%)"),
        "titan_tales": _("[Titan Tales] Angel Healing +30%"),
        "titan_tales+1": _("[Titan Tales+1] Locket Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Locket Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (+12%)"),
        "chaos": _("[Chaos] Gain Attack Speed for a short duration when taking projectile Damage.")
      }
    },
    "Bloodthirsty_Locket": {
      "displayName": _("Bloodthirsty Locket"),
      "description": _("An engraved locket which allows you to restore HP after kill."),
      "hidden_stats": {},
      "image": "image/items/bloodthirsty_locket.png",
      "rarity": {
        "common": _("Max HP +[x]<br>Can recover HP on kills when HP is lower than y%"),
        "great": "",
        "rare": "",
        "epic": _("[Epic] HP drops +20%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Max HP +4%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Enhanced Recovery Effects of Bloodthirst"),
        "mythic+1": _("[Mythic+1] Locket Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+28%)"),
        "titan_tales": _("[Titan Tales] Healing Effect of Red Heart +20%"),
        "titan_tales+1": _("[Titan Tales+1] Locket Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Locket Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] The more HP restored from Bloodthirst, the higher the Hero's Attack")
      }
    },
    "Piercer_Locket": {
      "displayName": _("Piercer Locket"),
      "description": _("An engraved locket which allows you to climb over walls."),
      "hidden_stats": {},
      "image": "image/items/piercer_locket.png",
      "rarity": {
        "common": _("Max HP +[x]<br>Can penetrate walls when HP is lower than y%"),
        "great": "",
        "rare": "",
        "epic": _("[Epic] HP drops +20%"),
        "perfect_epic": "",
        "legendary": _("[Legendary]  Max HP +4%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Movement Speed +3%"),
        "mythic+1": _("[Mythic+1] Locket Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+28%)"),
        "titan_tales": _("[Titan Tales] Healing Effect of Red Heart +20%"),
        "titan_tales+1": _("[Titan Tales+1] Locket Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Locket Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded (+5%)"),
        "chaos": _("[Chaos] While nearby a wall, takes less damage. ")
      }
    },
    "Counterattack_Charm": {
      "displayName": _("Counterattack Charm"),
      "description": _("Etched with a Counterattack. Performs Counterattacks on enemies each time damage is taken."),
      "hidden_stats": {},
      "image": "image/items/counterattack_locket.png",
      "rarity": {
        "common": _("Max HP +[x]"),
        "great": "",
        "rare": _("[Rare] x% chance to counter (increases with quality) enemies after taking damage (does 5x the damage taken to the enemy)"),
        "epic": _("[Epic] More Hearts equal better recovery effect, up to 100%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Max HP +5%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Counterattack damage to bosses is increased by 120%."),
        "mythic+1": _("[Mythic+1] Locket Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Counterattack Rate +15%"),
        "titan_tales+1": _("[Titan Tales+1] Locket Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Locket Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] The more HP lost, the higher the reflected damage")
      }
    },
    "Thunder_Bracelet": {
      "displayName": _("Thunder Bracelet"),
      "description": _("Bracelet containing thunder, bring down their wrath upon enemies."),
      "hidden_stats": {},
      "image": "image/items/thunder_bracelet.png",
      "rarity": {
        "common": _("Attack +[x]<br>Deals y times random Lightning damage to nearby enemies; damage amount is random too."),
        "great": "",
        "rare": "",
        "epic": _("[Epic] Crit Damage +15%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Attack +4%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Elemental Lightning damage increased"),
        "mythic+1": _("[Mythic+1] Bracelet Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+20%)"),
        "titan_tales": _("[Titan Tales] Attack +8%"),
        "titan_tales+1": _("[Titan Tales+1] Bracelet Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Bracelet Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Upon Killing an enemy, increases self lightning Damage.")
      }
    },
    "Frozen_Bracelet": {
      "displayName": _("Frozen Bracelet"),
      "description": _("Bracelet containing ice, freeze enemies on the spot."),
      "hidden_stats": {},
      "image": "image/items/frozen_bracelet.png",
      "rarity": {
        "common": _("Attack +[x]<br>Randomly freezes y enemies for t seconds."),
        "great": "",
        "rare": "",
        "epic": _("[Epic] Crit Damage +15%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Attack +4%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Elemental Freezing damage increased"),
        "mythic+1": _("[Mythic+1] Bracelet Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+20%)"),
        "titan_tales": _("[Titan Tales] Attack +8%"),
        "titan_tales+1": _("[Titan Tales+1] Bracelet Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Bracelet Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Upon Killing an enemy, increases self ice Damage.")
      }
    },
    "Blazing_Bracelet": {
      "displayName": _("Blazing Bracelet"),
      "description": _("Bracelet containing fire, burn enemies while they live."),
      "hidden_stats": {},
      "image": "image/items/blazing_bracelet.png",
      "rarity": {
        "common": _("Attack +[x]<br>Burns y enemies lasting t seconds."),
        "great": "",
        "rare": "",
        "epic": _("[Epic] Crit Damage +15%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Attack +4%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Elemental Fire damage increased"),
        "mythic+1": _("[Mythic+1] Bracelet Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+20%)"),
        "titan_tales": _("[Titan Tales] Attack +8%"),
        "titan_tales+1": _("[Titan Tales+1] Bracelet Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Bracelet Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Upon Killing an enemy, increases self fire Damage.")
      }
    },
    "Split_Bracelet": {
      "displayName": _("Split Bracelet"),
      "description": _("Bracelet containing a copy, brings out a copy when fighting enemies."),
      "hidden_stats": {},
      "image": "image/items/split_bracelet.png",
      "rarity": {
        "common": _("Attack +[x]<br>Summons y copy to help battle, lasting t seconds."),
        "great": "",
        "rare": "",
        "epic": _("[Epic] Crit Damage +15%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Summoned Creature Damage +15%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] The lower the HP, the higher the clones attack"),
        "mythic+1": _("[Mythic+1] Bracelet Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+20%)"),
        "titan_tales": _("[Titan Tales] Attack +8%"),
        "titan_tales+1": _("[Titan Tales+1] Bracelet Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Bracelet Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] While nearby a summoned creature, increases hero's Attack.")
      }
    },
    "Invincible_Bracelet": {
      "displayName": _("Invincible Bracelet"),
      "description": _("A bracelet which triggers an invincible star when enemies appear."),
      "hidden_stats": {
        "1": _("[Mythic] +30% Critical Damage when Invincibility trigger"),
        "2": _("[Titan Tales+3] +55% Critical Damage when Invincibility trigger")
      },
      "image": "image/items/invincible_bracelet.png",
      "rarity": {
        "common": _("Attack +[x]<br>Be protected by Invincible Star lasting t seconds when encountering enemies."),
        "great": "",
        "rare": "",
        "epic": _("[Epic] Attack +6%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Own buff duration extended +7%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] When the bracelet triggers Invincible, Crit Damage is increased"),
        "mythic+1": _("[Mythic+1] Bracelet Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+8%)"),
        "titan_tales": _("[Titan Tales] Attack +10%"),
        "titan_tales+1": _("[Titan Tales+1] Bracelet Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Bracelet Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Greatly increases Attack Speed when invincible shield is active")
      }
    },
    "Quickshot_Bracelet": {
      "displayName": _("Quickshot Bracelet"),
      "description": _("A bracelet which magically shoots multiple arrows when enemies appear."),
      "hidden_stats": {},
      "image": "image/items/quickshot_bracelet.png",
      "rarity": {
        "common": _("Attack +[x]<br>Shoot more arrows continuously lasting t seconds encountering enemies."),
        "great": "",
        "rare": "",
        "epic": _("[Epic] Attack +6%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Projectile flight speed +6%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Projectiles travel faster"),
        "mythic+1": _("[Mythic+1] Bracelet Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+8%)"),
        "titan_tales": _("[Titan Tales] Attack +10%"),
        "titan_tales+1": _("[Titan Tales+1] Bracelet Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Bracelet Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Upon Critical Hit, there is a chance to follow up with a shot.")
      }
    },
    "Shield_Bracelet": {
      "displayName": _("Shield Bracelet"),
      "description": _("Bracelet inscribed with Shield Guard, used to protect oneself when enemies appear."),
      "hidden_stats": {},
      "image": "image/items/shield_bracelet.png",
      "rarity": {
        "common": _("Attack +[x]<br>Gain x-y Shield Guards that add damage for t seconds in battle.<br>Gain Crit Rate when blocking shots."),
        "great": "",
        "rare": "",
        "epic": _("[Epic] Attack +7%"),
        "perfect_epic": "",
        "legendary": _("[Legendary] Shield Size +25%"),
        "ancient_legendary": "",
        "mythic": _("[Mythic] Chance to gain Shield Guard after a Crit hit"),
        "mythic+1": _("[Mythic+1] Bracelet Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded (+9%)"),
        "titan_tales": _("[Titan Tales] Attack +12%"),
        "titan_tales+1": _("[Titan Tales+1] Bracelet Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Bracelet Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Increases shield spin speed, Shield also deals damage")
      }
    },
    "Arcane_Archer": {
      "displayName": _("Arcane Archer"),
      "description": _("A book that has all powers and experiences of an Archer. Use it to get an active Ultimate skill."),
      "hidden_stats": {},
      "image": "image/items/arcane_archer.png",
      "rarity": {
        "common": _("Increases projectile frequency and own attack<br>Max HP +[x]<br>Attack +[y] (ULT)"),
        "great": _("[Great] Attack Speed +10% (ULT)"),
        "rare": _("[Rare] Side Arrow +1 (ULT)"),
        "epic": _("[Epic] Front Arrow +1 (ULT)"),
        "perfect_epic": _("[Perfect Epic] Rear Arrow +1 (ULT)"),
        "legendary": _("[Legendary] Time Span +1.2seconds (ULT)"),
        "ancient_legendary": _("[Ancient Legendary] Crit Damage +25% (ULT)"),
        "mythic": _("[Mythic] Time Span +1"),
        "mythic+1": _("[Mythic+1] Spellbook Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Enhance equipment +8.5%"),
        "titan_tales+1": _("[Titan Tales+1] Spellbook Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Spellbook Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Upon a Critical hit, there is a chance to increase bullet count for a while.")
      }
    },
    "Art_of_Combat": {
      "displayName": _("Art of Combat"),
      "description": _("A book containing the arts of powerful combat. Use it to get an auto Ultimate skill."),
      "hidden_stats": {},
      "image": "image/items/art_of_combat.png",
      "rarity": {
        "common": _("Increased projectile knockback effect when full<br>Max HP +[x]<br>Attack +[y] (ULT)"),
        "great": _("[Great] Increases projectile knockback effect (ULT)"),
        "rare": _("[Rare] Power Speed +25% (ULT)"),
        "epic": _("[Epic] Increases projectile speed (ULT)"),
        "perfect_epic": _("[Perfect Epic] Attack Speed +25% (ULT)"),
        "legendary": _("[Legendary] Attack contains Random Elemental (ULT)"),
        "ancient_legendary": _("[Ancient Legendary] Crit Chance +15% (ULT)"),
        "mythic": _("[Mythic] Max HP +8%"),
        "mythic+1": _("[Mythic+1] Spellbook Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Enhance equipment +8.5%"),
        "titan_tales+1": _("[Titan Tales+1] Spellbook Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Spellbook Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] For a while after taking damage, Crit chance is increased.")
      }
    },
    "Ice_Realm": {
      "displayName": _("Ice Realm"),
      "description": _("A book containing powerful Frost magic. Use it to get an active Ultimate skill."),
      "hidden_stats": {},
      "image": "image/items/ice_realm.png",
      "rarity": {
        "common": _("Freezes surrounding enemies and increases own attack<br>Max HP +[x]<br>(ULT.) Attack +[x]"),
        "great": _("[Great] Attack Speed +20% (ULT)"),
        "rare": _("[Rare] Power Speed +[x]% (ULT)"),
        "epic": _("[Epic] Frost Damage +[x] (ULT)<br>Frost area increased by 100% (ULT)"),
        "perfect_epic": _("[Perfect Epic] Time Span +[t] seconds (ULT)"),
        "legendary": _("[Legendary] Crit Chance +20% (ULT)"),
        "ancient_legendary": _("[Ancient Legendary] Initial Power +35% (ULT)"),
        "mythic": _("[Mythic] When used, it may return 50% of the power (ULT.)"),
        "mythic+1": _("[Mythic+1] Spellbook Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Enhance equipment +8.5%"),
        "titan_tales+1": _("[Titan Tales+1] Spellbook Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Spellbook Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] For a while after taking damage, attack inflict Freeze")
      }
    },
    "Enlightenment": {
      "displayName": _("Enlightenment"),
      "description": _("A book with magic that will help you learn new skills in battle. Use it to get an auto Ultimate skill."),
      "hidden_stats": {},
      "image": "image/items/enlightenment.png",
      "rarity": {
        "common": _("Grant a new skill when full<br>Max HP +[x]<br>Power Speed +[y] (ULT)"),
        "great": _("[Great] Collision Damage Resistance +5%"),
        "rare": _("[Rare] Projectile Damage Resistance +5%"),
        "epic": _("[Epic] Multi-Skill +1 (ULT)"),
        "perfect_epic": _("[Perfect Epic] Initial Power +40% (ULT)"),
        "legendary": _("[Legendary] Multi-Skill +1 (ULT)"),
        "ancient_legendary": _("[Ancient Legendary] Max HP +7%"),
        "mythic": _("[Mythic] Battle XP Gain +8%"),
        "mythic+1": _("[Mythic+1] Spellbook Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Enhance equipment +8.5%"),
        "titan_tales+1": _("[Titan Tales+1] Spellbook Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Spellbook Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] When HP is below 50%, upgrade speed +25%")
      }
    },
    "Giants_Contract": {
      "displayName": _("Giants Contract"),
      "description": _("The contract with 7 Giants, allowing the user the power of the Giants. Wear it to get an auto skill"),
      "hidden_stats": {},
      "image": "image/items/giants_contract.png",
      "rarity": {
        "common": _("Once the energy is fully charged, transform with the Courage Giant power<br>Max HP +[x]<br>Attack +[y] (ULT)"),
        "great": _("[Great] Crit Damage +[z] (ULT)<br>[Great] Wild Giant - Deals collision damage to enemy (ULT)"),
        "rare": _("[Rare] Stone Giant - Defence increased greatly (ULT)"),
        "epic": _("[Epic] Sword Giant - Receive all spinning sword skills (ULT)"),
        "perfect_epic": _("[Perfect Epic] Flaming Giant - Leaves behind a blaze when moving (ULT)"),
        "legendary": _("[Legendary] Gale Giant - Increased movement and attack speed (ULT)"),
        "ancient_legendary": _("[Ancient Legendary] Bolt Giant - Surrounding enemies will be hit by lightning (ULT)"),
        "mythic": _("[Mythic] Rage Giant - Skill can be released earlier if losing HP (ULT.)"),
        "mythic+1": _("[Mythic+1] Spellbook Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Enhance equipment +11%"),
        "titan_tales+1": _("[Titan Tales+1] Spellbook Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Spellbook Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Ult. energy cost -15%.")
      }
    },
    "Spectre_Book": {
      "displayName": _("Spectre Book"),
      "description": _("Holds the magic of the undead; you can use it to summon undead soldiers. Wear it to get an active skill."),
      "hidden_stats": {},
      "image": "image/items/spectre_book.png",
      "rarity": {
        "common": _("Summon undead enemies to help you battle<br>Max HP +[x]<br>Attack +[y] (ULT)<br>Undead Attack +[z] (ULT)"),
        "great": _("[Great] Higher the quality, the faster the release (ULT)"),
        "rare": _("[Rare] Higher the quality, the longer the duration (ULT)"),
        "epic": _("[Epic] Summon new warrior - Flame Mage (ULT)"),
        "perfect_epic": _("[Perfect Epic] Enter a short state of Rage"),
        "legendary": _("[Legendary] Summon an Ultimate warrior - Skeleton King (ULT)"),
        "ancient_legendary": _("[Ancient Legendary] Kill enemies to extend summon time (ULT)"),
        "mythic": _("[Mythic] When the undead disappears, it may drop a heart (ULT)"),
        "mythic+1": _("[Mythic+1] Spellbook Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Enhance equipment +11%"),
        "titan_tales+1": _("[Titan Tales+1] Spellbook Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Spellbook Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] Enhances Attack and duration of Undead allies.")
      }
    },
    "Arcanum_of_Time": {
      "displayName": _("Arcanum of Time"),
      "description": _("Perceive the mysteries of time that let you slow or speed up time. Gain an active Ultimate skill when equipped"),
      "hidden_stats": {
        "1": _("Recovers 1.5% HP for 3s after ULT ends.")
      },
      "image": "image/items/arcanum_of_time.png",
      "rarity": {
        "common": _("Max HP +[x]<br>(ULT.) Attack +[x]"),
        "great": _("[Great] Slow effect +[x]% (ULT)<br>[Great] Slow: Enemy attacks and movement are slowed (ULT)"),
        "rare": _("[Rare] Gain Crit Rate (ULT)"),
        "epic": _("[Epic] Effect range doubled. Ultimate skill duration increased (ULT)"),
        "perfect_epic": _("[Perfect Epic] Haste: Gain Crit Rate, increased buff duration and summoned creature duration (ULT)"),
        "legendary": _("[Legendary] Haste: Speed of attacks, movement, spins, shots, magic casts increased (ULT)"),
        "ancient_legendary": _("[Ancient Legendary] Manipulate Time: Reduces continuous damage intervals on enemies. Increases enemy debuff duration (ULT)"),
        "mythic": _("[Mythic] Greatly increase damage immunity after taking damage. Effect reduces time (ULT)"),
        "mythic+1": _("[Mythic+1] Spellbook Basic Stats +5%"),
        "mythic+2": _("[Mythic+2] Epic Skill Effect Upgraded"),
        "titan_tales": _("[Titan Tales] Enhance equipment +13.5%"),
        "titan_tales+1": _("[Titan Tales+1] Spellbook Basic Stats +10%"),
        "titan_tales+2": _("[Titan Tales+2] Spellbook Basic Stats +10%"),
        "titan_tales+3": _("[Titan Tales+3] Mythic Skill Effect Upgraded"),
        "chaos": _("[Chaos] When HP is below 20%, nearby bullets are slowed.")
      }
    }
  },
  "HeroData": {
    "Atreus": {
      "displayName": _("Atreus"),
      "description": _("A rookie archer on his way to become an archer hero"),
      "base_atk": "150 [+8]",
      "base_hp": "600 [+25]",
      "attributes": {
        "20": _("Max HP +100"), 
        "40": _("Damage to Ranged Units +15%"),
        "60": _("Max HP +4%"),
        "80": _("Attack Speed +5%"),
        "120": _("Projectile Resistance +7%")
      },
      "price": _("Free"),
      "skill": _("Once 3rd star is reached, give +1 Max in-game level"),
      "skill_details": "",
      "star": {
        "1": _("Patrol Gold Earnings +[x]%"),
        "2": _("Attack +30 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Skill - Growth: Acquire a new skill - Growth"),
        "4": _("Trait - Stubborn: When HP is lower than 20%, HP is restored for a while"),
        "5": _("Spirit - Upgrade: During Spirit's crit attack, Atreus's attack speed is increased for a while"),
        "6": _("Growth - Insight: Upgrade speed and Heart droprate increased"),
        "7": _("Max HP +800 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Max HP +5% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Atreus's base Attack +5%"),
        "20": _("Attack +80"),
        "30": _("Battle XP gain +20%"),
        "30_1": _("Battle XP gain +10%"),
        "40": _("Attack +2%"),
        "50": _("Atreus's base HP +10%"),
        "60": _("Attack Speed +5%"),
        "70": _("Bounces +1"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Max Hp +5%")
      },
      "hero_assist_evolve":"everlife-trialstone.svg",
      "list_hero_assist": ["Urasil", "Phoren", "Taranis", "Helix", "Ayana", "Onir", "Lina", "Iris"],
      "skins" :[]
    },
    "Urasil": {
      "displayName": _("Urasil"),
      "description": _("Proficient in the study of Medicine, an invisible killer allowing him to be skilled in Poison."),
      "base_atk": "120 [+9]",
      "base_hp": "550 [+30]",
      "attributes": {
        "20": _("Attack +40"),
        "40": _("Damage to Melee Units +15%"),
        "60": _("Crit Damage +15%"),
        "80": _("Max HP +6%"),
        "120": _("Damage to Melee Units +9%")
      },
      "price": _("Free (Unlocked after clearing stage 50 from chapter 2)"),
      "skill": _("Your attacks cause an enhanced Poison effect"),
      "skill_details": _("40% of base damage per second"),
      "star": {
        "1": _("Patrol Ring Scroll Earnings +[x]%"),
        "2": _("Max HP +120 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Poison - Feeble: Enemy movement speed reduced 10% when poisoned"),
        "4": _("Trait - Low-key: Toxic damaged +35% after killing enemy for a while"),
        "5": _("Spirit - Upgrade: Whenever an enemy dies of poison, Spirit's attack is increased by a little"),
        "6": _("Poison - Lethal: Toxic attack, chance to deal 3x more damage"),
        "7": _("Crit Chance +2% <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Healing Effect of Red Heart +7% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Urasil's base Attack +5%"),
        "20": _("Max Hp +320"),
        "30": _("Attack increased for short time when enemies are killed by Poison"),
        "30_1": _("Poison damage +15%"),
        "40": _("Damage to ground Units +4%"),
        "50": _("Urasil's base HP +10%"),
        "60": _("Poison Resistance +15%"),
        "70": _("Poison slows Movement speed"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Poison Damage +10%")
      },
      "hero_assist_evolve":"everlife-trialstone.svg",
      "list_hero_assist": ["Atreus", "Phoren", "Taranis", "Bonnie", "Sylvan", "Lina", "Melinda", "Stella"],
      "skins" :[
        {
          "name": _("Royal Knight"),
          "src": "Royal_Knight",
          "passiv_boost": _("[Lvl 30]: Max HP +150"),
          "activ_boost": _("15% chance to resist long-distance damage"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/purple_ticket.svg' width='18' height='18'></object> 55")
        },
        {
          "name": _("Black Order"),
          "src": "Black_Order",
          "passiv_boost": _("[Lvl 30]: Max HP +150"),
          "activ_boost": _("When HP is lower than 25%, Poison damage increased 100%"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/purple_ticket.svg' width='18' height='18'></object> 60")
        }
      ]
    },
    "Phoren": {
      "displayName": _("Phoren"),
      "description": _("Born from Fire, and Fire answers to no one but him."),
      "base_atk": "130 [+9]",
      "base_hp": "500 [+35]",
      "attributes": {
        "20": _("Critical Chance +2%"), 
        "40": _("Projectile Resistance: +15%"),
        "60": _("Critical Chance +2%"),
        "80": _("Critical Chance +5%"),
        "120": _("Damage to Ranged Units +9%")
      },
      "price": _("50,000 <object type='image/png' data='/static/image/svg/gold.svg' width='16' height='16'></object> or 30 Phoren Shards"),
      "skill": _("Your attacks cause an enhanced Flame effect"),
      "skill_details": "",
      "star": {
        "1": _("Patrol Sapphires Earnings +[x]%"),
        "2": _("Damage to Airborne Units +75 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Red Flame - Super Fire: Fire damage is increased"),
        "4": _("Trait - Passion: When entering a room, a random enemy will be ignited"),
        "5": _("Spirit - Upgrade: Extra damage is dealt when Spirit attacks burning enemy"),
        "6": _("Red Flame - Flame Star: Enemies that are burning will cause reduced damage to hero"),
        "7": _("Attack +200 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Ground Units damage reduced +6% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Phoren's base Attack +5%"),
        "20": _("Damage to Airborne Units +150"),
        "30": _("Attack increased for short time when enemies are killed by Fire"),
        "30_1": _("Flame Damage +10%"),
        "40": _("Damage to Melee Units +4%"),
        "50": _("Phoren's base HP +10%"),
        "60": _("Flame Resistance +15%"),
        "70": _("Fire lowers Attack"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Flame Damage +10%")
      },
      "hero_assist_evolve":"everlife-trialstone.svg",
      "list_hero_assist": ["Atreus", "Urasil", "Taranis", "Ayana", "Bonnie", "Sylvan", "Iris", "Stella"],
      "skins" :[
        {
          "name": _("Flame Student"),
          "src": "Flame_Student",
          "passiv_boost": _("[Lvl 30]: Attack +40"),
          "activ_boost": _("Flame damage can reduce enemy movement speed, lasting 5s"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/purple_ticket.svg' width='18' height='18'></object> 20")
        },
        {
          "name": _("Brawler"),
          "src": "Brawler",
          "passiv_boost": _("[Lvl50] Attack +85"),
          "activ_boost": _("Chance to instakill enemies. Enemies explode when taking Fire damage over time."),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Taranis": {
      "displayName": _("Taranis"),
      "description": _("Born of the Thunder, and naturally able to control and wield Thunder."),
      "base_atk": "130 [+10]",
      "base_hp": "550 [+40]",
      "attributes": {
        "20": _("Crit Chance +2%"), 
        "40": _("Damage to Airborne Units +20%"),
        "60": _("Attack +4%"),
        "80": _("Crit Damage +50%"),
        "120": _("Damage to Airborne Units +9%")
      },
      "price": _("1000 <object type='image/png' data='/static/image/svg/gem.svg' width='16' height='16'></object> or 30 Taranis Shards"),
      "skill": _("Your attacks cause an enhanced Lightning effect"),
      "skill_details": "",
      "star": {
        "1": _("Patrol XP Earnings +[x]%"),
        "2": _("Max HP +150 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Thunderstorm - Distance: Lightning range increased"),
        "4": _("Trait - Rapid: Hitting the enemy continuously will gradually increase movement speed"),
        "5": _("Spirit - Upgrade: Attacks have a Lightning Element in the first 15s after entering a room"),
        "6": _("Thunderstorm - Damage: Lightning damage increased by 20%"),
        "7": _("Damage to Airborne Units +300 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Airborne Units Damage Resistance +7% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Taranis's base Attack +5%"),
        "20": _("Max Hp +400"),
        "30": _("Attack increased for short time when enemies are killed by Lightning"),
        "30_1": _("Lightning Damage +15%"),
        "40": _("Damage to Ranged Units +5%"),
        "50": _("Taranis's base HP +10%"),
        "60": _("Lightning Damage Resistance +15%"),
        "70": _("Lightning lowers Attack"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Lightning Damage +10%")
      },
      "hero_assist_evolve":"everlife-trialstone.svg",
      "list_hero_assist": ["Urasil", "Phoren", "Ayana", "Sylvan", "Shingen", "Blazo", "Stella"],
      "skins" :[
        {
          "name": _("Thunder Lord"),
          "src": "Thunder_Lord",
          "passiv_boost": _("[Lvl 30]: Max HP +200"),
          "activ_boost": _("When moving, chance to deal Lightning damage to nearby enemies each sec"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/purple_ticket.svg' width='18' height='18'></object> 100")
        },
        {
          "name": _("Phoenixier"),
          "src": "Phoenixier",
          "passiv_boost": _("[Lvl 60]: Max HP +320"),
          "activ_boost": _("Gain the Phoenix's blessing, increasing Movement Speed, Attack Speed, and Dodge. Attacks are imbued with fire for every 20 enemies hit."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 50")
        },
        {
          "name": _("Pharaoh Taranis"),
          "src": "Pharaoh_Taranis",
          "passiv_boost": _("[Lvl 60]: Max HP +500"),
          "activ_boost": _("The lower the HP, the higher the lightning damage. When HP is below 25%, golden hammers will hurled repeatedly."),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Helix": {
      "displayName": _("Helix"),
      "description": _("A tribe warrior, a hunter; even the strong admire his power!"),
      "base_atk": "125 [+10]",
      "base_hp": "620 [+43]",
      "attributes": {
        "20": _("Crit Damage +20%"), 
        "40": _("Healing Effect of Red Heart +20%"),
        "60": _("Max HP +5%"),
        "80": _("Crit Chance +5%"),
        "120": _("Healing Effect +10%")
      },
      "price": _("1500 <object type='image/png' data='/static/image/svg/gem.svg' width='16' height='16'></object> or 30 Helix Shards"),
      "skill": _("Your attacks deal more damage at low HP."),
      "skill_details": _("Fury Command: +1.2% attack for every 1% of player HP lost."),
      "star": {
        "1": _("Patrol Gold Earnings +[x]%"),
        "2": _("Attack +40 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Rage - Fury: When losing HP, attack is increased (Increase up to x1.3% per 1% health lost)"),
        "4": _("Trait - Irritant: After losing HP, damage is increased on next attack"),
        "5": _("Spirit - Upgrade: Spirit has faster attack speed"),
        "6": _("Rage - Nimble: When HP is lower than 25%, movement speed increased slightly"),
        "7": _("Damage to Ranged Units +300 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Ranged Units Damage Resistance +8% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Helix's base Attack +5%"),
        "20": _("Attack +120"),
        "30": _("Attack Speed increased for a short time after taking damage"),
        "30_1": _("Attack +4%"),
        "40": _("Damage to Bosses +5%"),
        "50": _("Helix's base HP +10%"),
        "60": _("Healing Effect of Red Heart +10%"),
        "70": _("When HP is below 10%, gain invincibility shield for 2s"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Healing Effect of Red Heart +8%")
      },
      "hero_assist_evolve":"everlife-trialstone.svg",
      "list_hero_assist": ["Atreus", "Meowgik", "Shari", "Ophelia", "Shingen", "Gugu", "Bobo", "Elaine", "Taiga"],
      "skins" :[
        {
          "name": _("Bear Master"),
          "src": "Bear_Master",
          "passiv_boost": _("[Lvl 50]: Attack +60"),
          "activ_boost": _("5% increased damage to enemies on foot"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/purple_ticket.svg' width='18' height='18'></object> 120")
        },
        {
          "name": _("Coast Guard"),
          "src": "Coast_Guard",
          "passiv_boost": _("[Lvl 30]: Attack +60"),
          "activ_boost": _("When near water, attack & movement speed increase"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/purple_ticket.svg' width='18' height='18'></object> 120")
        },
        {
          "name": _("Sweetheart Teddy"),
          "src": "Sweetheart_Teddy",
          "passiv_boost": _("[Lvl 50]: Max HP +600"),
          "activ_boost": _("Hitting enemies has a chance to freeze or burn them."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 100")
        },
        {
          "name": _("Zombies Incoming"),
          "src": "Zombies_Incoming",
          "passiv_boost": _("[Lvl 30] Attack +60"),
          "activ_boost": _("Chance to Headshot when own HP is lower than 30%."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 100")
        },
        {
          "name": _("Netherwolf"),
          "src": "Netherwolf",
          "passiv_boost": _("[Lvl 70] Max HP +800"),
          "activ_boost": _("Increases Movement Speed. When HP drops below 30%, temporarily enter Netherwolf mode, increasing Movement Speed, Attack Speed, Melee Attack and Elemental Damage Resistance"),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Meowgik": {
      "displayName": _("Meowgik"),
      "description": _("The spirit of the cat combined with magic; not to be underestimated."),
      "base_atk": "135 [+11]",
      "base_hp": "550 [+40]",
      "attributes": {
        "20": _("Attack +50"), 
        "40": _("Dodge +5%"),
        "60": _("Attack +4%"),
        "80": _("Healing Effect of Red Heart +30%"),
        "120": _("Dodge +3%")
      },
      "price": _("1800 <object type='image/png' data='/static/image/svg/gem.svg' width='16' height='16'></object> or 30 Meowgik Shards"),
      "skill": _("A chance to summon an auto-attacking kitty when attacking enemies"),
      "skill_details": "",
      "star": {
        "1": _("Patrol Spirit Scroll Earnings +[x]%"),
        "2": _("Healing Effect of Red Heart +10% <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Meow - Giant: Meowing increases, attack and attack range increased"),
        "4": _("Trait - Lazy: Crit rate increased after standing still"),
        "5": _("Spirit - Upgrade: Spirit's crit damage increased"),
        "6": _("Meow - Tracking: Meowspirit becomes better at tracking and has its Attack increased"),
        "7": _("Max HP +1000 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Dodge +7% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Meowgik's base Attack +5%"),
        "20": _("Damage to Melee Units +160"),
        "30": _("Meowspirits triggers projectile's special effects"),
        "30_1": _("All Meteor skills damage dealt"),
        "40": _("Damage to Mobs +5%"),
        "50": _("Meowgik's base HP +10%"),
        "60": _("Projectile Flight speed +10%"),
        "70": _("Chance to summon extra Meowspirits after taking damage"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Coins from battle +5%")
      },
      "hero_assist_evolve":"everlife-trialstone.svg",
      "list_hero_assist": ["Urasil", "Phoren", "Taranis", "Rolla", "Shade", "Helix", "Aquea", "Sylvan", "Taiga"],
      "skins" :[
        {
          "name": _("Cat Warlock"),
          "src": "Cat_Warlock",
          "passiv_boost": _("[Lvl 30]: Max HP +200"),
          "activ_boost": _("Dodge rate increased 5s after kill; the higher your level, the higher the dodge rate."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/purple_ticket.svg' width='18' height='18'></object> 120")
        },
        {
          "name": _("Cherry Kitty"),
          "src": "Cherry_Kitty",
          "passiv_boost": _("[Lvl 50]: Max HP +500"),
          "activ_boost": _("When dying there's a 20% chance to be resurrected in a random Meowspirit's location"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 105")
        },
        {
          "name": _("Holiday Kitty"),
          "src": "Holiday_Kitty",
          "passiv_boost": _("[Lvl 50]: Max HP +500"),
          "activ_boost": _("Collision damage reduced 20%, spinning Crabs can be used replace Tornado"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 100")
        },
        {
          "name": _("Chef Kitty"),
          "src": "Chef_Kitty",
          "passiv_boost": _("[Lvl 50] Max HP +600"),
          "activ_boost": _("Increases attack after Crit attack. Meowspirit has a chance to cause Fire damage."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 150")
        },
        {
          "name": _("Reindeer Meowgik"),
          "src": "Reindeer",
          "passiv_boost": _("[Lvl 70] Max HP +600"),
          "activ_boost": _("Chance for Gold Star to appear when attacking. Gold Stars can deal damage. 7 Gold Stars can turn into an invincible Star."),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Shari": {
      "displayName": _("Shari"),
      "description": _("Born of the magical woodlands, she is in touch with nature."),
      "base_atk": "135 [+10]",
      "base_hp": "550 [+35]",
      "attributes": {
        "20": _("Damage to Melee Units +150"), 
        "40": _("Max HP +300"),
        "60": _("Crit Chance +5%"),
        "80": _("Damage to Melee Units +5%"),
        "120": _("Max HP +8%")
      },
      "price": _("30 Shari Shards"),
      "skill": _(" Summons a thorned vine to attack enemies."),
      "skill_details": "",
      "star": {
        "1": _("Patrol Gold Earnings +[x]%"),
        "2": _("Max HP +120 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Entangle - Vine: Vine has increased attack"),
        "4": _("Trait - Active: When moving, dodge rate slightly increased"),
        "5": _("Spirit - Upgrade: When Spirit is near Vine, attack speed is increased"),
        "6": _("Entangle - Auto Track: Vines will follow and attack enemies"),
        "7": _("Damage to Melee Units +300 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Melee Units Damage Resistance +7% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Shari's base Attack +5%"),
        "20": _("Max Hp +400"),
        "30": _("Attack +10%"),
        "30_1": _("Stand around summoned creature to gain Attack"),
        "40": _("Deals Damage to normal enemies +5%"),
        "50": _("Shari's base HP +10%"),
        "60": _("Summoned creature damage +12%"),
        "70": _("Increase Damage Reduction when moving"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Damage to heroes +9%")
      },
      "hero_assist_evolve":"everlife-trialstone.svg",
      "list_hero_assist": ["Atreus", "Urasil", "Phoren", "Meowgik", "Bonnie", "Lina", "Melinda", "Stella"],
      "skins" :[
        {
          "name": _("Shaman Sacrifice"),
          "src": "Shaman_Sacrifice",
          "passiv_boost": _("[Lvl 30]: Max HP +150"),
          "activ_boost": _("When around vines, damage resistance is increased by 10%"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/purple_ticket.svg' width='18' height='18'></object> 40")
        },
        {
          "name": _("Tribe Chief"),
          "src": "Tribe_Chief",
          "passiv_boost": _("[Lvl 50]: Max HP +400"),
          "activ_boost": _("Each attack has a chance to summon a staff that casts powerful debuffs. 100% summon rate when taking damage"),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Ayana": {
      "displayName": _("Ayana"),
      "description": _("Hailing from a magical city, a witch with powerful magic!"),
      "base_atk": "160 [+11]",
      "base_hp": "550 [+42]",
      "attributes": {
        "20": _("Damage to Airborne Units +80"), 
        "40": _("Damage to Ranged Units +15%"),
        "60": _("Attack +4%"),
        "80": _("Dodge +10%"),
        "120": _("Damage to Ranged Units +9%")
      },
      "price": _("2500 <object type='image/png' data='/static/image/svg/gem.svg' width='16' height='16'></object> or 30 Ayana Shards"),
      "skill": _("Attacks can charm the enemy, with a chance to summon a portal"),
      "skill_details": _("Charm: Charmed enemies will receive additional damage with reduced movement speed and loss of health.<br><br><b>Additional Skill Notes:</b><br> • Applies a 'Charm' when targetting an enemy every 10 seconds, or applies it instantly when attacking an enemy.<br> • Deals 48% of non-modifiable base damage (includes rune ATK% boosts) for 2 ticks.<br> • The damage ticked increases by 0.4% of your base damage each time you level up, maximum of 49.6%.<br> • Creates a portal that lasts 5 seconds at a time until used."),
      "star": {
        "1": _("Patrol Locket Scroll Earnings +[x]%"),
        "2": _("Crit Damage +15% <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Witchcraft - Dodger: After leaving the portal, dodge rate increased by 75% for a while"),
        "4": _("Trait - Elegance: After using the portal, enemies around the portal will be Charmed"),
        "5": _("Spirit - Upgrade: Damage towards furthest enemies is increased"),
        "6": _("Witchcraft - Charm: Strengthen Charmed effect"),
        "7": _("Attack +250 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Damage to Bosses +7% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Ayana's base Attack +5%"),
        "20": _("Damage to ground Units +200"),
        "30": _("Increased Movement Speed after being teleported"),
        "30_1": _("Attack +10% being teleported"),
        "40": _("Deals Damage to elite enemies +5%"),
        "50": _("Ayana's base HP +10%"),
        "60": _("Increased damage to slowed enemies"),
        "70": _("Control Effect Duration +30%"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Damage to mobs +8%")
      },
      "hero_assist_evolve":"everlife-trialstone.svg",
      "list_hero_assist": ["Rolla", "Shade", "Ryan", "Lina", "Aquea", "Gugu", "Bobo", "Blazo"],
      "skins" :[
        {
          "name": _("Little Witch"),
          "src": "Little_Witch",
          "passiv_boost": _("[Lvl 30]: Attack +60"),
          "activ_boost": _("After being transported, collision damage is reduced by 25% within 3s"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/purple_ticket.svg' width='18' height='18'></object> 145")
        },
        {
          "name": _("Beach Dance"),
          "src": "Beach_Dance",
          "passiv_boost": _("[Lvl 30]: Attack +60"),
          "activ_boost": _("After each Charm, a small puddle is left which reduces enemy speed"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 100")
        },
        {
          "name": _("Enchantress"),
          "src": "Enchantress",
          "passiv_boost": _("[Lvl 50] Attack +110"),
          "activ_boost": _("Continuously charms nearby enemies."),
          "price": _("Obtained from Valentine's Day limited-time event. Price: cannot be purchased at the moment.")
        }
      ]
    },
    "Onir": {
      "displayName": _("Onir"),
      "description": _("The son of Light, possessing all the powers from the Light like his shiny hair."),
      "base_atk": "140 [+11]",
      "base_hp": "650 [+45]",
      "attributes": {
        "20": _("Max HP +200"), 
        "40": _("Damage to Ground Units +20%"),
        "60": _("Healing Effect of Red Heart +20%"),
        "80": _("Attack +6%"),
        "120": _("Damage to Ground Units +6%")
      },
      "price": _("$9.99 USD or 30 Onir Shards"),
      "skill": _("Your attacks cause an enhanced Holy effect"),
      "skill_details": "",
      "star": {
        "1": _("Patrol Weapon Scroll Earnings +[x]%"),
        "2": _("Max HP +200 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Aurora - Shine: Light repeatedly attacks enemies, with increased damage"),
        "4": _("Trait - Justice: When only one enemy remains, own crit rate is increased by 10%"),
        "5": _("Spirit - Upgrade: Attack speed and projectile speed increased"),
        "6": _("Aurora - Re-Shine: When enemy dies, another powerful light is released"),
        "7": _("Projectile Resistance +10% <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Damage to Mobs +7% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Onir's base Attack +5%"),
        "20": _("Max Hp +480"),
        "30": _("Crit Chance +8%"),
        "30_1": _("Holy damage increased. +1 holy projectile"),
        "40": _("Damage to Airborne Units +6%"),
        "50": _("Onir's base HP +10%"),
        "60": _("Holy touch projectiles can bounce"),
        "70": _("Gain extra boost when increasing Max HP"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Weapon Damage +6%")
      },
      "hero_assist_evolve":"immortal-trialstone.svg",
      "list_hero_assist": ["Phoren", "Meowgik", "Shari", "Rolla", "Sylvan", "Aquea", "Shingen", "Bobo", "Melinda"],
      "skins" :[
        {
          "name": _("Athenian Lord"),
          "src": "Athenian_Lord",
          "passiv_boost": _("[Lvl 30]: Max HP +250"),
          "activ_boost": _("Every 10s, Light stats damage is increased 10%, disappears at the end of battle"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/purple_ticket.svg' width='18' height='18'></object> 95")
        },
        {
          "name": _("This is Sparta"),
          "src": "This_is_Sparta",
          "passiv_boost": _("[Lvl 60]: Attack +75"),
          "activ_boost": _("Chance to throw shield when attacking. Fires lances at surrounding enemies when attacked."),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Rolla": {
      "displayName": _("Rolla"),
      "description": _("The goddess of Ice, wielder of the power of ice and snow with virtuous heart."),
      "base_atk": "170 [+12]",
      "base_hp": "500 [+40]",
      "attributes": {
        "20": _("Attack +60"), 
        "40": _("Collision Damage Resistence +20%"),
        "60": _("Attack +5%"),
        "80": _("Dodge +10%"),
        "120": _("Collision Damage Resistance +7%")
      },
      "price": _("$16.99 USD or 30 Rolla Shards"),
      "skill": _("Your attacks freeze enemies for a longer time"),
      "skill_details": "",
      "star": {
        "1": _("Patrol XP Earnings +[x]%"),
        "2": _("Damage to Melee Units +75 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Frost - Sub-Zero: Frozen damage increased, frozen time increased"),
        "4": _("Trait - Ice Snow: Upgrade quicker during battle, Spellbook mana increased"),
        "5": _("Spirit - Upgrade: Attack is reduced for a while for the enemy the Spirit attacks"),
        "6": _("Frost - Ice Spike: Frozen enemies will have their first received damage increased"),
        "7": _("Crit Damage +20% <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Max HP +7% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Rolla's base Attack +5%"),
        "20": _("Damage to Melee Units +240"),
        "30": _("Attacking enemies stacks freeze damage"),
        "30_1": _("Ice Damage +22%"),
        "40": _("Max HP +4%"),
        "50": _("Rolla's base HP +10%"),
        "60": _("Deals more damage to frozen enemies"),
        "70": _("Attack +10%"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Attack +6%")
      },
      "hero_assist_evolve":"immortal-trialstone.svg",
      "list_hero_assist": ["Shari", "Ayana", "Bonnie", "Sylvan", "Lina", "Aquea", "Gugu", "Blazo", "Melinda"],
      "skins" :[
        {
          "name": _("Ice Empress"),
          "src": "Ice_Empress",
          "passiv_boost": _("[Lvl 50]: Attack +100"),
          "activ_boost": _("Surrounding enemies will automatically have reduced movement speed"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 70")
        },
        {
          "name": _("Sweet Proposal"),
          "src": "Sweet_Proposal",
          "passiv_boost": _("[Lvl 50]: Attack +100"),
          "activ_boost": _("Continuously attacking the enemy will increase attack and dodge rate, can be stack up to 10%"),
          "price": _("Obtainable from Exclusive Event")
        },
        {
          "name": _("Turkey Celebration"),
          "src": "Turkey_Celebration",
          "passiv_boost": _("[Lvl 60] Max HP +400"),
          "activ_boost": _("Damage reduction +4%. The more on-screen enemies the higher the effect."),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Bonnie": {
      "displayName": _("Bonnie"),
      "description": _("Heroic and kind woman of the sea! She robs the rich and helps the poor."),
      "base_atk": "150 [+11]",
      "base_hp": "600 [+45]",
      "attributes": {
        "20": _("Crit Damage +20%"), 
        "40": _("Attack Speed +5%"),
        "60": _("Max HP +5%"),
        "80": _("Attack +5%"),
        "120": _("Attack +6%")
      },
      "price": _("$9.99 USD or 30 Bonnie Shards"),
      "skill": _("Chance to summon Clone when attacking"),
      "skill_details": "",
      "star": {
        "1": _("Patrol Gold Earnings +[x]%"),
        "2": _("Attack +50 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Clone - Emergency: Chance to summon 2 clones"),
        "4": _("Trait - Fearless: When there are too many enemies, own attack speed increased"),
        "5": _("Spirit - Upgrade: The more coins on the floor, the quicker the attack speed"),
        "6": _("Clone - Crowd: Clone max limit increased"),
        "7": _("Max HP +1200 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Summoned Creature Damage +15% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Bonnie's base Attack +5%"),
        "20": _("Attack +150"),
        "30": _("After i critical hit, summoned shadow's damage increased for 4s"),
        "30_1": _("Summoned Creature Damage +9%"),
        "40": _("Attack +4%"),
        "50": _("Bonnie's base HP +10%"),
        "60": _("Summoned Creature Duration +20%"),
        "70": _("More summoned creature in a room increases own Attack"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Summoned Creature Damage +17%")
      },
      "hero_assist_evolve":"immortal-trialstone.svg",
      "list_hero_assist": ["Atreus", "Helix", "Meowgik", "Shari", "Ayana", "Lina", "Shingen", "Bobo", "Melinda"],
      "skins" :[
        {
          "name": _("Pirate Captain"),
          "src": "Pirate_Captain",
          "passiv_boost": _("[Lvl 50]: Max HP +250"),
          "activ_boost": _("Bonnie's clone duration increased with the amount of abilities"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 20")
        },
        {
          "name": _("Ghost Captain"),
          "src": "Ghost_Captain",
          "passiv_boost": _("[Lvl 50] Max HP +250"),
          "activ_boost": _("Turn into a ghost at intervals, during which projectiles and enemies will pass through."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 120")
        }
      ]
    },
    "Sylvan": {
      "displayName": _("Sylvan"),
      "description": _("An elf prince, master of the elements and loves nature."),
      "base_atk": "160 [+12]",
      "base_hp": "600 [+45]",
      "attributes": {
        "20": _("Max HP +200"), 
        "40": _("Damage to Ranged Units +20%"),
        "60": _("Attack +5%"),
        "80": _("Max HP +6%"),
        "120": _("Damage to Ranged Units +9%")
      },
      "price": _("$18.99 USD or 30 Sylvan Shards"),
      "skill": _("When attacking, there's a chance to trigger a random powerful elemental attack."),
      "skill_details": _("Every time an enemy is attacked, a random effect from fire, toxic, bolt or ice is used."),
      "star": {
        "1": _("Patrol Locket Scroll Earnings +[x]%"),
        "2": _("Damage to Ranged Units +75 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Elemental - Damage: Elemental damage increased"),
        "4": _("Trait - Pride: When HP is higher than 75%, get extra attack speed"),
        "5": _("Spirit - Upgrade: Enemy gets a second Elemental attack"),
        "6": _("Elemental - Critical Strike: Elemental damage has a chance to deal crit attack"),
        "7": _("Damage to Ground Units +400 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Elemental Damage +30% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Sylvan's base Attack +5%"),
        "20": _("Damage to Ranged Units +240"),
        "30": _("Increased attack after looting a Red Heart. Lasts 3 rooms"),
        "30_1": _("Elemental Damage +10%"),
        "40": _("Max HP +5%"),
        "50": _("Sylvan's base HP +10%"),
        "60": _("Elemental Damage +18%"),
        "70": _("Gain increased Element damage when attacked by enemies"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Elemental Damage +25%")
      },
      "hero_assist_evolve":"immortal-trialstone.svg",
      "list_hero_assist": ["Urasil", "Phoren", "Taranis", "Rolla", "Ryan", "Aquea", "Gugu", "Blazo", "Stella"],
      "skins" :[
        {
          "name": _("Elegant Prince"),
          "src": "Elegant_Prince",
          "passiv_boost": _("[Lvl 50]: Attack +120"),
          "activ_boost": _("When stationary, attack is increased by 4%"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 95")
        },
        {
          "name": _("Sweet Proposal"),
          "src": "Sweet_Proposal",
          "passiv_boost": _("[Lvl 50]: Attack +120"),
          "activ_boost": _("When getting Skills, there's a higher chance to get an Elemental skill"),
          "price": _("Leaderboard Top 3 Rewards (only during the 1st Season)")
        },
        {
          "name": _("Commander"),
          "src": "Commander",
          "passiv_boost": _("[Lvl50] Max HP +350"),
          "activ_boost": _("Gain elemental damage resistance. Boost summoned creatures' random elemental damage."),
          "price": _("Leaderboard Top 20 Rewards (Exclusive)")
        },
        {
          "name": _("Vampire Count"),
          "src": "Vampire_Count",
          "passiv_boost": _("[Lvl 50] Max HP +350"),
          "activ_boost": _("Killing enemies restores a little HP. Killing bosses restores more HP."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/purple_ticket.svg' width='18' height='18'></object> 250")
        }
      ]
    },
    "Shade": {
      "displayName": _("Shade"),
      "description": _("Killer of shadows, queen of the night, she can switch between her real and shadow self in battle."),
      "base_atk": "170 [+13]",
      "base_hp": "550 [+40]",
      "attributes": {
        "20": _("Damage to Ground Units +100"), 
        "40": _("Crit Chance +5%"),
        "60": _("Max HP +5%"),
        "80": _("Attack Speed +5%"),
        "120": _("Crit Damage +10%")
      },
      "price": _("$18.99 USD or 30 Shade Shards"),
      "skill": _("You can enjoy different effects with real and shadow forms, which switch automatically during battle."),
      "skill_details": _("<b><em>Real Self</em></b>: Attacks have strong dark powers, and deal continued damage.<br><b><em>Shadow Self:</em></b> Increased attack, attack speed and dodge rate.<br><br><b>Additional Skill Notes:</b><br> • Switches between her 2 forms every 4 seconds.<br> • Normal form: 135% Damage on hit, 30% damage for 2 ticks, and 135% Dark Touch Explosion.<br> • Shadow form: 75% Attack, 15% Attack Speed, ~15% Dodge Chance."),
      "star": {
        "1": _("Patrol Sapphire Earnings +[x]%"),
        "2": _("Crit Chance +2% <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Twin Shadows - Cold Blood: Chance for Dark stats increased"),
        "4": _("Trait - Calm: HP max limit is increased with each kill"),
        "5": _("Spirit - Upgrade: When switching forms, Spirit gets a new combat power"),
        "6": _("Twin Shadows - Cruel: Increases crit attack when in Dark form"),
        "7": _("Attack +300 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Attack +8% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Shade's base Attack +5%"),
        "20": _("Damage to Melee Units +240"),
        "30": _("Attack increased for short time when enemies are killed by Dark damage"),
        "30_1": _("Dark touch Damage +10%"),
        "40": _("Damage to heroes +8%"),
        "50": _("Shade's base HP +10%"),
        "60": _("HP Converted to MP +15%"),
        "70": _("Shadow forms ignore traps"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Attack +8%")
      },
      "hero_assist_evolve":"immortal-trialstone.svg",
      "list_hero_assist": ["Ayana", "Onir", "Rolla", "Sylvan", "Ophelia", "Aquea", "Gugu", "Iris", "Blazo"],
      "skins" :[
        {
          "name": _("Legendary Assassin"),
          "src": "Legendary_Assassin",
          "passiv_boost": _("[Lvl 50]: Attack +120"),
          "activ_boost": _("In shadow form, collision damage is reduced by 5%"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 95")
        },
        {
          "name": _("Crimson Blade"),
          "src": "Crimson_Blade",
          "passiv_boost": _("[Lvl 50]: Attack +120"),
          "activ_boost": _("Lower the HP, faster the movement speed"),
          "price": _("3000 Honor Points in Honor Shop (for 7d unlock and infinite Attack Boost)")
        },
        {
          "name": _("Diver Pro"),
          "src": "Diver_Pro",
          "passiv_boost": _("[Lvl 50]: Attack +120"),
          "activ_boost": _("During Shadow form, dodge rate increased 8%"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 100")
        }
      ]
    },
    "Ophelia": {
      "displayName": _("Ophelia"),
      "description": _("Huntress walking between darkness and light, adept at hunting evil monsters."),
      "base_atk": "160 [+12]",
      "base_hp": "650 [+42]",
      "attributes": {
        "20": _("Attack +70"), 
        "40": _("Damage to Melee Units +20%"),
        "60": _("Attack +120"),
        "80": _("Max HP +7%"),
        "120": _("Damage to Melee Units +9%")
      },
      "price": _("$9.99 USD or 30 Ophelia Shards"),
      "skill": _("Skill (Demon Soul): Chance to suck and absorb the enemy's soul, increasing own strength."),
      "skill_details": _("Souls are absorbed into different colors in the formation.<br><br><b>Green</b>: Increase attack speed and projectile speed.<br><b>Yellow</b>: Chance to recover HP during crit attacks.<br><b>Blue</b>: Attacked enemy will explode.<br><b>Red</b>: Increase attack and add knockback effect."),
      "star": {
        "1": _("Patrol Armor Scroll Earnings +[x]%"),
        "2": _("Damage to Ground Units +75 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Demon Soul - Amplify: Soul absorption effect increases"),
        "4": _("Trait - Tranquil: Each kill increases HP limit"),
        "5": _("Spirit - Upgrade: Spirit will provide own attack stats to Hero"),
        "6": _("Demon Soul - Distort: Get a new strengthening effect"),
        "7": _("Attack Speed +3% <span class='all_effect_span'>All Heroes</span>"),
        "8": _("MP Cast Speed +25% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Ophelia's base Attack +5%"),
        "20": _("Damage to Ground Units +240"),
        "30": _("Soul Absorption increases red heart drop rate (Max 50%)"),
        "30_1": _("Own buff duration extended"),
        "40": _("Blue Heart drop rate +12%"),
        "50": _("Ophelia's base HP +10%"),
        "60": _("Chance of Angel's healing x2 +20%"),
        "70": _("50% chance to not lose HP when exchanging demon skills"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Weapon Ranged damage +7%")
      },
      "hero_assist_evolve":"immortal-trialstone.svg",
      "list_hero_assist": ["Urasil", "Onir", "Bonnie", "Shade", "Ryan", "Lina", "Iris", "Melinda", "Stella", "Taiga"],
      "skins" :[
        {
          "name": _("Demon Shift"),
          "src": "Demon_Shift",
          "passiv_boost": _("[Lvl 50]: Attack +100"),
          "activ_boost": _("The lower the HP, the stronger the recovery of HP"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 55")
        },
        {
        "name": _("Present Envoy"),
        "src": "Present_Envoy",
        "passiv_boost": _("[Lvl 50]: Attack +100 <span class='all_effect_span'>All Heroes</span>"),
        "activ_boost": _("Summons a Christmas mimic that attacks enemies after Soul absorption."),
        "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Ryan": {
      "displayName": _("Ryan"),
      "description": _("A traveling red panda that loves to sing, dance, and meet new people"),
      "base_atk": "150 [+11]",
      "base_hp": "700 [+45]",
      "attributes": {
        "20": _("Damage to Ranged Units +100"), 
        "40": _("Max HP +5%"),
        "60": _("Damage to Airborne Units"),
        "80": _("Healing Effect of Red Heart +30%"),
        "120": _("Max HP +8%")
      },
      "price": _("50 Ryan Shards"),
      "skill": _("Revive upon death, with Invincibility for 1s. Invincibility increases with the amount of monsters killed."),
      "skill_details": _(" • Defeating enemies increase invincibilty time after revive. The time limit for invincibility is 6 seconds.<br> • Defeating bosses gives 10 times the amount extra invincibility time compared to normal monsters."),
      "star": {
        "1": _("Patrol Ring Scroll Earnings +[x]%"),
        "2": _("Damage to Ranged Units +75 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Luck - Counterattack: When invincible, attack and crit rate increased greatly"),
        "4": _("Trait - Leisure: Enemy projectiles will slow down near Ryan"),
        "5": _("Spirit - Power: Get a Front Arrow +1"),
        "6": _("Luck - Haven: After revival, doge rate, movement speed and crit attack increased during this game"),
        "7": _("Damage to Airborne Units +400 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Coin Drops +10% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Ryan's base Attack +5%"),
        "20": _("Damage to Airborne Units +240"),
        "30": _("Each revival permanently increase Attack by 8%"),
        "30_1": _("Max Mp +7%"),
        "40": _("Chance of Angel's Healing x2 +10%"),
        "50": _("Ryan's base HP +10%"),
        "60": _("Hp Drops +15%"),
        "70": _("Max Hp +20% when hero revies with talent skill"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Max hp +7%")
      },
      "hero_assist_evolve":"immortal-trialstone.svg",
      "list_hero_assist": ["Meowgik", "Rolla", "Shade", "Ophelia", "Lina", "Aquea", "Gugu", "Iris", "Elaine"],
      "skins" :[
        {
          "name": _("Christmas Elf"),
          "src": "Christmas_Elf",
          "passiv_boost": _("[Lvl 50]: Weapon droprate +8%"),
          "activ_boost": _("After killing the enemy, there is a chance to summon a chest that can freeze surrounding enemies"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 100")
        },
        {
          "name": _("Boy Scout"),
          "src": "Boy_Scout",
          "passiv_boost": _("[Lvl 50]: Max HP +600"),
          "activ_boost": _("Attack speed increased after Crit attack, can be stacked."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/purple_ticket.svg' width='18' height='18'></object> 150")
        },
        {
          "name": _("Trick or Treat"),
          "src": "Trick_or_Treat",
          "passiv_boost": _("[Lvl 50] Max HP +600"),
          "activ_boost": _("Hitting enemy has a chance to summon a magic Pumpkin, dealing continuous elemental damage."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 100")
        }
      ]
    },
    "Lina": {
      "displayName": _("Lina"),
      "description": _("A mysterious dancer who loves to travel and dance gracefully for strangers she meets."),
      "base_atk": "180 [+13]",
      "base_hp": "650 [+45]",
      "attributes": {
        "20": _("Attack +100"), 
        "40": _("Dodge +5%"),
        "60": _("Max HP +5%"),
        "80": _("Attack Speed +5%"),
        "120": _("Damage to Melee Units +9%")
      },
      "price": _("50 Lina Shards"),
      "skill": _("Hitting an enemy deals extra damage and summons a phantom dancer who attacks enemies and causes a negative effect."),
      "skill_details": _("Enemies around the Phantom Dancer will slow down and reduce HP."),
      "star": {
        "1": _("Patrol Sapphire Earnings +[x]%"),
        "2": _("Attack +60 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Dream Dance - Enlarge: Range increased 50%"),
        "4": _("Trait - Tender: Red hearts droprate +20%, HP Recovery +20%"),
        "5": _("Spirit - Strengthen: Attack increased 25%"),
        "6": _("Dream Dance - Freeze: Enemies in the range will be frozen after 5s"),
        "7": _("Max HP +1500 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Max MP +15% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Lina's base Attack +5%"),
        "20": _("Attack +150"),
        "30": _("Attack +10%"),
        "30_1": _("Summoned Creature Damage +14%"),
        "40": _("Max Mp +7%"),
        "50": _("Lina's base HP +10%"),
        "60": _("Summoned Creature Attack Speed +25%"),
        "70": _("The more red hearts obtained, the higher your Crit Chance"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Summoned Creature Duration +12%")
      },
      "hero_assist_evolve":"immortal-trialstone.svg",
      "list_hero_assist": ["Atreus", "Helix", "Meowgik", "Shari", "Bonnie", "Shade", "Ryan", "Shingen", "Bobo"],
      "skins" :[
        {
          "name": _("Royal Princess"),
          "src": "Royal_Princess",
          "passiv_boost": _("[Lvl 50]: Max HP +500"),
          "activ_boost": _("Damage received when moving reduced 10%"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 75")
        },
        {
          "name": _("Today's Chef"),
          "src": "Todays_Chef",
          "passiv_boost": _("[Lvl 60]: Max HP +550"),
          "activ_boost": _("Own and mirror image dancer attacks gain Fire damage. Fire damage increases with surrounding enemy count."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 100")
        }
      ]
    },
    "Aquea": {
      "displayName": _("Aquea"),
      "description": _("Princess of the seas, loved by all underwater."),
      "base_atk": "180 [+14]",
      "base_hp": "800 [+50]",
      "attributes": {
        "20": _("Max HP +250"), 
        "40": _("Healing Effect of Red Heart +30%"),
        "60": _("Attack +5%"),
        "80": _("Max HP +10%"),
        "120": _("Healing Effect of Red Heart +12%")
      },
      "price": _("50 Aquea Shards or $24.99 USD"),
      "skill": _("Attack carries a strong freezing effect which slows down enemies. When HP is lower than 35%, combat mode is entered."),
      "skill_details": _("<b><em>Combat Form:</em></b> Body size reduced 15%, crit rate increased 10%, dodge rate increased 15%, freezing damage increased."),
      "star": {
        "1": _("Patrol Bracelet Scroll Earnings +[x]%"),
        "2": _("Attack +70 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Duel Form - Freeze: Freezing effect is greatly increased"),
        "4": _("Trait - Optimism: When HP is lower than 10%, 20% HP is recovered"),
        "5": _("Spirit - Upgrade: Attack speed increased 20%"),
        "6": _("Duel Form - Bloodthirst: Get a bloodthirst effect in combat form"),
        "7": _("Max HP +1800 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Movement Speed +4% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Aquea's base Attack +5%"),
        "20": _("Attack +200"),
        "30": _("When HP is below 20%, chance to drop many red hearts. Only occurs 1 time"),
        "30_1": _("Ice Damage +20%"),
        "40": _("Attack +5%"),
        "50": _("Aquea's base HP +10%"),
        "60": _("Control Effect Duration +22%"),
        "70": _("Attack +10%"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Weapon Damage +7%")
      },
      "hero_assist_evolve":"eternal-trialstone.svg",
      "list_hero_assist": ["Ayana", "Rolla", "Sylvan", "Ophelia", "Shingen", "Gugu", "Iris", "Blazo", "Elaine", "Taiga"],
      "skins" :[
        {
          "name": _("Mermaid Garb"),
          "src": "Mermaid_Garb",
          "passiv_boost": _("[Lvl 50]: Max HP +525"),
          "activ_boost": _("Can walk on water"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 100")
        },
        {
          "name": _("Seahorse! Seahorse!"),
          "src": "Seahorse_Seahorse",
          "passiv_boost": _("[Lvl 50]: Max HP +600"),
          "activ_boost": _("Seahorse has chance to assist in attack when moving or attacking. Gain slight Movement speed."),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Shingen": {
      "displayName": _("Shingen"),
      "description": _("The only heir of an ancient clan, owning their curse and gifts. (Owns their family heirloom: Demon Blade - Rain)"),
      "base_atk": "200[+14]",
      "base_hp": "700 [+45]",
      "attributes": {
        "20": _("Damage to Melee Units +120"), 
        "40": _("Attack speed +5%"),
        "60": _("Max HP +6%"),
        "80": _("Damage to Melee Units +20%"),
        "120": _("Damage to Ground Units +6%")
      },
      "price": _("25.99\u20ac or 50 Shingen Shards"),
      "skill": _("Lower the HP, higher the attack speed. Has high Crit damage."),
      "skill_details": _("Lower the HP, higher the attack speed. Has high Crit Damage.<br><br><b>Hidden Skill Details:</b><br>Able to cast Slash when equipped with an Epic or above Demon Blade"),
      "star": {
        "1": _("Patrol Gold Earnings +[x]%"),
        "2": _("Damage to Melee Units +80 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Charge - Strengthen: Melee damage +12%, long range damage +7%, Crit damage +20%"),
        "4": _("Trait - Persevere: Hitting the same target consecutively increases damage dealt"),
        "5": _("Spirit - Upgrade: Attack increased 15%, Crit damage increased 25%"),
        "6": _("Charge - Souleater: The more enemies killed, the higher the attack (Max limit 10%)"),
        "7": _("Max HP +1800 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Weapon Melee Damage +11% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Shingen's base Attack +5%"),
        "20": _("Damage to Melee Units +320"),
        "30": _("Dodge +9%"),
        "30_1": _("Weapon Melee Damage +5%"),
        "40": _("Front Damage Resistance +6%"),
        "50": _("Shingen's base HP +10%"),
        "60": _("Increased Attack for short time after healing"),
        "70": _("When Hp is below 25%, Attack +35%, Movement Speed +20%, Shadow Samurai damage +50%"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Deal damage to elite enemies +12%")
      },
      "hero_assist_evolve":"eternal-trialstone.svg",
      "list_hero_assist": ["Onir", "Ophelia", "Ryan", "Gugu", "Iris", "Blazo", "Melinda", "Elaine", "Stella", "Taiga"],
      "skins" :[
        {
          "name": _("Family Armor"),
          "src": "Family_Armor",
          "passiv_boost": _("[Lvl 50] Attack +125"),
          "activ_boost": _("Immunity to collision damage +7%, projectile damage +4%, attack increased +4%"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 100")
        },
        {
          "name": _("Sushi Master"),
          "src": "Sushi_Master",
          "passiv_boost": _("[Lvl 50] Attack +130"),
          "activ_boost": _("Chance to perform +1 attack when melee attacking. Also increases movement speed."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 120")
        },
        {
          "name": _("Cherry Blossom"),
          "src": "Cherry_Blossom",
          "passiv_boost": _("[Lvl 50] Attack +130"),
          "activ_boost": _("Triggers berserk 5s after entering a chamber. Triggers again when receiving damage."),
          "price": _("Obtainable from Exclusive Event")
        },
        {
          "name": _("White-haired"),
          "src": "White_haired",
          "passiv_boost": _("[Lvl 50] Attack +150"),
          "activ_boost": _("Higher chance to get Phantom Sword and Shadow Samurai. Also increases own Critical Rate."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 150")
        }
      ]
    },
    "Gugu": {
      "displayName": _("Gugu"),
      "description": _("A brave warrior owl, with a gleam of wisdom in its eyes."),
      "base_atk": "160 (+14)",
      "base_hp": "600 (+45)",
      "attributes": {
        "20": _("Damage to Airborne Units +100"), 
        "40": _("Dodge +5%"),
        "60": _("Damage to Ranged Units +5%"),
        "80": _("Attack Speed +5%"),
        "120": _("Max HP +8%")
      },
      "price": _("50 Gugu Shards"),
      "skill": _("Small chance to summon an owl guardian on hitting enemies. Owl guardians can resist damage and strengthen their hero."),
      "skill_details": _("<FONT color='red'>Red Owl</FONT>: Increased attack, can be stacked.(Increases Attack by 0.1%. Attack is doubled [0.2%] when there are two red owls)<br><FONT color='yellow'>Yellow Owl</FONT>: Killing enemies can restore HP, can be stacked.(Gain 0.7% of Base HP on enemy kills. The amount of Healing is doubled [1.4%] when there are two yellow owls)<br><FONT color='blue'>Blue Owl</FONT>: Increased attack speed, can be stacked. (No data)<br><FONT color='green'>Green Owl</FONT>: Increased attack crit rate, can be stacked. (No data)"),
      "star": {
        "1": _("Patrol Sapphire Earnings +[x]%"),
        "2": _("Damage to Airborne Units +60 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Guardian Spirit - Hope: When own HP is low, chance for summon is higher"),
        "4": _("Trait - Intelligence: Level-up Speed is increased 15% during battle"),
        "5": _("Spirit - Upgrade: Noisy Owl's projectiles can penetrate walls"),
        "6": _("Guardian Spirit - Strength: Owl Guardian's stats increased"),
        "7": _("Damage to Ranged Units +400 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Spin Speed +15% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Gugu's base Attack +5%"),
        "20": _("Damage to Airborne Units +320"),
        "30": _("Collision Damage Resistance +9%"),
        "30_1": _("Dragon magic CoolDown -7%"),
        "40": _("Shield Size +7%"),
        "50": _("Gugu's base HP +10%"),
        "60": _("Spinning Shield spins faster +20%"),
        "70": _("Projectile Resistance +10%"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Max HP +8%")
      },
      "hero_assist_evolve":"eternal-trialstone.svg",
      "list_hero_assist": ["Shari", "Bonnie", "Ophelia", "Lina", "Shingen", "Iris", "Blazo", "Elaine", "Stella", "Taiga"],
      "skins" :[
        {
          "name": _("Mummy Returns"),
          "src": "Mummy_Returns",
          "passiv_boost": _("[Lvl 50] Attack +125"),
          "activ_boost": _("Reduces enemy movement speed, reduces damage received from behind."),
          "price": _("Obtainable from Exclusive Event")
        },
        {
          "name": _("Robin Gugu"),
          "src": "Robin_Gugu",
          "passiv_boost": _("[Lvl 60] Max HP +400"),
          "activ_boost": _("Each attack has a change to summon an owl auto-attacks nearby enemies"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 90")
        }
      ]
    },
    "Iris": {
      "displayName": _("Iris"),
      "description": _("A powerful archer and the guardian of the forest."),
      "base_atk": "160 [+15]",
      "base_hp": "950 [+43]",
      "attributes": {
        "20": _("Max HP +250"), 
        "40": _("Attack +200"),
        "60": _("Attack +5%"),
        "80": _("Dodge +10%"),
        "120": _("Damage to Airborne Units +10%")
      },
      "price": _("50 Iris Shards"),
      "skill": _("High Movement Speed and Dodge. Each ranged attack has a chance to shoot an extra projectile. (Front Arrow)"),
      "skill_details": "",
      "star": {
        "1": _("Patrol Gold Earnings +[x]%"),
        "2": _("Attack +70 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Sharpshooter - Power Attack: Increase damage of extra projectiles and knockback effect."),
        "4": _("Trait - Lively: Each successful dodge will increase Attack Speed temporarily."),
        "5": _("Spirit - Upgrade: Enemies hit by Spirits will have reduced Movement Speed."),
        "6": _("Sharpshooter - Charged Attack: Moving increases Crit Chance temporarily."),
        "7": _("Damage to Airborne Units +400 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Weapon Ranged Damage +10% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Iris's base Attack +5%"),
        "20": _("Attack +200"),
        "30": _("The higher your crit chance, the faster you move "),
        "30_1": _("Front arrow +1 chance increased +10%"),
        "40": _("Rear Damage Resistance +8%"),
        "50": _("Iris's base HP +10%"),
        "60": _("Front arrow damage up"),
        "70": _("Gain movement speed for short time after taking damage "),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Damage to Airborne units +12%")
      },
      "hero_assist_evolve":"eternal-trialstone.svg",
      "list_hero_assist": ["Helix", "Onir", "Shade", "Ophelia", "Ryan", "Blazo", "Melinda", "Elaine", "Stella", "Taiga"],
      "skins" :[
        {
          "name": _("Merry Christmas"),
          "src": "Merry_Christmas",
          "passiv_boost": _("[Lvl 50]: Max HP +700"),
          "activ_boost": _("When HP is low, it'll be recovered over time (only triggered once)"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 100")
        }
      ]
    },
    "Blazo": {
      "displayName": _("Blazo"),
      "description": _("A furious avenger, and an inquisitor against evil."),
      "base_atk": "200 [+15]",
      "base_hp": "900 [+44]",
      "attributes": {
        "20": _("Damage to Melee Units +130"), 
        "40": _("Attack +250"),
        "60": _("Max HP +6%"),
        "80": _("Damage to Ground Units +20%"),
        "120": _("Max HP +8%")
      },
      "price": _("28.99\u20ac or 50 Blazo Shards"),
      "skill": _("Attacks have a chance to be judged; repeated hits inflicts justice."),
      "skill_details": _("Greatly increases its own attack, and reduces the enemy's movement speed and attack. Enemies lose more HP when injured."),
      "star": {
        "1": _("Patrol Gold Earnings +[x]%"),
        "2": _("Damage to Ground Units +80 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Judge - Ghast: Increases Crit Chance for killing enemies when justice"),
        "4": _("Trait - Revenge: Chance to deal Revenge damage when receiving damage"),
        "5": _("Spirit - Enhance: Doubles spirit's attack when hero's HP is reduced"),
        "6": _("Judge - Execution: Performs Judgement more quickly with greater effect"),
        "7": _("Max HP +1800 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Free Magic Cast Rate +12% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Blazo's base Attack +5%"),
        "20": _("Damage to ground Units +320"),
        "30": _("The more red hearts obtained, the faster you attack"),
        "30_1": _("Enemy Debuff duration extended +15%"),
        "40": _("Increased Attack after killing enemies +7%"),
        "50": _("Blazo's base HP +10%"),
        "60": _("Increase Attack speed for short time after healing "),
        "70": _("Gain attack speed for short time after taking damage "),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Control Resistance +20%")
      },
      "hero_assist_evolve":"eternal-trialstone.svg",
      "list_hero_assist": ["Helix","Meowgik","Shari","Bobo","Ophelia","Ryan","Shingen","Melinda","Elaine","Taiga"],
      "skins" :[
        {
          "name": _("Rockstar"),
          "src": "Rockstar",
          "passiv_boost": _("[Lvl 50] Attack +130"),
          "activ_boost": _("Rock N' Roll style changes with mood; various styles have various effects"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 120")
        },
        {
          "name": _("It's Noon"),
          "src": "Its_Noon",
          "passiv_boost": _("[Lvl 60]: Attack +160"),
          "activ_boost": _("Chance to mark enemies, allowing projectiles to go through walls and deal additional damage when attacking them."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 150")
        }
      ]
    },
    "Melinda": {
      "displayName": _("Melinda"),
      "description": _("A beautiful and brave noble who has embarked on a journey to become a renowned ranger."),
      "base_atk": "200 [+16]",
      "base_hp": "1000 [+50]",
      "attributes": {
        "20": _("Damage to Ranged Units +150"), 
        "40": _("Attack Speed +5%"),
        "60": _("Damage to Melee Units +5%"),
        "80": _("Crit Chance +5%"),
        "120": _("Damage to Ranged Units +8%")
      },
      "price": _("29.99\u20ac or 50 Shards"),
      "skill": _("Chance to fire a projectile barrage with each attack. The lower the HP, the stronger the barrage."),
      "skill_details": "",
      "star": {
        "1": _("Patrol XP Earnings +[x]%"),
        "2": _("Damage to Ranged Units +100 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Ranger's Heart - Inspire: Chance to increase attack when projectile barrage is hitting enemies; can stack"),
        "4": _("Trait - Righteous: Surrounding enemies; more and closer will increase hero's attack"),
        "5": _("Spirit - Upgrade: Spirit gains multi-attacks"),
        "6": _("Ranger's Heart - Composure: Increased leveling speed at a higher level cap"),
        "7": _("Attack +400 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Attack +9% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Melinda's base Attack +5%"),
        "20": _("Damage to Airborne Units +400"),
        "30": _("Crit Chance +8%"),
        "30_1": _("Diagonal arrow damage up +10%"),
        "40": _("Attack+5%"),
        "50": _("Melinda's base HP +10%"),
        "60": _("Summoned flying object damage +30%"),
        "70": _("Extra arrows can deal critical hits and penetrate"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Attack +10%")
      },
      "hero_assist_evolve":"eternal-trialstone.svg",
      "list_hero_assist": ["Urasil","Phoren","Taranis","Onir","Aquea","Iris","Blazo","Elaine","Stella","Taiga"],
      "skins" :[
        {
          "name": _("Baking Sweety"),
          "src": "Baking_Sweety",
          "passiv_boost": _("[Lvl 50]: Max HP +750"),
          "activ_boost": _("Gain Rage 5s after damage, increases attack. Gain Joy 5s after looting a Heart, increases Dodge rate."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 120")
        },
        {
          "name": _("Huffy Melinda"),
          "src": "Huffy_Melinda",
          "passiv_boost": _("[Lvl 50]: Max HP +750"),
          "activ_boost": _("Melinda hates math, but when her HP is multiples of 3, 17 and 59, her Attack is greatly increased. Her Movement and Dodge Rate are increased at other HP value."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 150")
        },
        {
          "name": _("Cute Clown"),
          "src": "Cute_Clown",
          "passiv_boost": _("[Lvl 40] Max HP +700"),
          "activ_boost": _("Turns projectile barrage into daggers that deal damage over time and slow enemies"),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Elaine": {
      "displayName": _("Elaine"),
      "description": _("An adorable butterfly maiden blessed by elven gods since her birth"),
      "base_atk": "215 (+16)",
      "base_hp": "900 (+46)",
      "attributes": {
        "20": _("Damage to Airborne Units +120"), 
        "40": _("Max HP +5%"),
        "60": _("Max HP +7%"),
        "80": _("Crit Chance +7%"),
        "120": _("Damage to Ground Units +9%")
      },
      "price": _("50 Elaine Shards"),
      "skill": _("Gain invincibility shield at intervals that also increases Attack Speed. When shield fades, attack is greatly increased."),
      "skill_details": "",
      "star": {
        "1": _("Patrol Weapon Scroll Earnings +[x]%"),
        "2": _("Max HP +350 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Invincible Elaine - Counter: Shots blocked by invincibility shield are converted into attack when shield fades."),
        "4": _("Trait - Outgoing: Great at making friends, reducing hostility of surrounding enemies (reduces attack)"),
        "5": _("Spirit - Upgrade: Attack increases for every room cleared. Flying Spirits gain +20%"),
        "6": _("Invincible Elaine - Enhanced Shield: Shield's duration increased. Also increases Crit Rate and summoned creature attack."),
        "7": _("Max HP +2000 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Max HP +9% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Elaine's base Attack +5%"),
        "20": _("Max Hp +770 "),
        "30": _("Damage Resistance +9%"),
        "30_1": _("Invincibility star chance increased +15%"),
        "40": _("Max Hp +6%"),
        "50": _("Elaine's base HP +10%"),
        "60": _("Max level +1"),
        "70": _("Bosses have slight chance to drop 1 extra red heart"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Max Hp +10%")
      },
      "hero_assist_evolve":"eternal-trialstone.svg",
      "list_hero_assist": ["Helix","Bobo","Shade","Ryan","Shingen","Gugu","Blazo","Melinda","Stella","Taiga"],
      "skins" :[
        {
          "name": _("Snow Maiden Elaine"),
          "src": "Snow_Maiden_Elaine",
          "passiv_boost": _("[Lvl 50] Attack +150"),
          "activ_boost": _("Immune to freeze. Also slows or freezes surrounding enemies. Greatly increases ice damage and ice damage resistance."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 150")
        },
        {
          "name": _("Your Present"),
          "src": "Your_Present",
          "passiv_boost": _("[Lvl 50]: Max HP +800"),
          "activ_boost": _("Chance to get 1 random boost effect when Invincibility Shield fades."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 165")
        },
        {
          "name": _("Cherry Blossom"),
          "src": "Cherry_Blossom",
          "passiv_boost": _("[Lvl 50]: Max HP +800"),
          "activ_boost": _("Chance to get 1 cherry blossom when enemies are killed. Merge 3 cherries blossoms into 1 heart."),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 165")
        }
      ]
    },
    "Bobo": {
      "displayName": _("Bobo"),
      "description": _("A brainy bear from a faraway city"),
      "base_atk": "160 (+12)",
      "base_hp": "700 (+47)",
      "attributes": {
        "20": _("Damage to mobs +150"), 
        "40": _("Attack +5%"),
        "60": _("Damage to Ranged Units +5%"),
        "80": _("MP Strength +20%"),
        "120": _("Attack +6%")
      },
      "price": _("4000 <object type='image/png' data='/static/image/svg/gem.svg' width='16' height='16'></object> or 50 Bobo Shards"),
      "skill": _("Increases leveling speed. Attack increases with level in a chamber"),
      "skill_details": _("Bobo has 12.5% atk boost at start, and gains around 7.5% attack per lvl (credit to Chaos)"),
      "star": {
        "1": _("Patrol XP Earnings +[x]%"),
        "2": _("Max HP +240 <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Wisdom's Might - Upgrade: Gain higher Attack and leveling speed"),
        "4": _("Trait - Learner: Loot Hearts to increase slight Attack Speed (Max 10%)"),
        "5": _("Spirit - Upgrade: Inherits 10% of Hero's Attack"),
        "6": _("Wisdom's Might - Insight: Inflicts weakness on enemies. Hitting the same enemy repeatedly deals more damage"),
        "7": _("Max HP +1800 <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Battle XP Gain +5% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Bobo's base Attack +5%"),
        "20": _("Max Hp +480"),
        "30": _("Attack Speed +8%"),
        "30_1": _("MP Strength +6%"),
        "40": _("Attack +3%"),
        "50": _("Bobo's base HP +10%"),
        "60": _("Battle XP Gain +15%"),
        "70": _("Max level +1"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Battle XP Gain +6%")
      },
      "hero_assist_evolve":"everlife-trialstone.svg",
      "list_hero_assist": ["Atreus","Meowgik","Shari","Onir","Rolla","Aquea","Shingen","Elaine"],
      "skins" :[
        {
          "name": _("Pinobear"),
          "src": "Pinobear",
          "passiv_boost": _("[Lvl 50] Max HP +300"),
          "activ_boost": _("Each attack has a chance to fire lasers from the nose. Gain extra collision damage reduction."),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Stella": {
      "displayName": _("Stella"),
      "description": _("Princess of the Sky City, able to wield the power of the astral realm since birth."),
      "base_atk": "225 (+18)",
      "base_hp": "950 (+50)",
      "attributes": {
        "20": _("Attack +125"),
        "40": _("Crit Chance +6%"),
        "60": _("Attack +6%"),
        "80": _("Attack Speed +7%"),
        "120": _("HP drops +7%")
      },
      "price": _("40 USD or 50 Stella Shards"),
      "skill": _("Master of starlight and lightning. Attacks with guardian spirit. Possesses strong weapon damage and knockback."),
      "skill_details": "",
      "star": {
        "1": _("Patrol Armor Scroll Earnings +[x]%"),
        "2": _("Rear Damage Resistance +3% <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Starlight and Thunder - Dazzle: Increases Starlight damage, summon chance and max summons"),
        "4": _("Trait - Mischievous: Chance to use lightning to attack surrounding enemies when moving"),
        "5": _("Spirit - Enhance: When spirit attacks enemies, they take more damage when attacked by lightning and spirit."),
        "6": _("Starlight and Thunder - Eon Ward: Guardian spirit's weapon damage increased. Successive attacks on enemies increase Attack Speed"),
        "7": _("Meteor and Star damage +10% <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Weapon Damage +8% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Stella's base Attack +5%"),
        "20": _("Attack +230"),
        "30": _("After moving a distance, gain attack and elemental attack for a short time"),
        "30_1": _("All star skills damage +18%"),
        "40": _("Attack +5%"),
        "50": _("Stella's base HP +10%"),
        "60": _("Wall bounce +1"),
        "70": _("Increased damage reduction when moving "),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Increased attack after killing enemies +12%")
      },
      "hero_assist_evolve":"eternal-trialstone.svg",
      "list_hero_assist": ["Taranis","Bobo","Shade","Ryan","Gugu","Iris","Blazo","Melinda","Elaine","Taiga"],
      "skins" :[
        {
          "name": _("Ocean's Heart"),
          "src": "Oceans_Heart",
          "passiv_boost": _("[Lvl 60] Attack +155"),
          "activ_boost": _("The more water in the room, the higher your Attack"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 155")
        },
        {
          "name": _("Lethal Jello"),
          "src": "Lethal_Jello",
          "passiv_boost": _("[Lvl 70] Attack +200"),
          "activ_boost": _("Poisons all enemies in the room when taking damage. The lower the HP of Poisoned enemies, the higher the poison damage. Last 8s"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 160")
        },
        {
          "name": _("Kitchen's Secret"),
          "src": "Kitchens_Secret",
          "passiv_boost": _("[Lvl 80] Max Hp +820"),
          "activ_boost": _("Attacks deal Fire Damage"),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Taiga": {
      "displayName": _("Taiga"),
      "description": _("An enigmatic warrior from the East, probably the world's most powerful martial artist. None can withhand his full might."),
      "base_atk": "230 (+19)",
      "base_hp": "1000 (+55)",
      "attributes": {
        "20": _("Max Hp +400"),
        "40": _("Dodge +7%"),
        "60": _("Max Hp +6%"),
        "80": _("Attack Speed +7%"),
        "120": _("Crit Damage +17%")
      },
      "price": _("40 USD or 50 Taiga's Shards"),
      "skill": _("Summons a meteor to attack enemies and deal Fire damage to enemies in the area."),
      "skill_details": "",
      "star": {
        "1": _("Patrol Gold Earnings +[x]%"),
        "2": _("Dodge +2% <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Meteor Flamefist - Red Heart: Increases Blazing Meteor's damage. When HP is lower, meteor has a chance to drop Hearts"),
        "4": _("Trait - Brave: Sustained attacks increase Attack Speed"),
        "5": _("Spirit - Upgrade: Attack Speed and Crit Rate can be stacked after Spirit attacks enemies"),
        "6": _("Meteor Flamefist - Suppression: The higher the enemy's HP, the more damage Blazing Meteor deals"),
        "7": _("Attack +3% <span class='all_effect_span'>All Heroes</span>"),
        "8": _("Beast Damage Reduction +10% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
        "10": _("Taiga's base Attack +5%"),
        "20": _("Attack +240"),
        "30": _("When Blazing Meteor hits enemies, there is a slightly higher chance to summon another meteor"),
        "30_1": _("Meteor splits into 3 rays when it lands. Rays increase hero Crit Rate when they hit enemies."),
        "40": _("Beast Damage +10%"),
        "50": _("Taiga's base HP +10%"),
        "60": _("The lower your HP, the higher the Damage (also works on Rage skill)"),
        "70": _("The farther you move in one go, the higher the damage of your next attack"),
        "80": _("Can deploy at any time to assist in Battle"),
        "90": _("Weapon Damage +7%"),
        "100": _("Weapon Melee Damage +8%")
      },
      "hero_assist_evolve":"eternal-trialstone.svg",
      "list_hero_assist": ["Helix","Meowgik","Ophelia","Aquea","Iris","Blazo","Melinda","Elaine","Stella"],
      "skins" :[
        {
          "name": _("Asura"),
          "src": "Asura",
          "passiv_boost": _("[Lvl 60] Attack +1%"),
          "activ_boost": _("Chance to trigger Tiger Punch when enemy is hit. Chance increases with Crit Rate. Invincible for 3s when almost dead"),
          "price": _("Price: <object type='image/png' data='/static/image/svg/premium_ticket.svg' width='18' height='18'></object> 200")
        },
        {
          "name": _("Mandarin Taiga"),
          "src": "Mandarin_Taiga",
          "passiv_boost": _("[Lvl 80] Max Hp +1%"),
          "activ_boost": _("Body turns stiff, reducing damage taken by 8%, but also reduces Attack speed by 3%. Thrists for fresh blood; Bloodthirst effect +25%"),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    },
    "Wukong": {
      "displayName": _("Wukong"),
      "description": _("A spirit monkey borne of a sagestone when Heaven cleaved the earth, proclaimed to be the Monkey King."),
      "base_atk": "350 (+25)",
      "base_hp": "1300 (+75)",
      "attributes": {
        "20": _("Max Hp +500"),
        "40": _("Damage Resistance +5%"),
        "60": _("Attack +8%"),
        "80": _("Elemental Damage Resistance +15%"),
        "120": _("Max Hp +10%")
      },
      "price": _("60 Wukong's Shards"),
      "skill": _("Attacks have a chance to hurl Goldwish Cudgel that can penetrate walls and enemies. When moving, cudgel will appear and attack enemies."),
      "skill_details": _("<span class='center_content'><object type='image/png' data='/static/image/svg/icon-skill-Wukong-1.svg' width='22' height='22'></object>Heavenly Havoc :</span>Unlock condition: Raised to Lv.70<br>Unlock in-stage skill - Heavenly Havoc. Swings Goldwish Cudgel in a spin and destroys enemies.<br><span class='center_content'><object type='image/png' data='/static/image/svg/icon-skill-Wukong-2.svg' width='22' height='22'></object>Three Life-saving Hairs :</span>Unlock condition: Evolved to 7-Star<br>Chance to get 1 Life-saving hair that blocks damage each time you are damaged, get a Heart and defeat a boss."),
      "star": {
        "1": _("Skill - Bouncy Wall: Goldwish Cudgel bounces off walls."),
        "2": _("Attack +5% <span class='all_effect_span'>All Heroes</span>"),
        "3": _("Trait - Eradicating Evil: Damage +20% on enemies below 25% HP."),
        "4": _("Skill - Bolstered Bravery: 1 Goldwish Cudgel appears to attack enemies each time you take damage. Chance to summon 1-2 Monkey Mirages"),
        "5": _("Unseal - Exclusive Skill: Able to learn \"72 Forms\" and \"Monkey Mirage\" in stages."),
        "6": _("Skill - More the Merrier: Chance to summon 1-2 Monkey Mirages when Goldwish Cudgel hits enemies."),
        "7": _("Unseal - Relic: Activates Supreme Treasure - Goldwish Cudgel's seal effect (Deals damage to elite enemies +10%)."),
        "8": _("All Damage Increased +6% <span class='all_effect_span'>All Heroes</span>")
      },
      "hero_assist": {
            "10": _("Wukong's base Attack +7%"),
            "20": _("Attack +320"),
            "30": _("Increased Attack and Dodge rate after taking damage."),
            "30_1": _("Crit Chance +7%"),
            "40": _("Damage to Bosses +15%"),
            "50": _("Wukong's base HP +15%"),
            "60": _("Auto-throws cudgel after moving a certain distance."),
            "70": _("Deals damage to undead +15%"),
            "80": _("Can deploy at any time to assist in Battle"),
            "90": _("Weapon Damage +10%"),
            "100": _("Attack +15%")
      },
      "hero_assist_evolve":"eternal-trialstone.svg",
      "list_hero_assist": ["Atreus","Shari","Bobo","Shade","Ryan","Lina","Aquea","Gugu","Melinda", "Elaine", "Stella", "Taiga"],
      "skins" :[
        {
          "name": _("Golden Eyes"),
          "src": "Golden_Eyes",
          "passiv_boost": _("[Lvl 60] Max Hp +2%"),
          "activ_boost": _("After taking damage, moving leaves fiery trails. Gain higher Fire damage boost and Fire damage Resistance."),
          "price": _("Obtainable from Exclusive Event")
        }
      ]
    }
  },
  "SidebarContent": {
    "Menu": {
      "class": "traveling-inline-div",
      "onclick": "/",
      "childs_container": {
        "leftsidebar": {
          "self_class": "leftsidebarc traveling-left",
          "child_class": "shcl",
          "child_content": _("Home")
        },
        "rightsidebar": {
          "self_class": "rightsidebarc traveling-right ",
          "child_class": "shcr",
          "child_content": {
            "image_src": "/static/image/img-sidebar/home.png",
            "image_width": "21",
            "image_id": "svg-filter-home",
            "image_height": "21"
          }
        }
      }
    },
    "Stats": {
      "class": "traveling-inline-div",
      "onclick": "/calculator/index/",
      "childs_container": {
        "leftsidebar": {
          "self_class": "leftsidebarc traveling-left",
          "child_class": "shcl",
          "child_content": _("Stats")
        },
        "rightsidebar": {
          "self_class": "rightsidebarc traveling-right ",
          "child_class": "shcr",
          "child_content": {
            "image_src": "/static/image/img-sidebar/stats.png",
            "image_width": "21",
            "image_id": "Stats",
            "image_height": "21"
          }
        }
      }
    },
    "Wiki": {
      "class": "traveling-inline-div",
      "onclick": "/wiki/menu",
      "childs_container": {
        "leftsidebar": {
          "self_class": "leftsidebarc traveling-left",
          "child_class": "shcl",
          "child_content": _("Wiki")
        },
        "rightsidebar": {
          "self_class": "rightsidebarc traveling-right ",
          "child_class": "shcr",
          "child_content": {
            "image_src": "/static/image/img-sidebar/wiki.png",
            "image_width": "21",
            "image_id": "Wiki",
            "image_height": "21"
          }
        }
      }
    },
    "Heroes": {
      "class": "traveling-inline-div",
      "onclick": "/wiki/heroes",
      "childs_container": {
        "leftsidebar": {
          "self_class": "leftsidebarc traveling-left",
          "child_class": "shcl",
          "child_content": _("Heroes")
        },
        "rightsidebar": {
          "self_class": "rightsidebarc traveling-right ",
          "child_class": "shcr",
          "child_content": {
            "image_src": "/static/image/img-sidebar/hero.png",
            "image_width": "21",
            "image_id": "Heroes",
            "image_height": "21"
          }
        }
      }
    },
    "Items": {
      "class": "traveling-inline-div",
      "onclick": "/wiki/item",
      "childs_container": {
        "leftsidebar": {
          "self_class": "leftsidebarc traveling-left",
          "child_class": "shcl",
          "child_content": _("Items")
        },
        "rightsidebar": {
          "self_class": "rightsidebarc traveling-right ",
          "child_class": "shcr",
          "child_content": {
            "image_src": "/static/image/img-sidebar/icon_stuff.png",
            "image_width": "21",
            "image_id": "Item",
            "image_height": "21"
          }
        }
      }
    },
    "Skills": {
      "class": "traveling-inline-div",
      "onclick": "/wiki/skill",
      "childs_container": {
        "leftsidebar": {
          "self_class": "leftsidebarc traveling-left",
          "child_class": "shcl",
          "child_content": _("Skills")
        },
        "rightsidebar": {
          "self_class": "rightsidebarc traveling-right ",
          "child_class": "shcr",
          "child_content": {
            "image_src": "/static/image/img-sidebar/skill.png",
            "image_width": "21",
            "image_id": "Skill",
            "image_height": "21"
          }
        }
      }
    },
    "Damage": {
      "class": "traveling-inline-div",
      "onclick": "/wiki/damage-calculator",
      "childs_container": {
        "leftsidebar": {
          "self_class": "leftsidebarc traveling-left",
          "child_class": "shcl",
          "child_content": _("Damage")
        },
        "rightsidebar": {
          "self_class": "rightsidebarc traveling-right ",
          "child_class": "shcr",
          "child_content": {
            "image_src": "/static/image/img-sidebar/damage.png",
            "image_width": "21",
            "image_id": "Damage",
            "image_height": "21"
          }
        }
      }
    },
    "Upgrade": {
      "class": "traveling-inline-div",
      "onclick": "/wiki/upgrade",
      "childs_container": {
        "leftsidebar": {
          "self_class": "leftsidebarc traveling-left",
          "child_class": "shcl",
          "child_content": _("Upgrade")
        },
        "rightsidebar": {
          "self_class": "rightsidebarc traveling-right",
          "child_class": "shcr",
          "child_content": {
            "image_src": "/static/image/img-sidebar/upgrade.png",
            "image_width": "21",
            "image_id": "Upgrade",
            "image_height": "21"
          }
        }
      }
    },
    "Promos": {
      "class": "traveling-inline-div",
      "onclick": "/wiki/promo-code",
      "childs_container": {
        "leftsidebar": {
          "self_class": "leftsidebarc traveling-left",
          "child_class": "shcl",
          "child_content": _("Promos")
        },
        "rightsidebar": {
          "self_class": "rightsidebarc traveling-right",
          "child_class": "shcr",
          "child_content": {
            "image_src": "/static/image/img-sidebar/promotion_code.png",
            "image_width": "21",
            "image_id": "Promos",
            "image_height": "21"
          }
        }
      }
    },
    "Sheet": {
      "class": "traveling-inline-div",
      "onclick": "/wiki/google-sheet",
      "childs_container": {
        "leftsidebar": {
          "self_class": "leftsidebarc traveling-left",
          "child_class": "shcl",
          "child_content": _("Sheet")
        },
        "rightsidebar": {
          "self_class": "rightsidebarc traveling-right ",
          "child_class": "shcr",
          "child_content": {
            "image_src": "/static/image/img-sidebar/sheet.png",
            "image_width": "21",
            "image_id": "Sheet",
            "image_height": "21"
          }
        }
      }
    },
    "Maze": {
      "class": "traveling-inline-div",
      "onclick": "/wiki/maze",
      "childs_container": {
        "leftsidebar": {
          "self_class": "leftsidebarc traveling-left",
          "child_class": "shcl",
          "child_content": _("Maze Map")
        },
        "rightsidebar": {
          "self_class": "rightsidebarc traveling-right ",
          "child_class": "shcr",
          "child_content": {
            "image_src": "/static/image/img-sidebar/maze.png",
            "image_width": "21",
            "image_id": "Maze",
            "image_height": "21"
          }
        }
      }
    },
    "Theorycraft": {
      "class": "traveling-inline-div",
      "onclick": "/wiki/theorycraft/",
      "childs_container": {
        "leftsidebar": {
          "self_class": "leftsidebarc traveling-left",
          "child_class": "shcl",
          "child_content": _("TheoryCraft")
        },
        "rightsidebar": {
          "self_class": "rightsidebarc traveling-right ",
          "child_class": "shcr",
          "child_content": {
            "image_src": "/static/image/img-sidebar/theorycraft.png",
            "image_width": "21",
            "image_id": "Theorycraft",
            "image_height": "21"
          }
        }
      }
    }
  },
  "WikiContent": {
    "fusion": {
        "fusion_item": {
            "type": "img",
            "displayName": _("item"),
            "displayNameImg": "<img src='/static/image/rarity/epic.png' alt='epic rarity image fusion item'> - <img src='/static/image/rarity/mythic.png' alt='mythic rarity image fusion item'>",
            "classButton": "collapsible fusion",
            "collapsible_container": {
                "class_content": "fusion",
                "content": {
                "field": {
                    "src": "image/wiki-image/Fusing_Hierarchy.webp",
                    "class": "fusion_collaps_img",
                    "alt": "Fusion Archero Hierarchy"
                }
                }
            }
        },
        "fusion_item_above_mythic": {
            "type": "img",
            "displayName": _("item mythic+"),
            "displayNameImg": "<img src='/static/image/rarity/mythic.png' alt='mythic rarity image fusion item'> - <img src='/static/image/rarity/chaos.png' alt='chaos rarity image fusion item'>",
            "classButton": "collapsible fusion",
            "collapsible_container": {
                "class_content": "fusion",
                "content": {
                    "field": {
                        "src": "image/wiki-image/Fusing_Hierarchy2.webp",
                        "class": "fusion_collaps_img",
                        "alt": "Fusion Archero Hierarchy2"
                    }
                }
            }
        },
        "fusion_item_s_grade": {
            "type": "img",
            "displayName": _("item s grade"),
            "displayNameImg": "<img src='/static/image/dragon/S.png' alt='S grade image fusion item'>",
            "classButton": "collapsible fusion",
            "collapsible_container": {
                "class_content": "fusion",
                "content": {
                    "field": {
                        "src": "image/wiki-image/Fusing_Hierarchy_S.webp",
                        "class": "fusion_collaps_img",
                        "alt": "Fusion Chart Archero Item S grade"
                    }
                }
            }
        },
        "fusion_dragon": {
            "type": "img",
            "displayName": _("dragon"),
            "displayNameImg": "<img src='/static/image/wiki-image/Currency_Dragon_Random_RarityQuality_12.png' alt='great rarity image dragon'> - <img src='/static/image/wiki-image/Currency_Dragon_Random_RarityQuality_14.png' alt='epic rarity image dragon'>",
            "classButton": "collapsible fusion",
            "collapsible_container": {
                "class_content": "fusion",
                "content": {
                    "field": {
                        "src": "image/wiki-image/Dragon-Rarity-Guide.webp",
                        "class": "fusion_collaps_img",
                        "alt": "Achero rarity guide"
                    }
                }
            }
        },
    },
    "tierlist": {
        "tierlist_hero": {
            "type": "img",
            "displayName": _("hero"),
            "displayNameImg": "<img src='/static/image/img-sidebar/hero.png' alt='tierlist hero archero 2023'>",
            "classButton": "collapsible tierlist",
            "collapsible_container": {
                "class_content": "tierlist",
                "content": {
                    "field": {
                        "src": "image/wiki-image/HeroTierlist2023.webp",
                        "class": "tierlist_img",
                        "alt": "Tierlist Hero Archero"
                    }
                }
            }
        },
        "tierlist_item": {
            "type": "img",
            "displayName": _("item normal"),
            "displayNameImg": "<img src='/static/image/rarity/epic.png' alt='epic rarity image tierlist archero'> - <img src='/static/image/rarity/ancient_legendary.png' alt='ancient legendary rarity image tierlist archero'>",
            "classButton": "collapsible tierlist",
            "collapsible_container": {
                "class_content": "tierlist",
                "content": {
                    "field": {
                        "src": "image/wiki-image/General-Tier-List_1.webp",
                        "class": "tierlist_img",
                        "alt": "Tierlist Archero"
                    }
                }
            }
        },
        "tierlist_item_mythic": {
            "type": "img",
            "displayName": _("item mythic"),
            "displayNameImg": "<img src='/static/image/rarity/mythic.png' alt='mythic rarity image tierlist archero'>",
            "classButton": "collapsible tierlist",
            "collapsible_container": {
                "class_content": "tierlist",
                "content": {
                    "field": {
                        "src": "image/wiki-image/Mythic-Tier-List2023.webp",
                        "class": "tierlist_img_myt",
                        "alt": "Tierlist 2023 Archero"
                    }
                }
            }
        },
    },
    "guide": {
        "faq": {
            "type": "embed",
            "displayName": _("Frequently Asked Questions"),
            "displayNameImg": "<img src='/static/image/wiki-image/question_mark.png' alt='question mark archero'>",
            "classButton": "collapsible faq-container",
            "collapsible_container": {
                "class_content": "faq",
                "border_color": "style='border-color: rgb(177,177,177);'",
                "content": {
                    "title": {
                        "idTitle": "title_faq",
                        "innerText": _("Frequently Asked Questions")
                    },
                    "description": {
                        "idDesc": "desc_faq",
                        "innerText": ""
                    },
                    "field": [
                        {
                        "name": _("• Frequently Asked Questions •"),
                        "value": "<a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_should_i_dismantle_or_exchange_items.3F'>Should I dismantle or exchange items?</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_what_is_the_best_loadout.3F'>What is the best loadout?</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_what_are_the_best_abilities.3F'>What are the best abilities?</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_what_is_stutterstepping.3F'>What is stutterstepping?</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_where_do_i_find_eggs_of_certain_monsters.2Feggs.3F'>Where do I find eggs of certain monsters/eggs?</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_can_i_transfer_my_progress_from_ios_to_android_or_from_android_to_ios.3F'>Can I transfer my progress from iOS \u27f7 Android ?</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_why_did_i_not_get_the_latest_archero_update_yet.3F'>Why did I not get the latest Archero update yet?</a>"
                        },
                        {
                        "name": _("• Farming •"),
                        "value": "<a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_why_did_i_not_receive_my_loot_that_dropped_in_a_stage.3F'>Why did I not receive my loot ?</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_what_is_the_best_place_to_farm.3F'>What is the best place to farm?</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_what_is_the_best_place_to_farm_a_specific_item.3F'>What is the best place to farm a specific item?</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_where_do_i_find_bloodthirst_stones.3F'>Where do I find Bloodthirst Stones?</a>"
                        },
                        {
                        "name": _("• Progressing •"),
                        "value": "<a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_how_do_i_get_more_gems.3F'>How do I get more gems?</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_i_can.27t_beat_chapter_x.2C_what_should_i_do.3F'>I can't beat chapter x, what should I do?</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_how_do_i_get_more_atk_and_hp.3F'>How do I get more ATK and HP?</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_how_far_can_i_upgrade_my_talents.3F'>How far can I upgrade my talents?</a>"
                        },
                        {
                        "name": _("• When do I unlock ... ?"),
                        "value": "<a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_.ancient_maze'>Ancient Maze</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_.expedition_hero_mode'>Expedition Hero mode</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_.quick_raids'>Quick Raids</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_.equipment_altar'>Equipment Altar</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_.hero_altar'>Hero Altar</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_.dragon_statues'>Dragon Statues</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_.great_.28green.29_item_drops_in_chapters'>Great item drops</a><br><a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_.refining.2Fglyphs'>Refining/Glyphs</a>"
                        }
                    ],
                    "footer": {
                        "innerText": _("Source : Reddit r/Archero")
                    },
                    "thumbnail": {
                        "src": "",
                        "alt": "",
                        "class": ""
                    }
                }
            }
        },
        "gems_spending_guide": {
            "type": "embed",
            "displayName": _("Gems"),
            "displayNameImg": "<img src='/static/image/wiki-image/Gem.png' alt='gem image archero'>",
            "classButton": "collapsible gems_spending_guide",
            "collapsible_container": {
                "class_content": "gems_spending_guide_child",
                "border_color": "style='border-color: rgb(0,249,54);'",
                "content": {
                    "title": {
                        "idTitle": "title_gems_guide",
                        "innerText": _("Gem Guide")
                    },
                    "description": {
                        "idDesc": "desc_gems_guide",
                        "innerText": ""
                    },
                    "field": [
                        {
                        "name": _("Earning:"),
                        "value": ""
                        },
                        {
                        "name": "",
                        "value": _("• Daily Quests: Up to 40 Gems per day")
                        },
                        {
                        "name": "",
                        "value": _("• Weekly Quests: Up to 230 Gems per week")
                        },
                        {
                        "name": "",
                        "value": _("• Daily Ad Pack: 30 Gems per day")
                        },
                        {
                        "name": "",
                        "value": _("• Ad Boss wheel: Up to 100 Gems per day")
                        },
                        {
                        "name": "",
                        "value": _("• Hero Duo")
                        },
                        {
                        "name": "",
                        "value": _("• Hero Duel: Profit if you win ≥ 62% of 40 Gem matches or ≥ 67% of 100 Gem matches")
                        },
                        {
                        "name": "",
                        "value": _("• Monster Farm: Clean up obstacles for a chance to receive Gems")
                        },
                        {
                        "name": "",
                        "value": _("• Clear new chapters")
                        },
                        {
                        "name": "",
                        "value": _("• Clear Expedition stages")
                        },
                        {
                        "name": "",
                        "value": "<br>"
                        },
                        {
                        "name": _("Spending:"),
                        "value": ""
                        },
                        {
                        "name": "",
                        "value": _("• At least one main hero (Helix is recommended)")
                        },
                        {
                        "name": "",
                        "value": _("• Extra hatchery slots, to speed up egg hatching")
                        },
                        {
                        "name": "",
                        "value": _("• Extra monster book slots, to get more bonuses from monsters in use")
                        },
                        {
                        "name": "",
                        "value": _("• Extra attempt for Ancient Maze, if you can consistently finish it on Extreme/Misery difficulty")
                        },
                        {
                        "name": "",
                        "value": _("• Extra energy to farm Hero chapters or play events")
                        },
                        {
                        "name": "",
                        "value": _("• Extra attempt(s) for Up-Close Dangers, if you are at the point where you earn relatively high amounts of coins from it compared to chapter runs")
                        },
                        {
                        "name": "",
                        "value": _("• Mystery Chest in your Farm, if it shows up")
                        },
                        {
                        "name": "",
                        "value": _("• Login Rewards Event <a class='styled_a' href='https://cdn.discordapp.com/attachments/1018889785571540994/1113272516136407061/LoginRewardsEvent.png' target='_blank'>[Example]</a><br>")
                        }
                    ],
                    "footer": {
                        "innerText": ""
                    },
                    "thumbnail": {
                        "src": "/static/image/wiki-image/Gem.png",
                        "alt": "Gems Spending Thumbnail",
                        "class": ""
                    }
                }
            }
        },
        "gold_guide": {
            "type": "embed",
            "displayName": _("gold"),
            "displayNameImg": "<img src='/static/image/wiki-image/Gold.png' alt='gold image archero'>",
            "classButton": "collapsible gold_guide",
            "collapsible_container": {
                "class_content": "gold_guide_child",
                "border_color": "style='border-color: rgb(255,196,0);'",
                "content": {
                    "title": {
                        "idTitle": "title_gold_guide",
                        "innerText": _("Gold Guide")
                    },
                    "description": {
                        "idDesc": "desc_gold_guide",
                        "innerText": ""
                    },
                    "field": [
                        {
                        "name": _("Earning:"),
                        "value": _("• Use any other rings than Lion,Vilebat,Dragon Rings for +10% coins from battle")
                        },
                        {
                        "name": "",
                        "value": _("• In your Spirit jewel slots, have an overall level of 8 or higher, for +5% Coins from battle")
                        },
                        {
                        "name": "",
                        "value": _("• Play the Up-close Dangers event every time it is active (Tuesday, Thursday, Saturday, Sunday)")
                        },
                        {
                        "name": "",
                        "value": _("• Play the clan event (Monster Treasure) every day")
                        },
                        {
                        "name": "",
                        "value": _("• Watch 3 ads per day at the bottom of the Shop tab")
                        },
                        {
                        "name": "",
                        "value": _("• Watch 4 ads per day for 5 energy each by clicking on your energy at the top, use this energy to play chapters")
                        },
                        {
                        "name": "",
                        "value": _("• Hero Mode Boss chapters (7, 14, 21, 28, 35, 42)")
                        },
                        {
                        "name": "",
                        "value": "<br>"
                        },
                        {
                        "name": _("What should i spend my gold on ?"),
                        "value": "• <a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_what_should_i_spend_my_gold_on.3F' target='_blank'>Reddit</a>"
                        }
                    ],
                    "footer": {
                        "innerText": _("Credit: zkn#4789")
                    },
                    "thumbnail": {
                        "src": "/static/image/wiki-image/Gold.png",
                        "alt": "Gold Farming Thumbnail",
                        "class": ""
                    }
                }
            }
        },
        "gear_farming_guide": {
            "type": "embed",
            "displayName": _("gear farming"),
            "displayNameImg": "<img src='/static/image/wiki-image/Inventory.png' alt='gear farming inventory image archero'>",
            "classButton": "collapsible gear_farming_guide",
            "collapsible_container": {
                "class_content": "gear_farming_guide_child",
                "border_color": "style='border-color: rgb(177,177,177);'",
                "content": {
                    "title": {
                        "idTitle": "title_gear_guide",
                        "innerText": _("Gear Farming Guide")
                    },
                    "description": {
                        "idDesc": "desc_gear_guide",
                        "innerText": _("TIP: Always wait for dropped items to reach your character! If you proceed to the next stage and the items did not reach your character, you will not get those items.")
                    },
                    "field": [
                        {
                        "name": _("Flying Bullets"),
                        "value": ""
                        },
                        {
                        "name": "",
                        "value": _("• Can drop more than 5 items per run")
                        },
                        {
                        "name": "",
                        "value": _("• Drops relatively many scrolls")
                        },
                        {
                        "name": "",
                        "value": "<br>"
                        },
                        {
                        "name": _("Farm Chapters :"),
                        "value": ""
                        },
                        {
                        "name": "",
                        "value": _("• Farm the highest hero boss chapter you are able to clear (7, 14, 21, 28, 35, 42)")
                        },
                        {
                        "name": "",
                        "value": _("• Making QuickRaid of weapon and bracelet hero chapters is recommended (list can be found <a class='styled_a' href='https://docs.google.com/spreadsheets/d/1gI3lxMxjVT3iLb-71kyNrAGE8a4rhAp_tSo7IDwNm3w/'>here</a>)")
                        },
                        {
                        "name": "",
                        "value": _("• Clearing normal chapter 21 or hero chapter 17 enables great rarity(green) item drops from chapters")
                        },
                        {
                        "name": "",
                        "value": _("• Clearing normal chapter 35 or hero chapter 30 enables rare rarity(blue) item drops from chapters")
                        }
                    ],
                    "footer": {
                        "innerText": _("Credit: zkn#4789")
                    },
                    "thumbnail": {
                        "src": "/static/image/wiki-image/CommonWeapon.png",
                        "alt": "Gear Farming Thumbnail",
                        "class": ""
                    }
                }
            }
        },
        "runes_guide": {
            "type": "embed",
            "displayName": _("rune"),
            "displayNameImg": "<img src='/static/image/wiki-image/Runes.png' alt='runes guide image archero'>",
            "classButton": "collapsible runes_guide",
            "collapsible_container": {
                "class_content": "runes_guide_child",
                "border_color": "style='border-color: rgb(177,177,177);'",
                "content": {
                    "title": {
                        "idTitle": "title_runes_guide",
                        "innerText": _("Runes Guide")
                    },
                    "description": {
                        "idDesc": "desc_runes_guide",
                        "innerText": _("TIP: For Power|Courage rune you can also test on the <a class='a_styled' href='/wiki/damage-calculator/'>damage emulator here</a>.")
                    },
                    "field": [
                        {
                        "name": _("🔴 Power"),
                        "value": ""
                        },
                        {
                        "name": "",
                        "value": _("All Damage +x% > Crit Chance +x% > Attack +x% > Damage to <unit type> +x% (ground, airborne, undead etc...) > Rest")
                        },
                        {
                        "name": _("🔵 Saviour"),
                        "value": ""
                        },
                        {
                        "name": "",
                        "value": _("Damage Resistance +x% > Projectile Resistance or Collision Resistance +x% > Resistance +x% > Enhanced equipment +x% > HP +x% (not as important, mostly for flexing) > Rest")
                        },
                        {
                        "name": _("🟢 Recovery"),
                        "value": ""
                        },
                        {
                        "name": "",
                        "value": _("+x% Heal and +x% HP > +x% Chance for good skill (rage, rico most important) > Rest")
                        },
                        {
                        "name": _("🟣 Courage"),
                        "value": ""
                        },
                        {
                        "name": "",
                        "value": _("Attack +x% and Attack +x > Elemental Damage +x% (optional) > +x% Base Stats for <Hero> (don't waste runes on base stats rune, it's not worth)")
                        },
                        {
                        "name": _("🟡 Luck"),
                        "value": ""
                        },
                        {
                        "name": "",
                        "value": _("HP+ and HP +% > Egg hatch boost if you have many > Counterattack Rate/Damage for CA Locket players > Rest")
                        },
                    ],
                    "footer": {
                        "innerText": ""
                    },
                    "thumbnail": {
                        "src": "/static/image/wiki-image/Runes.png",
                        "alt": "Runes Thumbnail",
                        "class": ""
                    }
                }
            }
        },
    },
    "other": {
        "evo_cost": {
            "type": "img",
            "displayName": _("hero evolution cost"),
            "displayNameImg": "<img src='/static/image/wiki-image/cookie.png' alt='cookie image archero'><img src='/static/image/wiki-image/Random_HeroFragment.png' alt='shards image archero'>",
            "classButton": "collapsible evo_cost",
            "collapsible_container": {
                "class_content": "evo_cost",
                "content": {
                    "field": {
                        "src": "image/wiki-image/EvolutionCost.webp",
                        "class": "evo_cost_img",
                        "alt": "Evolution cost Archero"
                    }
                }
            }
        },
        "glyphs": {
            "type": "embed",
            "displayName": _("glyphs"),
            "displayNameImg": "<img src='/static/image/wiki-image/RandomGlyph.png' alt='glyph guide image archero'>",
            "classButton": "collapsible glyphs",
            "collapsible_container": {
                "class_content": "glyphs",
                "border_color": "style='border-color: rgb(177,177,177);'",
                "content": {
                    "title": {
                        "idTitle": "title_glyph_guide",
                        "innerText": _("Glyphs: ")
                    },
                    "description": {
                        "idDesc": "desc_glyph_guide",
                        "innerText": "<a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/refinement_guide/' target='_blank'>reddit guide</a>"
                    },
                    "field": [
                        {
                        "name": _("There is 2 type of glyphs :"),
                        "value": _("• Base Glyphs (without rank)<br>• Special Glyphs (rank A / S / SS)")
                        },
                        {
                        "name": _("How to get glyphs ??"),
                        "value": _("- you need to sacrifice stuff starting from epic to ancient legendary")
                        },
                        {
                        "name": "",
                        "value": _("- When you sacrificed your stuff you can get random rarity & number of the same glyphs")
                        },
                        {
                        "name": "",
                        "value": _("- There is a chance you will get duplicates of the same Glyphs.")
                        },
                        {
                        "name": "",
                        "value": _("- Each item gives different glyphs, S Item always gives special glyphs (S/SS) (S item are obtainable in obsidian or prisma chest)")
                        }
                    ],
                    "footer": {
                        "innerText": _("Glyph System - Unlocked at Chapter 17, you will need a Legendary item in order to access it.")
                    },
                    "thumbnail": {
                        "src": "",
                        "alt": "",
                        "class": ""
                    }
                }
            }
        },
        "refinement": {
        "type": "embed",
        "displayName": _("refinements guide"),
        "displayNameImg": "<img src='/static/image/wiki-image/RandomGlyph.png' alt='refinement guide image archero'>",
        "classButton": "collapsible refinement",
        "collapsible_container": {
            "class_content": "refinement",
            "border_color": "style='border-color: rgb(177,177,177);'",
            "content": {
            "title": {
                "idTitle": "title_refinement_guide",
                "innerText": _("Refine: ")
            },
            "description": {
                "idDesc": "desc_refinement_guide",
                "innerText": "<a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/refinement_guide/' target='_blank'>reddit guide</a>"
            },
            "field": [
                {
                "name": _("How to unlock them:"),
                "value": _("Refinement rarity starts at Epic, to unlock the second slot, Perfect Epic, you need to refine 8 times. Same goes for the next rarities.")
                },
                {
                "name": "",
                "value": _("• 1st Slot (Epic) → Can only equip Normal Glyphs")
                },
                {
                "name": "",
                "value": _("• 2nd Slot (Perfect Epic) → Unlocks Special Glyph slot")
                },
                {
                "name": "",
                "value": _("• 3rd Slot (Legendary) → Unlocks Normal Glyph slot")
                },
                {
                "name": "",
                "value": _("• 4th Slot (Ancient Legendary) → Unlocks Normal Glyph slot")
                }
            ],
            "footer": {
                "innerText": "<a class='styled_a' href='https://docs.google.com/spreadsheets/d/1Z0bGaCJ8EuKZQSqeW8q1eS5bWl_5z6E237-JAuf9pFk' target='_blank'>Glyph Sheets</a>"
            },
            "thumbnail": {
                "src": "",
                "alt": "",
                "class": ""
            }
            }
        }
        },
        "quickraid": {
        "type": "img",
        "displayName": _("quick raid rewards"),
        "displayNameImg": "<img src='/static/image/wiki-image/Quickraid_icon.png' alt='quickraid icon image archero'>",
        "classButton": "collapsible quickraid",
        "collapsible_container": {
            "class_content": "quickraid",
            "content": {
            "field": {
                "src": "image/wiki-image/qr_chart.webp",
                "class": "qr-chart-img",
                "alt": "Archero quickraid drop"
            }
            }
        }
        },
        "altar_cost": {
        "type": "embed",
        "displayName": _("altar cost"),
        "displayNameImg": "<img src='/static/image/wiki-image/BloodthirstStone.png' alt='bloodthirst stone image archero'>",
        "classButton": "collapsible altar_cost",
        "collapsible_container": {
            "class_content": "altar_cost_content",
            "border_color": "style='border-color: rgb(177,177,177);'",
            "content": {
            "title": {
                "idTitle": "altar_cost_title",
                "innerText": _("Altar Cost lvl0 to 120")
            },
            "description": {
                "idDesc": "altar_cost_desc",
                "innerText": ""
            },
            "field": [
                {
                "name": "",
                "value": "0 <i class='fa-solid fa-arrow-right'></i> 5 = 5 x 5 BS<br>5 <i class='fa-solid fa-arrow-right'></i> 10 = 5 x 10 BS"
                },
                {
                "name": _("Ascension n°10 = 100 BS"),
                "value": "10 <i class='fa-solid fa-arrow-right'></i> 15 = 5 x 20 BS<br>15 <i class='fa-solid fa-arrow-right'></i> 20 = 5 x 30 BS"
                },
                {
                "name": _("Ascension n°20 = 250 BS"),
                "value": "20 <i class='fa-solid fa-arrow-right'></i> 25 = 5 x 50 BS<br>25 <i class='fa-solid fa-arrow-right'></i> 30 = 5 x 70 BS"
                },
                {
                "name": _("Ascension n°30 = 450 BS"),
                "value": "30 <i class='fa-solid fa-arrow-right'></i> 35 = 5 x 100 BS<br>35 <i class='fa-solid fa-arrow-right'></i> 40 = 5 x 150 BS"
                },
                {
                "name": _("Ascension n°40 = 750 BS"),
                "value": "40 <i class='fa-solid fa-arrow-right'></i> 45 = 5 x 200 BS<br>45 <i class='fa-solid fa-arrow-right'></i> 50 = 5 x 250 BS"
                },
                {
                "name": _("Ascension n°50 = 1250 BS"),
                "value": "50 <i class='fa-solid fa-arrow-right'></i> 55 = 5 x 300 BS<br>55 <i class='fa-solid fa-arrow-right'></i> 60 = 5 x 350 BS"
                },
                {
                "name": _("Ascension n°60 = 2000 BS"),
                "value": "60 <i class='fa-solid fa-arrow-right'></i> 65 = 5 x 400 BS<br>65 <i class='fa-solid fa-arrow-right'></i> 70 = 5 x 450 BS"
                },
                {
                "name": _("Ascension n°70 = 3000 BS"),
                "value": "70 <i class='fa-solid fa-arrow-right'></i> 75 = 5 x 500 BS<br>75 <i class='fa-solid fa-arrow-right'></i> 80 = 5 x 600 BS"
                },
                {
                "name": _("Ascension n°80 = 4000 BS"),
                "value": "80 <i class='fa-solid fa-arrow-right'></i> 85 = 5 x 700 BS<br>85 <i class='fa-solid fa-arrow-right'></i> 90 = 5 x 800 BS"
                },
                {
                "name": _("Ascension n°90 = 5000 BS"),
                "value": "90 <i class='fa-solid fa-arrow-right'></i> 95 = 5 x 900 BS<br>95 <i class='fa-solid fa-arrow-right'></i> 100 = 5 x 1000 BS"
                },
                {
                "name": _("Ascension n°100 = 7500 BS"),
                "value": "100 <i class='fa-solid fa-arrow-right'></i> 105 = 5 x 1200 BS<br>105 <i class='fa-solid fa-arrow-right'></i> 110 = 5 x 1400 BS"
                },
                {
                "name": _("Ascension n°110 = 10000 BS"),
                "value": "110 <i class='fa-solid fa-arrow-right'></i> 115 = 5 x 1600 BS<br>115 <i class='fa-solid fa-arrow-right'></i> 120 = 5 x 1800 BS"
                }
            ],
            "footer": {
                "innerText": "BS <i class='fa-solid fa-arrow-right'></i> Bloodthirst Stones <object type='image/png' data='/static/image/svg/bloodthirst_stone.svg' width='16' height='16'></object> (<a class='styled_a' href='https://www.reddit.com/r/Archero/wiki/faq/#wiki_where_do_i_find_bloodthirst_stones.3F'>what is bloodstone ?</a>)"
            },
            "thumbnail": {
                "src": "",
                "alt": "",
                "class": ""
            }
            }
        }
        },
        "altar_boost": {
        "type": "embed",
        "displayName": _("altar bonus ascensions"),
        "displayNameImg": "<img src='/static/image/wiki-image/AltarImage.png' alt='archero altar boosts'>",
        "classButton": "collapsible altar_boost",
        "collapsible_container": {
            "class_content": "altar_boost_content",
            "border_color": "style='border-color: rgb(177,177,177);'",
            "content": {
            "title": {
                "idTitle": "altar_boost_title",
                "innerText": _("Altar Bonus Ascensions")
            },
            "description": {
                "idDesc": "altar_boost_desc",
                "innerText": ""
            },
            "field": [
                {
                "name": _("Lvl 10, 40, 70 and 100 :"),
                "value": "• Hp +5%"
                },
                {
                "name": "",
                "value": "<br><br>"
                },
                {
                "name": _("Lvl 20, 50, 80 and 110 :"),
                "value": _("• Attack +5%")
                },
                {
                "name": "",
                "value": "<br><br>"
                },
                {
                "name": _("Lvl 30, 60, 90 and 120: "),
                "value": _("• (Gear Altar) Red Heart Healing Effect +5%<br>• (Hero Altar) Red Heart Drop Rate +5%")
                },
                {
                "name": "",
                "value": "<br><br>"
                },
                {
                "name": _("Overall bonus :"),
                "value": _("• (Gear Altar) Item Base Stats Enhanced +[x]%")
                },
                {
                "name": "",
                "value": _("• (Gear Altar lvl30) Equipment Droprate +[x]%")
                },
                {
                "name": "",
                "value": _("• (Hero Altar) Hero Base Stats +[x]%")
                },
                {
                "name": "",
                "value": _("• (Hero Altar lvl50) Damage to Elite Enemies +[x]%")
                }
            ],
            "footer": {
                "innerText": ""
            },
            "thumbnail": {
                "src": "",
                "alt": "",
                "class": ""
            }
            }
        }
        },
        "egg_stats": {
        "type": "embed",
        "displayName": _("egg stats"),
        "displayNameImg": "<img src='/static/image/wiki-image/Egg_icon.png' alt='egg icon archero'>",
        "classButton": "collapsible egg_stats",
        "collapsible_container": {
            "class_content": "egg_stats_content",
            "border_color": "style='border-color: rgb(177,177,177);'",
            "content": {
            "title": {
                "idTitle": "title_egg_stats",
                "innerText": _("Archero Hatchery and Egg Farming Compilation (edited by @Abstrusity, @Luhcaran, @Shusaku, @𝗺𝗿𝗯)")
            },
            "description": {
                "idDesc": "desc_egg_stats",
                "innerText": ""
            },
            "field": [
                {
                "name": _("Includes"),
                "value": _("• List of available Monsters")
                },
                {
                "name": "",
                "value": _("• Numbers of kills required to hatch or complete quests")
                },
                {
                "name": "",
                "value": _("• Completed quest dialogue")
                },
                {
                "name": "",
                "value": _("• Automated hatch timers")
                },
                {
                "name": "",
                "value": _("• Where to find each Monster and which locations are recommended")
                },
                {
                "name": "",
                "value": _("• Monster training bonuses and costs (still Work in Progress)")
                },
                {
                "name": "",
                "value": "<a class='styled_a' href='https://docs.google.com/spreadsheets/d/1p0xAb6ZrgwqhynromVXTqJSsfWlK1W8EDDt2HyvmRKE' target='_blank'>Google Sheets</a>"
                }    
            ],
            "footer": {
                "innerText": _("Initially made by LanderZ")
            },
            "thumbnail": {
                "src": "",
                "alt": "",
                "class": ""
            }
            }
        }
        },
        "hidden_stats": {
        "type": "embed",
        "displayName": _("hidden stats"),
        "displayNameImg": "<img src='/static/image/img-sidebar/theorycraft.png' alt='archero calculation magnifying glass image archero'>",
        "classButton": "collapsible hidden_stats",
        "collapsible_container": {
            "class_content": "hidden_stats_content",
            "border_color": "style='border-color: rgb(177,177,177);'",
            "content": {
            "title": {
                "idTitle": "title_refine_stats",
                "innerText": _("Stats unlocked when reaching Mythic Refinement")
            },
            "description": {
                "idDesc": "desc_refine_stats",
                "innerText": ""
            },
            "field": [
                {
                "name": "",
                "value": _("•  Weapon → For a brief while after taking damage, the next hit fires an extra shot.")
                },
                {
                "name": "",
                "value": _("•  Armor → The Higher the HP, the higher the Attack.")
                },
                {
                "name": "",
                "value": _("•  Ring n°1 → While Standing still reduces incoming Bullets Damage.")
                },
                {
                "name": "",
                "value": _("•  Ring n°2 → While Standing still reduces incoming Colision Damage.")
                },
                {
                "name": "",
                "value": _("•  Bracelet → When recovering HP in the Angel room, there is a chance to receive 3x healing.")
                },
                {
                "name": "",
                "value": _("•  Pets n°1 & Pets n°2 → After 2 attacks, the next attack deals double damage. ")
                },
                {
                "name": "",
                "value": _("•  Locket → For the first 3s after entering a room, increases movement speed.")
                },
                {
                "name": "",
                "value": _("•  SpellBook → SpellBook can gain energy from Hearts.")
                },
                {
                "name": _("Comments"),
                "value": _("•  Pets n°1 & Pets n°2 → Works only for the pet attack.")
                }
            ],
            "footer": {
                "innerText": ""
            },
            "thumbnail": {
                "src": "",
                "alt": "",
                "class": ""
            }
            }
        }
        }
    }
  },
  "Theorycraft": [
    {
      "id_item": "diagonal_arrows",
      "type":"skills",
      "image_header": {
        "src": "skill/diagonal_arrows.png",
        "alt": "diagonal arrow skill image"
      },
      "content": {
        "title": "Diagonal Arrow",
        "description": [
          "-20% melee dmg",
          "-40% with 2x"
        ],
        "href":"/wiki/skill-list/Diagonal_Arrows/"
      }
    },
    {
      "id_item": "side_arrow",
      "type":"skills",
      "image_header": {
        "src": "skill/side_arrow.png",
        "alt": "side arrow skill image"
      },
      "content": {
        "title": "Side Arrows",
        "description": [
          "-20% melee dmg",
          "-20% with 2x (2nd one doesn't reduce)"
        ],
        "href":"/wiki/skill-list/Side_Arrow/"
      }
    },
    {
      "id_item": "rear_arrow",
      "type":"skills",
      "image_header": {
        "src": "skill/rear_arrow.png",
        "alt": "rear arrow skill image"
      },
      "content": {
        "title": "Rear Arrow",
        "description": [
          "+15% melee dmg"
        ],
        "href":"/wiki/skill-list/Rear_Arrow/"
      }
    },
    {
      "id_item": "multishot",
      "type":"skills",
      "image_header": {
        "src": "skill/multishot.png",
        "alt": "multishot skill image"
      },
      "content": {
        "title": "Multishot",
        "description": [
          "-5% melee dmg"
        ],
        "href":"/wiki/skill-list/Multishot/"
      }
    },
    {
      "id_item": "price_of_strength",
      "type":"skills",
      "image_header": {
        "src": "skill/price_of_strength.png",
        "alt": "price_of_strength"
      },
      "content": {
        "title": "Price Of Strength",
        "description": [
          "Buffs/Debuffs =>",
          "8second :  10% movespeed, 40% atk, regular dmg taken, 10% size, normal atkspd, 10% melee damage boost, 15% crit rate",
          "2second :  -5% movespeed, 28% atk, 1.1x dmg taken, 5% size, -15% atkspd, 10% melee damage boost",
          "6second :  -15% movespeed, -12% atk, 1.2x dmg taken, -5% size, -15% atkspd"
        ],
        "href":"/wiki/skill-list/Price_of_Strength/"
      }
    }
  ]
}
