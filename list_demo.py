# To find the smallest number in the given list
def smallest_num(lst):
    small_num = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                small_num = lst[i]
    return small_num


# To find the given number present in the list or not
def check_presence(lst):
    num = int(input("Enter the number: "))
    if num in lst:
        print("The given number present in the list")
    else:
        print("The given number not in the list")


num_list = [23, 78, 45, 34, 98, 123, 345, 22, 8, 7]
print(smallest_num(num_list))
check_presence(num_list)
