"""Defines four functions:

1. get_requirements()
2. add_emails()
3. get_phones()
4. create_contacts()
"""
# create constants
COMMANDS = ('U', 'D', 'L', 'Q')
MENU = """U Edit
D Delete
L List
Q Quit"""

def get_requirements():
    """Accepts 0 args. Displays program requirements"""
    print("Developer: Mark Trombly")
    print("Working with lists, dictionaries, and user-entered values.")
    print("\nProgram Requirements:\n"
          + "1. Write a program that prints all elements of a user-entered contact list. \n"
          + "2. Must perform data validation.\n"
          + "3. Dictionary key *must* be user's e-mail address.\n"
          + "4. ***Extra credit (20pts. Both are optional.):*** \n"
          + "\ta) Provide additional functionality to add contacts' first and last names (10 pts).\n"
          + "\tb) Provide additional functionality to update *and* delete contacts (10 pts. Both required.).\n")
    
    print("***Resource(s):***\n"
          + " Dictionaries:\n"
          + "https://www.codeacedemy.com/learn/learn-python-3/modules/learn-python3-dictionaries/cheatsheet\n"
          + "https://www.pythoncheatsheet.org/cheatsheet/dictionaries\n")
    
    print("Input:")


def add_emails():

    # test string input (can't be empty string!)

    print("Enter -1 to stop adding e-mails.\n")

    # initialize variable(s)
    email = ""
    count = 0
    my_emails = []

    # Note: -1 flag value
    while email != "-1":
        try:
            # prompt for email (Note: no newline, and counter variable to mak "user-friendly.")
            print("{0}  {1}{2}".format(
                "Enter email", count + 1, ": "), end="")
            
            email = input()
            # test for input (access first character, if none, error!)
            email[0]

            # stop loop with flag value
            if email == "-1":
                print("Stopping list!")
                break

            count += 1 #increment counter variable
            my_emails.append(email) # if all OK, append contact email

        except IndexError as e:
            # print(e) # only used for testing, to print generatede error message
            print("No email entered! Try again.\n")
            continue

    # use for testing logic
    # print(count, my_emails)
    # exit()
    return my_emails


def get_phones(emails_list):
    """Accepts 1 arg. Prompts for phone numbers, based upon emails, returns user-entered values. With data validation!"""
    # test string input (can't be empty string!)

    # initialize variables
    phone = ""
    i = 0 # list email counter variable
    my_phones = [] # phone list

    for my_iterator in range(len(emails_list)):
        while True:
            try:
                # prompt for phone number (Note: no newline, and counter variable to make "user-friendly.")
                # print("{0} {1}".format(phone", emails_list[i]))
                print("\n{0}{1}".format(emails_list[i], ", phone:"))
                # or...
                # print("Enter phone number for " + str(emails_list[i]) + ":", end="")

                phone = input()

                # test for input (acess first character, if none, error!)
                phone[0]

                i += 1 # increment list item variable
                my_phones.append(phone) # if all OK, append contact phone
                break

            except IndexError as e:
                # print(e) # only used to print generated error message
                print("No phone entered! Try again.")
                continue
        
    # use for testing logic
    # print(i, my_phones)
    # exit()
    return my_phones

def get_names(emails_list):
    """Accepts 1 arg. Prompts for phone numbers, based upon emails, returns user-entered values. With data validation!"""
    # test string input (can't be empty string!)

    # initialize variables
    firstname = ""
    lastname = ""
    i = 0 # list email counter variable
    my_firstname = [] 
    my_lastname = []

    for my_iterator in range(len(emails_list)):
        while True:
            try:
                # prompt for first name (Note: no newline, and counter variable to make "user-friendly.")
                # print("{0} {1}".format(phone", emails_list[i]))
                while len(firstname) == 0:
                    print("\n{0}{1}".format(emails_list[i], ", first name:"))
                    
                    firstname = input()

                    # test for input (acess first character, if none, error!)
                    firstname[0]
                
                while len(lastname) == 0:

                    print("\n{0}{1}".format(emails_list[i], ", last name:"))
                    
                    lastname = input()

                    # test for input (acess first character, if none, error!)
                    lastname[0]

                i += 1 # increment list item variable
                my_firstname.append(firstname) # if all OK, append contact phone
                my_lastname.append(lastname)
                firstname = ""
                lastname = ""
                break

            except IndexError as e:
                # print(e) # only used to print generated error message
                print("No name entered! Try again.")
                continue

    # use for testing logic
    # print(i, my_phones)
    # exit()
    return my_firstname, my_lastname

def create_contact(keys, values, values2, values3):
    """Accepts 2 args. Creates dictionary based upo two list parameters. Displays dictionary elements."""
    my_dictionary = [] # create empty dictionary (optional)

    # Note: zip() function conjoins elements in two lists,: dict() converts resulting tuples into dictionary key-value pairs
    #my_dictionary = dict(zip(keys, values, values2, values3))
    my_dictionary = dict(zip(keys, zip(values, values2, values3)))
    # testing returns
    # print(type(my_dictionary))
    # exit()


    """
    Following three functions returned through dictionary object:
    .keys() returns keys
    .values() returns values
    .items() returns both keys and values
    """

    print("\nPrinting dictionary:\n", my_dictionary)

    print("\nPrinting dictionary keys:\n", my_dictionary.keys())

    print("\nPrinting dictionary values:\n", my_dictionary.values())

    print("\nPrinting dictionary items:\n", my_dictionary.items())

    return my_dictionary

def get_menu():
    """Accepts 0 args. Displays menu items."""
    print("\nMENU:\n", MENU, sep="")


def get_command():
    """Accepts 0 args. Returns command number, or error message."""
    while True:
        command = input("\nEnter command: ")
        if not command.upper() in COMMANDS:
            print("Incorrect command!")
        else:
            return command.upper()
        
def run_command(command, my_dictionary):
    """Accepts 1 arg. Runs command based upon user-entered value."""

    if command =='U':
        update_contact(my_dictionary) # Update first/last name
    elif command == 'D':
        remove_contact(my_dictionary) # delete dictionary key/value
    elif command == 'L':
        list_contacts(my_dictionary) # display contact list

def list_contacts(my_dictionary):
    """Accepts 1 arg. Prints list of dictionary contacts."""

    print("\nPrinting dictionary:\n", my_dictionary)

    print("\nPrinting dictionary keys:\n", my_dictionary.keys())

    print("\nPrinting dictionary values:\n", my_dictionary.values())

    print("\nPrinting dictionary items:\n", my_dictionary.items())

def remove_contact(my_dictionary):
    """Accepts 1 arg. Lists contacts for removal, then prompts user for contact to remove."""

    contact_num = 0
    del_contact = ""

    for my_contact in my_dictionary.items():
        print(contact_num, "> ", f"{my_contact}")
        contact_num += 1
        #print(contact_num, "> ", my_dictionary[contact_num])
    contact_list = list(my_dictionary.keys())

    
    while del_contact != -1:
        try:
            print("\nEnter contact to delete (-1 to quit): ", end="")

            del_contact = int(input())

            if del_contact == -1:
                print("Stopping delete!")
                break
            
            #del_contact = int(del_contact)

            is_within_range = False
            while not is_within_range and del_contact != -1:
                if del_contact >= 0 and del_contact <= (len(contact_list) - 1):
                    is_within_range = True

                else:
                    print("Contact must be between 0 and", (len(contact_list) - 1), " (-1 to quit).\n")
                    print("\nEnter contact to delete (-1 to quit):", end="")
                    del_contact = int(input())
            break

        except ValueError:
                        print("Not an int! Try again.\n")
                        continue

    if del_contact != -1:
         del my_dictionary[contact_list[del_contact]]

def update_contact(my_dictionary):
    """Accepts 1 arg. Lists contacts for update, then prompts user to select contact and enter data to edit."""

    contact_num = 0
    update_contact = ""
    for my_contact in my_dictionary.items():
        print(contact_num, "> ", f"{my_contact}")
        contact_num += 1
        #print(contact_num, "> ", my_dictionary[contact_num])
    contact_list = list(my_dictionary.keys())

    
    while update_contact != -1:
        try:
            print("\nEnter contact to update (-1 to quit): ", end="")

            update_contact = int(input())

            if update_contact == -1:
                print("Stopping update!")
                break
            
            #update_contact = int(update_contact)

            is_within_range = False
            while not is_within_range and update_contact != -1:
                if update_contact >= 0 and update_contact <= (len(contact_list) - 1):
                    is_within_range = True

                else:
                    print("Contact must be between 0 and", (len(contact_list) - 1), " (-1 to quit).\n")
                    print("\nEnter contact to update (-1 to quit): ", end="")
                    update_contact = int(input())
            break

        except ValueError:
                        print("Not an int! Try again.\n")
                        continue
        
    if update_contact != -1:
        # enter phone number

        print("Phone Number: ", end="")
        my_phone = input()

        # enter first name

        print("First Name: ", end="")
        my_first = input()


        # enter last name
        print("Last Name: ", end="")
        my_last = input()

        # update contact 
        
        my_dictionary.update({contact_list[update_contact]: [my_phone, my_first, my_last]})
    
