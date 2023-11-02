#Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program.

print("En Büyük Sayıyı Bul")

#kullanıcıdan 3 sayı al
birinciSayi = int(input("Lütfen 1. Sayıyı Giriniz"))
ikinciSayi = int(input("Lütfen 2. Sayıyı Giriniz"))
ucuncuSayi = int(input("Lütfen 3. Sayıyı Giriniz"))

if(birinciSayi > ikinciSayi):
     if(birinciSayi > ucuncuSayi):
        print("Girilen En Büyük Sayı:", birinciSayi)
     else:
        print("Girilen En Büyük Sayı:", ucuncuSayi)

else:
     if(ikinciSayi > ucuncuSayi):
         print("Girilen En Büyük Sayı:", ikinciSayi)
     else: 
         print("Girilen En Büyük Sayı:", ucuncuSayi)

                   