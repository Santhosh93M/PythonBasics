s = "santhosh"

def remove_odd_indexed(s):
    res = ""
    for i in range(0,len(s)):
        if i%2==0:
            res+=s[i]

    return res

print(remove_odd_indexed(s))
