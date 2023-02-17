lst = [23,45,67,78,34,21]

def large_odd_even(lst):
    even_max = 0
    odd_max = 0
    for i in lst:
        if i%2==0:
            if even_max<i:
                even_max = i
        else:
            if odd_max < i:
                odd_max = i
    return even_max,odd_max

print(large_odd_even(lst))
