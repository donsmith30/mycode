#!/usr/bin/env python3

"""Alta3 research | Don | quiz about monty"""

def main():
    roundCount = 0

    while True:
        roundCount = roundCount + 1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input("Your guess--> ")

        if answer.lower() == 'brian':
            print("correct")
            break
        elif roundCount==3:
            print("you lose, correct answer was Brian")
            break
        else:
            print("sorry try again")

if __name__ == "__main__":
    main()
