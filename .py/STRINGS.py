# A string is a data structure in Python that represents a sequence of characters.
# Sətir Python-da simvollar ardıcıllığını təmsil edən məlumat strukturudur.
# "\n" -New Line ;   "\t"  -Tab ;  """   """ -Expantion Line

ad_soyad = "Chingiz"+ " " + "Aliyev"
#print(ad_soyad[0:6:2]) #-> "Cig"  beginning:ending:step_size
cumle = "MyXLifeXMyXRules"
list_cumle = cumle.split("X") #argumentine esasen bolub list edir STR -> LIST
print(list_cumle)
string_cumle = " ".join(list_cumle) # LIST -> STR
print(string_cumle)
#print("Ad: {} , Soyad: {}".format(string1,"Aliyev") -> "Ad: cingiz , Soyad: Aliyev"
# print(f" Ad: {string1}") = "Ad: cingiz"
# string1.capitalize() = "Cingiz"
# string1.upper() = "CINGIZ"
# string1.lower() = "cingiz"
# string1.startswith("Cin") -> False ("cin") -> True
# string1.endswith("giz") -> True
#Stringi liste cevirmek ucun -> import textwrap . textwrap.wrap(string,width)  -> (Width slice larin boyukluyudu eger boyuk reqem yazsan butov olaraq goturub list edecek)
# import textwrap -> textwrap.fill(string,width) -> ksoklara bolub print edir
# string_name.strip() -> default stringin her iki bashindan spacebarlari silir. string_name.strip("!") ->nidalari silecek