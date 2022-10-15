import tkinter
import random
from tkinter import *

def randomword():#генерация случайного слова
    global rus, eng
    rus, eng = random.choice(list(dictionary.items()))
    label2.config(text=rus)

def checkword():#проверка сгенерированного и введенного слова
    global k
    var = entry1.get()
    if label2.cget("text") != "":
        if var.isalpha():
            if k != 0:
                if var == dictionary[rus]:
                    label5.config(text="Верно!")
                    k = 5
                else:
                    label5.config(text="Не верно! Осталось попыток: " + str(k))
                    k -= 1
            else:
                label5.config(text="Не верно! Попыток не осталось! Сгенерируйте новое слово")
                randomword()
                k = 5
        else:
            label5.config(text="Ошибка ввода! Введите слово заново!")
    else:
        label5.config(text="Вы не сгенерировали слово!")

window = tkinter.Tk()
window.geometry('500x300')
window.title("Угадываем слова!")

dictionary = {"кот": "cat",
              "программист": "programmer",
              "питон": "python",
              "язык программирования": "programming language",
              "жук": "bug",
              "пары": "class",
              "курсовая": "course work",
              "каппибара": "capybara",
              "Диана": "Diana",
              "гитхаб": "guthub",
              }

k = 5
rus = ""
eng = ""

label1 = tkinter.Label(window, text='Случайное слово:')
label1.place(x=15, y=8, width=100, height=50)

label2 = tkinter.Label(width=30, borderwidth=2, relief="solid")
label2.place(x=150, y=10, width=200, height=30)

button1 = Button(text="Сгенерировать", font=('Coutier', 9, 'bold italic'), command=randomword)
button1.place(x=175, y=50, width=150, height=30)

label3 = tkinter.Label(window, text="Введите слово:")
label3.place(x=9, y=70, width=100, height=50)

entry1 = tkinter.Entry(width=30, borderwidth=2, relief="solid")
entry1.place(x=155, y=85, width=200, height=30)

button2 = Button(text="Проверка", font=('Coutier', 9, 'bold italic'), command=checkword)
button2.place(x=175, y=125, width=150, height=30)

label5 = Label(width=60, height=3, borderwidth=2, relief="solid")
label5.place(x=30, y=165, width=450, height=40)

window.mainloop()