#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests
from mtgsdk import Card

def main():
    """Run time code"""
    # Get all cards
    cards = Card.all()

    # Filter Cards
    # You can chain 'where' clauses together. The key of the hash
    # should be the URL parameter you are trying to filter on
    cards = Card.where(supertypes='legendary') \
                .where(types='creature') \
                .where(colors='red,white') \
                .all()

    # Get cards on a specific page / pageSize
    cards = Card.where(page=50).where(pageSize=50).all()



if __name__ == "__main__":
    main()
