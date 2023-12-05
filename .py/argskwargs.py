# *args(Tuple)-argumnets **kwargs {Dictionary} - KeyWordArguments
#args
def quvveti(x,y): #Positional arguments - Yeni siraya uygun argumentler ilk yazilan x ,ikinci y olacaq
    return x**y
# quvveti(5) yazsaq xeta verecek cunki mutleq iki positional argument yazmalisan ne az ne cox 
#----------------------------------------------------------------------------------------------------------
def melumat(ad = "Yoxdur",soyad="Yoxdur",yas = "Yoxdur"):# ad="Yoxdur" #KeywordArgument
    return f" Adi: {ad}, Soyadi: {soyad}, Yasi: {yas}"

# print(melumat())
# print(melumat("Cingiz",yas=24))
#----------------------------------------------------------------------------------------------------------
def goster(*args): #args yazdiqdan sonra data typeindan asili olmayaraq istediyin qeder argument elave ede bilersen, *args onlari yigib tuple-da birlshdiecek
    print(args)
#goster(1,2,"a","b",True) #yeni *argsi ne qeder argumentin olacagini bilmeyende ve ya cox sayida olanda istifade edirsen ve args tuple etdiyine gore itirable dir
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def vurma(*args):
    cavab = 1
    for i in args:
        cavab *= i
    return cavab

#print(vurma(1,2,3,5))

def ortalamasi(*args):
    return sum(args)/len(args)

#print(ortalamasi(1,2,3,4,10))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#**kwargs 

def haqqinda(**kwargs):
    for i in kwargs:
        print(kwargs[i])
    print(kwargs)
    print(type(kwargs))

haqqinda(ad = "Cingiz", soyad = "Aliyev")

