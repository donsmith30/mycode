#!/usr/bin/env python3

"""RZFeeser | Alta3 Research
   learning about for logic"""

# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]

def main():

    # create a list of strings
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
    # create a second list of strings
    approved_vendors = ["cisco", "juniper", "big_ip"]
    # loop across the list called vendors
    for x in vendors:
        print("\nThe vendor is " + x, end="")   # newline, print current vendor, and end without newline
        if x not in approved_vendors:   # if x does not appear within the list approved_vendors
            print(" - NOT AN APPROVED VENDOR!", end="")
    print("\nOur loop has ended.") # print when loop has finished

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    
    for name in farms:
        print(name["name"], end=" ")
        for x in name["agriculture"]:
            print(x, end= " ")
        print("\n")


if __name__ == "__main__":
    main()
