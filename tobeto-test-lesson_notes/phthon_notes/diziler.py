sayilar = [100,200,300,400, "merhaba"] #içindekilerin hepsinin integer tipinde olması gerekmez
#programlar saymaya 0dan başlar. 
print (sayilar[0])
print(sayilar) #sıfırıncı sayı olan 100 ü yazdırır

#noktaya basınca fonksiyonlar listelenir

sayilar.append(500) #listenin sonuna eleman ekler
print(sayilar)


sayilar.pop() #default (boş oluşu) son indexi siler
print(sayilar)

sayilar.pop(2) #indexe göre siler
print(sayilar)


sayilar.remove(100) #değere göre siler
print(sayilar)



sayilar.extend([10, 20, 30]) #appendin aksine çoklu veri ekler
print(sayilar)

sayilar.clear()
print(sayilar)

sayilar.