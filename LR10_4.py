# ЛР10
#Задание 4.Встречалось ли число раньше.
#Во входной строке записана последовательность чисел через пробел.
#Для каждого числа выведите слово YES(в отдельной строке),если это число ранее встречалось в последовательности или NO, если не встречалось.

#a = []
a = list(map(int, input().split()))
s = set()
for i in range(len(a)):
    if a[i] in s:
        print('YES')
    else:
        s.add(a[i])
        print('NO')
