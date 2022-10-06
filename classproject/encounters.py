#!/usr/bin/env python3

"""Alta3 Student | Donald Smith
The encounters that make the game... interesting"""

import random
import operator as o
import settings as s
from game import camp, clear, status, shop

def the_wanderer():
    food = s.SELECTEDCHARACTER.get("Backpack").get("Food")
    gold = s.SELECTEDCHARACTER.get("Backpack").get("Gold")
    ailment = s.SELECTEDCHARACTER.get("Health").get("Ailment")
    health = s.SELECTEDCHARACTER.get("Health").get("HitPoints")
    print("You come across another wanderer, he looks hungry!")
    print("You have "+ str(food) + " portions of food.")
    player_choice = input("Do you want to offer him 5 portions of your food? ")
    if player_choice.lower() == "yes":
        food=food-5
        s.SELECTEDCHARACTER['Backpack']['Food']=food
        print("You now have "+ str(food) + " portions of food remaining.")
    elif random.randint(1, 100) >= 90:
        print("The other wanderer lashes out at you and knocks you out!")
        print("You awaken and find that he has taken half your food and half your gold")
        food=food/2
        s.SELECTEDCHARACTER['Backpack']['Food']=food
        gold=gold/2
        s.SELECTEDCHARACTER['Backpack']['Gold']=gold
        print("You now have "+ str(food) + " portions of food remaining, and "+ str(gold) + " gold remaining...")
        print("At least he left you what he did... You carry on.")
        
    elif random.randint(1, 100) >= 80:
        print("The other wanderer lashes out at you and stabs you!")
        print("You run away, but have been injured in the ordeal, you take 5 damage.")
        print("If you don't fix it, your injury will continue to wear you down and reduce your health!")
        health=health-5
        s.SELECTEDCHARACTER['Health']['HitPoints']=health #if you get stabbed and lose all life you should die...
        ailment= ailment+5
        s.SELECTEDCHARACTER['Health']['Ailment']=ailment
        camp_option = input("Would you like to camp_option and have a chance to heal? [Yes]|[No] ")
        if camp_option.lower() == "yes":
            camp()
    input("press enter")
    clear()
    status()

def the_trader():
    print("You see a traveling trader, in the distance...")
    buy = input("Would you like to wave the trader down and make a purchase? [Yes]|[No] ")
    if buy.lower() == "yes":
        print("Supply & Demmand, is my motto... and I don't see anyone else out here")
        economy = random.randint(2,3)
        shop(economy)

def the_cronenberg():
    food = s.SELECTEDCHARACTER.get("Backpack").get("Food")
    med = s.SELECTEDCHARACTER.get("Backpack").get("Medicine")
    print("You see a genetically-mutated Cronenberg creatue!")
    player_choice = input("Would you like to try and communicate with it? [Yes]|[No] ")
    if player_choice.lower() == "yes":
        if random.randint(1, 100) >= 90: 
            print("The Cronenberg growls at you...")
            print("You don't know what to do, you throw some supplies in the general direction as a distraction and quickly walk away")
            if food > 30:
                inventory_change("Food", 1, 30, o.sub)
            if med > 3:
                inventory_change("Food", 1, 3, o.sub)
        if random.randint(1, 100) >= 70: 
            print("The Cronenberg waves you over")
            print('He says "Hello friend, could I bother you for some food?')
            if food > 5:
                player_choice = input("Do you want to offer him 5 portions of your food? ")
                if player_choice.lower() == "yes":
                    food=food-5
                    s.SELECTEDCHARACTER['Backpack']['Food']=food
                    print("You now have "+ str(food) + " portions of food remaining.")
                    if random.randint(1, 100) >= 95:
                        print('He says "Thank you friend, here is a bag of Gold I found')
                        inventory_change("Gold", 100, 500, o.add)
                    elif random.randint(1, 100) >= 90:
                        print('He says "Thank you friend, here is a bag of medicine I found')
                        inventory_change("Medicine", 2, 6, o.add) 
                    elif random.randint(1, 100) >= 85:
                        print('He says "Thank you friend, here is a bag of goodies I found')
                        inventory_change("Medicine", 1, 4, o.add)
                        inventory_change("Gold", 20, 200, o.add)
                    else:
                        print("He eats the food and waves you away")
    input("press enter")

def the_bag():
    ailment = s.SELECTEDCHARACTER.get("Health").get("Ailment")
    health = s.SELECTEDCHARACTER.get("Health").get("HitPoints")
    print("You find something!")
    if random.randint(1, 100) >= 95:
        print('You found a bag of Gold!')
        inventory_change("Gold", 100, 500, o.add)
    elif random.randint(1, 100) >= 90:
        print('You found a bag of medicine!')
        inventory_change("Medicine", 2, 6, o.add)
    elif random.randint(1, 100) >= 85:
        print('You find a bag of goodies!')
        inventory_change("Medicine", 1, 4, o.add)
        inventory_change("Gold", 20, 200, o.add)
    elif random.randint(1, 100) >= 80:
        print('You find a bag of food!')
        inventory_change("Food", 10, 50, o.add)
    elif random.randint(1, 100) >= 75:
        print('You find a bag of goodies!')
        inventory_change("Medicine", 1, 4, o.add)
        inventory_change("Gold", 20, 200, o.add)
        inventory_change("Food", 5, 30, o.add)
    else:
        predators = ["Snakes", "Scorpions", "Murder Hornets", "Spiders"]
        print(f"You find a bag of {random.choice(predators)}")
        damage = random.randint(1, 10)
        print(f"You run away, but have been injured in the ordeal, you take {str(damage)} damage.")
        print("If you don't fix it, your injury will continue to wear you down and reduce your health!")
        health=health-damage
        s.SELECTEDCHARACTER['Health']['HitPoints']=health #if you lose all life you should die...
        ailment= ailment+random.randint(1, 10)
        s.SELECTEDCHARACTER['Health']['Ailment']=ailment
        camp_option = input("Would you like to camp and have a chance to rest and medicate? [Yes]|[No] ")
        if camp_option.lower() == "yes":
            camp()
    input("press enter")
    clear()
    status()

def inventory_change(item, l, u, ops):
    item_mod = s.SELECTEDCHARACTER.get("Backpack").get(item)
    item_gain = random.randint(l, u)
    item_mod = ops(item_mod, item_gain)
    s.SELECTEDCHARACTER['Backpack'][item]= item_mod
    operate = "+"
    if ops ==  "sub":
        operate = "-"
    elif ops == "add":
        operate = "+"
    print(f"{operate} {item_gain} {item}!")