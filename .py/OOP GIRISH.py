#OOP Object Oriented Programming
#Class sinif, Instance Classin attributelarini alan bir uzvdur

class Ishciler:
        ishci_sayi = 0
        vergi_faizi = 1.1
        def __init__(self,ad="Yoxdur",soyad="Yoxdur",yas="bilinmir",maash="gosterilmir"):
                self.ad = ad  
                self.soyad = soyad
                self.yas = yas
                self.maash = maash
                self.mail = self.ad + self.soyad + "@shirketadi.com"
                Ishciler.ishci_sayi += 1
        def melumatlar(self):
                return f"Adi: {self.ad}, Soyadi: {self.soyad}, Yasi: {self.yas}, Maashi: {self.maash}, Emaili: {self.mail}"
                
                


ishci1 = Ishciler("Cingiz","Aliyev",19)
ishci2 = Ishciler("Eli","Veli",29)
ishci3 = Ishciler("Pirveli", maash=2000)

print(Ishciler.ishci_sayi)
print(ishci2.melumatlar())
print(ishci3.melumatlar())