#A list is a data structure in Python that is a changeable and ordered sequence of elements.
#Siyahı Python-da elementlərin dəyişkən və nizamlı ardıcıllığı olan məlumat strukturudur.

listim = ["a1","a2"]

listim.append("a3") #-> ["a1","a2","a3"] En sona elave edir

listim.insert(0,"a0.5")# -> ["a0.5","a1","a2","a3"] Istediyin indexe elave edir

listim.remove("a0.5") #-> ["a1","a2","a3"] Spesifik itemi silir

listim.pop() #-> ["a1","a2"] -> Listde en sonuncu itemi silir

listim.reverse()# -> ["a2","a1"] - Ters cevirir

listim.extend(listim2)# -> listleri birlesdirib tek list etmek ucun

listim.sort()# -> kicikden boyuye, alfabetik siralayir

sorted(listim)# -> Siralayir amma original listi deyismir

min(listim) , max(listim)# -> listdeki en kicik ve en boyuk

list(enumerate(listim))# -> [(1 , "a2"), (2, "a1")] Nomreleyir
