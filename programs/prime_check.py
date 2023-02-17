
def check_prime(num):
    if num<=0:
        return False
    elif num==1:
        return False

    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False

    return True

if __name__=="__main__":
    print(check_prime(2))
    print(check_prime(-2))
    print(check_prime(1))
    print(check_prime(7))
    print(check_prime(8))
