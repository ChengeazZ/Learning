#import modulename -> butun fubkisyalar gelir ama modulname.func() la cagirmalisan
#from modulename import funcname -> yalniz func gelir  func() la cagirirsan
#from modulename import *  butun funclar gelir func() la cagirirsan
#import modulname as new_name     new_name.func() la cagirirsan

#                                                     TIME MODULE
import time
def hecne():
    a = time.time()
    time.sleep(1)
    b = time.time()
    print(f"baslangic {a}, son {b}, ferq {b-a}") #a= time.time() b=time.time() a-b zaman ferqi
hecne()
print(time.ctime)
print(time.strftime("%d:%m:%y"))
#                                                     RANDOM MODULE
import random
random.random() #-> 0 la 1 arasinda bir eded verir

random.uniform(f,C) #-> floor la cieling arasinda bir reqem verir float

random.randint(f,C) #-> f la c arasinda bir integer verir

random.randrange(f,c,step) #f la c arasinda steplerle eded verir

random.choice(list1) # listden random bir item verir

random.shuffle(list1) # shuffles

random.sample(list,3) # sayili item secir tekrar secmir
