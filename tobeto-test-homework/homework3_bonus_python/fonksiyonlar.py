#bir işlemi tekrar tekrar yazmak yerine onu bir kez yapıp defalarca kullanmak için kullanılır

def kredileriListele(): 
    krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi" ]
    for kredi in krediler:
     print("<option"+kredi+"<option")
#şu an çalışmadı çünkü sadece tanım yaptık

kredileriListele() #yukarda yazdığım def i çağırdım
kredileriListele()
kredileriListele()



""" print("ikinci sayfa")
krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi" ]

for kredi in krediler:
    print("<option"+kredi+"<option")



print("üçüncü sayfa")
krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi" ]

for kredi in krediler:
    print("<option"+kredi+"<option")
 """ #bunu böyle yazmak yerine def tanımlayacağım ilk başa
