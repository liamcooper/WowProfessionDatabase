#!/usr/bin/env python3.7

recipes = {
    "Arcanite Rod": {
        "ID":       16206,
        "Learn":    275,
        "Yellow":   275,
        "Green":    280,
        "Grey":     285,
        "Source":   "Trainer",
        "Reagents": {
            "Arcanite Bar": 3,
            "Dense Grinding Stone": 1,
        }
    },
    "Arcanite Skeleton Key": {
        "ID":       15872,
        "Learn":    275,
        "Yellow":   275,
        "Green":    280,
        "Grey":     285,
        "Source":   "Trainer",
        "Reagents": {
            "Arcanite Bar": 1,
            "Dense Grinding Stone": 1
        },
        "AmuntCrafted": 2
    },
    "Barbaric Iron Boots": {
        "ID":       7916,
        "Learn":    180,
        "Yellow":   205,
        "Green":    217,
        "Grey":     230,
        "Source":   "Quest",
		"Faction":  "Horde",
        "RecipeID": 7981,
        "Reagents": {
            "Iron Bar": 12,
            "Large Fang": 4,
			"Tigerseye": 4,
			"Heavy Grinding Stone": 2
        }
    },
    "Barbaric Iron Breastplate": {
        "ID":       7914,
        "Learn":    160,
        "Yellow":   185,
        "Green":    197,
        "Grey":     210,
        "Source":   "Quest",
		"Faction":  "Horde",
        "RecipeID": 7979,
        "Reagents": {
            "Iron Bar": 20,
            "Heavy Grinding Stone": 4
        }
    },
    "Barbaric Iron Gloves": {
        "ID":       7917,
        "Learn":    185,
        "Yellow":   210,
        "Green":    222,
        "Grey":     235,
        "Source":   "Quest",
		"Faction":  "Horde",
        "RecipeID": 7982,
        "Reagents": {
            "Iron Bar": 14,
            "Heavy Grinding Stone": 3,
			"Large Fang": 2
        }
    },
    "Barbaric Iron Helm": {
        "ID":       7915,
        "Learn":    175,
        "Yellow":   200,
        "Green":    212,
        "Grey":     225,
        "Source":   "Quest",
		"Faction":  "Horde",
        "RecipeID": 7980,
        "Reagents": {
            "Iron Bar": 10,
            "Large Fang": 2,
			"Sharp Claw": 2
        }
    },
    "Barbaric Iron Shoulders": {
        "ID":       7913,
        "Learn":    160,
        "Yellow":   185,
        "Green":    197,
        "Grey":     210,
        "Source":   "Quest",
		"Faction":  "Horde",
        "RecipeID": 7978,
        "Reagents": {
            "Iron Bar": 8,
            "Sharp Claw": 4,
			"Shadowgem": 2,
			"Heavy Grinding Stone": 2
        }
    },
    "Big Black Mace": {
        "ID":       7945,
        "Learn":    230,
        "Yellow":   255,
        "Green":    267,
        "Grey":     280,
        "Source":   "Trainer",
        "Reagents": {
            "Mithril Bar": 16,
            "Black Pearl": 1,
			"Shadowgem": 4,
			"Solid Grinding Stone": 1,
			"Thick Leather": 2
        }
    },
    "Big Bronze Knife": {
        "ID":       3848,
        "Learn":    105,
        "Yellow":   135,
        "Green":    150,
        "Grey":     165,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 6,
            "Weak Flux": 4,
			"Rough Grinding Stone": 2,
			"Tigerseye": 1,
			"Medium Leather": 1
        }
    },
    "Blazing Rapier": {
        "ID":       12777,
        "Learn":    280,
        "Yellow":   305,
        "Green":    317,
        "Grey":     330,
        "Source":   "Quest",
		"Faction":  "Any",
        "RecipeID": 12825,
        "Reagents": {
            "Enchanted Thorium Bar": 10,
            "Essence of Fire": 4,
			"Heart of Fire": 4,
			"Azerothian Diamond": 2,
			"Dense Grinding Stone": 2
        }
    },
    "Blight": {
        "ID":       7959,
        "Learn":    250,
        "Yellow":   275,
        "Green":    287,
        "Grey":     300,
        "Source":   "Trainer",
        "School":   "Weapon",
        "Reagents": {
            "Mithril Bar": 28,
            "Ichor of Undeath": 10,
			"Truesilver Bar": 10,
			"Solid Grinding Stone": 6,
			"Thick Leather": 6
        }
    },
    "Blue Glittering Axe": {
        "ID":       7942,
        "Learn":    220,
        "Yellow":   245,
        "Green":    257,
        "Grey":     270,
        "Source":   "Drop",
        "RecipeID": 7992,
        "Reagents": {
            "Mithril Bar": 16,
            "Aquamarine": 2,
			"Solid Grinding Stone": 1,
			"Thick Leather": 4
        }
    },
    "Bronze Axe": {
        "ID":       2849,
        "Learn":    115,
        "Yellow":   145,
        "Green":    160,
        "Grey":     175,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 7,
            "Weak Flux": 4,
			"Medium Leather": 1
        }
    },
    "Bronze Battle Axe": {
        "ID":       7958,
        "Learn":    135,
        "Yellow":   165,
        "Green":    180,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 14,
            "Strong Flux": 1,
			"Medium Leather": 2
        }
    },
    "Bronze Greatsword": {
        "ID":       7957,
        "Learn":    130,
        "Yellow":   160,
        "Green":    175,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 12,
            "Strong Flux": 2,
			"Medium Leather": 2
        }
    },
    "Bronze Mace": {
        "ID":       2848,
        "Learn":    110,
        "Yellow":   140,
        "Green":    155,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 6,
            "Weak Flux": 4,
			"Medium Leather": 1
        }
    },
    "Bronze Shortsword": {
        "ID":       2850,
        "Learn":    120,
        "Yellow":   150,
        "Green":    165,
        "Grey":     180,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 5,
            "Weak Flux": 4,
			"Medium Leather": 2
        }
    },
    "Bronze Warhammer": {
        "ID":       7956,
        "Learn":    125,
        "Yellow":   155,
        "Green":    170,
        "Grey":     185,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 8,
            "Strong Flux": 1,
			"Medium Leather": 1
        }
    },
    "Coarse Grinding Stone": {
        "ID":       3478,
        "Learn":    75,
        "Yellow":   75,
        "Green":    87,
        "Grey":     100,
        "Source":   "Trainer",
        "Reagents": {
            "Coarse Stone": 2
        }
    },
    "Coarse Sharpening Stone": {
        "ID":       2863,
        "Learn":    65,
        "Yellow":   65,
        "Green":    72,
        "Grey":     80,
        "Source":   "Trainer",
        "Reagents": {
            "Coarse Stone": 1
        }
    },
    "Coarse Weightstone": {
        "ID":       3240,
        "Learn":    65,
        "Yellow":   65,
        "Green":    72,
        "Grey":     80,
        "Source":   "Trainer",
        "Reagents": {
            "Coarse Stone": 1,
            "Wool Cloth": 1
        }
    },
    "Copper Axe": {
        "ID":       2845,
        "Learn":    20,
        "Yellow":   60,
        "Green":    80,
        "Grey":     100,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 6,
            "Weak Flux": 1,
			"Linen Cloth": 2
        }
    },
    "Copper Battle Axe": {
        "ID":       3488,
        "Learn":    35,
        "Yellow":   75,
        "Green":    95,
        "Grey":     115,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 12,
            "Weak Flux": 2,
			"Malachite": 2,
			"Rough Grinding Stone": 2,
			"Light Leather": 2
        }
    },
    "Copper Bracers": {
        "ID":       2853,
        "Learn":    1,
        "Yellow":   20,
        "Green":    40,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 2
        }
    },
    "Copper Chain Belt": {
        "ID":       2851,
        "Learn":    35,
        "Yellow":   75,
        "Green":    95,
        "Grey":     115,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 6
        }
    },
    "Copper Chain Boots": {
        "ID":       3469,
        "Learn":    20,
        "Yellow":   60,
        "Green":    80,
        "Grey":     100,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 8
        }
    },
    "Copper Chain Pants": {
        "ID":       2852,
        "Learn":    1,
        "Yellow":   50,
        "Green":    70,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 4
        }
    },
    "Copper Chain Vest": {
        "ID":       3471,
        "Learn":    35,
        "Yellow":   75,
        "Green":    95,
        "Grey":     115,
        "Source":   "Drop",
        "RecipeID": 3609,
        "Reagents": {
            "Copper Bar": 8,
            "Malachite": 1,
			"Rough Grinding Stone": 2
        }
    },
    "Copper Claymore": {
        "ID":       7955,
        "Learn":    30,
        "Yellow":   70,
        "Green":    90,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 10,
            "Weak Flux": 2,
			"Rough Grinding Stone": 1,
			"Light Leather": 1
        }
    },
    "Copper Dagger": {
        "ID":       7166,
        "Learn":    30,
        "Yellow":   70,
        "Green":    90,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 6,
            "Weak Flux": 1,
			"Rough Grinding Stone": 1,
			"Light Leather": 1
        }
    },
    "Copper Mace": {
        "ID":       2844,
        "Learn":    15,
        "Yellow":   55,
        "Green":    75,
        "Grey":     95,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 6,
            "Weak Flux": 1,
			"Linen Cloth": 2
        }
    },
    "Copper Shortsword": {
        "ID":       2847,
        "Learn":    25,
        "Yellow":   65,
        "Green":    85,
        "Grey":     105,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 6,
            "Weak Flux": 1,
			"Linen Cloth": 2
        }
    },
    "Dark Iron Bracers": {
        "ID":       17014,
        "Learn":    295,
        "Yellow":   315,
        "Green":    325,
        "Grey":     335,
        "Source":   "Reputation",
        "School":   "Armor",
        "RecipeID": 17051,
        "Reagents": {
            "Dark Iron Bar": 4,
            "Fiery Core": 2,
			"Lava Core": 2
        }
    },
    "Dark Iron Mail": {
        "ID":       11606,
        "Learn":    270,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Drop",
        "RecipeID": 11614,
        "Reagents": {
            "Dark Iron Bar": 10,
            "Heart of Fire": 2
        }
    },
    "Dark Iron Plate": {
        "ID":       11604,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 11612,
        "School":   "Armor",
        "Reagents": {
            "Dark Iron Bar": 20,
            "Heart of Fire": 8
        }
    },
    "Dark Iron Pulverizer": {
        "ID":       11608,
        "Learn":    265,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Drop",
        "RecipeID": 11610,
        "School":   "Weapon",
        "Reagents": {
            "Dark Iron Bar": 18,
            "Heart of Fire": 4
        }
    },
    "Dark Iron Shoulders": {
        "ID":       11605,
        "Learn":    280,
        "Yellow":   300,
        "Green":    310,
        "Grey":     320,
        "Source":   "Drop",
        "RecipeID": 11615,
        "Reagents": {
            "Dark Iron Bar": 6,
            "Heart of Fire": 1
        }
    },
    "Dark Iron Sunderer": {
        "ID":       11607,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Drop",
        "RecipeID": 11611,
        "School":   "Weapon",
        "Reagents": {
            "Dark Iron Bar": 26,
            "Heart of Fire": 4
        }
    },
    "Dawns Edge": {
        "ID":       12774,
        "Learn":    275,
        "Yellow":   300,
        "Green":    312,
        "Grey":     325,
        "Source":   "Quest",
		"Faction":  "Any",
        "RecipeID": 12821,
        "Reagents": {
            "Thorium Bar": 30,
            "Enchanted Thorium Bar": 4,
			"Star Ruby": 4,
			"Blue Sapphire": 4,
			"Dense Grinding Stone": 2,
			"Rugged Leather": 4
        }
    },
    "Dawnbringer Shoulders": {
        "ID":       12625,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Drop",
        "RecipeID": 12698,
        "School":   "Armor",
        "Reagents": {
            "Thorium Bar": 20,
            "Arcanite Bar": 4,
			"Huge Emerald": 2,
			"Essence of Water": 2
        }
    },
    "Dazzling Mithril Rapier": {
        "ID":       7944,
        "Learn":    240,
        "Yellow":   265,
        "Green":    277,
        "Grey":     290,
        "Source":   "Drop",
        "RecipeID": 7993,
        "Reagents": {
            "Mithril Bar": 14,
            "Aquamarine": 1,
			"Lesser Moonstone": 2,
			"Moss Agate": 2,
			"Solid Grinding Stone": 1,
			"Mageweave Cloth": 2
        }
    },
    "Deadly Bronze Poniard": {
        "ID":       3490,
        "Learn":    125,
        "Yellow":   155,
        "Green":    170,
        "Grey":     185,
        "Source":   "Drop",
        "RecipeID": 2883,
        "Reagents": {
            "Bronze Bar": 4,
            "Strong Flux": 1,
			"Swiftness Potion": 1,
			"Shadowgem": 2, 
			"Coarse Grinding Stone": 2,
			"Medium Leather": 2
        }
    },
    "Dense Grinding Stone": {
        "ID":       12644,
        "Learn":    250,
        "Yellow":   255,
        "Green":    257,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
            "Dense Stone": 4
        }
    },
    "Dense Sharpening Stone": {
        "ID":       12404,
        "Learn":    250,
        "Yellow":   255,
        "Green":    257,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
            "Dense Stone": 1
        }
    },
    "Dense Weightstone": {
        "ID":       12643,
        "Learn":    250,
        "Yellow":   255,
        "Green":    257,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
            "Dense Stone": 1,
            "Runecloth": 1
        }
    },
    "Ebon Shiv": {
        "ID":       7947,
        "Learn":    255,
        "Yellow":   280,
        "Green":    292,
        "Grey":     305,
        "Source":   "Vendor",
        "RecipeID": 8030,
        "Reagents": {
            "Mithril Bar": 12,
            "Truesilver Bar": 6,
			"Star Ruby": 2,
			"Solid Grinding Stone": 1,
			"Thick Leather": 2
        }
    },
    "Edge of Winter": {
        "ID":       17704,
        "Learn":    190,
        "Yellow":   215,
        "Green":    227,
        "Grey":     240,
        "Source":   "Quest",
		"Faction":  "Any",
        "RecipeID": 17706,
        "Reagents": {
            "Steel Bar": 10,
            "Frost Oil": 1,
			"Elemental Water": 2,
			"Elemental Air": 2,
			"Heavy Leather": 2
        }
    },
    "Enchanted Battlehammer": {
        "ID":       12776,
        "Learn":    280,
        "Yellow":   305,
        "Green":    317,
        "Grey":     330,
        "Source":   "Quest",
		"Faction":  "Alliance",
        "RecipeID": 12824,
        "Reagents": {
            "Thorium Bar": 20,
            "Enchanted Thorium Bar": 6,
			"Huge Emerald": 2,
			"Powerful Mojo": 4,
			"Rugged Leather": 4
        }
    },
    "Fiery Chain Girdle": {
        "ID":       16989,
        "Learn":    295,
        "Yellow":   315,
        "Green":    325,
        "Grey":     335,
        "Source":   "Reputation",
        "School":   "Armor",
        "RecipeID": 17049,
        "Reagents": {
            "Dark Iron Bar": 6,
            "Fiery Core": 3,
			"Lava Core": 3
        }
    },
    "Fiery Plate Gauntlets": {
        "ID":       12631,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Quest",
		"Faction":  "Any",
        "RecipeID": 12699,
        "Reagents": {
            "Thorium Bar": 20,
            "Enchanted Thorium Bar": 6,
			"Essence of Fire": 2,
			"Star Ruby": 4
        }
    },
    "Frost Tiger Blade": {
        "ID":       3854,
        "Learn":    200,
        "Yellow":   225,
        "Green":    237,
        "Grey":     250,
        "Source":   "Drop",
        "RecipeID": 3868,
        "Reagents": {
            "Steel Bar": 8,
            "Strong Flux": 2,
			"Heavy Grinding Stone": 2,
			"Jade": 2,
			"Frost Oil": 1,
			"Heavy Leather": 4
        }
    },
    "Gemmed Copper Gauntlets": {
        "ID":       3474,
        "Learn":    60,
        "Yellow":   100,
        "Green":    120,
        "Grey":     140,
        "Source":   "Drop",
        "RecipeID": 3610,
        "Reagents": {
            "Copper Bar": 8,
            "Tigerseye": 1,
			"Malachite": 1
        }
    },
    "Girdle of the Dawn": {
        "ID":       19051,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Reputation",
        "RecipeID": 19203,
        "Reagents": {
            "Thorium Bar": 8,
            "Truesilver Bar": 6,
			"Righteous Orb": 1
        }
    },
    "Glinting Steel Dagger": {
        "ID":       12259,
        "Learn":    180,
        "Yellow":   205,
        "Green":    217,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
            "Steel Bar": 10,
            "Strong Flux": 2,
			"Moss Agate": 1,
			"Elemental Earth": 1,
			"Heavy Leather": 1
        }
    },
    "Golder Iron Destroyer": {
        "ID":       3852,
        "Learn":    170,
        "Yellow":   195,
        "Green":    207,
        "Grey":     220,
        "Source":   "Drop",
        "RecipeID": 3867,
        "Reagents": {
            "Iron Bar": 10,
            "Gold Bar": 4,
			"Lesser Moonstone": 2,
			"Strong Flux": 2,
			"Heavy Leather": 2,
			"Heavy Grinding Stone": 2
        }
    },
    "Golden Rod": {
        "ID":       11128,
        "Learn":    150,
        "Yellow":   155,
        "Green":    157,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
            "Gold Bar": 1,
            "Coarse Grinding Stone": 2
        }
    },
    "Golden Scale Boots": {
        "ID":       3847,
        "Learn":    200,
        "Yellow":   225,
        "Green":    237,
        "Grey":     250,
        "Source":   "Drop",
        "RecipeID": 3875,
        "Reagents": {
            "Steel Bar": 10,
            "Gold Bar": 4,
			"Heavy Grinding Stone": 4,
			"Citrine": 1
        }
    },
    "Golden Scale Bracers": {
        "ID":       6040,
        "Learn":    185,
        "Yellow":   210,
        "Green":    222,
        "Grey":     235,
        "Source":   "Trainer",
        "Reagents": {
            "Steel Bar": 5,
            "Heavy Grinding Stone": 2
        }
    },
    "Golden Scale Coif": {
        "ID":       3837,
        "Learn":    190,
        "Yellow":   215,
        "Green":    227,
        "Grey":     240,
        "Source":   "VendorLimited",
        "RecipeID": 6047,
        "Reagents": {
            "Steel Bar": 8,
			"Gold Bar": 2,
			"Heavy Grinding Stone": 2
        }
    },
    "Golden Scale Cuirass": {
        "ID":       3845,
        "Learn":    195,
        "Yellow":   220,
        "Green":    232,
        "Grey":     245,
        "Source":   "Drop",
        "RecipeID": 3873,
        "Reagents": {
            "Steel Bar": 12,
			"Gold Bar": 2,
			"Heavy Grinding Stone": 4,
			"Jade": 2
        }
    },
    "Golden Scale Gauntlets": {
        "ID":       9366,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Quest",
		"Faction":  "Alliance",
        "RecipeID": 9367,
        "Reagents": {
            "Steel Bar": 10,
			"Gold Bar": 4,
			"Heavy Grinding Stone": 4,
			"Citrine": 1
        }
    },
    "Golden Scale Leggings": {
        "ID":       3843,
        "Learn":    170,
        "Yellow":   195,
        "Green":    207,
        "Grey":     220,
        "Source":   "Drop",
        "RecipeID": 3872,
        "Reagents": {
            "Iron Bar": 10,
			"Gold Bar": 2,
			"Heavy Grinding Stone": 1
        }
    },
    "Golden Scale Shoulders": {
        "ID":       3841,
        "Learn":    175,
        "Yellow":   200,
        "Green":    212,
        "Grey":     225,
        "Source":   "Drop",
        "RecipeID": 3871,
        "Reagents": {
            "Steel Bar": 6,
			"Gold Bar": 2,
			"Heavy Grinding Stone": 1
        }
    },
    "Golden Skeleton Key": {
        "ID":       15870,
        "Learn":    150,
        "Yellow":   150,
        "Green":    160,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
            "Gold Bar": 1,
			"Heavy Grinding Stone": 1
        },
        "AmuntCrafted": 2
    },
    "Green Iron Boots": {
        "ID":       3484,
        "Learn":    145,
        "Yellow":   175,
        "Green":    190,
        "Grey":     205,
        "Source":   "Drop",
        "RecipeID": 3611,
        "Reagents": {
            "Iron Bar": 4,
			"Lesser Moonstone": 2,
			"Coarse Grinding Stone": 2,
			"Green Dye": 1
        }
    },
    "Green Iron Bracers": {
        "ID":       3835,
        "Learn":    165,
        "Yellow":   190,
        "Green":    202,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
            "Iron Bar": 6,
			"Green Dye": 1
        }
    },
    "Green Iron Gauntlets": {
        "ID":       3485,
        "Learn":    150,
        "Yellow":   180,
        "Green":    195,
        "Grey":     210,
        "Source":   "Drop",
        "RecipeID": 3612,
        "Reagents": {
            "Iron Bar": 4,
			"Small Lustrous Pearl": 2,
			"Coarse Grinding Stone": 2,
			"Green Dye": 1
        }
    },
    "Green Iron Hauberk": {
        "ID":       3844,
        "Learn":    180,
        "Yellow":   205,
        "Green":    217,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
            "Iron Bar": 20,
			"Heavy Grinding Stone": 4,
			"Jade": 2,
			"Moss Agate": 2,
			"Green Leather Armor": 1
        }
    },
    "Green Iron Helm": {
        "ID":       3836,
        "Learn":    170,
        "Yellow":   195,
        "Green":    207,
        "Grey":     220,
        "Source":   "Trainer",
        "Reagents": {
            "Iron Bar": 12,
			"Citrine": 1,
			"Green Dye": 1
        }
    },
    "Green Iron Leggings": {
        "ID":       3842,
        "Learn":    155,
        "Yellow":   180,
        "Green":    192,
        "Grey":     205,
        "Source":   "Trainer",
        "Reagents": {
            "Iron Bar": 8,
			"Heavy Grinding Stone": 1,
			"Green Dye": 1
        }
    },
    "Green Iron Shoulders": {
        "ID":       3840,
        "Learn":    160,
        "Yellow":   185,
        "Green":    197,
        "Grey":     210,
        "Source":   "Drop",
        "RecipeID": 3870,
        "Reagents": {
            "Iron Bar": 7,
			"Heavy Grinding Stone": 1,
			"Green Dye": 1
        }
    },
    "Hardened Iron Shortsword": {
        "ID":       3849,
        "Learn":    160,
        "Yellow":   185,
        "Green":    197,
        "Grey":     210,
        "Source":   "VendorLimited",
        "RecipeID": 12162,
        "Reagents": {
            "Iron Bar": 6,
			"Strong Flux": 2,
			"Heavy Grinding Stone": 1,
			"Lesser Moonstone": 2,
			"Heavy Leather": 3
        }
    },
    "Heavy Bronze Mace": {
        "ID":       3491,
        "Learn":    130,
        "Yellow":   160,
        "Green":    175,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 8,
			"Strong Flux": 1,
			"Moss Agate": 1,
			"Shadowgem": 1,
			"Coarse Grinding Stone": 2,
			"Medium Leather": 2
        }
    },
    "Heavy Copper Broadsword": {
        "ID":       3487,
        "Learn":    95,
        "Yellow":   135,
        "Green":    155,
        "Grey":     175,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 14,
			"Weak Flux": 2,
			"Tigerseye": 2,
			"Medium Leather": 2
        }
    },
    "Heavy Copper Maul": {
        "ID":       6214,
        "Learn":    65,
        "Yellow":   105,
        "Green":    125,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 12,
			"Weak Flux": 2,
			"Light Leather": 2
        }
    },
    "Heavy Grinding Stone": {
        "ID":       3486,
        "Learn":    125,
        "Yellow":   125,
        "Green":    137,
        "Grey":     150,
        "Source":   "Trainer",
        "Reagents": {
            "Heavy Stone": 3
        }
    },
    "Heavy Mithril Axe": {
        "ID":       7941,
        "Learn":    210,
        "Yellow":   235,
        "Green":    247,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
            "Mithril Bar": 12,
			"Citrine": 2,
			"Solid Grinding Stone": 1,
			"Heavy Leather": 4
        }
    },
    "Heavy Mithril Boots": {
        "ID":       7933,
        "Learn":    235,
        "Yellow":   255,
        "Green":    265,
        "Grey":     275,
        "Source":   "Trainer",
        "Reagents": {
            "Mithril Bar": 14,
			"Thick Leather": 4
        }
    },
    "Heavy Mithril Breastplate": {
        "ID":       7930,
        "Learn":    230,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
            "Mithril Bar": 16
        }
    },
    "Heavy Mithril Gauntlet": {
        "ID":       7919,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
        "Reagents": {
            "Mithril Bar": 6,
			"Mageweave Cloth": 4
        }
    },
    "Heavy Mithril Helm": {
        "ID":       7934,
        "Learn":    245,
        "Yellow":   255,
        "Green":    265,
        "Grey":     275,
        "Source":   "Drop",
        "RecipeID": 7990,
        "Reagents": {
            "Mithril Bar": 14,
			"Aquamarine": 1
        }
    },
    "Heavy Mithril Pants": {
        "ID":       7912,
        "Learn":    210,
        "Yellow":   230,
        "Green":    240,
        "Grey":     250,
        "Source":   "Drop",
        "RecipeID": 7975,
        "Reagents": {
            "Mithril Bar": 10,
			"Lesser Moonstone": 2
        }
    },
    "Heavy Mithril Shoulder": {
        "ID":       7918,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
        "Reagents": {
            "Mithril Bar": 8,
			"Heavy Leather": 6
        }
    },
    "Heavy Sharpening Stone": {
        "ID":       2871,
        "Learn":    125,
        "Yellow":   125,
        "Green":    132,
        "Grey":     140,
        "Source":   "Trainer",
        "Reagents": {
            "Heavy Stone": 1
        }
    },
    "Heavy Timbermaw Belt": {
        "ID":       19043,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Reputation",
        "RecipeID": 19202,
        "Reagents": {
            "Thorium Bar": 12,
			"Essence of Earth": 3,
			"Living Essence": 3
        }
    },
    "Heavy Weightstone": {
        "ID":       3241,
        "Learn":    125,
        "Yellow":   125,
        "Green":    132,
        "Grey":     140,
        "Source":   "Trainer",
        "Reagents": {
            "Heavy Stone": 1,
			"Wool Cloth": 1
        }
    },
    "Huge Thorium Battleaxe": {
        "ID":       12775,
        "Learn":    280,
        "Yellow":   305,
        "Green":    317,
        "Grey":     330,
        "Source":   "Vendor",
        "RecipeID": 12823,
        "Reagents": {
            "Thorium Bar": 40,
			"Dense Grinding Stone": 6,
			"Rugged Leather": 6
        }
    },
    "Imperial Plate Belt": {
        "ID":       12424,
        "Learn":    265,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Quest",
		"Faction":  "Any",
        "RecipeID": 12688,
        "Reagents": {
            "Thorium Bar": 22,
			"Rugged Leather": 6,
			"Aquamarine": 1
        }
    },
    "Imperial Plate Boots": {
        "ID":       12426,
        "Learn":    295,
        "Yellow":   315,
        "Green":    325,
        "Grey":     335,
        "Source":   "Quest",
		"Faction":  "Any",
        "RecipeID": 12700,
        "Reagents": {
            "Thorium Bar": 34,
			"Star Ruby": 1,
			"Aquamarine": 1
        }
    },
    "Imperial Plate Bracers": {
        "ID":       12425,
        "Learn":    270,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Quest",
        "RecipeID": 12690,
        "Reagents": {
            "Thorium Bar": 20,
			"Star Ruby": 1
        }
    },
    "Imperial Plate Helm": {
        "ID":       12427,
        "Learn":    295,
        "Yellow":   315,
        "Green":    325,
        "Grey":     335,
        "Source":   "Quest",
        "RecipeID": 12701,
        "Reagents": {
            "Thorium Bar": 34,
			"Star Ruby": 2
        }
    },
    "Imperial Plate Shoulders": {
        "ID":       12428,
        "Learn":    265,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Quest",
        "RecipeID": 12687,
        "Reagents": {
            "Thorium Bar": 24,
			"Rugged Leather": 6,
			"Citrine": 2
        }
    },
    "Inlaid Mithril Cylinder": {
        "ID":       9060,
        "Learn":    200,
        "Yellow":   225,
        "Green":    237,
        "Grey":     250,
        "Source":   "Drop",
        "RecipeID": 10713,
        "Reagents": {
            "Mithril Bar": 5,
			"Gold Bar": 1,
			"Truesilver Bar": 1
        }
    },
    "Iridescent Hammer": {
        "ID":       5541,
        "Learn":    140,
        "Yellow":   170,
        "Green":    185,
        "Grey":     200,
        "Source":   "Drop",
        "RecipeID": 5543,
        "Reagents": {
            "Bronze Bar": 10,
			"Strong Flux": 1,
			"Iridescent Pearl": 1,
			"Coarse Grinding Stone": 2,
			"Medium Leather": 2
        }
    },
    "Iron Buckle": {
        "ID":       7071,
        "Learn":    150,
        "Yellow":   150,
        "Green":    152,
        "Grey":     155,
        "Source":   "Trainer",
        "Reagents": {
            "Iron Bar": 1
        },
        "AmountCrafted": 2
    },
    "Iron Counterweight": {
        "ID":       6043,
        "Learn":    165,
        "Yellow":   190,
        "Green":    202,
        "Grey":     215,
        "Source":   "Drop",
        "RecipeID": 6045,
        "Reagents": {
            "Iron Bar": 4,
			"Coarse Grinding Stone": 2,
			"Lesser Moonstone": 1
        }
    },
    "Iron Shield Spike": {
        "ID":       6042,
        "Learn":    150,
        "Yellow":   180,
        "Green":    195,
        "Grey":     210,
        "Source":   "Drop",
        "RecipeID": 6044,
        "Reagents": {
            "Iron Bar": 6,
			"Coarse Grinding Stone": 4
        }
    },
    "Ironforge Breastplate": {
        "ID":       6731,
        "Learn":    100,
        "Yellow":   140,
        "Green":    160,
        "Grey":     180,
        "Source":   "Quest",
		"Faction":  "Alliance",
        "RecipeID": 6735,
        "Reagents": {
            "Copper Bar": 16,
			"Tigerseye": 2,
			"Rough Grinding Stone": 3
        }
    },
    "Jade Serpentblade": {
        "ID":       3850,
        "Learn":    175,
        "Yellow":   200,
        "Green":    212,
        "Grey":     225,
        "Source":   "Drop",
        "RecipeID": 3866,
        "Reagents": {
            "Iron Bar": 8,
			"Strong Flux": 2,
			"Heavy Grinding Stone": 2,
			"Jade": 2,
			"Heavy Leather": 3
        }
    },
    "Massive Iron Axe": {
        "ID":       3855,
        "Learn":    185,
        "Yellow":   210,
        "Green":    222,
        "Grey":     235,
        "Source":   "VendorLimited",
        "RecipeID": 12164,
        "Reagents": {
            "Iron Bar": 14,
			"Strong Flux": 2,
			"Heavy Grinding Stone": 2,
			"Gold Bar": 4,
			"Heavy Leather": 2
        }
    },
    "Mighty Iron Hammer": {
        "ID":       3492,
        "Learn":    145,
        "Yellow":   175,
        "Green":    190,
        "Grey":     205,
        "Source":   "Drop",
        "RecipeID": 3608,
        "Reagents": {
            "Iron Bar": 6,
			"Strong Flux": 2,
			"Elixir of Ogres Strength": 1,
			"Lesser Moonstone": 2,
			"Coarse Grinding Stone": 2,
			"Medium Leather": 2
        }
    },
    "Mithril Coif": {
        "ID":       7931,
        "Learn":    230,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
            "Mithril Bar": 10,
			"Mageweave Cloth": 6
        }
    },
    "Mithril Scale Bracers": {
        "ID":       7924,
        "Learn":    215,
        "Yellow":   235,
        "Green":    245,
        "Grey":     255,
        "Source":   "VendorLimited",
        "RecipeID": 7995,
        "Reagents": {
            "Mithril Bar": 8,
			"Citrine": 2
        }
    },
    "Mithril Scale Pants": {
        "ID":       7920,
        "Learn":    210,
        "Yellow":   230,
        "Green":    240,
        "Grey":     250,
        "Source":   "Trainer",
        "Reagents": {
            "Mithril Bar": 12
        }
    },
    "Mithril Scale Shoulders": {
        "ID":       7932,
        "Learn":    235,
        "Yellow":   255,
        "Green":    265,
        "Grey":     275,
        "Source":   "Drop",
        "RecipeID": 7991,
        "Reagents": {
            "Mithril Bar": 14,
			"Thick Leather": 4,
			"Citrine": 4
        }
    },
    "Mithril Shield Spike": {
        "ID":       7967,
        "Learn":    215,
        "Yellow":   235,
        "Green":    245,
        "Grey":     255,
        "Source":   "Drop",
        "RecipeID": 7976,
        "Reagents": {
            "Mithril Bar": 4,
			"Truesilver Bar": 2,
			"Solid Grinding Stone": 4
        }
    },
    "Mithril Spurs": {
        "ID":       7969,
        "Learn":    235,
        "Yellow":   255,
        "Green":    265,
        "Grey":     275,
        "Source":   "Drop",
        "RecipeID": 7989,
        "Reagents": {
            "Mithril Bar": 4,
			"Solid Grinding Stone": 3
        }
    },
    "Moonsteel Broadsword": {
        "ID":       3853,
        "Learn":    180,
        "Yellow":   205,
        "Green":    217,
        "Grey":     230,
        "Source":   "VendorLimited",
        "RecipeID": 12163,
        "Reagents": {
            "Steel Bar": 8,
			"Strong Flux": 2,
			"Heavy Grinding Stone": 2,
			"Lesser Moonstone": 3,
			"Heavy Leather": 3,
        }
    },
    "Orcish War Leggings": {
        "ID":       7929,
        "Learn":    230,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Quest",
		"Faction":  "Horde",
        "RecipeID": 7994,
        "Reagents": {
            "Mithril Bar": 12,
			"Elemental Earth": 1
        }
    },
    "Ornate Mithril Boots": {
        "ID":       7936,
        "Learn":    245,
        "Yellow":   265,
        "Green":    275,
        "Grey":     285,
        "Source":   "Quest",
		"Faction":  "Any",
        "RecipeID": 7988,
        "Reagents": {
            "Mithril Bar": 14,
			"Truesilver Bar": 2,
			"Thick Leather": 4,
			"Solid Grinding Stone": 1,
			"Aquamarine": 1
        }
    },
    "Ornate Mithril Breastplate": {
        "ID":       7935,
        "Learn":    240,
        "Yellow":   260,
        "Green":    270,
        "Grey":     280,
        "Source":   "Quest",
		"Faction":  "Any",
        "RecipeID": 7986,
        "Reagents": {
            "Mithril Bar": 16,
			"Truesilver Bar": 6,
			"Heart of Fire": 1,
			"Solid Grinding Stone": 1
        }
    },
    "Ornate Mithril Gloves": {
        "ID":       7927,
        "Learn":    220,
        "Yellow":   240,
        "Green":    250,
        "Grey":     260,
        "Source":   "Quest",
		"Faction":  "Any",
        "RecipeID": 7984,
        "Reagents": {
            "Mithril Bar": 10,
			"Mageweave Cloth": 6,
			"Truesilver Bar": 1,
			"Solid Grinding Stone": 1
        }
    },
    "Ornate Mithril Helm": {
        "ID":       7937,
        "Learn":    245,
        "Yellow":   265,
        "Green":    275,
        "Grey":     285,
        "Source":   "Quest",
		"Faction":  "Any",
        "RecipeID": 7987,
        "Reagents": {
            "Mithril Bar": 16,
			"Truesilver Bar": 2,
			"Black Pearl": 1,
			"Solid Grinding Stone": 1
        }
    },
    "Ornate Mithril Pants": {
        "ID":       7926,
        "Learn":    220,
        "Yellow":   240,
        "Green":    250,
        "Grey":     260,
        "Source":   "Quest",
		"Faction":  "Any",
        "RecipeID": 7983,
        "Reagents": {
            "Mithril Bar": 12,
			"Truesilver Bar": 1,
			"Solid Grinding Stone": 1,
			"Aquamarine": 1
        }
    },
    "Ornate Mithril Shoulders": {
        "ID":       7928,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Quest",
		"Faction":  "Any",
        "RecipeID": 7985,
        "Reagents": {
            "Mithril Bar": 12,
			"Truesilver Bar": 1,
			"Thick Leather": 6
        }
    },
    "Ornate Thorium Handaxe": {
        "ID":       12773,
        "Learn":    275,
        "Yellow":   300,
        "Green":    312,
        "Grey":     325,
        "Source":   "Vendor",
        "RecipeID": 12819,
        "Reagents": {
            "Thorium Bar": 20,
			"Large Opal": 2,
			"Dense Grinding Stone": 2,
			"Rugged Leather": 4
        }
    },
    "Patterned Bronze Bracers": {
        "ID":       2868,
        "Learn":    120,
        "Yellow":   150,
        "Green":    165,
        "Grey":     180,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 5,
			"Coarse Grinding Stone": 2
        }
    },
    "Pearl-handled Dagger": {
        "ID":       5540,
        "Learn":    110,
        "Yellow":   140,
        "Green":    155,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 6,
			"Strong Flux": 1,
			"Small Lustrous Pearl": 2,
			"Coarse Grinding Stone": 2
        }
    },
    "Phandom Blade": {
        "ID":       7961,
        "Learn":    245,
        "Yellow":   270,
        "Green":    282,
        "Grey":     295,
        "Source":   "Trainer",
        "School":   "Weapon",
        "Reagents": {
            "Mithril Bar": 28,
			"Breath of Wind": 6,
			"Truesilver Bar": 8,
			"Lesser Invisibility Potion": 2,
			"Aquamarine": 6,
			"Solid Grinding Stone": 4,
			"Thick Leather": 2
        }
    },
    "Polished Steel Boots": {
        "ID":       3846,
        "Learn":    185,
        "Yellow":   210,
        "Green":    222,
        "Grey":     235,
        "Source":   "Drop",
        "RecipeID": 3874,
        "Reagents": {
            "Steel Bar": 8,
			"Citrine": 1,
			"Lesser Moonstone": 1,
			"Heavy Grinding Stone": 2
        }
    },
    "Radiant Belt": {
        "ID":       12416,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     300,
        "Source":   "Drop",
        "RecipeID": 12685,
        "Reagents": {
            "Thorium Bar": 10,
			"Heart of Fire": 2
        }
    },
    "Radiant Boots": {
        "ID":       12419,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Drop",
        "RecipeID": 12697,
        "Reagents": {
            "Thorium Bar": 14,
			"Heart of Fire": 4
        }
    },
    "Radiant Breastplate": {
        "ID":       12415,
        "Learn":    270,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Drop",
        "RecipeID": 12689,
        "Reagents": {
            "Thorium Bar": 18,
			"Heart of Fire": 2,
			"Star Ruby": 1
        }
    },
    "Radiant Circlet": {
        "ID":       12417,
        "Learn":    295,
        "Yellow":   315,
        "Green":    325,
        "Grey":     335,
        "Source":   "Drop",
        "RecipeID": 12702,
        "Reagents": {
            "Thorium Bar": 18,
			"Heart of Fire": 4
        }
    },
    "Radiant Gloves": {
        "ID":       12418,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 12695,
        "Reagents": {
            "Thorium Bar": 18,
			"Heart of Fire": 4
        }
    },
    "Rough Bronze Boots": {
        "ID":       6350,
        "Learn":    95,
        "Yellow":   125,
        "Green":    140,
        "Grey":     155,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 6,
			"Rough Grinding Stone": 6
        }
    },
    "Rough Bronze Cuirass": {
        "ID":       2866,
        "Learn":    105,
        "Yellow":   145,
        "Green":    160,
        "Grey":     175,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 7
        }
    },
    "Rough Bronze Leggings": {
        "ID":       2865,
        "Learn":    105,
        "Yellow":   145,
        "Green":    160,
        "Grey":     175,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 6
        }
    },
    "Rough Bronze Shoulders": {
        "ID":       3480,
        "Learn":    110,
        "Yellow":   140,
        "Green":    155,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 5,
			"Shadowgem": 1,
			"Coarse Grinding Stone": 1
        }
    },
    "Rough Copper Vest": {
        "ID":       10421,
        "Learn":    1,
        "Yellow":   15,
        "Green":    35,
        "Grey":     55,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 4
        }
    },
    "Rough Grinding Stone": {
        "ID":       3470,
        "Learn":    25,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Trainer",
        "Reagents": {
            "Rough Stone": 2
        }
    },
    "Rough Sharpening Stone": {
        "ID":       2862,
        "Learn":    1,
        "Yellow":   15,
        "Green":    35,
        "Grey":     55,
        "Source":   "Trainer",
        "Reagents": {
            "Rough Stone": 1
        }
    },
    "Rough Weightstone": {
        "ID":       3239,
        "Learn":    1,
        "Yellow":   15,
        "Green":    35,
        "Grey":     55,
        "Source":   "Trainer",
        "Reagents": {
            "Rough Stone": 1,
			"Linen Cloth": 1
        }
    },
    "Runed Copper Belt": {
        "ID":       2857,
        "Learn":    70,
        "Yellow":   110,
        "Green":    130,
        "Grey":     150,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 10
        }
    },
    "Runed Copper Bracers": {
        "ID":       2854,
        "Learn":    90,
        "Yellow":   115,
        "Green":    127,
        "Grey":     140,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 10,
			"Rough Grinding Stone": 3
        }
    },
    "Runed Copper Breastplate": {
        "ID":       2864,
        "Learn":    80,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160,
        "Source":   "Drop",
        "RecipeID": 2881,
        "Reagents": {
            "Copper Bar": 12,
			"Shadowgem": 1,
			"Rough Grinding Stone": 2
        }
    },
    "Runed Copper Gauntlets": {
        "ID":       3472,
        "Learn":    40,
        "Yellow":   80,
        "Green":    100,
        "Grey":     120,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 8,
			"Rough Grinding Stone": 2
        }
    },
    "Runed Copper Pants": {
        "ID":       3473,
        "Learn":    45,
        "Yellow":   85,
        "Green":    105,
        "Grey":     125,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 8,
			"Fine Thread": 2,
			"Rough Grinding Stone": 3
        }
    },
    "Runed Mithril Hammer": {
        "ID":       7946,
        "Learn":    245,
        "Yellow":   270,
        "Green":    282,
        "Grey":     295,
        "Source":   "Drop",
        "RecipeID": 8028,
        "Reagents": {
            "Mithril Bar": 18,
			"Core of Earth": 2,
			"Solid Grinding Stone": 1,
			"Thick Leather": 4
        }
    },
    "Searing Golden Blade": {
        "ID":       12260,
        "Learn":    190,
        "Yellow":   215,
        "Green":    227,
        "Grey":     240,
        "Source":   "Drop",
        "RecipeID": 12261,
        "Reagents": {
            "Steel Bar": 10,
			"Gold Bar": 4,
			"Elemental Fire": 2,
			"Heavy Leather": 2
        }
    },
    "Serenity": {
        "ID":       12781,
        "Learn":    285,
        "Yellow":   310,
        "Green":    322,
        "Grey":     335,
        "Source":   "Drop",
        "RecipeID": 12827,
        "Reagents": {
            "Enchanted Thorium Bar": 6,
			"Arcanite Bar": 2,
			"Powerful Mojo": 4,
			"Large Opal": 2,
			"Blue Sapphire": 2,
			"Huge Emerald": 1
        }
    },
    "Shadow Crescent Axe": {
        "ID":       3856,
        "Learn":    200,
        "Yellow":   225,
        "Green":    237,
        "Grey":     250,
        "Source":   "Drop",
        "RecipeID": 3869,
        "Reagents": {
            "Steel Bar": 10,
			"Strong Flux": 2,
			"Heavy Grinding Stone": 3,
			"Shadow Oil": 1,
			"Heavy Leather": 3
        }
    },
    "Shining Silver Breastplate": {
        "ID":       2870,
        "Learn":    145,
        "Yellow":   175,
        "Green":    190,
        "Grey":     205,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 20,
			"Moss Agate": 2,
			"Lesser Moonstone": 2,
			"Iridescent Pearl": 2,
			"Silver Bar": 4
        }
    },
    "Silver Rod": {
        "ID":       6338,
        "Learn":    100,
        "Yellow":   105,
        "Green":    107,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
            "Silver Bar": 1,
			"Rough Grinding Stone": 2
        }
    },
    "Silver Skeleton Key": {
        "ID":       15869,
        "Learn":    100,
        "Yellow":   100,
        "Green":    110,
        "Grey":     120,
        "Source":   "Trainer",
        "Reagents": {
            "Silver Bar": 1,
			"Rough Grinding Stone": 1
        },
        "AmuntCrafted": 2
    },
    "Silvered Bronze Boots": {
        "ID":       3482,
        "Learn":    130,
        "Yellow":   160,
        "Green":    175,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 6,
			"Silver Bar": 1,
			"Coarse Grinding Stone": 2
        }
    },
    "Silvered Bronze Breastplate": {
        "ID":       2869,
        "Learn":    130,
        "Yellow":   160,
        "Green":    175,
        "Grey":     190,
        "Source":   "Drop",
        "RecipeID": 5578,
        "Reagents": {
            "Bronze Bar": 10,
			"Silver Bar": 2,
			"Coarse Grinding Stone": 2,
			"Lesser Moonstone": 1
        }
    },
    "Silvered Bronze Gauntlets": {
        "ID":       3483,
        "Learn":    135,
        "Yellow":   165,
        "Green":    180,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 8,
			"Silver Bar": 1,
			"Coarse Grinding Stone": 2
        }
    },
    "Silvered Bronze Leggings": {
        "ID":       10423,
        "Learn":    155,
        "Yellow":   180,
        "Green":    192,
        "Grey":     205,
        "Source":   "Drop",
        "RecipeID": 10424,
        "Reagents": {
            "Bronze Bar": 12,
			"Silver Bar": 4,
			"Coarse Grinding Stone": 2
        }
    },
    "Silvered Bronze Shoulders": {
        "ID":       3481,
        "Learn":    125,
        "Yellow":   155,
        "Green":    170,
        "Grey":     185,
        "Source":   "Drop",
        "RecipeID": 2882,
        "Reagents": {
            "Bronze Bar": 8,
			"Silver Bar": 2,
			"Coarse Grinding Stone": 2
        }
    },
    "Solid Grinding Stone": {
        "ID":       7966,
        "Learn":    200,
        "Yellow":   200,
        "Green":    200,
        "Grey":     205,
        "Source":   "Trainer",
        "Reagents": {
            "Solid Stone": 4
        }
    },
    "Solid Iron Maul": {
        "ID":       3851,
        "Learn":    155,
        "Yellow":   180,
        "Green":    192,
        "Grey":     205,
        "Source":   "VendorLimited",
        "RecipeID": 10858,
        "Reagents": {
            "Iron Bar": 8,
			"Strong Flux": 2,
			"Heavy Grinding Stone": 1,
			"Silver Bar": 4,
			"Heavy Leather": 2
        }
    },
    "Solid Sharpening Stone": {
        "ID":       7964,
        "Learn":    200,
        "Yellow":   200,
        "Green":    205,
        "Grey":     210,
        "Source":   "Trainer",
        "Reagents": {
            "Solid Stone": 1
        }
    },
    "Solid Weightstone": {
        "ID":       7965,
        "Learn":    200,
        "Yellow":   200,
        "Green":    205,
        "Grey":     210,
        "Source":   "Trainer",
        "Reagents": {
            "Solid Stone": 1,
			"Silk Cloth": 1
        }
    },
    "Steel Breastplate": {
        "ID":       7963,
        "Learn":    200,
        "Yellow":   225,
        "Green":    237,
        "Grey":     250,
        "Source":   "Trainer",
        "Reagents": {
            "Steel Bar": 16,
			"Heavy Grinding Stone": 3
        }
    },
    "Steel Plate Helm": {
        "ID":       7922,
        "Learn":    215,
        "Yellow":   235,
        "Green":    245,
        "Grey":     255,
        "Source":   "Trainer",
        "Reagents": {
            "Steel Bar": 14,
			"Solid Grinding Stone": 1
        }
    },
    "Steel Weapon Chain": {
        "ID":       6041,
        "Learn":    190,
        "Yellow":   215,
        "Green":    227,
        "Grey":     240,
        "Source":   "Drop",
        "RecipeID": 6046,
        "Reagents": {
            "Steel Bar": 8,
			"Heavy Grinding Stone": 2,
			"Heavy Leather": 4
        }
    },
    "Storm Gauntlets": {
        "ID":       12632,
        "Learn":    295,
        "Yellow":   315,
        "Green":    325,
        "Grey":     335,
        "Source":   "Vendor",
        "School":   "Armor",
        "RecipeID": 12703,
        "Reagents": {
            "Thorium Bar": 20,
			"Enchanted Thorium Bar": 4,
			"Essence of Water": 4,
			"Blue Sapphire": 4
        }
    },
    "The Shatterer": {
        "ID":       7954,
        "Learn":    235,
        "Yellow":   260,
        "Green":    272,
        "Grey":     285,
        "Source":   "Trainer",
        "School":   "Weapon",
        "Reagents": {
            "Mithril Bar": 24,
			"Core of Earth": 4,
			"Truesilver Bar": 6,
			"Citrine": 5,
			"Jade": 5,
			"Solid Grinding Stone": 4,
			"Thick Leather": 4
        }
    },
    "Thick War Axe": {
        "ID":       3489,
        "Learn":    70,
        "Yellow":   110,
        "Green":    130,
        "Grey":     150,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 10,
			"Weak Flux": 2,
			"Silver Bar": 2,
			"Rough Grinding Stone": 2,
			"Light Leather": 2
        }
    },
    "Thorium Armor": {
        "ID":       12405,
        "Learn":    250,
        "Yellow":   270,
        "Green":    280,
        "Grey":     290,
        "Source":   "Drop",
        "RecipeID": 12682,
        "Reagents": {
            "Thorium Bar": 16,
			"Blue Sapphire": 1,
			"Yellow Power Crystal": 4
        }
    },
    "Thorium Belt": {
        "ID":       12406,
        "Learn":    250,
        "Yellow":   270,
        "Green":    280,
        "Grey":     290,
        "Source":   "Drop",
        "RecipeID": 12683,
        "Reagents": {
            "Thorium Bar": 12,
			"Red Power Crystal": 4
        }
    },
    "Thorium Boots": {
        "ID":       12409,
        "Learn":    280,
        "Yellow":   300,
        "Green":    310,
        "Grey":     320,
        "Source":   "Drop",
        "RecipeID": 12693,
        "Reagents": {
            "Thorium Bar": 20,
			"Rugged Leather": 8,
			"Green Power Crystal": 4
        }
    },
    "Thorium Bracers": {
        "ID":       12408,
        "Learn":    255,
        "Yellow":   275,
        "Green":    285,
        "Grey":     295,
        "Source":   "Drop",
        "RecipeID": 12684,
        "Reagents": {
            "Thorium Bar": 12,
			"Blue Power Crystal": 4
        }
    },
    "Thorium Helm": {
        "ID":       12410,
        "Learn":    280,
        "Yellow":   300,
        "Green":    310,
        "Grey":     320,
        "Source":   "Drop",
        "RecipeID": 12694,
        "Reagents": {
            "Thorium Bar": 24,
			"Star Ruby": 1,
			"Yellow Power Crystal": 4
        }
    },
    "Thorium Shield Spike": {
        "ID":       12645,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Drop",
        "RecipeID": 12692,
        "Reagents": {
            "Thorium Bar": 4,
			"Dense Grinding Stone": 4,
			"Essence of Earth": 2
        }
    },
    "Truesilver Breastplate": {
        "ID":       7939,
        "Learn":    245,
        "Yellow":   265,
        "Green":    275,
        "Grey":     285,
        "Source":   "Trainer",
        "School":   "Armor",
        "Reagents": {
            "Mithril Bar": 12,
			"Truesilver Bar": 24,
			"Star Ruby": 4,
			"Black Pearl": 4,
			"Solid Grinding Stone": 2
        }
    },
    "Truesilver Champion": {
        "ID":       7960,
        "Learn":    260,
        "Yellow":   285,
        "Green":    297,
        "Grey":     310,
        "Source":   "Trainer",
        "School":   "Weapon",
        "Reagents": {
            "Mithril Bar": 30,
			"Truesilver Bar": 16,
			"Star Ruby": 6,
			"Breath of Wind": 4,
			"Solid Grinding Stone": 8,
			"Thick Leather": 6
        }
    },
    "Truesilver Gauntlets": {
        "ID":       7938,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Trainer",
        "School":   "Armor",
        "Reagents": {
            "Mithril Bar": 10,
			"Truesilver Bar": 8,
			"Aquamarine": 3,
			"Citrine": 3,
			"Guardian Gloves": 1,
			"Solid Grinding Stone": 2
        }
    },
    "Truesilver Rod": {
        "ID":       11144,
        "Learn":    200,
        "Yellow":   205,
        "Green":    207,
        "Grey":     210,
        "Source":   "Trainer",
        "Reagents": {
            "Truesilver Bar": 1,
			"Heavy Grinding Stone": 1
        }
    },
    "Truesilver Skeleton Key": {
        "ID":       15871,
        "Learn":    200,
        "Yellow":   200,
        "Green":    210,
        "Grey":     220,
        "Source":   "Trainer",
        "Reagents": {
            "Truesilver Bar": 1,
			"Solid Grinding Stone": 1
        },
        "AmuntCrafted": 2
    },
    "Volcanic Hammer": {
        "ID":       12792,
        "Learn":    290,
        "Yellow":   315,
        "Green":    327,
        "Grey":     340,
        "Source":   "Drop",
        "RecipeID": 12828,
        "Reagents": {
            "Thorium Bar": 30,
			"Heart of Fire": 4,
			"Star Ruby": 4,
			"Rugged Leather": 4
        }
    },
    "Wicked Mithril Blade": {
        "ID":       7943,
        "Learn":    225,
        "Yellow":   250,
        "Green":    262,
        "Grey":     275,
        "Source":   "Drop",
        "RecipeID": 8029,
        "Reagents": {
            "Mithril Bar": 14,
			"Truesilver Bar": 4,
			"Solid Grinding Stone": 1,
			"Thick Leather": 2
        }
    },
    "Wildthorn Mail": {
        "ID":       12624,
        "Learn":    270,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Drop",
        "RecipeID": 12691,
        "School":   "Armor",
        "Reagents": {
            "Thorium Bar": 40,
			"Enchanted Thorium Bar": 2,
			"Living Essence": 4,
			"Wildvine":  4,
			"Huge Emerald": 1
        }
    }
}

import json
with open('blacksmithing.json', 'w') as jsonFile:
    json.dump(recipes, jsonFile)