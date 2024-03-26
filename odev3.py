class Personel():
    def __init__(self, adi, departmani, calisma_yili, maas):
        self.adi = adi
        self.departmani = departmani
        self.calisma_yili = calisma_yili
        self.maas = maas

class Firma():
    def __init__(self,adi,personel_listesi=[]):
        self.adi=adi
        self.personel_listesi= personel_listesi

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print("adı:",personel.adi)
            print("Departmanı:", personel.departmani)
            print("Çalışma Yılı:", personel.calisma_yili)
            print("Maaşı:", personel.maas)
            print("\n")

    def maas_zammı(self,personel, zam_oranı):
        personel.maas += personel.maas * zam_oranı / 100

    def personel_cikart(self,personel):
        self.personel_listesi.remove(personel)

personel1 = Personel("Ahmet", "Muhasebe", 5, 5000)
personel2 = Personel("Ayşe", "İnsan Kaynakları", 3, 4500)


firma = Firma("ABC Şirketi", [personel1, personel2])
firma.personel_listele()


yeni_personel = Personel("Mehmet", "Satış", 2, 4800)
firma.personel_ekle(yeni_personel)

firma.personel_cikart(personel2)


