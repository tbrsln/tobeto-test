#Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteren program.

print("Hangi Zamla Ne Kadar Maaş Alacağınızı Öğrenin")

#mevcut maaş
eskimaas = int(input("Lütfen şuanki maaşınızı giriniz."))

#uygulanacak zam yüzdesi
zamorani = float(input("Lütfen Zam Oranını Giriniz"))

#Zam Hesaplaması 
yeni_maas = eskimaas + (eskimaas * zamorani / 100)
print(f"Yeni Maaşınız: {yeni_maas}")