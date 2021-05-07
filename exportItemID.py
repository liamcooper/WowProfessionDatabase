#!/usr/bin/env python3.7

items = {
    "Accurate Scope": 4407,
    "Aquamarine": 7909,
    "Arcanite Bar": 12360,
    "Arcanite Rod": 16206,
    "Arthas Tears": 8836,
    "Azerothian Diamond": 12800,
    "Bear Meat": 3173,
    "Big Bear Meat": 3730,
    "Big Iron Bomb": 4394,
    "Black Dragonscale": 15416,
    "Black Dye": 2325,
    "Black Lotus": 13468,
    "Black Mageweave Boots": 10026,
    "Black Pearl": 7971,
    "Black Whelp Scale": 7286,
    "Blackmouth Oil": 6370,
    "Blank Parchment": 10648,
    "Bleach": 2324,
    "Blindweed": 8839,
    "Blood of the Mountain": 11382,
    "Blue Dragonscale": 15415,
    "Blue Dye": 6260,
    "Blue Pearl": 4611,
    "Blue Power Crystal": 11184,
    "Blue Sapphire": 12361,
    "Boar Intestines": 3172,
    "Boar Ribs": 2677,
    "Bolt of Linen Cloth": 2996,
    "Bolt of Mageweave": 4339,
    "Bolt of Runecloth": 14048,
    "Bolt of Silk Cloth": 4305,
    "Bolt of Woolen Cloth": 2997,
    "Breath of Wind": 7081,
    "Briarthorn": 2450,
    "Bronze Bar": 2841,
    "Bronze Framework": 4382,
    "Bronze Tube": 4371,
    "Bruiseweed": 2453,
    "Buzzard Wing": 3404,
    "Catseye Elixir": 10592,
    "Chimera Leather": 15423,
    "Chunk of Boar Meat": 769,
    "Citrine": 3864,
    "Clam Meat": 5503,
    "Coarse Blasting Powder": 4364,
    "Coarse Gorilla Hair": 4096,
    "Coarse Grinding Stone": 3478,
    "Coarse Stone": 2836,
    "Coarse Thread": 2320,
    "Copper Bar": 2840,
    "Copper Modulator": 4363,
    "Copper Rod": 6217,
    "Copper Tube": 4361,
    "Core Leather": 17012,
    "Core of Earth": 7075,
    "Coyote Meat": 2673,
    "Crag Boar Rib": 2886,
    "Crawler Claw": 2675,
    "Crawler Meat": 2674,
    "Crisp Spider Meat": 1081,
    "Crocolisk Meat": 2924,
    "Crystal Vial": 8925,
    "Cured Heavy Hide": 4236,
    "Cured Light Hide": 4231,
    "Cured Medium Hide": 4233,
    "Cured Rugged Hide": 19047,
    "Cured Thick Hide": 8172,
    "Dark Iron Bar": 11371,
    "Dark Rune": 20520,
    "Darkclaw Lobster": 13888,
    "Deadly Scope": 10546,
    "Deeprock Salt": 8150,
    "Delicate Arcanite Converter": 16006,
    "Dense Blasting Powder": 15992,
    "Dense Grinding Stone": 12644,
    "Dense Stone": 12365,
    "Deviate Fish": 6522,
    "Deviate Scale": 6470,
    "Devilsaur Leather": 15417,
    "Dig Rat": 5051,
    "Discolored Worg Heart": 3164,
    "Dream Dust": 11176,
    "Dreamfoil": 13463,
    "Dusky Belt": 7387,
    "Earthroot": 2449,
    "Elemental Air": 7069,
    "Elemental Earth": 7067,
    "Elemental Fire": 7068,
    "Elemental Water": 7070,
    "Elixir of Agility": 8949,
    "Elixir of Defense": 3389,
    "Elixir of Demonslaying": 9224,
    "Elixir of Greater Defense": 8951,
    "Elixir of Lesser Agility": 3390,
    "Elixir of Minor Agility": 2457,
    "Elixir of Ogres Strength": 3391,
    "Elixir of Wisdom": 3383,
    "Empty Vial": 3371,
    "Enchanted Leather": 12810,
    "Enchanted Thorium Bar": 12655,
    "Engineers Ink": 10647,
    "Essence of Air": 7082,
    "Essence of Earth": 7076,
    "Essence of Fire": 7078,
    "Essence of Undeath": 12808,
    "Essence of Water": 7080,
    "Fadeleaf": 3818,
    "Felcloth": 14256,
    "Fiery Core": 17010,
    "Fine Leather Belt": 4246,
    "Fine Leather Gloves": 2312,
    "Fine Leather Tunic": 4243,
    "Fine Thread": 2321,
    "Fire Goggles": 10500,
    "Fire Oil": 6371,
    "Firebloom": 4625,
    "Firefin Snapper": 6359,
    "Flask of Big Mojo": 8152,
    "Flask of Mojo": 8151,
    "Flask of Oil": 814,
    "Flying Tiger Goggles": 4368,
    "Frost Oil": 3829,
    "Frostsaber Leather": 15422,
    "Fused Wiring": 7191,
    "Giant Clam Meat": 4655,
    "Giant Egg": 12207,
    "Ghost Dye": 9210,
    "Ghost Mushroom": 8845,
    "Globe of Water": 7079,
    "Goblin Construction Helmet": 10543,
    "Goblin Rocket Fuel": 9061,
    "Gold Bar": 3577,
    "Gold Power Core": 10558,
    "Golden Pearl": 13926,
    "Golden Rod": 11128,
    "Golden Sansam": 13464,
    "Goldthorn": 3821,
    "Gooey Spider Leg": 2251,
    "Goretusk Liver": 723,
    "Goretusk Snout": 731,
    "Grave Moss": 3369,
    "Gray Dye": 4340,
    "Great Rage Potion": 5633,
    "Greater Astral Essence": 11082,
    "Greater Eternal Essence": 16203,
    "Greater Magic Essence": 10939,
    "Greater Mystic Essence": 11135,
    "Greater Nether Essence": 11175,
    "Green Dragonscale": 15412,
    "Green Dye": 2605,
    "Green Leather Armor": 4255,
    "Green Power Crystal": 11185,
    "Green Tinted Googles": 4385,
    "Green Whelp Scale": 7392,
    "Gromsblood": 8846,
    "Guardian Gloves": 5966,
    "Guardian Stone": 12809,
    "Gyrochronatom": 4389,
    "Handful of Copper Bolts": 4359,
    "Healing Potion": 929,
    "Heart of Fire": 7077,
    "Heart of the Wild": 10286,
    "Heavy Blasting Powder": 4377,
    "Heavy Grinding Stone": 3486,
    "Heavy Hide": 4235,
    "Heavy Kodo Meat": 12204,
    "Heavy Leather": 4234,
    "Heavy Scorpid Scale": 15408,
    "Heavy Silken Thread": 8343,
    "Heavy Stock": 4400,
    "Heavy Stone": 2838,
    "Holiday Spices": 17194,
    "Holiday Spirits": 17196,
    "Hot Spices": 2692,
    "Huge Emerald": 12364,
    "Ice Cold Milk": 1179,
    "Icecap": 13467,
    "Ichor of Undeath": 7972,
    "Illusion Dust": 16204,
    "Imbued Vial": 18256,
    "Inlaid Mithril Cylinder": 9060,
    "Iridescent Pearl": 5500,
    "Iron Bar": 3575,
    "Iron Buckle": 7071,
    "Iron Ore": 2772,
    "Iron Strut": 4387,
    "Ironfeather": 15420,
    "Ironweb Spider Silk": 14227,
    "Jade": 1529,
    "Jet Black Feather": 8168,
    "Khadgars Whisker": 3358,
    "Kingsblood": 3356,
    "Kodo Meat": 5467,
    "Large Brilliant Shard": 14344,
    "Large Fang": 5637,
    "Large Glimmering Shard": 11084,
    "Large Glowing Shard": 11139,
    "Large Opal": 12799,
    "Large Radiant Shard": 11178,
    "Large Raw Mightfish":  13893,
    "Large Venom Sac": 1288,
    "Lava Core": 17011,
    "Leaded Vial": 3372,
    "Lean Wolf Flank": 1015,
    "Lesser Astral Essence": 10998,
    "Lesser Eternal Essence": 16202,
    "Lesser Invisibility Potion": 3823,
    "Lesser Magic Essence": 10938,
    "Lesser Moonstone": 1705,
    "Lesser Mystic Essence": 11134,
    "Lesser Nether Essence": 11174,
    "Liferoot": 3357,
    "Light Hide": 783,
    "Light Leather": 2318,
    "Linen Cloth": 2589,
    "Lion Meat": 3731,
    "Living Essence": 12803,
    "Long Elegant Feather": 4589,
    "Long Tail Feather": 5116,
    "Lucky Charm": 5373,
    "Mageroyal": 785,
    "Mageweave Cloth": 4338,
    "Malachite": 774,
    "Mana Potion": 3827,
    "Maple Seed": 17034,
    "Meaty Bat Wing": 12223,
    "Medium Hide": 4232,
    "Medium Leather": 2319,
    "Mild Spices": 2678,
    "Minor Healing Potion": 118,
    "Mithril Bar": 3860,
    "Mithril Casing": 10561,
    "Mithril Ore": 3858,
    "Mithril Tube": 10559,
    "Mooncloth": 14342,
    "Morrowgrain": 11040,
    "Moss Agate": 1206,
    "Mountain Silversage": 13465,
    "Murloc Eye": 730,
    "Murloc Fin": 1468,
    "Mystery Meat": 12037,
    "Naga Scale": 7072,
    "Nexus Crystal": 20725,
    "Nightcrawlers": 6530,
    "Oily Blackmouth": 6358,
    "Orange Dye": 6261,
    "Peacebloom": 2447,
    "Perfect Deviate Scale": 6471,
    "Pink Dye": 10290,
    "Plaguebloom": 13466,
    "Powerful Mojo": 12804,
    "Purple Dye": 4342,
    "Purple Lotus": 8831,
    "Raptor Hide": 4461,
    "Raptor Egg": 3685,
    "Raptor Flesh": 12184,
    "Raw Brilliant Smallfish": 6291,
    "Raw Bristle Whisker Catfish": 6308,
    "Raw Glossy Mightfish": 13754,
    "Raw Greater Sagefish": 21153,
    "Raw Loch Frenzy": 6317,
    "Raw Longjaw Mud Snapper": 6289,
    "Raw Mithril Head Trout": 8365,
    "Raw Nightfin Snapper": 13759,
    "Raw Rainbow Fin Albacore": 6361,
    "Raw Redgill": 13758,
    "Raw Rockscale Cod": 6362,
    "Raw Sagefish": 21071,
    "Raw Slitherskin Mackerel": 6303,
    "Raw Spotted Yellowtail": 4603,
    "Raw Summer Bass": 13756,
    "Raw Sunscale Salmon": 13760,
    "Raw Whitescale Salmon": 13889,
    "Red Dye": 2604,
    "Red Power Crystal": 11186,
    "Red Whelp Scale": 7287,
    "Red Wolf Meat": 12203,
    "Refined Deeprock Salt": 15409,
    "Refreshing Spring Water": 159,
    "Rhapsody Malt": 2894,
    "Righteous Orb": 12811,
    "Rough Blasting Powder": 4357,
    "Rough Grinding Stone": 3470,
    "Rough Stone": 2835,
    "Rugged Hide": 8171,
    "Rugged Leather": 8170,
    "Ruined Leather Scraps": 2934,
    "Rune Thread":14341,
    "Runecloth": 14047,
    "Runn Tum Tuber": 18255,
    "Salt": 4289,
    "Sandworm Meat": 20424,
    "Scorpid Scale": 8154,
    "Scorpid Stinger": 5466,
    "Shadow Oil": 3824,
    "Shadow Protection Potion": 6048,
    "Shadow Silk": 10258,
    "Shadowcat Hide": 7428,
    "Shadowgem": 1210,
    "Sharp Claw": 5635,
    "Shiny Red Apple": 4536,
    "Silk Cloth": 4306,
    "Silken Thread": 4291,
    "Silver Bar": 2842,
    "Silver Contact": 4404,
    "Silver Rod": 6338,
    "Silverleaf": 765,
    "Simple Wood": 4470,
    "Skin of Dwarven Stout": 2596,
    "Slimy Murloc Scale": 5784,
    "Small Brilliant Shard": 14343,
    "Small Egg": 6889,
    "Small Flame Sac": 4402,
    "Small Glimmering Shard": 10978,
    "Small Glowing Shard": 11138,
    "Small Lustrous Pearl": 5498,
    "Small Spider Leg": 5465,
    "Small Radiant Shard": 11177,
    "Snowball": 17202,
    "Soft Frenzy Fish": 5468,
    "Solid Blasting Powder": 10505,
    "Solid Dynamite": 10507,
    "Solid Grinding Stone": 7966,
    "Solid Stone": 7912,
    "Soothing Spices": 3713,
    "Soul Dust": 11083,
    "Spellpower Goggles Xtreme": 10502,
    "Spider Ichor": 3174,
    "Spiders Silk": 3182,
    "Stag Meat": 5471,
    "Star Ruby": 7910,
    "Star Wood": 11291,
    "Steel Bar": 3859,
    "Stonescale Eel": 13422,
    "Stonescale Oil": 13423,
    "Stormwind Seasoning Herbs": 2665,
    "Strange Dust": 10940,
    "Stranglekelp": 3820,
    "Stranglethorn Seed": 17035,
    "Strider Meat": 5469,
    "Stringy Vulture Meat": 729,
    "Stringy Wolf Meat": 2672,
    "Strong Flux": 3466,
    "Sungrass": 8838,
    "Swiftness Potion": 2459,
    "Swiftthistle": 2452,
    "Tangy Clam Meat": 5504,
    "Tender Crab Meat": 12206,
    "Tender Crocolisk Meat": 3667,
    "Tender Wolf Meat": 12208,
    "The Big One": 10586,
    "Thick Hide": 8169,
    "Thick Leather": 4304,
    "Thick Murloc Scale": 5785,
    "Thick Spiders Silk": 4337,
    "Thick Wolfhide": 8368,
    "Thin Kodo Leather": 8368,
    "Thorium Bar": 12359,
    "Thorium Ore": 10620,
    "Thorium Tube": 16000,
    "Thorium Widget": 15994,
    "Thunder Lizard Tail": 5470,
    "Tiger Meat": 12202,
    "Tigerseye": 818,
    "Tough Condor Meat": 1080,
    "Truesilver Bar": 6037,
    "Truesilver Rod": 11144,
    "Truesilver Transformer": 18631,
    "Turtle Meat": 3712,
    "Turtle Scale": 8167,
    "Unstable Trigger": 10560,
    "Vision Dust": 11137,
    "Volatile Rum": 9260,
    "Warbear Leather": 15419,
    "Weak Flux": 2880,
    "Whirring Bronze Gizmo": 4375,
    "White Spider Meat": 12205,
    "Wicked Claw": 8146,
    "Wild Steelbloom": 3355,
    "Wildvine": 8153,
    "Winter Squid": 13755,
    "Wintersbite": 3819,
    "Wooden Stock": 4399,
    "Wool Cloth": 2592,
    "Worn Dragonscale": 8165,
    "Yellow Dye": 4341,
    "Yellow Power Crystal": 11188,
    "Zesty Clam Meat": 7974
}

import json

with open("itemID.json", 'w') as jsonFile:
    json.dump(items, jsonFile)