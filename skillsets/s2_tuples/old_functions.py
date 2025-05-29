#
# Functions created by Mark Trombly

# Print tuple
def tuPrint(tupleIn):
    print(tupleIn)

# Unpack tuple
def tuUnpack(tupleIn):
    elem1, elem2, elem3, elem4 = tupleIn
    return elem1, elem2, elem3, elem4

# Count number of tuple elements
def tuCount(tupleIn):
    return len(tupleIn)

# Third element in tuple
def tuThirdElem(tupleIn):
    return (tupleIn[2])

# Slice of tuples
def tuSlice(tupleIn, beg, end):
    return (tupleIn[beg:end])

# Reassign tuple
def tuReassignParen(tupleIn):
    tupleIn = (1, 2, 3, 4)
    return (tupleIn)

# Reassign tuple *packing*
def tuReassignPack(tupleIn):
    elem1, elem2, elem3, elem4 = tupleIn
    elem1 = 5
    elem2 = 6
    elem3 = 7
    elem4 = 8
    return (elem1, elem2, elem3, elem4)

""" # Delete tuple
def tuDelete(tupleIn):
    del tupleIn
    return (tupleIn) """