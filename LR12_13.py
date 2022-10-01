# 11 ЛР. Задание 13.

def get_key(dict,value):
    for key,values in dict.items():
        if value in values:
            return key

file = open("elements.txt","r")
inf = file.readlines()
elements = {}
for elem in inf:
    elem = elem.rstrip().split(',')
    elements[elem[0]] = {elem[1], elem[2]}

print("Введите число протонов,обозначение или название химического элемента:")
line = input()
while line != "":
    try:
        if line.isdecimal():
            print(elements[line])
        elif not line.isdigit():
            if get_key(elements,line) != None:
                print(get_key(elements,line))
            else:
                raise KeyError
        print("Введите число протонов,обозначение или название химического элемента:")
        line = input()
    except KeyError:
        print("Такого элемента не существует! ")
        print("Введите число протонов,обозначение или название химического элемента:")
        line = input()






