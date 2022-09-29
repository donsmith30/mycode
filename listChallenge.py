#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""
import random

def main():

    wordbank= ["indentation", "spaces"]

    tlgstudents= ["Aaron", "Andy", "Asif", 
            "Brent", "Cedric", "Chris", 
            "Cory", "Ebrima", "Franco", 
            "Greg", "Hoon", "Joey", 
            "Jordan", "JC", "LB", 
            "Mabel", "Shon", "Pat", "Zach"]

    wordbank.append(4)

    num = int(input(f"enter a student number between 1 and {len(tlgstudents)} "))-1
    
    student_name = tlgstudents[num]

    print(f"{student_name} always uses {int(wordbank[2])} {wordbank[1]} to indent")

    randomA = 1
    randomB = 6
    randomC = random.randint(randomA, randomB)
    print(f"Finding random between {randomA} and {randomB}, {randomC}")

main()
