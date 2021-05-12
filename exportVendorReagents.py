#!/usr/bin/env python3.7

items = {
    "Black Dye": 1000,
    "Blank Parchment": 500,
    "Bleach": 25,
    "Blue Dye": 50,
    "Coarse Thread": 10,
    "Copper Rod": 130,
    "Crystal Vial": 500,
    "Empty Vial": 4,
    "Engineers Ink": 2000,
    "Fine Thread": 100,
    "Gray Dye": 350,
    "Green Dye": 100,
    "Heavy Silken Thread": 2000,
    "Heavy Stock": 2000,
    "Holiday Spices": 10,
    "Holiday Spirits": 50,
    "Hot Spices": 40,
    "Ice Cold Milk": 100,
    "Imbued Vial": 6000,
    "Leaded Vial": 40,
    "Maple Seed": 200,
    "Mild Spices": 10,
    "Nightcrawlers": 100,
    "Orange Dye": 1000,
    "Pink Dye": 2500,
    "Purple Dye": 2500,
    "Red Dye": 50,
    "Refreshing Spring Water": 5,
    "Rhapsody Malt": 50,
    "Rune Thread": 4500,
    "Salt": 50,
    "Shiny Red Apple": 5,
    "Silken Thread": 500,
    "Simple Wood": 40,
    "Skin of Dwarven Stout": 110,
    "Snowball": 2,
    "Soothing Spices": 160,
    "Star Wood": 4050,
    "Stormwind Seasoning Herbs": 20,
    "Stranglethorn Seed": 400,
    "Strong Flux": 2000,
    "Weak Flux": 100,
    "Wooden Stock": 200,
    "Yellow Dye": 500
}

import json

with open("vendorReagents.json", 'w') as jsonFile:
    json.dump(items, jsonFile)