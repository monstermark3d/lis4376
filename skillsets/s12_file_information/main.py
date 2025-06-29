#!/usr/bin/env python3
import functions as f


def main():
    """Program entry. Calling environment to user-defined functions"""
    # initialize variable(s)

    # function calls
    f.get_requirements()

    while True:
        f.get_menu() # display cwd and menu before each command
        command = f.get_command()

        if command !="7":
            f.run_command(command)
        else:
            print("\nStopping program!\n")
            break


if __name__ == "__main__":
    main()