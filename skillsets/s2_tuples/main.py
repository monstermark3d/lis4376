#!/usr/bin/env python3
import functions

# Note: shebang line only needed in executable files (e.g.,main.py, *not* functions.py)

my_tuple = (1, 'test', 3.14, True)

print("\nPython Tuples")

print("\nProgram Requirements:\n"
    + "Developer: Mark Trombly\n"
    + "1. Tuples (Python data structure): *immutable* (cannot be changed!), ordered sequence of elements.\n"
    + "2. Tuples are immutable/unchangeable--that is, cannot insert, update, delete.\n"
    + "\tNote: can reassign or delete an *entire* tuple--but, *not* individual items or slices.\n"
    + "3. Create tuple using parentheses (tuple): tuple = (include below list elements here...).\n"
    + "4. Reassign tuple with, and w/o parentheses (), aka tuple \"packing.\"\n"
    + "5. Use tuple (unpacking), that is, assign values from tuple to sequence of variables: elem1, elem2, elem3, elem4 = my_tuple\n"
    + "6. Backward-engineer the following program.\n")

# Print my_tuple
print("Print my_tuple:")
functions.tuPrint(my_tuple)

# Print my_tuple unpacking:
print("Print my_tuple unpacking:")
elem1, elem2, elem3, elem4 = functions.tuUnpack(my_tuple)
print(f"elem1={elem1}"
      +f" elem2={elem2}"
      +f" elem3={elem3}"
      +f" elem4={elem4}")

# Display number of my_tuple elements
print("\nDisplay number of my_tuple elements:")
print(functions.tuCount(my_tuple))

# Print third element in my_tuple
print("\nPrint third element in my_tuple:")
print(functions.tuThirdElem(my_tuple))

# Print "slice" of my_tuple (second and third elements):
print("\nPrint \"slice\" of my_tuple (second and third elements):")
print(functions.tuSlice(my_tuple, 1, 3))

# Reassign my_tuple using prentheses.
print("\nReassign my_tuple using parentheses."
      +"Print reassigned my_tuple:")
my_tuple = functions.tuReassignParen(my_tuple)
functions.tuPrint(my_tuple)

# Reassign my_tuple using "packing" method (no parentheses).
print("\nReassign my_tuple using \"packing\" method (no parentheses).")
my_tuple = functions.tuReassignPack(my_tuple)
functions.tuPrint(my_tuple)

# Delete tuple
print("\nDelete my_tuple:"
      +"\nNote: will generate error, if trying to print after delete, as it no longer exists.")
del my_tuple
# my_tuple = functions.tuDelete(my_tuple)
# functions.tuPrint(my_tuple)

# Print blank line
print("\n")