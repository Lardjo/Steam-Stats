#!/usr/bin/env python3
# All right reserved 2013
# Description: Dota 2 Library
# URL: http://github.com/Lardjo

mode = {1: {"name": 'All Pick'},
        2: {'name': 'Captains Mode'},
        3: {'name': 'Random Draft'},
        4: {'name': 'Single Draft'},
        5: {'name': 'All Random'},
        7: {'name': 'Diretide'},
        9: {'name': 'Greeviling'},
        12: {'name': 'Least Played'},
        13: {'name': 'Limited Hero'},
        14: {'name': 'Compendium Matchmaking'},
        16: {'name': 'Captains Draft'}}

cluster = {111: {'name': 'US West'},
           112: {'name': 'US West'},
           121: {'name': 'US East'},
           122: {'name': 'US East'},
           123: {'name': 'US East'},
           131: {'name': 'Europe West'},
           132: {'name': 'Europe West'},
           133: {'name': 'Europe West'},
           134: {'name': 'Europe West'},
           135: {'name': 'Europe West'},
           136: {'name': 'Europe West'},
           143: {'name': 'Hong Kong'},
           151: {'name': 'Southeast Asia'},
           152: {'name': 'Southeast Asia'},
           153: {'name': 'Southeast Asia'},
           161: {'name': 'China'},
           163: {'name': 'China'},
           171: {'name': 'Australia'},
           181: {'name': 'Russia'},
           182: {'name': 'Russia'},
           183: {'name': 'Russia'},
           184: {'name': 'Russia'},
           191: {'name': 'Europe East'},
           200: {'name': 'South America'},
           211: {'name': 'South Africa'},
           221: {'name': 'China'},
           222: {'name': 'China'}}

heroes = {1: {'name': 'Antimage', 'avatar': 'img/dota/heroes/antimage.png'},
          2: {'name': 'Axe', 'avatar': 'img/dota/heroes/axe.png'},
          3: {'name': 'Ban', 'avatar': 'img/dota/heroes/bane.png'},
          4: {'name': 'Bloodseeker', 'avatar': 'img/dota/heroes/bloodseeker.png'},
          5: {'name': 'Crystal Maiden', 'avatar': 'img/dota/heroes/crystal_maiden.png'},
          6: {'name': 'Drow Ranger', 'avatar': 'img/dota/heroes/drow_ranger.png'},
          7: {'name': 'Earthshaker', 'avatar': 'img/dota/heroes/earthshaker.png'},
          8: {'name': 'Juggernaut', 'avatar': 'img/dota/heroes/juggernaut.png'},
          9: {'name': 'Mirana', 'avatar': 'img/dota/heroes/mirana.png'},
          10: {'name': 'Morphling', 'avatar': 'img/dota/heroes/morphling.png'},
          11: {'name': 'Shadow Fiend', 'avatar': 'img/dota/heroes/nevermore.png'},
          12: {'name': 'Phantom Lancer', 'avatar': 'img/dota/heroes/phantom_lancer.png'},
          13: {'name': 'Puck', 'avatar': 'img/dota/heroes/puck.png'},
          14: {'name': 'Pudge', 'avatar': 'img/dota/heroes/pudge.png'},
          15: {'name': 'Razor', 'avatar': 'img/dota/heroes/razor.png'},
          16: {'name': 'Sand King', 'avatar': 'img/dota/heroes/sand_king.png'},
          17: {'name': 'Storm Spirit', 'avatar': 'img/dota/heroes/storm_spirit.png'},
          18: {'name': 'Sven', 'avatar': 'img/dota/heroes/sven.png'},
          19: {'name': 'Tiny', 'avatar': 'img/dota/heroes/tiny.png'},
          20: {'name': 'Vengeful Spirit', 'avatar': 'img/dota/heroes/vengefulspirit.png'},
          21: {'name': 'Windranger', 'avatar': 'img/dota/heroes/windrunner.png'},
          22: {'name': 'Zeus', 'avatar': 'img/dota/heroes/zuus.png'},
          23: {'name': 'Kunkka', 'avatar': 'img/dota/heroes/kunkka.png'},
          25: {'name': 'Lina', 'avatar': 'img/dota/heroes/lina.png'},
          26: {'name': 'Lion', 'avatar': 'img/dota/heroes/lion.png'},
          27: {'name': 'Shadow Shaman', 'avatar': 'img/dota/heroes/shadow_shaman.png'},
          28: {'name': 'Slardar', 'avatar': 'img/dota/heroes/slardar.png'},
          29: {'name': 'Tidehunter', 'avatar': 'img/dota/heroes/tidehunter.png'},
          30: {'name': 'Witch Doctor', 'avatar': 'img/dota/heroes/witch_doctor.png'},
          31: {'name': 'Lich', 'avatar': 'img/dota/heroes/lich.png'},
          32: {'name': 'Riki', 'avatar': 'img/dota/heroes/riki.png'},
          33: {'name': 'Enigma', 'avatar': 'img/dota/heroes/enigma.png'},
          34: {'name': 'Tinker', 'avatar': 'img/dota/heroes/tinker.png'},
          35: {'name': 'Sniper', 'avatar': 'img/dota/heroes/sniper.png'},
          36: {'name': 'Necrophos', 'avatar': 'img/dota/heroes/necrolyte.png'},
          37: {'name': 'Warlock', 'avatar': 'img/dota/heroes/warlock.png'},
          38: {'name': 'Beastmaster', 'avatar': 'img/dota/heroes/beastmaster.png'},
          39: {'name': 'Queen of Pain', 'avatar': 'img/dota/heroes/queenofpain.png'},
          40: {'name': 'Venomancer', 'avatar': 'img/dota/heroes/venomancer.png'},
          41: {'name': 'Faceless Void', 'avatar': 'img/dota/heroes/faceless_void.png'},
          42: {'name': 'Skeleton King', 'avatar': 'img/dota/heroes/skeleton_king.png'},
          43: {'name': 'Death Prophet', 'avatar': 'img/dota/heroes/death_prophet.png'},
          44: {'name': 'Phantom Assassin', 'avatar': 'img/dota/heroes/phantom_assassin.png'},
          45: {'name': 'Pugna', 'avatar': 'img/dota/heroes/pugna.png'},
          46: {'name': 'Templar Assassin', 'avatar': 'img/dota/heroes/templar_assassin.png'},
          47: {'name': 'Viper', 'avatar': 'img/dota/heroes/viper.png'},
          48: {'name': 'Luna', 'avatar': 'img/dota/heroes/luna.png'},
          49: {'name': 'Dragon Knight', 'avatar': 'img/dota/heroes/dragon_knight.png'},
          50: {'name': 'Dazzle', 'avatar': 'img/dota/heroes/dazzle.png'},
          51: {'name': 'Clockwerk', 'avatar': 'img/dota/heroes/rattletrap.png'},
          52: {'name': 'Leshrac', 'avatar': 'img/dota/heroes/leshrac.png'},
          53: {'name': 'Nature\'s Prophet', 'avatar': 'img/dota/heroes/furion.png'},
          54: {'name': 'Lifestealer', 'avatar': 'img/dota/heroes/life_stealer.png'},
          55: {'name': 'Dark Seer', 'avatar': 'img/dota/heroes/dark_seer.png'},
          56: {'name': 'Clinkz', 'avatar': 'img/dota/heroes/clinkz.png'},
          57: {'name': 'Omniknight', 'avatar': 'img/dota/heroes/omniknight.png'},
          58: {'name': 'Enchantress', 'avatar': 'img/dota/heroes/enchantress.png'},
          59: {'name': 'Huskar', 'avatar': 'img/dota/heroes/huskar.png'},
          60: {'name': 'Night Stalker', 'avatar': 'img/dota/heroes/night_stalker.png'},
          61: {'name': 'Broodmother', 'avatar': 'img/dota/heroes/broodmother.png'},
          62: {'name': 'Bounty Hunter', 'avatar': 'img/dota/heroes/bounty_hunter.png'},
          63: {'name': 'Weaver', 'avatar': 'img/dota/heroes/weaver.png'},
          64: {'name': 'Jakiro', 'avatar': 'img/dota/heroes/jakiro.png'},
          65: {'name': 'Batrider', 'avatar': 'img/dota/heroes/batrider.png'},
          66: {'name': 'Chen', 'avatar': 'img/dota/heroes/chen.png'},
          67: {'name': 'Spectre', 'avatar': 'img/dota/heroes/spectre.png'},
          68: {'name': 'Ancient Apparition', 'avatar': 'img/dota/heroes/ancient_apparition.png'},
          69: {'name': 'Doom Bringer', 'avatar': 'img/dota/heroes/doom_bringer.png'},
          70: {'name': 'Ursa', 'avatar': 'img/dota/heroes/ursa.png'},
          71: {'name': 'Spirit Breaker', 'avatar': 'img/dota/heroes/spirit_breaker.png'},
          72: {'name': 'Gyrocopter', 'avatar': 'img/dota/heroes/gyrocopter.png'},
          73: {'name': 'Alchemist', 'avatar': 'img/dota/heroes/alchemist.png'},
          74: {'name': 'Invoker', 'avatar': 'img/dota/heroes/invoker.png'},
          75: {'name': 'Silencer', 'avatar': 'img/dota/heroes/silencer.png'},
          76: {'name': 'Outworld Destroyer', 'avatar': 'img/dota/heroes/obsidian_destroyer.png'},
          77: {'name': 'Lycan', 'avatar': 'img/dota/heroes/lycan.png'},
          78: {'name': 'Brewmaster', 'avatar': 'img/dota/heroes/brewmaster.png'},
          79: {'name': 'Shadow Demon', 'avatar': 'img/dota/heroes/shadow_demon.png'},
          80: {'name': 'Lone Druid', 'avatar': 'img/dota/heroes/lone_druid.png'},
          81: {'name': 'Chaos Knight', 'avatar': 'img/dota/heroes/chaos_knight.png'},
          82: {'name': 'Meepo', 'avatar': 'img/dota/heroes/meepo.png'},
          83: {'name': 'Treant Protector', 'avatar': 'img/dota/heroes/treant.png'},
          84: {'name': 'Ogre Magi', 'avatar': 'img/dota/heroes/ogre_magi.png'},
          85: {'name': 'Undying', 'avatar': 'img/dota/heroes/undying.png'},
          86: {'name': 'Rubick', 'avatar': 'img/dota/heroes/rubick.png'},
          87: {'name': 'Disruptor', 'avatar': 'img/dota/heroes/disruptor.png'},
          88: {'name': 'Nyx Assassin', 'avatar': 'img/dota/heroes/nyx_assassin.png'},
          89: {'name': 'Naga Siren', 'avatar': 'img/dota/heroes/naga_siren.png'},
          90: {'name': 'Keeper of the Light', 'avatar': 'img/dota/heroes/keeper_of_the_light.png'},
          91: {'name': 'Io', 'avatar': 'img/dota/heroes/wisp.png'},
          92: {'name': 'Visage', 'avatar': 'img/dota/heroes/visage.png'},
          93: {'name': 'Slark', 'avatar': 'img/dota/heroes/slark.png'},
          94: {'name': 'Medusa', 'avatar': 'img/dota/heroes/medusa.png'},
          95: {'name': 'Troll Warlord', 'avatar': 'img/dota/heroes/troll_warlord.png'},
          96: {'name': 'Centaur Warrunner', 'avatar': 'img/dota/heroes/centaur.png'},
          97: {'name': 'Magnus', 'avatar': 'img/dota/heroes/magnataur.png'},
          98: {'name': 'Timbersaw', 'avatar': 'img/dota/heroes/shredder.png'},
          99: {'name': 'Bristleback', 'avatar': 'img/dota/heroes/bristleback.png'},
          100: {'name': 'Tusk', 'avatar': 'img/dota/heroes/tusk.png'},
          101: {'name': 'Skywrath Mage', 'avatar': 'img/dota/heroes/skywrath_mage.png'},
          102: {'name': 'Elder Titan', 'avatar': 'img/dota/heroes/elder_titan.png'},
          103: {'name': 'Abaddon', 'avatar': 'img/dota/heroes/abaddon.png'},
          106: {'name': 'Ember Spirit', 'avatar': 'img/dota/heroes/ember_spirit.png'},
          107: {'name': 'Earth Spirit', 'avatar': 'img/dota/heroes/earth_spirit.png'}}

items = {0: {'avatar': 'holder.js/60x45/text:Empty'},
         1: {'name': 'Blink Dagger', 'avatar': 'img/dota/items/blink_dagger.png'},
         2: {'name': 'Blades of Attack', 'avatar': 'img/dota/items/blades_of_attack.png'},
         3: {'name': 'Broadsword', 'avatar': 'img/dota/items/broadsword.png'},
         4: {'name': 'Chainmail', 'avatar': 'img/dota/items/chainmail.png'},
         5: {'name': 'Claymore', 'avatar': 'img/dota/items/claymore.png'},
         6: {'name': 'Helm of Iron Will', 'avatar': 'img/dota/items/helm_of_iron_will.png'},
         7: {'name': 'Javelin', 'avatar': 'img/dota/items/javelin.png'},
         8: {'name': 'Mithril Hammer', 'avatar': 'img/dota/items/mithril_hammer.png'},
         9: {'name': 'Platemail', 'avatar': 'img/dota/items/platemail.png'},
         10: {'name': 'Quarterstaff', 'avatar': 'img/dota/items/quarterstaff.png'},
         11: {'name': 'Quelling Blade', 'avatar': 'img/dota/items/quelling_blade.png'},
         12: {'name': 'Ring of Protection', 'avatar': 'img/dota/items/ring_of_protection.png'},
         13: {'name': 'Gauntlets of Strength', 'avatar': 'img/dota/items/gauntlets_of_strength.png'},
         14: {'name': 'Slippers of Agility', 'avatar': 'img/dota/items/slippers_of_agility.png'},
         15: {'name': 'Mantle of Intelligence', 'avatar': 'img/dota/items/mantle_of_intelligence.png'},
         16: {'name': 'Iron Branch', 'avatar': 'img/dota/items/iron_branch.png'},
         17: {'name': 'Belt of Strength', 'avatar': 'img/dota/items/belt_of_strength.png'},
         18: {'name': 'Band of Elvenskin', 'avatar': 'img/dota/items/band_of_elvenskin.png'},
         19: {'name': 'Robe of the Magi', 'avatar': 'img/dota/items/robe_of_the_magi.png'},
         20: {'name': 'Circlet', 'avatar': 'img/dota/items/circlet.png'},
         21: {'name': 'Ogre Club', 'avatar': 'img/dota/items/ogre_club.png'},
         22: {'name': 'Blade of Alacrity', 'avatar': 'img/dota/items/blade_of_alacrity.png'},
         23: {'name': 'Staff of Wizardry', 'avatar': 'img/dota/items/staff_of_wizardry.png'},
         24: {'name': 'Ultimate Orb', 'avatar': 'img/dota/items/ultimate_orb.png'},
         25: {'name': 'Gloves of Haste', 'avatar': 'img/dota/items/gloves_of_haste.png'},
         26: {'name': 'Morbid Mask', 'avatar': 'img/dota/items/morbid_mask.png'},
         27: {'name': 'Ring of Regen', 'avatar': 'img/dota/items/ring_of_regen.png'},
         28: {'name': 'Sage\'s Mask', 'avatar': 'img/dota/items/sages_mask.png'},
         29: {'name': 'Boots of Speed', 'avatar': 'img/dota/items/boots_of_speed.png'},
         30: {'name': 'Gem of True Sight', 'avatar': 'img/dota/items/gem_of_true_sight.png'},
         31: {'name': 'Cloak', 'avatar': 'img/dota/items/cloak.png'},
         32: {'name': 'Talisman of Evasion', 'avatar': 'img/dota/items/talisman_of_evasion.png'},
         33: {'name': 'Cheese', 'avatar': 'img/dota/items/cheese.png'},
         34: {'name': 'Magic Stick', 'avatar': 'img/dota/items/magic_stick.png'},
         35: {'name': 'Recipe: Magic Wand', 'avatar': 'img/dota/items/recipe_scroll.png'},
         36: {'name': 'Magic Wand', 'avatar': 'img/dota/items/magic_wand.png'},
         37: {'name': 'Ghost Scepter', 'avatar': 'img/dota/items/ghost_scepter.png'},
         38: {'name': 'Clarity', 'avatar': 'img/dota/items/clarity.png'},
         39: {'name': 'Healing Salve', 'avatar': 'img/dota/items/healing_salve.png'},
         40: {'name': 'Dust of Appearance', 'avatar': 'img/dota/items/dust_of_appearance.png'},
         41: {'name': 'Bottle', 'avatar': 'img/dota/items/bottle.png'},
         42: {'name': 'Observer Ward', 'avatar': 'img/dota/items/observer_ward.png'},
         43: {'name': 'Sentry Ward', 'avatar': 'img/dota/items/sentry_ward.png'},
         44: {'name': 'Tango', 'avatar': 'img/dota/items/tango.png'},
         45: {'name': 'Courier', 'avatar': 'img/dota/items/courier.png'},
         46: {'name': 'Teleport Scroll', 'avatar': 'img/dota/items/town_portal_scroll.png'},
         48: {'name': 'Travel Boots', 'avatar': 'img/dota/items/boots_of_travel.png'},
         50: {'name': 'Phase Boots', 'avatar': 'img/dota/items/phase_boots.png'},
         51: {'name': 'Demon Edge', 'avatar': 'img/dota/items/demon_edge.png'},
         52: {'name': 'Eaglesong', 'avatar': 'img/dota/items/eaglesong.png'},
         53: {'name': 'Reaver', 'avatar': 'img/dota/items/reaver.png'},
         54: {'name': 'Sacred Relic', 'avatar': 'img/dota/items/sacred_relic.png'},
         55: {'name': 'Hyperstone', 'avatar': 'img/dota/items/hyperstone.png'},
         56: {'name': 'Ring of Health', 'avatar': 'img/dota/items/ring_of_health.png'},
         57: {'name': 'Void Stone', 'avatar': 'img/dota/items/void_stone.png'},
         58: {'name': 'Mystic Staff', 'avatar': 'img/dota/items/mystic_staff.png'},
         59: {'name': 'Energy Booster', 'avatar': 'img/dota/items/energy_booster.png'},
         60: {'name': 'Point Booster', 'avatar': 'img/dota/items/point_booster.png'},
         61: {'name': 'Vitality Booster', 'avatar': 'img/dota/items/vitality_booster.png'},
         63: {'name': 'Power Treads', 'avatar': 'img/dota/items/power_treads.png'},
         65: {'name': 'Hand of Midas', 'avatar': 'img/dota/items/hand_of_midas.png'},
         67: {'name': 'Oblivion Staff', 'avatar': 'img/dota/items/oblivion_staff.png'},
         69: {'name': 'Perseverance', 'avatar': 'img/dota/items/perseverance.png'},
         71: {'name': 'Poor Man\'s Shield', 'avatar': 'img/dota/items/poor_mans_shield.png'},
         73: {'name': 'Bracer', 'avatar': 'img/dota/items/bracer.png'},
         75: {'name': 'Wraith Band', 'avatar': 'img/dota/items/wraith_band.png'},
         77: {'name': 'Null Talisman', 'avatar': 'img/dota/items/null_talisman.png'},
         79: {'name': 'Mekansm', 'avatar': 'img/dota/items/mekansm.png'},
         81: {'name': 'Vladmir\'s Offering', 'avatar': 'img/dota/items/vladmirs_offering.png'},
         86: {'name': 'Buckler', 'avatar': 'img/dota/items/buckler.png'},
         88: {'name': 'Ring of Basilius', 'avatar': 'img/dota/items/ring_of_basilius.png'},
         90: {'name': 'Pipe of Insight', 'avatar': 'img/dota/items/pipe_of_insight.png'},
         92: {'name': 'Urn of Shadows', 'avatar': 'img/dota/items/urn_of_shadows.png'},
         94: {'name': 'Headdress', 'avatar': 'img/dota/items/headdress.png'},
         96: {'name': 'Scythe of Vyse', 'avatar': 'img/dota/items/scythe_of_vyse.png'},
         98: {'name': 'Orchid Malevolence', 'avatar': 'img/dota/items/orchid_malevolence.png'},
         100: {'name': 'Euls Scepter of Divinity', 'avatar': 'img/dota/items/euls_scepter_of_divinity.png'},
         102: {'name': 'Force Staff', 'avatar': 'img/dota/items/force_staff.png'},
         104: {'name': 'Dagon Level 1', 'avatar': 'img/dota/items/dagon_1.png'},
         108: {'name': 'Aghanim\'s Scepter', 'avatar': 'img/dota/items/aghanims_scepter.png'},
         110: {'name': 'Refresher Orb', 'avatar': 'img/dota/items/refresher_orb.png'},
         112: {'name': 'Assault Cuirass', 'avatar': 'img/dota/items/assault_cuirass.png'},
         114: {'name': 'Heart of Tarrasque', 'avatar': 'img/dota/items/heart_of_tarrasque.png'},
         117: {'name': 'Aegis', 'avatar': 'img/dota/items/aegis.png'},
         119: {'name': 'Shiva\'s Guard', 'avatar': 'img/dota/items/shivas_guard.png'},
         116: {'name': 'Black King Bar', 'avatar': 'img/dota/items/black_king_bar.png'},
         121: {'name': 'Bloodstone', 'avatar': 'img/dota/items/bloodstone.png'},
         122: {'name': 'Recipe: Linken\'s Sphere', 'avatar': 'img/dota/items/recipe_scroll.png'},
         123: {'name': 'Linken\'s Sphere', 'avatar': 'img/dota/items/linkens_sphere.png'},
         125: {'name': 'Vanguard', 'avatar': 'img/dota/items/vanguard.png'},
         127: {'name': 'Blade Mail', 'avatar': 'img/dota/items/blade_mail.png'},
         131: {'name': 'Hood of Defiance', 'avatar': 'img/dota/items/hood_of_defiance.png'},
         133: {'name': 'Divine Rapier', 'avatar': 'img/dota/items/divine_rapier.png'},
         135: {'name': 'Monkey King Bar', 'avatar': 'img/dota/items/monkey_king_bar.png'},
         137: {'name': 'Radiance', 'avatar': 'img/dota/items/radiance.png'},
         139: {'name': 'Butterfly', 'avatar': 'img/dota/items/butterfly.png'},
         140: {'name': 'Recipe: Daedalus', 'avatar': 'img/dota/items/recipe_scroll.png'},
         141: {'name': 'Daedalus', 'avatar': 'img/dota/items/daedalus.png'},
         143: {'name': 'Basher', 'avatar': 'img/dota/items/skull_basher.png'},
         145: {'name': 'Battlefury', 'avatar': 'img/dota/items/battle_fury.png'},
         147: {'name': 'Manta', 'avatar': 'img/dota/items/manta_style.png'},
         149: {'name': 'Crystalys', 'avatar': 'img/dota/items/crystalys.png'},
         151: {'name': 'Armlet of Mordiggian', 'avatar': 'img/dota/items/armlet_of_mordiggian.png'},
         152: {'name': 'Shadow Blade', 'avatar': 'img/dota/items/shadow_blade.png'},
         154: {'name': 'Sange and Yasha', 'avatar': 'img/dota/items/sange_and_yasha.png'},
         156: {'name': 'Satanic', 'avatar': 'img/dota/items/satanic.png'},
         158: {'name': 'Mjollnir', 'avatar': 'img/dota/items/mjollnir.png'},
         160: {'name': 'Eye of Skadi', 'avatar': 'img/dota/items/eye_of_skadi.png'},
         162: {'name': 'Sange', 'avatar': 'img/dota/items/sange.png'},
         164: {'name': 'Helm of the Dominator', 'avatar': 'img/dota/items/helm_of_the_dominator.png'},
         166: {'name': 'Maelstrom', 'avatar': 'img/dota/items/maelstrom.png'},
         167: {'name': 'Recipe: Desolator', 'avatar': 'img/dota/items/recipe_scroll.png'},
         168: {'name': 'Desolator', 'avatar': 'img/dota/items/desolator.png'},
         170: {'name': 'Yasha', 'avatar': 'img/dota/items/yasha.png'},
         172: {'name': 'Mask of Madness', 'avatar': 'img/dota/items/mask_of_madness.png'},
         174: {'name': 'Diffusal Blade Level 1', 'avatar': 'img/dota/items/diffusal_blade_1.png'},
         176: {'name': 'Ethereal Blade', 'avatar': 'img/dota/items/ethereal_blade.png'},
         178: {'name': 'Soul Ring', 'avatar': 'img/dota/items/soul_ring.png'},
         180: {'name': 'Arcane Boots', 'avatar': 'img/dota/items/arcane_boots.png'},
         181: {'name': 'Orb of Venom', 'avatar': 'img/dota/items/orb_of_venom.png'},
         182: {'name': 'Stout Shield', 'avatar': 'img/dota/items/stout_shield.png'},
         185: {'name': 'Drum of Endurance', 'avatar': 'img/dota/items/drum_of_endurance.png'},
         187: {'name': 'Medallion of Courage', 'avatar': 'img/dota/items/medallion_of_courage.png'},
         188: {'name': 'Smoke of Deceit', 'avatar': 'img/dota/items/smoke_of_deceit.png'},
         190: {'name': 'Veil of Discord', 'avatar': 'img/dota/items/veil_of_discord.png'},
         193: {'name': 'Necronomicon: Level 2', 'avatar': 'img/dota/items/necronomicon_2.png'},
         194: {'name': 'Necronomicon', 'avatar': 'img/dota/items/necronomicon.png'},
         196: {'name': 'Diffusal Blade: Level 2', 'avatar': 'img/dota/items/diffusal_blade.png'},
         201: {'name': 'Dagon Level 2', 'avatar': 'img/dota/items/dagon_2.png'},
         202: {'name': 'Dagon Level 3', 'avatar': 'img/dota/items/dagon_3.png'},
         203: {'name': 'Dagon Level 4', 'avatar': 'img/dota/items/dagon_4.png'},
         204: {'name': 'Dagon Level 5', 'avatar': 'img/dota/items/dagon.png'},
         206: {'name': 'Rod of Atos', 'avatar': 'img/dota/items/rod_of_atos.png'},
         208: {'name': 'Abyssal Blade', 'avatar': 'img/dota/items/abyssal_blade.png'},
         210: {'name': 'Heaven\'s Halberd', 'avatar': 'img/dota/items/heavens_halberd.png'},
         212: {'name': 'Ring of Aquila', 'avatar': 'img/dota/items/ring_of_aquila.png'},
         214: {'name': 'Tranquil Boots', 'avatar': 'img/dota/items/tranquil_boots.png'},
         215: {'name': 'Shadow Amulet', 'avatar': 'img/dota/items/shadow_amulet.png'},
         229: {'name': 'Xmas Stocking', 'avatar': 'img/dota/items/xmas_stocking.png'},
         230: {'name': 'Speed Skates', 'avatar': 'img/dota/items/speed_skates.png'},
         231: {'name': 'Fruit-bit Cake', 'avatar': 'img/dota/items/fruit-bit_cake.png'},
         232: {'name': 'Wizard Cookie', 'avatar': 'img/dota/items/wizard_cookie.png'},
         233: {'name': 'Cocoa with Marshmallows', 'avatar': 'img/dota/items/cocoa.png'},
         234: {'name': 'Clove Studded Ham', 'avatar': 'img/dota/items/clove_studded_ham.png'},
         235: {'name': 'Greevil Whistle', 'avatar': 'img/dota/items/greevil_whistle.png'},
         236: {'name': 'Kringle', 'avatar': 'img/dota/items/kringle.png'}}