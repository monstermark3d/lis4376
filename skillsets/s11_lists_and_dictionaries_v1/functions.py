"""Defines four functions:

1. get_requirements()
2. add_emails()
3. get_phones()
4. create_contacts()
"""


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


def create_contact(keys, values):
    """Accepts 2 args. Creates dictionary based upo two list parameters. Displays dictionary elements."""
    my_dictionary = [] # create empty dictionary (optional)

    # Note: zip() function conjoins elements in two lists,: dict() converts resulting tuples into dictionary key-value pairs
    my_dictionary = dict(zip(keys, values))
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