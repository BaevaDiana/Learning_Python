# ЛР10.Задание 5.
# В первой строке входных данных записаны числа 𝑁 и 𝑀 – число кубиков у Ани и Бори.
# В следующих 𝑁 строках заданы номера цветов кубиков Ани. В последних 𝑀 строках номера цветов Бори.
# Найдите три множества:
# номера цветов кубиков, которые есть в обоих наборах;
# номера цветов кубиков, которые есть только у Ани и
# номера цветов кубиков, которые есть только у Бори.
# Для каждого из множеств выведите сначала количество элементов в нем, а затем сами элементы, отсортированные по возрастанию.

print("Введите N и M:")
n,m = map(int,input().split())
a = set() #множество для кубиков Ани
b = set() #множество для кубиков Бори

for i in range(n):
    k = int(input("Введите номера цветов кубиков Ани: "))
    a.add(k)

for i in range(m):
    k = int(input("Введите номер цветов кубиков Бори: "))
    b.add(k)

both = set()#множество для кубиков в обоих наборах
bothlist = []
Ann = set() #множество для кубиков Ани
Annlist = []
Borya = set() #множество для кубиков Бори
Boryalist = []

#номера цветов кубиков, которые есть в обоих наборах;
both = a.intersection(b)
for elem in both:
    bothlist.append(elem)
bothlist.sort()

# номера цветов кубиков, которые есть только у Ани
Ann = a.difference(b)
for elem in Ann:
    Annlist.append(elem)
Annlist.sort()

# номера цветов кубиков, которые есть только у Бори.
Borya = b.difference(a)
for elem in Borya:
    Boryalist.append(elem)
Boryalist.sort()

n1 = len(both)
print("Количество номеров цветов кубиков,которые есть в общих наборах = ",n1)
for elem in bothlist:
    print(elem)

n2 = len(Ann)
print("Количество номеров цветов кубиков,которые есть только у Ани = ",n2)
for elem in Annlist:
    print(elem)

n3 = len(Borya)
print("Количество номеров цветов кубиков,которые есть только у Бори = ",n3)
for elem in Boryalist:
    print(elem)