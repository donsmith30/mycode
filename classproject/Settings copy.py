#!/usr/bin/env python3

"""Escaping the Oregon trail, this is a game based on the famous educational text-based game "The Oregon Trail", created In 1971, by Don Rawitsch.
In ETOT players are set in a post-apocalyptic scenario where they have to escape the west"""

import yaml

with open("Characters.yml", "r") as myf:
    global characters
    characters = yaml.load(myf, Loader=yaml.FullLoader)

with open("Landmarks.yml", "r") as myf:
    global landmarks
    landmarks = yaml.load(myf, Loader=yaml.FullLoader)

with open("Shop.yml", "r") as myf:
    global shop
    shop = yaml.load(myf, Loader=yaml.FullLoader)

character = "BANKER"
selectedCharacter = characters[character]
currentLocation = "Boring"
pointOfOrigin = ""
destinationLocation = ""
daysTraveled = 0
milesTraveled = 0
playerStatus="Alive"
pace = 12

