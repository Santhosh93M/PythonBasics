s = "fly until you touch the sky"

def count_vowels(s):
    count = 0
    vowels = ["a","e","i","o","u"]
    for i in s:
        if i in vowels:
            count+=1

    return count

print(count_vowels(s))

        
