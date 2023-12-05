#Generatorlar yield funksiyasiyla ishleyen ve esas meqsedi memory efficient olmaq olan funksiyalardi. Normalda bir liste bir hesablama edende ve icindeki bir sheyi 
# goturende python birinci listdeki butun hesablamalari bitirir ve sonda neticeden istediyini verir.
#Amma generator sadece hemin an qaytardiqi deyeri tutur , novbetiye kecende evvelkini silir/unudur

def kokalti(liste):
    for i in liste:
        yield i**0.5

list1 = kokalti([1,2,3,4])

# print(list1)
# print(next(list1)) # her seyi birden yaddan saxlamadigi ucun icindekileri baxmawq ucun ya forla ya da nextle baxmalisanS
# print(next(list1))
print("----------------------")
for i in list1:
    print(i) #ilk baxishda eyni gorunsede ishleyish prinsipi ferqlidi ve memory efficentdi. Output etmek ucun hamisini hesablayib axirda etmedi, etdikce gonderdi
