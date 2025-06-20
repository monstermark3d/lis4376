#!/usr/bin/env python3
import functions as f
#
# skillset 9 Guessing Game by Mark Trombly
#

def main():
    """Progrm entry. Calling environment to user-defined functions."""
    # initialize variable(s)
    low_num = 0
    high_num = 0

    # function calls
    f.get_requirements()
    low_num = f.get_lower()
    high_num = f.get_upper()

    # unit test
    # Note: In practice, test each function call individually!
    # print("\nPrinting lower num: ", low_num)
    # print("Printing higher num: ", high_num)
    # exit() # or, quit()

    while low_num > high_num:
        print("Lower number must be less than or equal to upper number! Try again!\n")
        low_num = f.get_lower()
    
    f.play_game(low_num, high_num)


if __name__ == "__main__":
    main()