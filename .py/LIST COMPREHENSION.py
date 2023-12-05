#List comprehension avtomatik list yaratmaq ucun istifade olunur.
#Bunun ucun ilk hisseye olunacaq prosses orataya for ve argument sona ise shert yazilir
list1 = [1,2,3,4,5]

print([i*i for i in list1]) #birinci prosses yeni kvadrat, ikinci for i ve in arguemt
print([i*i for i in list1 if i%2==0]) #ve sonda shert

list_reqemler = [1,2,3,4]
list_herfler =["a","b","c","d"]

print([(a,b) for a in list_reqemler for b in list_herfler])

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,3,5,7,9]

list3 = [i*i for i in list1 if not i in list2]
print(list3)