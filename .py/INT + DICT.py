
#Integer, is a whole number, positive or negative, without decimals, of unlimited length.
#int = 5 float = 5.5
#abs(-5) = 5   5//2 = 2  5%2 = 1
#----------------------------------------------------------------------------------------------------------------------------------------------------
#A Python dictionary is an unordered collection of key-value pairs enclosed in curly braces {}, allowing efficient retrieval of values using their associated keys.


dict1 = {"ad" : "congiz" , "yas" : 24}

dict1["ad"] = "Chingiz" # -> Dictde neyise deyismek, yenisini ELAve etmek
dict1["state"] = "Evli"
dict1.update({"ad" : "CHINGIZ" , "boy" : 188})# -> bir nece sheyi birden deyishib Yenisini ELAVE etmek

dict1.__delitem__("yas") # Silmek ucun



dict1.get("soyad") # -> ID olmasa bele error almamaq ucun
dict1.get("soyad" , "Tapilmadi") #  -> 2 ci hisseye tapilmasa ne yazsin onu yaza bilersen
print(dict1)

#dict1.keys() dict1.values() dict1.items() --> Keyler , Deyerler , ve hamsi