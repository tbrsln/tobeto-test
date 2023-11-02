#kullanıcıdan alınan sayının palindrom olup olmadığını bulan bir program
#palindromik sayı: iki taraftan da okunduğunda değişmeyen sayılar örn: 232, 414, 151
#bir sayının palindrom olup olmadığını kontrol etmek için sayıyı stringe çevirip ters çevrilmiş haliyle karşılaştırıyoruz. 
#eğer iki hali eşitse sayı palindromdur.

print("Girdiğin Sayı Palindrom Mu?")

def is_palindrome(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    return number_str == reversed_str

#kullanıcıdan bir sayı al
sayi = int(input("Bir Sayı Giriniz:"))

if is_palindrome(sayi):
    print("Bu Sayı Bir Palindrom Sayıdır")
else:
    print("Bu Sayı Palindrom Bir Sayı Değildir.")

