#!/usr/bin/env python3

"""TLG Student | Donald Smith
The main code for the game"""

# MVP Features:
# Begin game screen - Press Start
# Pick Character Profession - Difficulty based on this
# Play Game() - holds all game functions
# The quest route - A starting point, an end point with landmarks along the way
# Distances between landmarks (dictionary?)
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
# Achievements

import getpass
import os
import time
import random
from tkinter.messagebox import YES
from unittest import case
import Settings as s
from Encounters import *


def title_screen():
    print("Welcome to ETOT")
    start_game = getpass.getpass("Hit Enter", stream=None)

    if start_game == "uuddlrlrba":
        print("Special Code Entered")
    else:
        s.CHARACTERS.pop("KC")
    clear()

def the_story():
    print(" ------------- Escaping the Oregon Trail ------------- "
    +"\nIn the not so distant future, a rival country on a"
    +"\nwarpath engages in a nuclear engagement with the US."
    +"\nThe country is a wasteland; most infrastructure is"
    +"\ndestroyed and communication and trasportation is non existent now."
    +"\nPockets of the country have survivors,"
    +"\nsome towns have even stood up functioning economies."
    +"\nThe west coast is perhaps the worst off though, a mad scientist"
    +"\nin Washington accidently mutated a large part of their population."
    +"\nThese genetically-mutated creatures are called Cronenbergs,"
    +"\ndue to their disturbing mutated and disfigured appearance"
    +"\nSomewhere in central Oregon another scientist and his grifter"
    +"\nbrother have unleashed unnatural curiosities into the wilderness."
    +"\nYou hear that the East Coast is still somewhat functioning and most"
    +"\nsurvivors have made their way to Independence, Missouri."
    +"\nIt is rumored that Independence has been built into a make shift passage" 
    +"\nway into the slightly normal functioning society of the East Coast."
    +"\nIn a strange coincidence to the proximity of where you live and where you must go,"
    +"\nyou find yourself backtracking the old Oregon Trail to find a better life.\n")

def character_select():
    while True:
        print("What is your profession?")
        for key, value in s.CHARACTERS.items():
            print(key)

        s.CHARACTER = (input("Type a profession to see character info and confirm your choice: ")).title()
        
        # if character is valid load bio
        if s.CHARACTER in s.CHARACTERS:
            s.SELECTEDCHARACTER=s.CHARACTERS[s.CHARACTER]
            print("You were a " + str(s.SELECTEDCHARACTER.get("Profession")) + ", " + str(s.SELECTEDCHARACTER.get("Bio")+ "."))
            confirm_character = input("Would you like this character? [yes] | [no] ")
            if confirm_character.lower() == "yes":
                break
            else:
                clear()
    clear()

def play_game():
    while True:
        town()
        move()
        if s.PLAYERSTATUS == "Alive":
            settle()
        else:
            break

def town():
    s.POINTOFORIGIN = s.LANDMARKS[s.CURRENTLOCATION]
    while True:
        print(f"You are in {s.CURRENTLOCATION}, " + s.POINTOFORIGIN.get("State")+ "!")
        status()
        town_action = input("Would you like to [Shop], [Camp], [Gamble], [Status] or [Leave]? ")
        if town_action.lower() == "shop":
            shop(1)
        if town_action.lower() == "camp":
            camp()
        if town_action.lower() == "gamble":
            gamble()
        if town_action.lower() == "status":
            status()
        if town_action.lower() == "leave":
            print("the journey ahead is " + str(s.LANDMARKS[s.CURRENTLOCATION].get("Distance")) + 
            " miles, you should get there in " + str(s.LANDMARKS[s.CURRENTLOCATION].get("Distance")/12) + " days!")
            print("You have " + str(s.CHARACTERS[s.CHARACTER].get("Backpack").get("Food")) + " portions of food!")
            moveOn = input("Would you like to move out? [Yes]|[No] ")
            if moveOn.lower() == "yes":
                clear()
                break
            else:
                clear()

def move():
    i = 0
    s.POINTOFORIGIN = s.LANDMARKS[s.CURRENTLOCATION]
    s.DESTINATIONLOCATION = str(s.POINTOFORIGIN.get("NextStop"))
    print("Going to - "+ s.DESTINATIONLOCATION + " this will be a " + str(s.POINTOFORIGIN.get("Distance")) + " mile journey!")
    input("Hit Enter")
    
    while i < s.POINTOFORIGIN.get("Distance"):
        clear()
        status()
        print("Going to - "+ s.DESTINATIONLOCATION + f" | {i} miles of a " + str(s.POINTOFORIGIN.get("Distance")) + " mile journey!")
        survivalCheck()
        if s.PLAYERSTATUS == "Alive":
            print("-", end=' ', flush=True)
            time.sleep(.1)
            print("+", end=' ', flush=True)
            time.sleep(.1)
            print("WANDERING", end=' ', flush=True)
            if random.randint(1, 100) >= 90:
                random_encounters()
            i = i + s.PACE
            s.MILESTRAVELED = s.MILESTRAVELED + s.PACE  
            if i > s.POINTOFORIGIN.get("Distance"):
                extra_miles = i - s.POINTOFORIGIN.get("Distance")
                i = s.POINTOFORIGIN.get("Distance")
                s.MILESTRAVELED = s.MILESTRAVELED - extra_miles
                print("Arrived!")
                time.sleep(.3)
        else:
            break

def survivalCheck():
    food = s.SELECTEDCHARACTER.get("Backpack").get("Food")
    ailment = s.SELECTEDCHARACTER.get("Health").get("Ailment")
    med = s.SELECTEDCHARACTER.get("Backpack").get("Medicine")
    health = s.SELECTEDCHARACTER.get("Health").get("HitPoints")
    max_health = s.SELECTEDCHARACTER.get("Health").get("MaxHealth")
    s.DAYSTRAVELED = s.DAYSTRAVELED + 1
    if health > 0:
        if food >= 1:
            food = food-1
            s.SELECTEDCHARACTER['Backpack']['Food']=food
        else:
            health = health-2
            s.SELECTEDCHARACTER['Health']['HitPoints']=health
            print("STARVING, -2 HP ", end=' ', flush=True)
            print(f"{health} / {max_health} HP ", end=' ', flush=True)
        if ailment > 0:
            while True:
                if med >= 1:
                    takeMeds = input(f"You have {ailment} days before you will recover your ailment, "
                    + "Would you like to take medicine to try and reduce or heal your ailment? [Yes]|[No]")
                    if takeMeds.lower() == "yes":
                        medicate()
                        ailment = s.SELECTEDCHARACTER.get("Health").get("Ailment")
                if ailment > 0:
                    ailment = ailment-1
                    s.SELECTEDCHARACTER['Health']['Ailment'] = ailment
                    health = health-2
                    s.SELECTEDCHARACTER['Health']['HitPoints']=health
                    print("ailment, -2 HP", flush=True)
                    print(f"{health} / {max_health} HP ", end=' ', flush=True)
                    break
                else:
                    print("You have recovered from your ailment", flush=True)
                    break  
        
    else:
        print("\nYou have died!")
        s.PLAYERSTATUS = "Dead"
        input("Hit Enter")
        clear()

def random_encounters():
    encounters = [the_bag, the_wanderer, the_trader, the_cronenberg, the_bag]
    print("-", end=' ', flush=True)
    time.sleep(.1)
    print(".", end=' ', flush=True)
    time.sleep(.1)
    print(".", end='', flush=True)
    time.sleep(.1)
    print(".", end='', flush=True)
    time.sleep(.1)
    print(".", end='', flush=True)
    time.sleep(.1)
    print("Random event thing happens")
    input("Hit Enter")
    clear()
    status()
    random_e = random.choice(encounters)
    random_e()


def settle():
    s.CURRENTLOCATION = s.DESTINATIONLOCATION
    print(f"Welcome to - {s.CURRENTLOCATION}!")
    input("Hit Enter")
    clear()

def gamble():
    while True:
        clear()
        print("You have: "+str(s.SELECTEDCHARACTER.get("Backpack").get("Gold"))+" Gold!")
        while True:
            try:
                player_bet = int(input("How much would you like to bet? "))
                assert player_bet <= s.SELECTEDCHARACTER.get("Backpack").get("Gold")
                player_number = int(input("Pick a number between 1-6: "))
                #assert between 1-6
            except ValueError:
                print("Not a number!, use a number or 0 to cancel")
            except AssertionError:
                print("You can't afford to play!")
            else:
                break
        number_to_match = random.randint(1, 6)
        print(f"The number to match was {number_to_match}!")
        players_gold = s.SELECTEDCHARACTER.get("Backpack").get("Gold")
        if player_number == number_to_match:
            print("You win!") 
            players_gold = players_gold+player_bet*2
        else:
            print("You lose!")
            players_gold = players_gold-player_bet 
        s.SELECTEDCHARACTER['Backpack']['Gold']=players_gold
        print("Your Gold balance: "+str(s.SELECTEDCHARACTER.get("Backpack").get("Gold")))        
    
        play_again = input("Play again? [yes] | [no] ")
        if play_again.lower() == "no":
            break

def status():
    food = s.SELECTEDCHARACTER.get("Backpack").get("Food")
    gold = s.SELECTEDCHARACTER.get("Backpack").get("Gold")
    ailment = s.SELECTEDCHARACTER.get("Health").get("Ailment")
    med = s.SELECTEDCHARACTER.get("Backpack").get("Medicine")
    health = s.SELECTEDCHARACTER.get("Health").get("HitPoints")
    max_health = s.SELECTEDCHARACTER.get("Health").get("MaxHealth")
    print("--------STATUS--------")
    print(s.CHARACTER)
    print(f"{health} / {max_health} HP ")
    if health > 0:
        if ailment != 0:
            print(f"You have {ailment} days before you will recover your ailment"
            +"\nYou should try to medicate...")
        if health < max_health:
            print("Your health is low, you should try to rest")
    print(f"{gold} Gold | {med} Meds | {food} Portions of Food ")
    print(f"{s.DAYSTRAVELED} days traveled, and {s.MILESTRAVELED} miles traveled!")
    print(f"Last location: {s.CURRENTLOCATION}, "+(s.LANDMARKS.get(s.CURRENTLOCATION).get("State"))+f" | Player's status: {s.PLAYERSTATUS}")
    print("======================")

def camp():
    clear()
    print("Setting up camp..."
    + "\nEvery day of rest you will consume food, but heal damage delt by the journey!"
    + "\nUntreated ailments will still hurt you over time") 
    while True:
        status()
        campAction = input("Would you like to [Medicate], [Rest] or [Leave]? ")
        if campAction.lower() == "medicate":
            medicate()
            input("Hit Enter")
            clear()
        elif campAction.lower() == "rest":
            rest()
            input("Hit Enter")
            clear()
        elif campAction.lower() == "leave":
            print(f"You break down camp, and continue on your journey")
            break

def rest():
    health = s.SELECTEDCHARACTER.get("Health").get("HitPoints")
    max_health = s.SELECTEDCHARACTER.get("Health").get("MaxHealth")
    while True:
        try:
            days = int(input("How many days would you like to rest... "))
        except ValueError:
            print("Not a number!, use a number or 0 to cancel")
        else:
            break
    restDay = 0
    while restDay < days:
        time.sleep(.2)
        restDay = restDay + 1
        print(f"Resting {str(restDay)} out of {days} days!", flush=True)
        if max_health > health:
            health = health + 1
            s.SELECTEDCHARACTER['Health']['HitPoints']=health
            print(f"{health} / {max_health} HP", flush=True)
        survivalCheck()

def medicate():
    ailment = s.SELECTEDCHARACTER.get("Health").get("Ailment")
    med = s.SELECTEDCHARACTER.get("Backpack").get("Medicine")
    if med >= 1:
        med = med-1
        s.SELECTEDCHARACTER['Backpack']['Medicine']=med    
        medEffects = random.randint(3, 9)
        if ailment >= medEffects:
            ailment = ailment-medEffects
            s.SELECTEDCHARACTER['Health']['Ailment'] = ailment
            print(f"Medicine reduced ailment by {medEffects} days")
        else:
            s.SELECTEDCHARACTER['Health']['Ailment'] = 0
            print("You have recovered!")
    else:
        print("You have no medicine!")

def shop(Economy):
    clear()
    gold = s.SELECTEDCHARACTER.get("Backpack").get("Gold")
    print("What would you like to buy? ")
    while True:
        print("\n---------For  Sale---------")
        print("Item | Cost\n")
        for key, val in s.SHOP.items():
            print(key, end=" | ")
            print(val*Economy)
        print("\n-----Current Inventory-----"
        +"\nItem | Qty\n")
        for key, val in s.SELECTEDCHARACTER.get("Backpack").items():
            print(key, end=" | ")
            print(val)
        print("\n===========================\n")
        buyItem = (input("What would you like to buy? ")).title()
        while True:
            try:
                buyQty = int(input("How many do you want? "))
                cost = s.SHOP.get(buyItem) * buyQty * Economy
                assert gold > cost
            except ValueError:
                print("Not a number!, use a number or 0 to cancel")
            except AssertionError:
                print("You can't afford that!")
            else:
                break
        if buyItem in s.SHOP:
            cost = s.SHOP.get(buyItem) * buyQty * Economy
            print("Total cost: "+str(cost))
            if gold >= cost:
                gold = gold - cost
                s.SELECTEDCHARACTER['Backpack']['Gold']= gold 
                newQty = s.SELECTEDCHARACTER.get("Backpack").get(buyItem) + buyQty
                s.SELECTEDCHARACTER["Backpack"][buyItem] = newQty
                print("-----Updated Inventory-----"
                +"\nItem | Qty\n")
                for key, val in s.SELECTEDCHARACTER.get("Backpack").items():
                    print(key, end=" | ")
                    print(val)
                print("\n===========================\n")
            else:
                print("Not enough money")
        buyMore = input("Would you like to continue shopping? [yes] | [no] ")
        if buyMore.lower() == "no":
            break
        else:
            clear()
    clear()

def clear():
    time.sleep(.1)
    i = 0
    while i < 5:
        i = i + 1
        print("-", end=' ', flush=True)
        time.sleep(.05)
        print("+", end=' ', flush=True)
        time.sleep(.05)
    os.system("cls" if os.name == "nt" else "clear")

def end_game():
    print("----------Game Over!----------")
    status()

def main():
    clear()
    the_story()
    title_screen()

    while True:
        character_select()
        play_game()
        end_game()
        break
    #results()

if __name__ == "__main__":
    main()
