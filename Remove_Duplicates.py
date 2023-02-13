lst = [1,1,13,13, 21, 23, 34, 45, 45, 67, 67, 78, 90]

def remove_duplicates(lst):
    l = []
    for i in lst:
        if i not in l:
            l.append(i)
    return l  


print(remove_duplicates(lst))
