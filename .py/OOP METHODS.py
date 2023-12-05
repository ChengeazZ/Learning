# 3 MEthod var default Instance MEthod , @classmethod ve @staticmethod

class Insan:
    def __init__(self,ad,yas):
        self.ad = ad
        self.yas = yas
        
    def info_ver(self): #instance method
        return f"Ad: {self.ad}, yas:{self.yas}"
    
    @classmethod #classmethod bu numunede ad,yas gelmeli oldugu halda "ad-yas" gelse nece ederik 
    def stringden_cevir(cls,abc):
        ad,yas = abc.split("-")
        return cls(ad,yas)
    
    @staticmethod # static method digerlerinden(CLASS,  INSTANCE) elaqesiz methoddu
    def hecne():
        return "hecne"
    
insan1 = Insan("Cingiz",24)
print(insan1.info_ver())
insan2 = Insan.stringden_cevir("Eldar-24")
print(insan2.info_ver())

