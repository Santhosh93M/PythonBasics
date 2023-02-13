

def factorial(num):
    fact = 1
    if num<0:
        return 0
    elif num==0:
        return 1
    else:
        for i in range(1,num+1):
            fact *= i
        return fact

if __name__=="__main__":
    print(factorial(5))
