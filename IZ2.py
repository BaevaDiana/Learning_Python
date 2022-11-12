#Задание 9 Разработать класс «Предметный указатель».
# Каждый компонент указателя содержит слово и номера страниц на которых это слово встречается.
# Количество номеров страниц может достигать 10
# Предусмотреть возможность формирования указателя с клавиатуры и из файла,
# вывода указателя, вывода номеров страниц для заданного слова, удаление элемента из указателя.

class SubjectIndex():
    word = "" #слово
    numberspages = 0 #номера страниц
    newWord = ""
    newNumber = 0
#
    def __init__(self, newWord, newNumber):
        self.word = newWord
        self.numberspages = newNumber
    def setVar(self, newWord, newNumber): #задать слово и номер
        self.word = newWord
        self.numberspages = newNumber

#создать список,в него записать элементы, оттуда удалить и потом выводить


mySubInd = SubjectIndex(" ", 0)
# формирование указателя с клавиатуры
print("Введите количество записей:")
n = int(input())
for i in range(n):
    w1 = input()
    np1 = int(input())
    mySubInd.setVar(w1, np1)





