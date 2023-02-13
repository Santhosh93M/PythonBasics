s = "Fly Until You Touch The Sky"

def count_upper_lower(s):
    c_upper = 0
    c_lower = 0

    for i in s:
        if i.isupper():
            c_upper+=1
        else:
            c_lower+=1

    return c_upper,c_lower

print(count_upper_lower(s))

