lst = [-32,-12,-56,23,45,67,78,34,21,-98]

def sumOf(lst):
    neg_sum = []
    pos_even_sum = 0
    pos_odd_sum = 0
    for i in lst:
        if i<0:
            neg_sum.append(i)
        elif i%2==0:
            pos_even_sum+=i
        elif i%2!=0:
            pos_odd_sum+=i

    return sum(neg_sum),pos_even_sum,pos_odd_sum

print(sumOf(lst))
