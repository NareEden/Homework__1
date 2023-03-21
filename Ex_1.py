# Given an unsorted list of numbers (integers) n, find and print all
# the duplicates in the list.

n = [5, 1, 2, 1, 4]
# 1
# n = [4, 1, 2]
# None
# n = []
# None
# n = [6, 2, 5, 2, 6, 2]
# 2 6
# n = [42, 42, 42, 42]
# 42


def duplicates(lst):
    uniqueList = []
    dupl_lst = []
    if len(lst) <= 1:
        print(None)
    else:
        for i in lst:
            if i not in uniqueList:
                uniqueList.append(i)
            elif i not in dupl_lst:
                dupl_lst.append(i)
        if len(dupl_lst) == 0:
            print(None)
        else:
            print(dupl_lst)


duplicates(n)

# The complexity of the code is O(n)