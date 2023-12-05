def goster():
    print(x)
x = 8

#goster() #funksiya cagirlmamisdan evvel funksiyannin argumentleri (bu misalda x) tanitilmish olmalidi

#-----------------------------------------------------------------------------------------------------------

def func():
    #a = "local" #eger funksiya daxilinde yeni localda tapa bilmezse , globalda axtarir
    print(a)

a = "global"

#print(a)
#func()
#--------------------------------------------------------------------------------------------------
#eger ic ice funksiyalar varsa en ic funksiyadaki variable local , bir ust funskiyadaki enclosing , ve umumideki global olur

ax = "global"

def funksiya():
    ax = "enclosing"
    print(ax)
    def icerideki_funksiya():
        ax = "local"  #eger localda olmasa birinci gedib enclosingde baxacaq , eger ordada yoxdusa globala baxacaq
        print(ax)
    icerideki_funksiya()

#print(ax)
#funksiya()
#_-----------------------------------------------------------------------------------------------------------------
#eger her hansi bir yerde globalda oldan variable i cagirmaq istesen global variable_name ede bilersen. Localdan bir ustdekini isteyirsense nonlocal variable_name

xx = "global"

def funcc():
    global xx
    print(xx)

def funcc():
    xx = "enclosing"
    print(xx)
    def local_func():
        nonlocal xx
        print(xx)
    local_func()


        