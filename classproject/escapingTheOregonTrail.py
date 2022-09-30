#!/usr/bin/env python3
"""Escaping the Oregon trail, this is a game based on the famous educational text based game "The Oregon Trail", created In 1971, by Don Rawitsch. 
In ETOT players are set in a post apocalyptic scenerio where they have to escape the west"""

# MVP Features:
# Begin game screen - Press Start
# Pick Character Profession - like OT,start out with more or less money makes things easier or harder
# Play Game() - holds all game functions
# The quest route - A starting point, an end point with landmarks along the way
# distances between landmarks (dictionary?)
# Inventory System
# Town function
# Shop, Rest, Gamble
# move - while moving reduce distance to next stop, lose food and random encounters
# Team
# random encounters
#
# Bonus items:
# Sign in
# Top Scores
# Achievments

import getpass
import os
import time
from termcolor import colored, cprint

characters = {"Player1": {"Profession": "Banker", "Bio": "A master of managing money, starts out with a substantial life savings", "MaxHealth": 20, "Backpack": {"size": 10,"Gold": 400}}, 
"Player2": {"Profession": "Doctor","Bio": "Somewhat wealthy, healthy and writes perscriptions, a tripple threat","MaxHealth": 30,"Backpack": {"size": 10,"Gold": 200,"Medicine": 20}},
"Player3": {"Profession": "Hunter","Bio": "Has a cache of food saved up from recent hunts, and can carry more than his share","MaxHealth": 20,"Backpack": {"size": 15,"Gold": 100,"Food": 100}},
"Player4": {"Profession": "Hiking Instructor","Bio": "A packing expert, and prepared for almost anything on the trail","MaxHealth": 20,"Backpack": {"size": 20,"Gold": 50,"Medicine": 5,"food": 50}},
"Player5": {"Profession": "?","Bio": "?","MaxHealth": 100,"Backpack": {"size": 100,"Gold": 1000,"Medicine": 100,"Food": 1000}}}


def main():
    titleScreen()

    while True:
        characterSelect()
    # playGame()
    # results()
        break

def titleScreen():
    text = colored("Hit Enter", "green", "on_yellow")
    print("Welcome to ETOT")
    startGame = getpass.getpass(prompt=text, stream=None)

    if startGame == "uuddlrlrba":
        print("congrats")

    clear()

def characterSelect():
    currentSelection=characters["Player1"]
    print(currentSelection)
    input("Would you like this character? ")

def clear():
    print("-")
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()

