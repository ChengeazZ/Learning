class Insan:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    @property #aciqlamasi asagidaki birinci aciqlama
    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"    
    @property
    def adsoyad(self):
        return self.ad+ " "+self.soyad
    @adsoyad.setter #bu decoratorla funksiyani deyishe bilirsen. meselen asagida insan1.adsoyad = "eldar" nomralda funskiyani beraber etmek olmazdi ama bununla edib her seyi deyismek olur
    def adsoyad(self,name):
        ad,soyad = name.split(" ")
        self.ad = ad
        self.soyad = soyad
    

insan1 = Insan("cingiz","aliyev")

print(insan1.ad)
#print(insan1.email()) email Class daxili method oldugu ucun onu cagiran zaman funskiya ishe dushsun deye sonun () yazmaq lazim olur , amma @property Decoratoruyla onsuz ishletmek olur
print(insan1.email)
print(insan1.adsoyad)

insan1.adsoyad = "Eldar Mustafayev"
print(insan1.adsoyad)
