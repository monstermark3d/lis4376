"""Defines four functions

1. get_requirements()
2. add_items()
3. get_items_cost()
4. get_cart()
"""


def get_requirements():
    """Accepts 0 args. Displays program requirements."""
    print("\nDeveloper: Mark Trombly")
    print("Simple Shopping Cart!")
    print("\nProgram Requirements:\n"
          + "1. Capture user-entered shopping items.\n"
          + "2. Retrieve cost for each item.\n"
          + "3. Print items, cost, and total of all items.\n"
          + "4. Must perform data and range validation.\n"
          
          + "\n***Extra credit (10 pts):***\n"
          + "\ta. Request tax rate: between 1% and 10%.\n"
          + "\tb. Print pre-tax total, total tax, and total amount with tax.\n"
          + "\tc. Must perform data and range validation.\n")
    
    print("***Resource(s):***\n"
          + "Prompt user until valid response: https://www.python-engineer.com/posts/ask-user-for-input/\n"
          + "Print tabular data: \n"
          + "\thttps://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data\n"
          + "\thttps://www.educba.com/python-print-table/\n")
    
    print("Input:")

# Input/Process/Output: IPO


def add_items():

    print("Enter -1 to stop program.\n.")

    
    
    # initialize variable(s)
    name = ""
    count = 0
    my_items = []

    # Note: -1 flag value
    while name != "-1":
        try:
            # prompt for item name (Note: no newline, and counter variable to make "user-friendly.")
            print("{0}{1} {2}".format(
                "Enter item", count + 1, "name: "), end="")
            
            name = input()
            name[0] # test for input (access first character, if none, error!)

            # stop loop with flag value
            if name == "-1":
                print("Stopping list!\n")
                break

            count += 1 # increment counter variable
            my_items.append(name)  # if all OK, append cart item

        except IndexError as e:
            # print(e) # only used to print generated error message
            print("No item name entered! Try again.\n")
            continue
    
    # use for testing logic
    # print(count, my_items)
    # exit()
    return my_items


def get_items_cost(items_list):
    """Accepts 0 args. Prompts for item amount, returns user-entered value. With data validation!"""
    # test valid float and w/in range

    # initialize variables
    i = 0 # list item counter variable
    my_cost = [] # shopping cart list items cost

    for my_iterator in range(len(items_list)):
        while True:
            try:
                # initialize variable(s)
                cost = 0.0 # optional initialization

                # prompt for item cost (Note: no newline, and counter variable to make "user-friendly.")
                print("{0} {1} {2}".format(
                    "Enter", items_list[i], "cost: $"), end="")
                # or...
                # pint("Enter item" + str(my_iterator +1) + " cost: $", end="")

                cost = float(input()) # No need for prompt in input() function

                # cost = float(input("Enter item cost: $")) # prompt w/o counter variable

                is_within_range = False
                while not is_within_range:
                    if cost >= 1 and cost <= 100:
                        is_within_range = True
                    else:
                        print("Item cost must be between $1 and $100.\n")
                        print("{0} {1} {2}". format(
                            "Enter", items_list[i], "cost: $"), end="")
                        # No need for prompt in input() function
                        cost = float(input())

                i += 1 # increment list item variable
                my_cost.append(cost)
                break

            except ValueError:
                        print("Not a float! Try again.\n")
                        continue
            
    return my_cost
        

def get_cart(items, costs):
        # initialize variable(s)
        j = 0 # initialize counter variable
        total = 0.0 # cart total

        print()    # blank line

        # Note: There are a number of table-formatting packages for reports.
        # display table header
        print("{0:<10s} {1:<12s}".format("Item", "Cost"))

        while j < len(items):
            print("{0:<10s} {1:>6.2f}".format(items[j], costs[j]))
            total = total + costs[j] # accumulate total
            j += 1 # increment counter variable

        # display total
        print("\nTotal: ${0:.2f}".format(total))
        print("\n")
        