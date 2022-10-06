#!/usr/bin/env python3

"""Alta3 Student | Donald Smith
Global Settings"""

import yaml


with open("Characters.yml", "r") as myf:
    global CHARACTERS
    CHARACTERS = yaml.load(myf, Loader=yaml.FullLoader)

with open("Landmarks.yml", "r") as myf:
    global LANDMARKS
    LANDMARKS = yaml.load(myf, Loader=yaml.FullLoader)

with open("Shop.yml", "r") as myf:
    global SHOP
    SHOP = yaml.load(myf, Loader=yaml.FullLoader)

CHARACTER = "Banker"
SELECTEDCHARACTER = CHARACTERS[CHARACTER]
CURRENTLOCATION = "Boring"
POINTOFORIGIN = ""
DESTINATIONLOCATION = ""
DAYSTRAVELED = 0
MILESTRAVELED = 0
PLAYERSTATUS="Alive"
PACE = 12
