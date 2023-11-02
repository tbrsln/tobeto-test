#birbirine benzeyen işleri tekrar ettirmek için kullandığımız yapılar

krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi" ]

for x in krediler: #for bir döngü türü #in krediler demek; biz neyin içinde gezeceğimizi gösterir
    print(x)  #alias 'takma ad' x ya da başka bişey de yazabiliriz, o an neyde gezdiğimizi gösterir sadece


for i in range(10): #10 kez tekrarlanacak döngü (range içine yazdığınız değere kadar)
    print(i)

for i in range(len(krediler)): #i 0dan başlıyor
    print(krediler[i])

for i in range(3,10): #saymaya 3ten başla diyorum, 3 dahil 10 dahil değil
    print(i)

    for i in range(0,10,2): #3 elemanlı kullanım: 0 dan başla 10(10 dahil değil)a kadar 2şer artırarak yazdır
        print(i) 

