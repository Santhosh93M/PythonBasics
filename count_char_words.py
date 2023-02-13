s = "fly until you touch the sky"

def count_char_word(s):
    if len(s)==0:
        return (0,0)
    l = s.split(" ")
    count_char = 0
    for i in l:
        count_char+=len(i)

    return len(l),count_char

print(count_char_word(s))

        
