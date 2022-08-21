# To get repeated characters count
def char_frequency(strng):
    dict = {}
    for char in strng:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


# To check the string palindrome or not
def palindrome_or_not(strng):
    temp = strng[::-1]
    if strng == temp:
        print("The given string is palindrome")
    else:
        print("The given string is not palindrome")


print(char_frequency("sunrising"))
palindrome_or_not("amma")
