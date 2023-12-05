# __iter__() ,  __next__()
#iteratorlar iterable itemleri iterate edir . Amma siz deyende bir addim atir ve harda qaldigini unutmur

reqemler = [1,2,3]
reqemler_iter = reqemler.__iter__() #iterable edir
print(next(reqemler_iter))#1
print(next(reqemler_iter))#2 #kod her ishleyende bir addim atir
print(next(reqemler_iter))#3
#print(next(reqemler_iter)) iteration itdiyi ucun xeta verir

#classlar yaradarken classin iterable olmasi ucun icinde __iter__ ve __next__ i gostermek lazimldi

class Cumle:
    def __init__(self,cumle):
        self.cumle = cumle
        self.index = 0
        self.kelimler = self.cumle.split()
    
    def __iter__(self): #bu standart olaraq yazilirki iterable olsun
        return self
    def __next__(self):
        if self.index >= len(self.kelimler): #next dunderinin en sonucunu gosterdikden sonra dayanmasi ucun bele bir kod yaziriq
            raise StopIteration #sona catdiqda error veririk
        qaytarilacaq = self.index #burda birinci indexi qaytarilacaqa beraber edir sonra indexi artirir belece indiki indexi qaytarmish olur sonra artirir
        self.index += 1
        return self.kelimler[qaytarilacaq]
    
yeni_cumle = Cumle("Salam usaglar xosh gelmisniz")

for kelime in yeni_cumle:
    print(kelime)

