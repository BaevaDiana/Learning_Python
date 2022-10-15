import tkinter
from tkinter import filedialog
from tkinter import *

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

def save_as1():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
        window.title('Editor ' + path + ".txt")
    except:
        return
    with open(path + ".txt", 'w') as f:
        f.write(entry.get())
        f.close()

def save_as2():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Html file", "*.html"), ("All files", "*.*"))).name
        window.title('Notepad - ' + path + ".html")
    except:
        return
    with open(path + ".html", 'w') as f:
        f.write(html_template1)
        f.write(entry.get())
        f.write(html_template2)
        f.close()


window = tkinter.Tk()
window.geometry("400x300")
window.title("Editor")
label1 = tkinter.Label(window, text='Введите текст:')
label1.pack()
entry = tkinter.Entry(window,width=60)
entry.pack()
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=2)
filemenu.add_command(label="Save as .txt",  command=save_as1, font=('Courier', 12))
filemenu.add_command(label="Save as .html", command=save_as2, font=('Courier', 12))
filemenu.add_separator()
menubar.add_cascade(label="Файл", menu=filemenu)
window.config(menu=menubar)
window.mainloop()