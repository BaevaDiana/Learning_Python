# 11 ЛР.Задание 5.

permissions = {} #словарь,где храним имена файлов и атрибуты
print("Введите количество файлов в файловой системе:")
n = int(input())
print("Введите файл и режим доступа:")
for _ in range(n):
    s = input().split()
    permissions[s[0]] = set(s[1:])#собираем словарь:ключ - имя файла, значение - право доступа
print("Введите количество файлов в файловой системе:")
m = int(input())
print("Введите файл и операцию над ним:")
for _ in range(m):
    perm,file = input().split()
    if perm == 'read':
        perm = 'R'
    if perm == 'write':
        perm = 'W'
    if perm == 'execute':
        perm = 'X'
    if perm in permissions[file]:
        print('OK')
    else:
        print('Access denied')

