#!/usr/bin/env python3
import functions as f


def main():
    """Program entry. Calling environment to user-defined functions"""
    # initialize variables

    # create empty lists
    your_items = []
    your_costs = []

    # function calls
    f.get_requirements()
    your_items = f.add_items()

    # use for testing return values
    # print(len(your_items), your_items)
    # exit()

    if len(your_items) == 0:
        print("No shopping cart items.")
    else:
        your_costs = f.get_items_cost(your_items)
        # testing returns
        # print(your_costs)
        # exit()
        f.get_cart(your_items, your_costs)

    
if __name__ == "__main__":
    main()