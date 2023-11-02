Not = input("Lütfen notunuzu giriniz.")
#print(type(Not))
#kullanıcıdan aldığım değer string bir şekilde geliyor, tip dönümüşümü yapmam gerekiyor

#NotAsInteger = int(Not)
#print(type(NotAsInteger))


if NotAsInteger > 80 :
    print("Harika, geçtiniz.")
    if NotAsInteger > 90:
        print("Bravo")
#elseif
elif NotAsInteger >50:
    print("Başarılı")
else:
    print("Kaldınız.")




