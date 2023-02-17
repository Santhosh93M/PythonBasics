print("---------------SIMPLE CALCULATOR---------------")
print()


def calci(opt,num1,num2):
    if opt=="1":
        return num1+num2
    elif opt=="2":
        return num1-num2
    elif opt=="3":
        return num1*num2
    elif opt=="4":
        return num1/num2
    else:
        return "Enter the correct option"

option = input("1.Addition 2.Sub 3.Multiplication 4.Divison : ")
num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))

print(calci(option,num1,num2))
