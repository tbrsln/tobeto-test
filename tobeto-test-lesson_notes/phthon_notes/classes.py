#pyhton nesne tabanlı bir proglama dilidir. 
#fonksiyonlar yerine metodları kullanıyoruz
#değişkenler yerine atributeleri kullanıyoruz.



class Human:
    #property, attribute => nitelik, özellik
    """ name = "irem"
    age = 25 """

    #yapıcı bloklar init şeklinde tanımlanır
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print("yapıcı blok çalıştı")


    #method, davranışlar
    def talk(message):
        print(message)

    def walk():
        print(f"{self.name} is walking")
              
              
#instance üretmek => örnek ürettiğimi belirtiyorum
human1 = Human("şeyma", 25)
# human1.name = "şeyma"
# human1.age = 24
human1.talk("Merhaba")
human1.walk()

