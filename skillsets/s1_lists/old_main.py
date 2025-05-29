#!/usr/bin/env python3
import functions

# Note: shebang line only needed in executable files (e.g.,main.py, *not* functions.py)

list1 = [1, 'test', 3.14, True]
list2 = ['test', 'a', 'new', 'list']

print("\nPython Lists")

print("\nProgram Requirements:\n"
    + "Developer: Mark Trombly\n"
    + "1. Lists (Python data structure): mutable, ordered sequence of elements.\n"
    + "2. Lists are muable/changeable--that is, can insert, update, delete.\n"
    + "3. Create two lists - using square brackets [list items]: list = [include below list elements here...].\n"
    + "4. Backward-engineer the following program.\n")

# Print list1
print("Print list1:")
functions.lsPrint(list1)

# Append '@' to end of list1
print("\nAppend '@' character to end of list1:")
functions.lsAppend(list1, "@")
functions.lsPrint(list1)

# Insert 6 at beginning of list1
print("\nInsert number 6 at beginning of list1:")
functions.insertBeginning(list1, 6)
functions.lsPrint(list1)

# Display number of elements in list1
print("\nDisplay number of list1 elements:")
print(functions.lsNumElements(list1))

# Reverse elements in list1
print("\nReverse list1:")
list1 = functions.lsReverse(list1)
functions.lsPrint(list1)

# Remove last element in list1
print("\nRemove last list1 element:")
list1 = functions.lsRemoveLast(list1)
functions.lsPrint(list1)

# Delete second element from list1 using index
print("\nDelete second element from list1 by *index* (note: index 1 = 2nd element):")
list1 = functions.lsRemoveSecond(list1)
functions.lsPrint(list1)

# Delete element with value 3.14 from list1 by value
print("\nDelete element from list1 by *value* (3.14):")
list1 = functions.lsDelByVal(list1,3.14)
functions.lsPrint(list1)

# Delete all elements in list1
print("\nDelete all elements from list1:")
list1 = functions.lsDelAllElements(list1)
functions.lsPrint(list1)

# Print list2
print("\nPrint list2:")
functions.lsPrint(list2)

# Sort elements in list2 alphabetically using sort() method
print("\nSort elements in list2 alphabetically using sort():")
list2 = functions.lsSort(list2)
functions.lsPrint(list2)

# Sort elements in list2 in reverse alphabetically using sort() method
print("\nSort elements in list2 reverse alphabetically - using sort():")
list2 = functions.lsRevSort(list2)
functions.lsPrint(list2)

# Blank like at end
print("\n")