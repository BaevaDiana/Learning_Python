# 13 ЛР

#Задание 1.
class Cat():#класс
    #атрибуты
    name = ""
    colour = ""
    weight = 0
    def meow(self):#метод "мяуканье"
        print(self.name,"видит меня и говорит: Mяу,мяу,мяу!")

myCat = Cat()
myCat.name = "Парамон"
myCat.weight = 5
myCat.meow()


