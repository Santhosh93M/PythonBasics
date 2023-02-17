import random

def random_nums():
    l = []

    for i in range(10):
        l.append(random.randint(1,20))

    return l
print(random_nums())
