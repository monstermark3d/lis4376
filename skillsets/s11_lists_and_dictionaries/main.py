#!/usr/bin/env python3
import functions as f


def main():
    """Progrm entry. Calling environment to user-difined functions."""
    # initialize variable(s)
    your_emails = [] # create empty list for email addresses
    your_phones = [] # create empty list for phone numbers
    your_firstname = []
    your_lastname = []
    your_dictionary = []

    # function calls
    f.get_requirements()
    your_emails = f.add_emails()

    # use for testing return values
    # print(len(your_emails), your_emails)
    # exit()

    if len(your_emails) == 0:
        print("No emails!")
    else:
        your_phones = f.get_phones(your_emails)
        your_firstname, your_lastname = f.get_names(your_emails)
        # testing returns
        # print(your_phones)
        # exit()

        your_dictionary = f.create_contact(your_emails, your_phones, your_firstname, your_lastname)
    while True:
        f.get_menu() # display cwd and menu before each command
        command = f.get_command()

        if command.upper() !="Q":
            f.run_command(command, your_dictionary)
        else:
            print("\nEnding program!\n")
            break
    

if __name__ == "__main__":
    main()