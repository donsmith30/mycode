#!/usr/bin/env python3

"""Alta3 Student | Donald Smith
The encounters that make the game... interesting"""

import random
import operator as o
import settings as s
from game import camp, clear, status, shop

def the_wanderer():
    """Another agressive wanderer"""
    print("You come across another wanderer, he looks hungry!")
    player_choice = input("Do you want to offer him some of your food? ")
    if player_choice.lower() == "yes":
        # give the wanderer a random ammount of your food, risking 10%
        negative_inventory_change("Food", .10)
    elif random.randint(1, 100) >= 80:
        # if you don't 20% chance you will risk 50% of your supplies
        print("The other wanderer lashes out at you and knocks you out!")
        print("You awaken and find that he may have taken some of your inventory")
        negative_inventory_change("Food", .5)
        negative_inventory_change("Gold", .5)
        negative_inventory_change("Medicine", .5)
        print("At least he left you what he did... You carry on.")
    elif random.randint(1, 100) >= 60:
        # or... 20% chance you end up getting stabbed
        # health risk is 25%
        # ailment from stab will last up to 10 days
        # give option to camp/rest/medicate if hurt
        print("The other wanderer lashes out at you and stabs you!")
        print("You run away, but have been injured in the ordeal!")
        health_change(.25)
        ailment_change(1, 10)
        print("If you don't fix it, your injury will continue"
        +" to wear you down and reduce your health!")
        camp_option = input("Would you like to camp and have a"
        +" chance to rest and medicate? [Yes]|[No] ")
        if camp_option.lower() == "yes":
            camp()
    else:
        print("He sits down, does nothing and you go on your way...")
    input("press enter")
    clear()
    status()

def the_trader():
    """traveling shop | links to shop with economy adjusted"""
    print("You see a traveling trader, in the distance...")
    buy = input("Would you like to wave the trader down and make a purchase? [Yes]|[No] ")
    if buy.lower() == "yes":
        print("Supply & demand, is my motto... and I don't see anyone else out here")
        input("press enter")
        # as she said supply * demand is a thing, economy will be 2-3 times higher than town
        economy = random.randint(2,3)
        shop(economy)

def the_cronenberg():
    """fairly nice most the time | use adjusting functions"""
    print("You see a genetically-mutated Cronenberg creature!")
    player_choice = input("Would you like to try and communicate with it? [Yes]|[No] ")
    if player_choice.lower() == "yes":
        if random.randint(1, 100) >= 90:
            # 10% chance this doesn't go well
            print("The Cronenberg growls at you...")
            print("You don't know what to do, you throw some supplies in the"
            +"\ngeneral direction as a distraction and jump back!")
            negative_inventory_change("Food", .1)
            negative_inventory_change("Medicine", .1)
        if random.randint(1, 100) >= 70:
            # 20% chance he bums food, but he will reward you with other items
            print("The Cronenberg waves you over")
            print('He says "Hello friend, could I bother you for some food?')
            player_choice = input("Do you want to offer him some of your food? ")
            if player_choice.lower() == "yes":
                negative_inventory_change("Food", .1)
                if random.randint(1, 100) >= 80:
                    print('He says "Thank you friend, here is a bag of Gold I found')
                    positive_inventory_change("Gold", 100, 500)
                elif random.randint(1, 100) >= 60:
                    print('He says "Thank you friend, here is a bag of medicine I found')
                    positive_inventory_change("Medicine", 2, 6) 
                elif random.randint(1, 100) >= 40:
                    print('He says "Thank you friend, here is a bag of goodies I found')
                    positive_inventory_change("Medicine", 1, 4)
                    positive_inventory_change("Gold", 20, 200)
                else:
                    print("He eats the food and waves you away")
    print("You both look at each other awkwardly and go your separate ways")
    input("press enter")

def the_bag():
    """random bag of things | use adjusting functions"""
    print("You find something!")
    if random.randint(1, 100) >= 90:
        print('You found a bag of Gold!')
        positive_inventory_change("Gold", 100, 500)
    elif random.randint(1, 100) >= 80:
        print('You found a bag of medicine!')
        positive_inventory_change("Medicine", 2, 6)
    elif random.randint(1, 100) >= 70:
        print('You find a bag of goodies!')
        positive_inventory_change("Medicine", 1, 4)
        positive_inventory_change("Gold", 20, 200)
    elif random.randint(1, 100) >= 60:
        print('You find a bag of food!')
        positive_inventory_change("Food", 10, 50)
    elif random.randint(1, 100) >= 50:
        print('You find a bag of goodies!')
        positive_inventory_change("Medicine", 1, 4)
        positive_inventory_change("Gold", 20, 200)
        positive_inventory_change("Food", 5, 30)
    else:
        # 50% chance you see this, using a list to add some more variety into the function
        predators = ["Snakes", "Scorpions", "Murder Hornets", "Spiders"]
        print(f"You find a bag of {random.choice(predators)}")
        print("You run away, but have been injured in the ordeal!")
        health_change(.25)
        ailment_change(1, 10)
        print("If you don't fix it, your injury will continue"
        +" to wear you down and reduce your health!")
        # camp option again due to injury
        camp_option = input("Would you like to camp and have a"
        +" chance to rest and medicate? [Yes]|[No] ")
        if camp_option.lower() == "yes":
            camp()
    input("press enter")
    clear()
    status()

def the_trickster():
    """sometimes sweet, sometimes mean | use adjusting functions"""
    food = s.SELECTEDCHARACTER.get("Backpack").get("Food")
    print("You see a monster nearly 13 feet and seems to be"
    +" made of loser candy found throughout the wastelands")
    player_choice = input("Do you want to approach him? [Yes] | [No] ")
    if player_choice.lower() == "yes":
        print("I am the Summerween Trickster!")
        if random.randint(1, 100) >= 90:
            # 10% chance he reacts bad
            print('Gimmie food or I will kill you!')
            if food == 0:
                health_change(.5)
                print("He slaps you with his payday punch!"
                +"\nYou are still alive but injured!")
                camp_option = input("Would you like to camp and have a"
                +" chance to rest and medicate? [Yes]|[No] ")
                if camp_option.lower() == "yes":
                    camp()
            negative_inventory_change("Food", .25)
            print("You give him food and run away!")
        elif random.randint(1, 100) >= 80:
            print('Please take some of my candy!')
            positive_inventory_change("Food", 5, 50)
        elif random.randint(1, 100) >= 70:
            print('please take this bag of goodies!')
            positive_inventory_change("Medicine", 1, 4)
            positive_inventory_change("Gold", 20, 200)
        else:
            print('The monster growls and you run away')
    else:
        print("You run away")
    input("press enter")
    clear()
    status()



def the_gnomes():
    """awful beings | use adjusting functions"""
    print("You see a gaggle of gnomes, 10 to 18 inches tall each")
    input("press enter")
    print('We want food!, they say'
    +'\nThey chase after you and try to steal your food')
    input("press enter")
    if random.randint(1, 100) >= 80:
        print('They manage to overwhelm you and steal some of your food!')
        negative_inventory_change("Food", .40)
    elif random.randint(1, 100) >= 60:
        print('They manage to overwhelm you and steal some of your food & meds!')
        negative_inventory_change("Medicine", .2)
        negative_inventory_change("Food", .2)
    else:
        # 60% chance you get away
        print('You run away before they get anything!')
    input("press enter")
    clear()
    status()

def positive_inventory_change(item, l, u):
    """adjust to give good things"""
    item_mod = s.SELECTEDCHARACTER.get("Backpack").get(item)
    item_gain = random.randint(l, u)
    # biggest thing on this function is we floordiv by 1
    # this is to make the number whole
    item_mod = o.floordiv(o.add(item_mod, item_gain),1)
    s.SELECTEDCHARACTER['Backpack'][item]= item_mod
    print(f"+ {item_gain} {item}!")

def negative_inventory_change(item, percent):
    """Negative based on your % in .int format"""
    item_mod = s.SELECTEDCHARACTER.get("Backpack").get(item)
    # noticed a couple things here 1st dont want to throw error for a zero
    # next if the risk was under 1 we had more issues... that is how I 
    # was lead to max()
    if item_mod >= 1:
        risk = o.mul(percent, item_mod)
        risk = max(risk, 1)
        item_loss = random.randint(1, int(risk))
        item_mod = o.floordiv(o.sub(item_mod, item_loss),1)
        s.SELECTEDCHARACTER['Backpack'][item]= item_mod
        print(f"- {item_loss} {item}!")
    else:
        print(f"No {item} to lose!")

def health_change(percent):
    """Negative based on your % in .int format"""
    # pretty much the same as the above function
    health_mod = s.SELECTEDCHARACTER.get("Health").get("HitPoints")
    if health_mod >= 1:
        risk = o.mul(percent, health_mod)
        risk = max(risk, 1)
        health_loss = random.randint(1, int(risk))
        health_mod = o.floordiv(o.sub(health_mod, health_loss),1)
        s.SELECTEDCHARACTER["Health"]["HitPoints"]= health_mod
        print(f"- {health_loss} HP!")
    else:
        print("No health to lose! You will die")

def ailment_change(l, u):
    """adjust to give player ailments"""
    # same idea as positive inventory
    ailment_mod = s.SELECTEDCHARACTER.get("Health").get("Ailment")
    ailment_gain = random.randint(l, u)
    ailment_mod = o.floordiv(o.add(ailment_mod, ailment_gain),1)
    s.SELECTEDCHARACTER['Health']["Ailment"]= ailment_mod
    print(f"+ {ailment_gain} days to recover ailment!")

def main():
    """Main does nothing really"""
    print()

if __name__ == "__main__":
    main()
