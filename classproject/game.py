#!/usr/bin/env python3

"""Alta3 Student | Donald Smith
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
# Team - NOPE
# random encounters
#
# Bonus items:
# Sign in
# Top Scores
# Achievements

import getpass
import operator as o
import os
import time
import random
import settings as s
import encounters as e

def title_screen():
    """A quick title screen | with cheat codes"""
    print("Welcome to Escaping the Oregon Trail")
    #Secret code accepted as pass, if not given just pops off the extra character
    start_game = getpass.getpass("Hit Enter")
    if start_game == "uuddlrlrba":
        print("Special Code Entered")
    else:
        s.CHARACTERS.pop("Kona")
    clear()

def the_story():
    """The story so far..."""
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
    """Character select | pulls from settings yaml load"""
    while True:
        print("What is your profession?")
        for key, value in s.CHARACTERS.items():
            print(key)
        s.CHARACTER = (input("Type a profession to see character"
        +" info and confirm your choice: ")).title()
        # title case for character to make sure no errors
        if s.CHARACTER in s.CHARACTERS: 
            s.SELECTEDCHARACTER=s.CHARACTERS[s.CHARACTER]
            print("You were a " + str(s.SELECTEDCHARACTER.get("Profession")) 
            + ", " + str(s.SELECTEDCHARACTER.get("Bio")+ "."))
            status()
            # small story and status prints so player can decide their character
            confirm_character = input("Would you like this character? [yes] | [no] ")
            if confirm_character.lower() == "yes":
                break
            clear()
    clear()

def clear():
    """Clear | reused frequently"""
    # using time sleep for animation and OS commands to clear screen
    time.sleep(.1)
    i = 0
    while i < 5:
        i = i + 1
        print("-", end=' ', flush=True)
        time.sleep(.05)
        print("+", end=' ', flush=True)
        time.sleep(.05)
    os.system("cls" if os.name == "nt" else "clear")

def play_game():
    """The brain of the game"""
    while True:
        town()
        move()
        # if you are dead or at final location, should stop game
        if s.CURRENTLOCATION == "Independence":
            print("---------Winner! You made it to Independence!---------")
            break
        if s.PLAYERSTATUS == "Alive":
            settle()
        else:
            break

def town():
    """Things you can do around town"""
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
            # using floordiv in my farewell msg so we don't get weird remainders
            print("the journey ahead is " + str(s.LANDMARKS[s.CURRENTLOCATION].get("Distance")) +
            " miles, you should get there in " 
            + str(o.floordiv(s.LANDMARKS[s.CURRENTLOCATION].get("Distance"),12)) + " days!")
            print("You have " + str(s.CHARACTERS[s.CHARACTER].get("Backpack").get("Food"))
            + " portions of food!")
            move_on = input("Would you like to move out? [Yes]|[No] ")
            if move_on.lower() == "yes":
                clear()
                break
            clear()

def move():
    """Moving from town to town..."""
    i = 0
    s.POINTOFORIGIN = s.LANDMARKS[s.CURRENTLOCATION]
    s.DESTINATIONLOCATION = str(s.POINTOFORIGIN.get("NextStop"))
    print("Going to - "+ s.DESTINATIONLOCATION + " this will be a "
    + str(s.POINTOFORIGIN.get("Distance")) + " mile journey!")
    input("Hit Enter")
    # setting a giant loop that handles wandering the wasteland
    while i < s.POINTOFORIGIN.get("Distance"):
        clear()
        status()
        print("Going to - "+ s.DESTINATIONLOCATION + f" | {i} miles of a "
        + str(s.POINTOFORIGIN.get("Distance")) + " mile journey!")
        survival_check()
        if s.PLAYERSTATUS == "Alive":
            print("-", end=' ', flush=True)
            time.sleep(.1)
            print("+", end=' ', flush=True)
            time.sleep(.1)
            print("WANDERING", end=' ', flush=True)
            if random.randint(1, 100) >= 80:
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

def survival_check():
    """The daily status, are you alive?"""
    food = s.SELECTEDCHARACTER.get("Backpack").get("Food")
    ailment = s.SELECTEDCHARACTER.get("Health").get("Ailment")
    med = s.SELECTEDCHARACTER.get("Backpack").get("Medicine")
    health = s.SELECTEDCHARACTER.get("Health").get("HitPoints")
    max_health = s.SELECTEDCHARACTER.get("Health").get("MaxHealth")
    s.DAYSTRAVELED = s.DAYSTRAVELED + 1
    # if you have food, eat food... or you are starving and eventually die
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
            # if you have an ailment you have a chance to fix, or it will continue to hurt you
            while True:
                if med >= 1:
                    take_meds = input(f"You have {ailment} days"
                    +" before you will recover your ailment,"
                    +" would you like to take medicine to try and"
                    +" reduce or heal your ailment? [Yes]|[No] ")
                    if take_meds.lower() == "yes":
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
                print("You have recovered from your ailment", flush=True)
                break
    else:
        print("\nYou have died!")
        s.PLAYERSTATUS = "Dead"
        input("Hit Enter")
        clear()

def random_encounters():
    """The fun things that happen on trail | links move to encounters.py"""
    encounters = [e.the_bag, e.the_wanderer, e.the_trader,
    e.the_cronenberg, e.the_bag, e.the_trickster, e.the_gnomes]
    # a fun thing using a list to hold all the random events
    # then selecting one random function and calling it at end
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
    """After move, you need to settle"""
    s.CURRENTLOCATION = s.DESTINATIONLOCATION
    print(f"Welcome to - {s.CURRENTLOCATION}!")
    input("Hit Enter")
    clear()

def gamble():
    """The gambling mini game | used in town"""
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
    """Your status bar | used almost everywhere"""
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
    if s.DAYSTRAVELED > 0:
        print(f"{s.DAYSTRAVELED} days traveled, and {s.MILESTRAVELED} miles traveled!")
        print(f"Last location: {s.CURRENTLOCATION}, "
        +(s.LANDMARKS.get(s.CURRENTLOCATION).get("State"))
        +f" | Player's status: {s.PLAYERSTATUS}")
    print("======================")

def camp():
    """Camp Out | links to rest and medicate"""
    clear()
    print("Setting up camp..."
    + "\nEvery day of rest you will consume food, but heal damage delt by the journey!"
    + "\nUntreated ailments will still hurt you over time") 
    while True:
        status()
        camp_action = input("Would you like to [Medicate], [Rest] or [Leave]? ")
        if camp_action.lower() == "medicate":
            medicate()
            input("Hit Enter")
            clear()
        elif camp_action.lower() == "rest":
            rest()
            input("Hit Enter")
            clear()
        elif camp_action.lower() == "leave":
            print("You break down camp, and continue on your journey")
            break

def rest():
    """resting days to recover HP | runs a daily survival check"""
    health = s.SELECTEDCHARACTER.get("Health").get("HitPoints")
    max_health = s.SELECTEDCHARACTER.get("Health").get("MaxHealth")
    while True:
        try:
            days = int(input("How many days would you like to rest... "))
        except ValueError:
            print("Not a number!, use a number or 0 to cancel")
        else:
            break
    rest_day = 0
    while rest_day < days:
        time.sleep(.2)
        rest_day = rest_day + 1
        print(f"Resting {str(rest_day)} out of {days} days!", flush=True)
        if max_health > health:
            health = health + 1
            s.SELECTEDCHARACTER['Health']['HitPoints']=health
            print(f"{health} / {max_health} HP", flush=True)
        survival_check()

def medicate():
    """medication can reduce ailments"""
    ailment = s.SELECTEDCHARACTER.get("Health").get("Ailment")
    med = s.SELECTEDCHARACTER.get("Backpack").get("Medicine")
    if med >= 1:
        med = med-1
        s.SELECTEDCHARACTER['Backpack']['Medicine']=med
        med_effects = random.randint(3, 9)
        if ailment >= med_effects:
            ailment = ailment-med_effects
            s.SELECTEDCHARACTER['Health']['Ailment'] = ailment
            print(f"Medicine reduced ailment by {med_effects} days")
        else:
            s.SELECTEDCHARACTER['Health']['Ailment'] = 0
            print("You have recovered!")
    else:
        print("You have no medicine!")

def shop(economy):
    """shoppin features | adjust to economy like traveling trader"""
    clear()
    gold = s.SELECTEDCHARACTER.get("Backpack").get("Gold")
    print("What would you like to buy? ")
    while True:
        print("\n---------For  Sale---------")
        print("Item | Cost\n")
        for key, val in s.SHOP.items():
            print(key, end=" | ")
            print(val*economy)
        print("\n-----Current Inventory-----"
        +"\nItem | Qty\n")
        for key, val in s.SELECTEDCHARACTER.get("Backpack").items():
            print(key, end=" | ")
            print(val)
        print("\n===========================\n")
        while True:
            try:
                buy_item = (input("What would you like to buy? ")).title()
                assert buy_item in s.SHOP
            except AssertionError:
                print("Thats not a thing")
            else:
                break
        while True:
            try:
                buy_qty = int(input("How many do you want? "))
                cost = s.SHOP.get(buy_item) * buy_qty * economy
                assert gold >= cost
            except ValueError:
                print("Not a number!, use a number or 0 to cancel")
            except AssertionError:
                print("You can't afford that!")
            else:
                break
        if buy_item in s.SHOP:
            cost = s.SHOP.get(buy_item) * buy_qty * economy
            print("Total cost: "+str(cost))
            gold = gold - cost
            s.SELECTEDCHARACTER['Backpack']['Gold']= gold
            new_qty = s.SELECTEDCHARACTER.get("Backpack").get(buy_item) + buy_qty
            s.SELECTEDCHARACTER["Backpack"][buy_item] = new_qty
            clear()
            print("-----Updated Inventory-----"
            +"\nItem | Qty\n")
            for key, val in s.SELECTEDCHARACTER.get("Backpack").items():
                print(key, end=" | ")
                print(val)
            print("\n===========================\n")
            buy_more = input("Would you like to continue shopping? [yes] | [no] ")
            if buy_more.lower() == "no":
                break
            clear()
    clear()


def end_game():
    """Game over and see final status"""
    print("----------Game Over!----------")
    status()

def main():
    """The main brain that runs everything"""
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
