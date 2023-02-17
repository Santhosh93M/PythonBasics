lst = [12,34,56,78,90]

def swap_first_last(lst):
    if len(lst)==1 or len(lst)==0:
        return lst
    lst[0],lst[len(lst)-1]= lst[len(lst)-1],lst[0]

    return lst

print(swap_first_last(lst))
print(swap_first_last([1]))
print(swap_first_last([]))

