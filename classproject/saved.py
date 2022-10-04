def theWanderer():
    print("You come across another wanderer, he looks hungry!")
    print("You have "+ str(g.food) + " portions of food.")
    playerChoice = input("Do you want to offer him 5 portions of your food? ")
    if playerChoice.lower() == "yes":
        g.food = g.food-5
        g.selectedCharacter['Backpack']['Food']=g.food
        print("You now have "+ str(g.food) + " portions of food remaining.")
    elif random.randint(1, 100) >= 90:
        print("The other wanderer lashes out at you and knocks you out!")
        print("You awaken and find that he has taken half your food and half your gold")
        g.food = g.food/2
        g.selectedCharacter['Backpack']['Food']=g.food
        g.gold = g.gold/2
        g.selectedCharacter['Backpack']['Gold']=g.food
        print("You now have "+ str(g.food) + " portions of food remaining, and "+ str(g.gold) + " gold remaining...")
        print("At least he left you what he did... You carry on.")
    elif random.randint(1, 100) >= 80:
        print("The other wanderer lashes out at you and stabs you!")
        print("You run away, but have been injured in the ordeal, you take 5 damage.")
        print("If you don't fix it, your injury will continue to wear you down and reduce your health!")
        if g.med >= 1:
                rest = input("Would you like to take medicine and rest to reduce your ailment? [Yes]|[No] ")
                if rest.lower() == "yes":
                    g.med = g.med-1
                    g.selectedCharacter['Backpack']['Medicine']=g.med
                    if g.ailment >= 5:
                        g.ailment = g.ailment-5
                        g.selectedCharacter['Health']['Ailment'] = g.ailment
                    else:
                        g.selectedCharacter['Health']['Ailment'] = 0
                        print("You have recovered!")

                            # def shop(Economy):
    # while True:
    #     print("---------For  Sale---------")
    #     for key, val in g.shop.items():
    #         print(key, end="--- $$$ COST $$$ ---> ")
    #         print(val)
    #     print("-----Current Inventory-----")
    #     for key, val in g.selectedCharacter.get("Backpack").items():
    #         print(key, end="--- qty ---> ")
    #         print(val)
    #     print("---------------------------")
    #     buyItem = input("What would you like to buy? ")
    #     buyQty = int(input("How many do you want? "))
    #     if buyItem in g.shop:
    #         cost = g.shop.get(buyItem) * buyQty * Economy
            
    #         if g.gold >= cost:
    #             print("Total cost: "+str(cost))
    #             g.gold = g.gold - cost
    #             g.playerGold = g.gold 
    #             g.selectedCharacter["Backpack"][buyItem] = g.selectedCharacter.get("Backpack").get(buyItem, 0) + buyQty
    #             print("-----Updated Inventory-----")
    #             for key, val in g.selectedCharacter.get("Backpack").items():
    #                 print(key, end="--- new qty ---> ")
    #                 print(val)
    #             print("---------------------------")
    #         buyMore = input("Would you like to continue shopping? [yes] | [no] ")
    #         if buyMore.lower() == "no":
    #             break
    #         else:
    #             clear()
    # clear()
