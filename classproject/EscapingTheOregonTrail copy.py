#!/usr/bin/env python3

"""Escaping the Oregon trail, this is a game based on the famous educational text-based game "The Oregon Trail", created In 1971, by Don Rawitsch.
In ETOT players are set in a post-apocalyptic scenario where they have to escape the west"""

# MVP Features:
# Begin game screen - Press Start
# Pick Character Profession - like OT, start out with more or less money makes things easier or harder
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
# Achievements

import getpass
import os
import time
import random
from tkinter.messagebox import YES
from unittest import case
import Settings as g
from Encounters import *

def titleScreen():
    print("Welcome to ETOT")
    startGame = getpass.getpass("Hit Enter", stream=None)

    if startGame == "uuddlrlrba":
        print("Special Code Entered")
    else:
        g.characters.pop("KC")

    clear()

def characterSelect():
    while True:
        print("What is your profession?")
        for key, value in g.characters.items():
            print(key)

        g.character = (input("Type a profession to see character info and confirm your choice: ")).upper()
        
        # if character is valid load bio
        if g.character in g.characters:
            g.selectedCharacter=g.characters[g.character]
            print("You were a " + str(g.selectedCharacter.get("Profession")) + ", " + str(g.selectedCharacter.get("Bio")+ "."))
            confirmCharacter = input("Would you like this character? [yes] | [no] ")
            if confirmCharacter.lower() == "yes":
                break
            else:
                clear()
    clear()

def playGame():
    while True:
        town()
        move()
        if g.playerStatus == "Alive":
            settle()
        else:
            break

def town():
    g.pointOfOrigin = g.landmarks[g.currentLocation]
    
    while True:
        print(f"You are in {g.currentLocation}, " + g.pointOfOrigin.get("State")+ "!")
        status()
        townAction = input("Would you like to [Shop], [Camp], [Gamble], [Status] or [Leave]? ")
        if townAction.lower() == "shop":
            shop(1)
        if townAction.lower() == "camp":
            camp()
        if townAction.lower() == "gamble":
            gamble()
        if townAction.lower() == "status":
            status()
        if townAction.lower() == "leave":
            print(f"the journey ahead is " + str(g.landmarks[g.currentLocation].get("Distance")) + 
            " miles, you should get there in " + str(g.landmarks[g.currentLocation].get("Distance")/12) + " days!")
            print("You have " + str(g.characters[g.character].get("Backpack").get("Food")) + " portions of food!")
            moveOn = input("Would you like to move out? [Yes]|[No] ")
            if moveOn.lower() == "yes":
                clear()
                break
            else:
                clear()

def move():
    i = 0
    g.pointOfOrigin = g.landmarks[g.currentLocation]
    g.destinationLocation = str(g.pointOfOrigin.get("NextStop"))
    print("Going to - "+ g.destinationLocation + " this will be a " + str(g.pointOfOrigin.get("Distance")) + " mile journey!")
    input("Hit Enter")
    
    while i < g.pointOfOrigin.get("Distance"):
        clear()
        status()
        print("Going to - "+ g.destinationLocation + f" | {i} miles of a " + str(g.pointOfOrigin.get("Distance")) + " mile journey!")
        survivalCheck()
        if g.playerStatus == "Alive":
            i = i + g.pace
            g.milesTraveled = g.milesTraveled + g.pace
            print("-", end=' ', flush=True)
            time.sleep(.1)
            print("+", end=' ', flush=True)
            time.sleep(.1)
            print("WANDERING", end=' ', flush=True)
            if random.randint(1, 100) >= 90:
                randomEncounter()  
            if i > g.pointOfOrigin.get("Distance"):
                extraMiles = i - g.pointOfOrigin.get("Distance")
                i = g.pointOfOrigin.get("Distance")
                g.milesTraveled = g.milesTraveled - extraMiles
                print("Arrived!")
                time.sleep(.3)
        else:
            break

def survivalCheck():
    food = g.selectedCharacter.get("Backpack").get("Food")
    ailment = g.selectedCharacter.get("Health").get("Ailment")
    med = g.selectedCharacter.get("Backpack").get("Medicine")
    health = g.selectedCharacter.get("Health").get("HitPoints")
    maxHealth = g.selectedCharacter.get("Health").get("MaxHealth")
    g.daysTraveled = g.daysTraveled + 1
    if health > 0:
        if food >= 1:
            food = food-1
            g.selectedCharacter['Backpack']['Food']=food
        else:
            health = health-2
            g.selectedCharacter['Health']['HitPoints']=health
            print(f"STARVING, -2 HP ", end=' ', flush=True)
            print(f"{health} / {maxHealth} HP ", end=' ', flush=True)
        if ailment > 0:
            while True:
                if med >= 1:
                    takeMeds = input(f"You have {ailment} days before you will recover your ailment, "
                    + "Would you like to take medicine to try and reduce or heal your ailment? [Yes]|[No]")
                    if takeMeds.lower() == "yes":
                        medicate()
                        ailment = g.selectedCharacter.get("Health").get("Ailment")
                if ailment > 0:
                    ailment = ailment-1
                    g.selectedCharacter['Health']['Ailment'] = ailment
                    health = health-2
                    g.selectedCharacter['Health']['HitPoints']=health
                    print("ailment, -2 HP", flush=True)
                    print(f"{health} / {maxHealth} HP ", end=' ', flush=True)
                    break
                else:
                    print("You have recovered from your ailment", flush=True)
                    break  
        
    else:
        print("\nYou have died!")
        g.playerStatus = "Dead"
        input("Hit Enter")
        clear()

def randomEncounter():
    Encounters = [theBag, theWanderer, theTrader, theCronenberg, theBag]
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
    randomE = random.choice(Encounters)
    randomE()


def settle():
    g.currentLocation = g.destinationLocation
    print(f"Welcome to - {g.currentLocation}!")
    input("Hit Enter")
    clear()

def gamble():
    while True:
        print("You have: "+str(g.selectedCharacter.get("Backpack").get("Gold"))+" Gold!")
        playerbet = int(input("How much would you like to bet? "))
        if g.selectedCharacter.get("Backpack").get("Gold")>=playerbet:
            playerNumber = int(input("Pick a number between 1-6: "))
            numberToMatch = random.randint(1, 6)
            print(f"The number to match was {numberToMatch}!")
            playersGold = g.selectedCharacter.get("Backpack").get("Gold")
            if playerNumber == numberToMatch:
                print("You win!") 
                playersGold = playersGold+playerbet*2 
            else:
                print("You lose!")
                playersGold = playersGold-playerbet 
            g.selectedCharacter['Backpack']['Gold']=playersGold
            print("Your Gold balance: "+str(g.selectedCharacter.get("Backpack").get("Gold")))        
        else:
            print("not enough money")
        playAgain = input("Play again? [yes] | [no] ")
        if playAgain.lower() == "no":
            break
        else:
            clear()

def status():
    food = g.selectedCharacter.get("Backpack").get("Food")
    gold = g.selectedCharacter.get("Backpack").get("Gold")
    ailment = g.selectedCharacter.get("Health").get("Ailment")
    med = g.selectedCharacter.get("Backpack").get("Medicine")
    health = g.selectedCharacter.get("Health").get("HitPoints")
    maxHealth = g.selectedCharacter.get("Health").get("MaxHealth")
    print("--------STATUS--------")
    print(g.character)
    print(f"{health} / {maxHealth} HP ")
    if ailment != 0:
        print(f"You have {ailment} days before you will recover your ailment"
        +"\nYou should try to medicate...")
    if health < maxHealth:
        print("Your health is low, you should try to rest")
    print(f"{gold} Gold | {med} Meds | {food} Portions of Food ")
    print(f"{g.daysTraveled} days traveled, and {g.milesTraveled} miles traveled!")
    print(f"Last location: {g.currentLocation}, "+(g.landmarks.get(g.currentLocation).get("State"))+f" | Player's status: {g.playerStatus}")
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
    
        #     " miles, you should get there in " + str(g.landmarks[g.currentLocation].get("Distance")/12) + " days!")
        #     print("You have " + str(g.characters[g.character].get("Backpack").get("Food")) + " portions of food!")
        #     moveOn = input("Would you like to move out? [Yes]|[No] ")
        #     if moveOn.lower() == "yes":
        #         clear()
        #         break
        #     else:
        #         clear() 
    
def rest():
    health = g.selectedCharacter.get("Health").get("HitPoints")
    maxHealth = g.selectedCharacter.get("Health").get("MaxHealth")
    days = input("How many days would you like to rest... ")
    restDay = 0
    while restDay < int(days):
        time.sleep(.2)
        restDay = restDay + 1
        print(f"Resting {str(restDay)} out of {days} days!", flush=True)
        if maxHealth > health:
            health = health + 1
            g.selectedCharacter['Health']['HitPoints']=health
            print(f"{health} / {maxHealth} HP", flush=True)
        survivalCheck()

def medicate():
    ailment = g.selectedCharacter.get("Health").get("Ailment")
    med = g.selectedCharacter.get("Backpack").get("Medicine")
    if med >= 1:
        med = med-1
        g.selectedCharacter['Backpack']['Medicine']=med    
        medEffects = random.randint(3, 9)
        if ailment >= medEffects:
            ailment = ailment-medEffects
            g.selectedCharacter['Health']['Ailment'] = ailment
            print(f"Medicine reduced ailment by {medEffects} days")
        else:
            g.selectedCharacter['Health']['Ailment'] = 0
            print("You have recovered!")
    else:
        print("You have no medicine!")        

        # while True:
        # print(f"You are in {g.currentLocation}, " + g.pointOfOrigin.get("State")+ "!")
        # townAction = input("Would you like to [Shop], [Camp], [Gamble], [Status] or [Leave]? ")
        # if townAction.lower() == "shop":
        #     shop(1)
        # if townAction.lower() == "camp":
        #     camp()
        # if townAction.lower() == "gamble":
        #     gamble()
        # if townAction.lower() == "status":
        #     status()
        # if townAction.lower() == "leave":
        #     print(f"the journey ahead is " + str(g.landmarks[g.currentLocation].get("Distance")) + 
        #     " miles, you should get there in " + str(g.landmarks[g.currentLocation].get("Distance")/12) + " days!")
        #     print("You have " + str(g.characters[g.character].get("Backpack").get("Food")) + " portions of food!")
        #     moveOn = input("Would you like to move out? [Yes]|[No] ")
        #     if moveOn.lower() == "yes":
        #         clear()
        #         break
        #     else:
        #         clear()



def shop(Economy):
    food = g.selectedCharacter.get("Backpack").get("Food")
    gold = g.selectedCharacter.get("Backpack").get("Gold")
    med = g.selectedCharacter.get("Backpack").get("Medicine")
    health = g.selectedCharacter.get("Health").get("HitPoints")
    print("What would you like to buy? ")
    while True:
        print("---------For  Sale---------")
        for key, val in g.shop.items():
            print(key, end="--- $$$ COST $$$ ---> ")
            print(val*Economy)
        print("-----Current Inventory-----")
        for key, val in g.selectedCharacter.get("Backpack").items():
            print(key, end="--- qty ---> ")
            print(val)
        print("---------------------------")
        buyItem = input("What would you like to buy? ")
        buyQty = int(input("How many do you want? "))
        if buyItem in g.shop:
            cost = g.shop.get(buyItem) * buyQty * Economy
            if gold >= cost:
                print("Total cost: "+str(cost))
                gold = gold - cost
                g.selectedCharacter['Backpack']['Gold']= gold 
                newQty = g.selectedCharacter.get("Backpack").get(buyItem) + buyQty
                g.selectedCharacter["Backpack"][buyItem] = newQty
                print("-----Updated Inventory-----")
                for key, val in g.selectedCharacter.get("Backpack").items():
                    print(key, end="--- new qty ---> ")
                    print(val)
                print("---------------------------")
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

def endGame():
    print("----------Game Over!----------")
    status()


def main():
    clear()
    titleScreen()

    while True:
        characterSelect()
        playGame()
        endGame()
        break
    # 
    # results()
        

if __name__ == "__main__":
    main()
