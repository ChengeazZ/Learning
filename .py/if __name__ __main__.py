# if __name__ == "__main__":
# __name__ methodu hal hazirda ishlediyiniz .py filein adini qaytarmalidi , amma Python bu adi __main__ olaraq qaytarir
print(__name__)
#Eger .py modulunun icine diger bir modulunu import etmisense , run etdiyin moduleun adi hemise __main__ olacag , diger modulun adi ise , adi nedirse o olacaq 

# Burdaki butun meqsed if __name__ == "__main__" sherti qoyaraq sadece biz run etdiyim fayldaki funksiyalarini ishletmekdi cunki yalniz run etddiyimizin adi __main__ olur
#import edtiyimizdekileri onsuz imported.funskiaadi() ile isteyende cagira bilirik

def funksiya1():
    print("Bu fayli run etdiyimiz ucun adi main oldu ve run etdi")


if __name__ == "__main__":
    funksiya1()