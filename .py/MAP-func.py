#map bizden argument olaraq bir funksiya ve bir list alir,sonra listdeki itemleri bir bir o funksiyaya salir ve cavablardan yeni bir list yaradir ve for istifade etmeden daha qisa kod olur
#meselen  bu funksiyasiz listin kvadratlarindan yeni list yaratamaq istesek..
def kvdrt(X): #bu bizim kvadrat eden funksiyamiz iki metodlada baxaq
    return X*X
# mapsiz
list1 = [ 1,2,3,4]
list2 =[]
for i in list1:
    list2.append(kvdrt(i))
#print(list2)
#mapla
list3 = map(kvdrt,list1)
print(list3) #-> Outputdan gorduyunuz kimi bir map objecti qaytarir onu list tuple set ve s ede bilersiz
print(list(list3))

#lambdayla ishlederek dahada qisaltmaq olar
list4 = map(lambda x : x*x,list1)
print(list(list4)) 
#--------------------------------------------------------------------------------------------------------------
#map funksiyadan elave birden cox argument ala bilir. asagidaki listleri indexe uygun toplamaqda istifade edek
list5= [1,2,3,4]
list6=[9,8,7,6]

def toplam(x,y):
    return x+y

print(list(map(toplam,list5,list6)))
#eger list3 olsa ve onun icindeki elemntlrn sayi digerlerinden az olsa error vermeyecek cunki map() uzunlugu icinde en az element olana gore goturur
