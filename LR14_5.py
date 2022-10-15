import tkinter
from tkinter import filedialog
from tkinter import *
from math import pi

html_template1 = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Текст в формате html</h2>
<p>
"""
html_template2 = """.</p>
</body>
</html>
"""
def calculate():
    if entry1.get().isdigit():
        inp = float(entry1.get())
        try:
            res = (4 * pi * inp ** 3) / 3
            label3.config(text=res)
        except:
            label3.config(text="Ошибка, некорректный ввод!")
    else:
        label3.config(text="Ошибка, внекорректный ввод!")

def saveastxt():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
        window.title('Калькулятор - ' + path + ".txt")
    except:
        return
    with open(path + ".txt", 'w') as f:
        f.write("Результат вычислений = "+str(label3.cget("text")))
        f.close()

def saveashtml():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Html file", "*.html"), ("All files", "*.*"))).name
        window.title('Калькулятор - ' + path + ".html")
    except:
        return
    with open(path + ".html", 'w') as f:
        f.write(html_template1)
        f.write("Результат вычислений = "+str(label3.cget("text")))
        f.write(html_template2)
        f.close()

window = tkinter.Tk()
window.geometry("400x300")
window.title('Калькулятор')

label0 = tkinter.Label(window, text='Программа для вычисления обьема сферы',font=('Coutier', 10, 'bold'))
label0.place(x=10, y=7)

label1 = tkinter.Label(window, text='Введите радиус:', font=('Coutier', 9))
label1.place(x=10, y=45)

entry1 = tkinter.Entry(window, bg='gray')
entry1.place(x=118, y=45, width=100, height=30)

label2 = tkinter.Label(window, text='Результат вычислений:', font=('Coutier', 9))
label2.place(x=10, y=90)

label3 = tkinter.Label(window, bg='gray')
label3.place(x=150, y=90, width=130, height=30)

button1 = tkinter.Button(window, text='Вычислить', bg='gray', command=calculate)
button1.place(x=100, y=130, width=130, height=30)

button2 = tkinter.Button(window, text='Сохранить в .txt', bg='gray', command=saveastxt)
button2.place(x=25, y=170, width=120, height=30)

button3 = tkinter.Button(window, text='Сохранить в .html', bg='gray', command=saveashtml)
button3.place(x=175, y=170, width=120, height=30)

window.mainloop()