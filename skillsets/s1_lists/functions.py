# Functions created by Mark Trombly

# Print list function
def lsPrint(listin):
    print(listin)

# Append item to end of list
def lsAppend(listin, appVal):
    listin.append(appVal)

# Insert item to beginning of list    
def insertBeginning(listin, begVal):
    listin.insert(0, begVal)

# Return number of elements in list
def lsNumElements(listin):
    return(len(listin))

# Reverse list order
def lsReverse(listin):
    return(listin[::-1])

# Remove last element in list
def lsRemoveLast(listin):
    listin.pop()
    return(listin)

# Remove second element in list
def lsRemoveSecond(listin):
    del listin[1]
    return(listin)

# Delete item from list by value
def lsDelByVal(listin,delVal):
    if delVal in listin:
        listin.remove(delVal)
    return(listin)

# Delete all items in list
def lsDelAllElements(listin):
    listin.clear()
    return(listin)

# Sort list alphabetically
def lsSort(listin):
    return(sorted(listin))

# Sort list reverse alphabetically
def lsRevSort(listin):
    return(sorted(listin,reverse=True))