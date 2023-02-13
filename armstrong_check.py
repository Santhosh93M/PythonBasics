
def check_armstrong(num):
    temp = num
    res = 0

    while int(num)>0:
        rem = int(num)%10
        res += (rem*rem*rem)
        num /= 10
        
    if temp==res:
        return True
    else:
        return False
        
print(__name__)

if __name__=="__main__":
    print(check_armstrong(0))
    print(check_armstrong(153))
    print(check_armstrong(-45))
    print(check_armstrong(111))
    
