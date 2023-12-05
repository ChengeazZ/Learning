list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
def kvadrat(x):
    return x*x
def kub(x):
    return x**3

def map_func(func,listi):#funksiya icine funksiya gonderdik , funksiuyani run etmeden cagiramq ucun sonuna () yazmiriq
    netice = []
    for i in listi:
        netice.append(func(i))
    return netice

print(map_func(kvadrat,list1))
