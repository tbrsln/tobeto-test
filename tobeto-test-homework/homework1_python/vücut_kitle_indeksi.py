#Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayan program.

print("Vücut Kitle İndeksi Hesaplama")
print("_________________________________")

#kullanıcıdan boy ve ağırlık değerlerini al 
boy = float(input("Lütfen boyunuzu giriniz. (örn: 170 cm)"))
kilo = int(input("Lütfen kilonuzu giriniz. (örn: 65 kg)"))

#kullanıcıdan alınan değerlerle vki hesapla ve yazdır
vki = (kilo / (boy * boy))
print("Vücut Kitle İndeksiniz : ", vki)

