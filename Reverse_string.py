s = "fly until you touch the sky"

def reverse_string(s):
    res = ""
    for i in s:
        res = i + res
    return res

print(reverse_string(s))
