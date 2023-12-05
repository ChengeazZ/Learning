# Classlarin instanclerini bir birine vurmaq bolmek ve s isteye bilerik. Bunun nece bash vermesini pythona dunder ethodlarla izah edirik
# object.__add__(self,other) meselen int.__add__(3,5) 

class reqemler(int): #int classindan inheritence yeni int classinin xusisiyetlerinden biri olan toplamani miras alib istifade etdik
    def __init__(self,eded):
        self.eded = eded

reqem1 = reqemler(10)
reqem2 = reqemler(20)
print(reqem2+reqem1)
#---------------------------------------------------------------------------------------------------------------------------------
#Bu int clasinin normal toplamasi idi. Ozunuze uygun riyazi hereket mumkundu
# Asagidaki kodda listleri ard arda yoxda her siradakini bir biriyle toplayacaq kod yazaciq. Eger listdeki item sayi eynideyilse
#toplamayacaq ve bir string return edecek

class TezeListim(list): #burda listi inherit etmeyimizin sebebi listin funksiyalraini getirmek ve ozumuze uygunlasdirmagdi
    def __add__(self,other): #Toplama
        if len(self) != len(other):
            return "List daxili sayi eyni deyil"
        else:
            result = TezeListim() # TezeListim() list inherit etdiyine gore resul =[] kimi olur
            for i in range(len(self)):
                result.append(self[i]+other[i])
        return result
    def __sub__(self,other): #cixma
        result = TezeListim()
        for i in range(len(self)):
            result.append(self[i]-other[i])
        return result
    def __eq__(self,other): #beraberlik isharesi
        
        if sum(self) == sum(other):
            return "Listlerin Toplami Beraberdi"
        else:
            return "Listlerin Toplami Beraber Deyil"
    def __abs__ (self):
        result1 = TezeListim()
        for i in self:
            if i<0:
                result1.append(i*-1)
            else:
                result1.append(i)
        
        return result1

        

list1 = TezeListim([-1,2,3])
list2 = TezeListim([2,-3,3])
print(abs(list2))
# print(list1==list2)
#-------------------------------------------------------------------------------------------------------------------------------

class Futbolcu:
    def __init__(self,ad,soyad,rating):
        self.ad = ad
        self.soyad = soyad
        self.rating = rating
    def __lt__ (self,other):
        if self.rating < other.rating:
            return f"Oyuncu {other.ad} oyuncu {self.ad} dan daha gucludur"
        
        
messi = Futbolcu("MEssi","Leo",97)
ronaldo = Futbolcu("Ronaldo","Cristiano",98)

print(messi<ronaldo)





