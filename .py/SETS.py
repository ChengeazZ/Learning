#                                             SETS

#A Python set is an UNORDERED collection of unique elements enclosed in curly braces {} that Eliminates Duplicates from the data.


#                                           SOME FUNCS AND METHODS
set1=set([1,2,3,4])
set2 = set([3,4,5,6])
set1.update([10,11]) #bir neche shey elave etmek ucun or | as union

set1.add("bir")

set1.remove("bir")
print(set1)
set1.discard("bir") #buda remove edir amma item orda yoxdursa error vermir
#umumen sonlarina _update yazilmish variantlari seti deyishir ve funksiya daki kimi olur
set1.intersection(set2) #-> iki setdeki ortaq itemleri gosterir .intersection() = & -> set1&set2
#intersection_update edende listi ortaq olanlara cevirir
set1.difference(set2) # -> birinci setde olub ,ikide olmayanlar .difference() = - -> set1-set2

set1.union(set2) #-> iki seti birlesdirir .union = | -> set1|set2

set1.symmetric_difference(set2) #-> iki setin ortaq olmayanlarini gosterir  -> ^  -> set1^set2