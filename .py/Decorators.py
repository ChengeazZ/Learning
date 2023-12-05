# Decorators source kodu deyishmeden funksiyalari modify ve enhance etmek ucun bir yoldur
def decorator(func):
    def wrapper():
        print("Funksiya bashlamazdan evvel olan sheyler")
        func()
        print("Funksiya bitdikden sonra olan sheyler")
    return wrapper #niye return edirik return edende ne olur?


@decorator
def funksiya():
    print("Funskiya ishledi")

#funksiya()
#---------------------------------------------------------------------------------------------------------------------------------
#@decorator ->  funksiya = decorater(funksiya) . wrapperi sonunda return edende dolayisiyla funksiyani wrappere beraber etmis olursan. Belelikle run etdikde icindeki wrapperin daxili run olmus olur

# 1 asagidaki kodda olanlar 1 decorator funksiya  yaradiriq , icinde wrapper(*args) funksiya yaradiriq sonda wrapperi return edirik
# 2 kvadrat funksiyasi yaradiriq . @decorate edirik @decorate -> kvadrat = decorate(kvadrat)
# 3 decorate altindaki funksiyani run edirik. kodun sonunda return wrapper yazilib deye kvadrat wrapper funksiyasina berbaer olur ve kvadratin argumentleriyle ishleyir
# kvadrat(range(10)) -> decorator2(kvadrat)-> funksiyani oxuyur ve sonda return wrapperi gorur  ->#(@decorate -> kvadrat = decorate(kvadrat olduguna gore) ---->
#---> bele dushune bilersen funskiya wrapperi return eledi ve kvadrat = wrapper oldu . kvadrat(arguments) print edende wrapper(arguments) etmis olursan ve wrapper ishleyir ve neticesi gelir




import time

def decorator2(func):
    def wrapper(*args,**kwargs):
        baslangic = time.time()
        func(*args,**kwargs)
        sonlandi = time.time()
        print (f"{baslangic}-da basladi ve {sonlandi} - da sonlandi. Umumi {sonlandi-baslangic} cekdi")
    return wrapper

@decorator2 #kvadrat = decorator2(kvadrat)
def kvadrat(list1):
    time.sleep(1)
    for i in list1:

        print(i*i)


@decorator2 #kub = decorator2(kub)
def kub(list1):
    time.sleep(2)
    for i in list1:
        return i**3
@decorator2 #toplama = decorator2(toplama)
def toplama(a,b):
    time.sleep(3)
    return a+b

#kvadrat(range(100))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PRACTICE
def vaxtini_hesablayan(func):
    def wrapper(*args):
        a = time.time()
        print(f"Baslangic vaxti {a}")
        cavab = func(*args)
        b = time.time()
        print(f" Bitis vaxti {b}")
        return cavab
    return wrapper


@vaxtini_hesablayan
def kvadratlari_listele(my_list):
    listim = []
    for i in my_list:
        listim.append(i**2)
    return listim

#print(kvadratlari_listele([5,10,12]))




