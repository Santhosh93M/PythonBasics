def digit_sum(num):
    res = 0

    while num > 0:
        rem = int(num)%10
        res+=rem
        num /= 10
    return res

print(digit_sum(132456))
