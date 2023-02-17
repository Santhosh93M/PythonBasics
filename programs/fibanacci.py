
def fibanacci(num):
    if num<0:
        return 0
    elif num==1 or num==2:
        return 1
    else:
        return fibanacci(num-1)+fibanacci(num-2)
    

print(fibanacci(8))

