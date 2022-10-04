#!/usr/bin/env python3

"""Escaping the Oregon trail, this is a game based on the famous educational text-based game "The Oregon Trail", created In 1971, by Don Rawitsch.
In ETOT players are set in a post-apocalyptic scenario where they have to escape the west"""

import random
import Settings as g
from EscapingTheOregonTrail import *



def theWanderer():
    food = g.selectedCharacter.get("Backpack").get("Food")
    gold = g.selectedCharacter.get("Backpack").get("Gold")
    ailment = g.selectedCharacter.get("Health").get("Ailment")
    med = g.selectedCharacter.get("Backpack").get("Medicine")
    health = g.selectedCharacter.get("Health").get("HitPoints")
    print(g.selectedCharacter) #delete
    print(f"Days traveled, {g.daysTraveled}!")
    print("You come across another wanderer, he looks hungry!")
    print("You have "+ str(food) + " portions of food.")
    playerChoice = input("Do you want to offer him 5 portions of your food? ")
    if playerChoice.lower() == "yes":
        food=food-5
        g.selectedCharacter['Backpack']['Food']=food
        print("You now have "+ str(food) + " portions of food remaining.")
    elif random.randint(1, 100) >= 90:
        print("The other wanderer lashes out at you and knocks you out!")
        print("You awaken and find that he has taken half your food and half your gold")
        food=food/2
        g.selectedCharacter['Backpack']['Food']=food
        gold=gold/2
        g.selectedCharacter['Backpack']['Gold']=gold
        print("You now have "+ str(food) + " portions of food remaining, and "+ str(gold) + " gold remaining...")
        print("At least he left you what he did... You carry on.")
    elif random.randint(1, 100) >= 80:
        print("The other wanderer lashes out at you and stabs you!")
        print("You run away, but have been injured in the ordeal, you take 5 damage.")
        print("If you don't fix it, your injury will continue to wear you down and reduce your health!")
        health=health-5
        g.selectedCharacter['Health']['HitPoints']=health #if you get stabbed and lose all life you should die...
        ailment= ailment+5
        g.selectedCharacter['Health']['Ailment']=ailment
        if med >= 1:
            rest = input("Would you like to take medicine and rest to reduce your ailment? [Yes]|[No] ")
            if rest.lower() == "yes":
                med=med-1
                g.selectedCharacter['Backpack']['Medicine']=med
                if ailment >= 5:
                    ailment=ailment-5
                    g.selectedCharacter['Health']['Ailment'] = ailment
                else:
                    ailment=0
                    g.selectedCharacter['Health']['Ailment'] = ailment
                    print("You have recovered!")
    input("press enter")

def theTrader():
    print("You see a traveling trader, in the distance...")
    buy = input("Would you like to wave the trader down and make a purchase? [Yes]|[No]")
    if buy.lower() == "yes":
        print("Supply & Demmand, is my motto... and I don't see anyone else out here")
        Economy = random.randint(2,3)
        shop(Economy)

def theCronenberg():
    food = g.selectedCharacter.get("Backpack").get("Food")
    gold = g.selectedCharacter.get("Backpack").get("Gold")
    ailment = g.selectedCharacter.get("Health").get("Ailment")
    med = g.selectedCharacter.get("Backpack").get("Medicine")
    health = g.selectedCharacter.get("Health").get("HitPoints")
    print("You see a genetically-mutated Cronenberg creatue!")
    playerChoice = input("Would you like to try and communicate with it? [Yes]|[No] ")
    if playerChoice.lower() == "yes":
        if random.randint(1, 100) >= 90: 
            print("The Cronenberg growls at you...")
            print("You don't know what to do, you throw some supplies in the general direction as a distraction and quickly walk away")
            if food > 1:
                food=food-1
                g.selectedCharacter['Backpack']['Food']=food
                print("You now have " + str(food) + " food!")
            if med > 1:
                med=med-1
                g.selectedCharacter['Backpack']['Medicine']=med
                print("You now have " + str(med) + " meds!")
        if random.randint(1, 100) >= 70: 
            print("The Cronenberg waves you over")
            print('He says "Hello friend, could I bother you for some food?')
            if food > 5:
                playerChoice = input("Do you want to offer him 5 portions of your food? ")
                if playerChoice.lower() == "yes":
                    food=food-5
                    g.selectedCharacter['Backpack']['Food']=food
                    print("You now have "+ str(food) + " portions of food remaining.")
                    if random.randint(1, 100) >= 95:
                        print('He says "Thank you friend, here is a bag of food I found')
                        gold = gold + random.randint(100, 500)
                        g.selectedCharacter['Backpack']['Gold']=gold
                        print("You now have "+ str(gold) + " gold.") 
                    elif random.randint(1, 100) >= 90:
                        print('He says "Thank you friend, here is a bag of medicine I found')
                        med = med + random.randint(2, 6)
                        g.selectedCharacter['Backpack']['Medicine']=med
                        print("You now have "+ str(med) + " meds.") 
                    elif random.randint(1, 100) >= 85:
                        print('He says "Thank you friend, here is a bag of goodies I found')
                        med = med + random.randint(1, 4)
                        g.selectedCharacter['Backpack']['Medicine']=med
                        print("You now have "+ str(med) + " meds.") 
                        gold = gold + random.randint(20, 200)
                        g.selectedCharacter['Backpack']['Gold']=gold
                        print("You now have "+ str(gold) + " gold.")
                    else:
                        print("He eats the food and waves you away") 

def theBag():
    food = g.selectedCharacter.get("Backpack").get("Food")
    gold = g.selectedCharacter.get("Backpack").get("Gold")
    ailment = g.selectedCharacter.get("Health").get("Ailment")
    med = g.selectedCharacter.get("Backpack").get("Medicine")
    health = g.selectedCharacter.get("Health").get("HitPoints")
    print("You find something!")
    if random.randint(1, 100) >= 95:
        print('You found a bag of Gold!')
        gold = gold + random.randint(100, 500)
        g.selectedCharacter['Backpack']['Gold']=gold
        print("You now have "+ str(gold) + " gold.")
    elif random.randint(1, 100) >= 90:
        print('You found a bag of medicine!')
        med = med + random.randint(2, 6)
        g.selectedCharacter['Backpack']['Medicine']=med
        print("You now have "+ str(med) + " meds.") 
    elif random.randint(1, 100) >= 85:
        print('You find a bag of goodies!')
        med = med + random.randint(1, 4)
        g.selectedCharacter['Backpack']['Medicine']=med
        print("You now have "+ str(med) + " meds.") 
        gold = gold + random.randint(20, 200)
        g.selectedCharacter['Backpack']['Gold']=gold
        print("You now have "+ str(gold) + " gold.")
    elif random.randint(1, 100) >= 80:
        print('You find a bag of food!')
        food = food + random.randint(10, 50)
        g.selectedCharacter['Backpack']['Food']=food
        print("You now have "+ str(food) + " rations of food.")
    elif random.randint(1, 100) >= 75:
        print('You find a bag of goodies!')
        med = med + random.randint(1, 4)
        g.selectedCharacter['Backpack']['Medicine']=med
        print("You now have "+ str(med) + " meds.") 
        gold = gold + random.randint(20, 200)
        g.selectedCharacter['Backpack']['Gold']=gold
        print("You now have "+ str(gold) + " gold.")
        food = food + random.randint(5, 30)
        g.selectedCharacter['Backpack']['Food']=food
        print("You now have "+ str(food) + " rations of food.")  
    else:
        predators = ["Snakes", "Scorpions", "Murder Hornets", "Spiders"]
        print(f"You find a bag of {random.choice(predators)}")
        damage = random.randint(1, 10)
        print(f"You run away, but have been injured in the ordeal, you take {str(damage)} damage.")
        print("If you don't fix it, your injury will continue to wear you down and reduce your health!")
        health=health-damage
        g.selectedCharacter['Health']['HitPoints']=health #if you lose all life you should die...
        ailment= ailment+random.randint(1, 10)
        g.selectedCharacter['Health']['Ailment']=ailment
        if med >= 1:
            rest = input("Would you like to take medicine and rest to reduce your ailment? [Yes]|[No] ")
            if rest.lower() == "yes":
                med=med-1
                g.selectedCharacter['Backpack']['Medicine']=med
                if ailment >= 5:
                    ailment=ailment-5
                    g.selectedCharacter['Health']['Ailment'] = ailment
                else:
                    ailment=0
                    g.selectedCharacter['Health']['Ailment'] = ailment
                    print("You have recovered!")  
    input("press enter")

