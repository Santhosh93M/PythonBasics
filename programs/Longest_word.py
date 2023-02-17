lst = ["hello" ,"world","think","first", "before", "you", "do"]

def longest_word(lst):
    max = 0
    for i in lst:
        if len(i)>max:
            max = len(i)

    return max

print(longest_word(lst))
