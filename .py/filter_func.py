#Filter funksiyasi map kimi bir funksiya ve list alir , ve teyinata uygun olaraq yeni bir list yaradir. Filtri True Flasa esasen edir
list1 = [1,2,3,4,5,6,7,8,9,10]

def cutler(x):
    if x % 2 ==0:
        return True
    return False
    
list2 = filter(cutler,list1)
print(list(list2))#filterda map kimi filter objecti qaytarir. liste, tuple ve s cevirmek lazimdi
#_---------------------------------------------------------------------------------------------------------------
list3 = [1,2,3,4,5,6,7,8,9,10,15,20]

list4 = filter(lambda x : x>=10 and x<100,list3) # burada lambda dan True False qayidir
print(list(list4))

