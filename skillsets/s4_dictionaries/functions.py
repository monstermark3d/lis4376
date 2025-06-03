"""module docstring goes here"""
#
# skillset 4 dictionaries by Mark Trombly
#
"""
State Capitals: https://www.britannica.com/topic/list-of-state-capitals-in-the-United-States-2119210
State Sizes (sq mi): https://www.britannica.com/topic/largest/-U-S-state-by-area
"""

def get_requirements():
    print("\nPython Dictionaries")
    print("\nProgram Requirements:\n"
          + "Developer: Mark Trombly\n"
          + "1. Dictionaries (Python data structure): unordered key:value pairs,\n"
          + "2. Dictionray: an associative array (also known as hashes).\n"
          + "3. Any key in a dictionary is associated (or mapped) to a value (i.e., any Python data type).\n"
          + "4. Keys: must be of immutable type (string, number or tuple with immutable elements) and must be unique.\n"
          + "5. Values: can be any data type and can repeat.\n"
          + "6. Dictionaries have key-value pairs instead of single values; differentiating a dictionary from a set.\n"
          + "7. Two methods to create dictionaries:\n"
          + "\ta. Initialize dictionary with key/value pairs.\n"
          + "\tb. Create empty dictionary, using curly braces {}: my_dictionary.={}\n"
          + "\t   Then, assign values to keys: my_dictionary['key1'] = \"some value\"\n"
          + "8. Backward-engineer the following program.\n")
    
def get_dictionary():
    """function to create dictionary"""
    state_capitals = {
        "Alaska": "Juneau",
        "Texas": "Austin",
        "California": "Sacramento",
        "Montana": "Helena",
        "New Mexico": "Santa Fe"
    }

    """
    # Or...
    my_dictionary = {} # create empty dictionary
    # then, populate key/value pairs
    
    my_dictionary['ak_sqmi'] = 665384
    my_dictionary['tx_sqmi'] = 268596
    my_dictionary['ca_sqmi'] = 163695
    my_dictionary['mt_sqmi'] = 147040
    my_dictionary['nm_sqmi'] = 121590
    """

    print("Print dictionary:")
    print(state_capitals)

    print("\nPrint data structure type:")
    print(type(state_capitals))

    return state_capitals

def parse_dictionary(my_dictionary):
    """function to parse dictionary"""
    print("\nReturn dictionary's (key, value) pairs, built-in function:")
    print(my_dictionary.items())

    print("\nOr, use looping structure to return dictionary's (key, value) pairs, built-in function:")
    for k, v in my_dictionary.items():
        print("key:", k, ", value:", v, sep="")

    print("\nDisplay all keys, built-in function:")
    print(my_dictionary.keys())

    print("\nDisplay all values in dictionary, built-in unction:")
    print(my_dictionary.values())

    print("\nPrint vlue using key:")
    print(my_dictionary['Alaska'])

def count_dictionary(my_dictionary):
    """function to count dictnioary elements"""
    print("\nCount number of items (key:value pairs) in dictionary:")
    # also works for strings, tuples, list elements
    print(len(my_dictionary))

def add_element(my_dictionary):
    """function to add dictionary element"""
    my_dictionary["Arizona"] = "Scottsdale"

    print("\nPrint dictionary after added element:")
    print(my_dictionary)

def update_element(my_dictionary):
    """function to update dictionalry element"""
    my_dictionary["Arizona"] = "Phoenix"

    print("\nPrint dictionary after updated element:")
    print(my_dictionary)

def delete_element(my_dictionary):
    """function to delete dictionary element"""
    print("\nDelete \"Arizona\" element:")
    del my_dictionary["Arizona"]

    print("\nPrint dictionary after deleted element:")
    print(my_dictionary)

def delete_dictionary(my_dictionary):
    print("\nDelete all dictionary elements: ")
    my_dictionary.clear()   # delete all items
    print(my_dictionary)    # Note: here, my_dictionary still exists
    print(type(my_dictionary))

    # different from...
    # delete entire dictionary object (no longer exists)
    del my_dictionary
    # print(My_dictionary)  # Can't print! UnboundLocalError: local variable 'my_dictionary'