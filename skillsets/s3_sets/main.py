#!/usr/bin/env python3
import functions

# Note: shebang line only needed in executable files (e.g.,main.py, *not* functions.py)

set1 = {True, 2, 3.14, 'test'}

set2_list = [True, 2, 3.14, 'test']
set2 = set(set2_list)

set3_tuple = (True, 2, 3.14, 'test')
set3 = set(set3_tuple)

print("\nPython Sets - like mathematical sets!")

print("\nProgram Requirements:\n"
    + "Developer: Mark Trombly\n"
    + "1. Sets (Python data structure): mutable, heterogeneous, unordered sequence of elements, CANNOT contain duplicate values.\n"
    + "2. Sets are mutable/changeable--that is, can insert, update, delete.\n"
    + "3. While setsa re mutable/changeable, they *cannot* contain other mutable items like list, set, or dictionary**\n"
    + "\tthat is, elements contained in set must be immutable."
    + "4. Also, since sets are unordered, CANNOT use indexing (or, slicing) to access, update, or delete elemets.\"\n"
    + "5. Two methods to create sets:\n"
    + "\ta. Create set using curly brackets {set}: set1 = {include below set elements here...}\n"
    + "\tb. Create set using set() function: set1 = set(<iterable>)\n"
    + "\n\tExamples:\n"
    + "\tset2 = set([include below set elements here...]) # set with list\n"
    + "\tset3 = set((include below set elements here...)) # set with tuple\n"
    + "\tNote: An \"iterable\" is *any* object, which can be iterated over--that is, lists, tuples, or even strings.\n"
    + "6. Backward-engineer the following program.\n"
    + "\n***Note***: All three sets below print as \"sets\" (i.e., curly brackets), *regardless* of how they were created!\n")

# Print set1 created using curly brackes:
print("Print set1 created using curly brackets:\n"
      + "Note: Following values used: 2, \"test\", 3.14, True\n"
      + "Note: Value sequence *used* not guaranteed!")
functions.setPrint(set1)

# Print set1 type
print("\nPrint set1 type:")
functions.setPrintTyp(set1)

# Print set2 created using set() function with list:
print("\nPrint set2 created using set() function with list:")
functions.setPrint(set2)

# Print set2 type
print("\nPrint set2 type:")
functions.setPrintTyp(set2)

# Print s3t3 created using set() function with tuple
print("\nPrint set3 created using set() function with tuple:")
functions.setPrint(set3)

# Print set3 type
print("\nPrint set3 type:")
functions.setPrintTyp(set3)

# Print set1 # elements
print("\nDisplay number of set1 elements:")
functions.setPrintLen(set1)

# Add set element (5) using add() method
print("\nAdd set element (5) using add() method:")
set1.add(5)
functions.setPrint(set1)

# Display number of set1 elements
print("\nDisplay number of set1 elements:")
functions.setPrintTyp(set1)

# Display updated set elements
print("\nDisplay updated set1 elements:"
      + "\nNote: UPdated with following values: 1, 2, 3, 4"
      + "\nNote: Sets can ONLY contain unique elements! (Note: True=1, and value 2 already exist!)")
set1.add(1)
set1.add(2)
set1.add(3)
set1.add(4)
functions.setPrint(set1)

# Display number of set1 elements
print("\nDisplay number of set1 elements:")
functions.setPrintLen(set1)

# Discard '4' from set 1
set1.remove(4)
print("\nDiscard 4:")
functions.setPrint(set1)

# Display length of set1
print("\nLength of set1:")
functions.setPrintLen(set1)

# Remove 'test' from set1
set1.remove('test')
print("\nRemove 'test':")
functions.setPrint(set1)

# Display length of set1
print("\nLength of set1:")
functions.setPrintLen(set1)

print("\nNote: When deleting set element that doesn't exist, discard() ignores it, but remove() raises KeEror!")

# Display minimum value (Note: True=1)
print("\nDisplay minimum value (Note: True=1)")
functions.setPrintMin(set1)

# Display maximum value of set 1
print("\nDisplay maximum value:")
functions.setPrintMax(set1)

# Display set1 elements
print("\nDisplay set1 elements:")
functions.setPrint(set1)

# Display sum of values of set1
print("\nDisplay sum of values (*must* be numeric, or able to conver to numeric):")
functions.setPrintSum(set1)

# Delete all set elements
print("\nDelete all set elements:")
set1.clear()
functions.setPrint(set1)

# Length of set1
print("\nLength of set1:")
functions.setPrintLen(set1)

# Blank line
print("\n")