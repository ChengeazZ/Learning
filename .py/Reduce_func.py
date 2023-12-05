# reduce funksiyasinin ish prinsipi map ve filtere benzeyir , argument olaraq funksiya ve list alir amma sadece tek bir shey qaytarir. 
# ish prossesi bele olur: funksiya nedirse listdeki ilk iki iteme onu edir alinan cavabi sonrakiyla edir ve bele bele devam edir
# reduce u import etmek lazimdi

from functools import reduce

def vurma(x,y):
    return x*y

list1 = [2,4,6,9]
list2 = reduce(vurma,list1) # Bash veren: listde 2 ve 4 u funksiyaya saldi etdi 8, sonra 8 ve 6 eledi 48 sonra 48 ve 9 u saldi funksiyaya ve 432
#print(list2)
#--------------------------------------------------------------------------------------------------------------------------------------------------
#Pyhtonda ebob var ama ekob yoxdu. ekobu tapmaq ucun bu funskiyadan istifade edek
from math import gcd #(ebob)

def ekob(a,b):
    return int(a*b/gcd(a,b))

ekoblar= reduce(ekob,list1)
print(ekoblar)
