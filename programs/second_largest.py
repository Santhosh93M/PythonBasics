lst = [23,45,67,78,34,21]

def second_largest(lst):
    lst.sort()
    return lst[len(lst)-2]

print(second_largest(lst))
