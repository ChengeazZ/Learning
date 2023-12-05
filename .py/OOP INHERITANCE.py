#Inhertiance xusisiyettini oturmek, alt classdan ustekileri goturmek ucun super().__init__(gotureceyi,argumentler)

class Ishciler:
        vergi_faizi = 1.1
        def __init__(self,ad,soyad,maas):
                self.ad = ad
                self.soyad = soyad
                self.maas = maas
                self.mail = self.ad + self.soyad +"@shirket.com"
        def info_goster(self):
                return f"Adi: {self.ad}, Soyad: {self.soyad} , mail: {self.mail}"
class Developerler(Ishciler):
        vergi_faizi = 1.2
        def __init__(self,ad,soyad,maas,bildiyi_dil):
                super().__init__(ad,soyad,maas)
                self.bildiyi_dil = bildiyi_dil
                self.mail = self.ad + self.soyad +"@shirket.com"

class Mudurler(Ishciler):
        vergi_faizi = 2
        
        def __init__(self,ad,soyad,maas):
                super().__init__(ad,soyad,maas)
                self.ishcileri = []
        def ishci_elave_et (self,ishci):
                self.ishcileri.append(ishci)
        def ishcileri_goster(self):
                for i in self.ishcileri:
                        print(i.info_goster())

ishci1 = Ishciler("Eli","Veli",1000)
developer1 = Developerler("Cingiz","Aliyev","5000","Pyhton")
mudur1 = Mudurler("Eldar","Mustafaev",20000)

mudur1.ishci_elave_et(ishci1)
mudur1.ishci_elave_et(developer1)
mudur1.ishcileri_goster()


        
        

                
                

