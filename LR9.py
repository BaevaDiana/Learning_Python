# 9 ЛР
#  Даны два числа n и m.
#  Создайте двумерный массив размером n×m и заполните его символами «.» и «*» в шахматном порядке.
#  В левом верхнем углу должна стоять точка.

print('Введите n:')
n = int(input())
print('Введите m:')
m = int(input())
a=[[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if (i+j)%2==0:
            a[i][j]='.'
        else:
            a[i][j]='*'

for i in range(n):
    for j in range(m):
        print(a[i][j],' ',end = '')
    print()


