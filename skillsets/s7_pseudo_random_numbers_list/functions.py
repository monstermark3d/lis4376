import random
"""Defines four functions:

1. get_requiments()
2. get_list_size()
3. create_list()
4. sort_list()
"""


def get_requirements():
    """Accepts 0 args. Displays program requirements."""
    print("\nDeveloper: Mark Trombly")
    print("Pseudo-Random Number Lists!")
    print("\nProgram Requirements:\n"
          + "1. Create pseudo-random list of numbers.\n"
          + "2. Sort pseudo-random list of numbers.\n"
          + "3. Must perform data and range validation.\n")
    
    print("***Resource(s):***\n"
          + "Generate pseudo-random numbers: https://docs.python.org/3/library/random.html\n"
          + "for loop with range() function: https://www.freecodecamp.org/news/python-for-loop-for-i-in-range-example/\n")
    
    print("Input:")

    # Input/Process/Output: IPO


def get_list_size():
    """Accepts 0 args. Prompts for list size returns user-entered value. With data validation!"""
    # test valid int and w/in range
    while True:
        try:
            # initialize variable(s)
            size = 0 # could leave out this initialization

            # prompt size number
            size = int(input("Enter list size: "))

            is_within_range = False
            while not is_within_range:
                if size >=1 and size <= 10:
                    is_within_range = True
                else:
                    print("List size must be between 1 and 10.\n")
                    size = int(input("Enter list size: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return size
        

def create_list(size):
    """Accepts 1 args. Returns pseudo-random number list--no duplicates!"""
    # range() function generic syntax:
    # range(stop) # stop value mandatory (default start value = 0), stop = stop - 1
    # range(start, stop[, step]) # start and step values optional

    my_list = []
    for my_iterator in range(size):
        while True:
            # here, randint() returns random integer between 1 and size, inclusive
            number = random.randint(1, size)
            # no duplicates
            if not number in my_list:
                my_list.append(number)
                break
    return my_list


def sort_list(test_list):
    """Accepts 1 args. Returns original and sorted number lists."""
    print("\nOriginal pseudo-random number list: ", test_list)

    test_list.sort()
    print("Sorted list (ascending):", test_list)

    test_list.sort(reverse=True)
    print("Sorted list (descending):", test_list, "\n")