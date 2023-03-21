# You are given a list nums and an integer target. Return the indeces of the
# elements from n that sum to target.

# nums = [2, 5, 3, 7, 3, 8]
# targets = 12
# [1, 3]
# nums = [2, 5, 3, 7, 3, 8]
# target=10
# 2, 3
# nums = [1, 5, 3, 1, 5, 1]
# target=12
# None
# nums = [0, 0, 0, 0]
# target=0
# 0, 1
# nums = [1]
# target=1
# None
# nums = [1, 3, 2, 42, 1]
# target=42
# None
# nums = []
# target=42
# None


def target_sum(lst, trg):
    indices = []
    if len(lst) <= 1:
        print(None)
    elif target in lst:
        print(None)
    else:
        for i in range(len(lst)):
            if trg - lst[i] in lst and i not in indices:
                indices.append(i)
        if len(indices) == 0:
            print(None)
        else:
            print(indices)


target_sum(nums, target)

# Complexity is O(n) or O(1) in case of the lists which are less or equal to 1.

# Could not find a solution for case 2