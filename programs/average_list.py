lst = [23,45,67,78,34,21]

def average(lst):
    if len(lst)==0:
        return 0
    sum = 0
    for i in lst:
        sum += i

    return int(sum/len(lst))

print(average(lst))
