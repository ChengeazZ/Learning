#__str__ ve __repr__ Classlarimizin instanclerini insanlarin oxuya bilceyi sekilde print etmek ucun istifade edirik
# __str__ istifadecinin oxuya bilmesi ucun print edir print(str("salam")) -> salam , print(str(datetime.datetime.today())) -> 2023-09-09
# __repr__ dveloperin oxuya bilmesi ucun print edir print(repr("salam")) -> "salam", print(repr(datetime.datetime.today())) -> datetime.datetime(2023, 9, 9) print olunmush kodu gosterir
# Class icinde hem __str__ hem __repr__ funksiyasi varsa Python hemsihe birinci __str__ ni oxuyacaq ve __repr__ ni oxumayacaq
# Eger ikisinde yazmisansa onda print(repr(futbolcu1)) ve ya futbolcu1.__repr__
# import datetime
# print(repr(datetime.datetime.today()))
#-------------------------------------------------------------------------------------------------------------------------

class Futbolcu:
    def __init__(self,ad,soyad,yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
    def __str__(self):
        return f"Oyuncunun adi: {self.ad}, Soyadi: {self.soyad}, Yasi: {self.yas}"
    def __repr__(self):
        return f'Futbolcu("{self.ad}","{self.soyad}",{self.yas})'
       
futbolcu1 = Futbolcu("Ronaldo","Cristiano",38)
print(futbolcu1)
print(repr(futbolcu1))

