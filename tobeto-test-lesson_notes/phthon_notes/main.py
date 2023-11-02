#Command + S ile yazdğımız kodu kaydediyoruz ve sağ yukarıda Run Phython File diyeyerek yazdığımız kodu terminalde görebiliyoruz.

print("Merhaba Tobeto Test Ekibi")

#degiskenler
#metinsel => STRING
text = "Merhaba"
print(text)

#numerik => INT, INTEGER - Tam Sayı
studentCount = 45
print(studentCount)

studentCount2 = "50"
#print(studentCode + studentCount2)

#double, decimel, float => ondalık sayı 
averagePoint = 25.5
print(averagePoint)

#boolean => true - false (0,1)
isVerified = True
print(isVerified)

print(type(studentCount))
print(type(studentCount2))
print(type(averagePoint))
print(type(isVerified))

#operatörler 
#matematiksel + - * / %
number = 10

print(number + number)
print(number - number)
print(number * number)
print(number / 2 )
#soldaki sayının sağdaki sayıya bölümünden kalanı verir; mod alma işlemi
print(number % 3) 

#mantıksal (karşılaştrma)

print(number == 10) #true
print(number == 11) #false

print(number != 10) #false
print(number != 11) #true

print(number > 10) #false
print(number >= 10) #true

print(number < 10) #false
print(number <= 10) #true

#string interpolation => metin birleştirme

hello = "merhaba"
userName = "Tuba"

totalText = hello +" "+ userName
print(totalText)

totalText = "{message} Sayın {name}".format(message="Selam", name=userName)
print(totalText)

#f-string
totalText = f"Hoşgeldiniz {userName}"
print(totalText)



