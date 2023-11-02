#dont repeat yourself 
#döngüler

#FOR 

#start : başlangıç döngümüzün başlangıcı (0)
#stop : döngümüzün biteceği değeri belirler
#step : artış miktarı (1) 
""" 
# biggestValue = 0
# for i in range(0,11,1): #0dan başlayıp 10a kadar devam eden rakamları görürüz
#      print(i)


# for i in range(5):
#      sayi = int(input(f"{i+1}. sayıyı giriniz.")) 
#                       #başındaki f pyhton değişkenlerine ulaşmamızı sağlıyor
#     if sayi > biggestValue:
#         biggestValue = sayi
# print(f"Girdiğiniz sayılar arasında en büyük olanı: {biggestValue}")

 """

""" forRangeMin = int(input("Döngünün alt limitini belirleyiniz: "))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz: "))


for i in range(forRangeMin, forRangeMax+1):
     if i % 2 == 0:
          #2ye bölümünden kalan o sa çift sayı
          print(i) """

""" sayilar = []

for i in range(3):
    sayilar.append(int(input(f"{i+1}. sayiyi giriniz.")))

    print(sayilar)
    
 #defaultu küçükten büyüğe doğru sıralar
    sayilar.sort()
    print(sayilar)
#tam tersi büyükten küçüğe sıralamak için 
    sayilar.sort(reverse=True)
    print(sayilar)

 """
ogrenciler = ["Güneş", "Recep", "Betül", "Yunus", "İrem"]
#lengt öğrenciler dizininin uzunluğunu verir
""" print(len(ogrenciler))

for i in range(len(ogrenciler)):
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}) """
          

"""  fori in ogrenciler: 
          print                    
          terarla yanlış yazdın """

#ilgili döngünün o anda kırılmasını sağlıyor: break
for i in range(len(ogrenciler)):
    if i>3:
        break
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}")

#contine : iterasyondaki current değeri atla, bir sonraki değer ile devam et
for ogrenci in ogrenciler:
    if ogrenci == "Recep":
        continue
    print(f"Öğrenci: {ogrenci}")

#WHILE 

i = 0 
while i < 10:
    print("Merhaba") #sonsus döngüye girer sadece burda bırakırsak
    i += 1  #10 kez yazar

    

