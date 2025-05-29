
def get_requirements():
    # prints program requirements
    print("Python Lists")
    print("\nProgram Requirements:\n"
        + "Developer: Mark Trombly\n"
        + "1. Lists (Python data structure): mutable, ordered sequence of elements.\n"
        + "2. Lists are muable/changeable--that is, can insert, update, delete.\n"
        + "3. Create two lists - using square brackets [list items]: list = [include below list elements here...].\n"
        + "4. Backward-engineer the following program.\n")
    
def get_list1():
    # initialize list1
    list1 = [1, "test", 3.14, True]
    print("Print list1: ", end="")
    print(list1)

    return list1

def add_list1(test_list):
    # append() adds element to end of list1
    print("\nAppend '@' character to end of list1: ")
    test_list.append("@")
    print(test_list)

    # insert(pos,elem) #Note: pos=index position, elem=value
    # insert() adds element at specified index (here, 1st element)
    print("\nInsert number 6 at beginning of list1: ")
    test_list.insert(0,6)
    print(test_list)

    return test_list

def count_list1(num_list):
    # count list 1 elements
    print("\nDisplay number of list1 elements: ")
    # also works for strings, tuples, dict objects
    print(len(num_list))

def reverse_list1(num_list):
    # reverse list1 elements
    print("\nReverse list1: ")
    num_list.reverse()  # reverse list
    print(num_list)

def remove_list1(num_list):
    # remove list1 elements
    print("\nRemove last list1 element: ")
    num_list.pop() # delete last element (LIFO)
    print(num_list)

    print("\nDelete second element from list1 by *index* (note: index 1=2nd element): ")
    # pops element at index specified
    # num_list.pop(1)
    # or...
    del num_list[1]
    print(num_list)

    print("\nDelete element from list1 by *value* (3.14): ")
    num_list.remove(3.14)
    print(num_list)

    print("\nDelete all elements from list1: ")
    num_list.clear()    # delete all elements
    print(num_list)

def get_list2():
    # create list2
    # initialize list2
    list2 = ["test", "a", "new", "list"]
    print("\nPrint list2: ", end="")
    print(list2)
    return list2

def sort_list2(another_list):
    # sort list2 elements
    print("\nSort elements in list2 alphabetically - using sort(): ")
    another_list.sort() # sort alphabetically
    print(another_list)

    print("\nSort elements in list2 reverse alphabetically - using sort(): ")
    another_list.sort(reverse=True) # reverse sort alphabetically
    print(another_list)