# How Much is True?
# Create a function which returns the number of True values in a list.

# Examples
# count_true([True, False, False, True, False]) ➞ 2

# count_true([False, False, False, False]) ➞ 0

# count_true([]) ➞ 0
# Notes
# Return 0 if given an empty list.
# All list items are of the type bool (True or False).

def count_true(lst):
    return len(list(filter(lambda x: x == True, lst)))

# Other solutions
def count_true(lst):
    return sum(lst)

def count_true(lst):
    return lst.count(True)

x = [True, False, True, False]

print(count_true(x))