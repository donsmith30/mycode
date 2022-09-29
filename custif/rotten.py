#!/usr/bin/env python3

"""rotten ratings custom if statements"""

def main():

    rating = float(input("What is the movie review rating? "))

    if rating > 89:
        print("Certified fresh")
    elif rating > 69:
        print("Fresh")
    elif rating < 70:
        print("Rotten")

if __name__ ==  "__main__":
    main()
