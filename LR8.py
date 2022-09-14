# 8 ЛР
#Дано действительное положительное число a и целоe число n .
# Вычислите a^n.
# Решение оформите в виде функции power(a, n).Стандартной функцией возведения в степень пользоваться нельзя.

def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n == 0:
        return a
    elif n > 0:
        return res
    else:
        return 1 / res


print('Введите а:')
a = float(input())
print('Введите n:')
n = int(input())
print('a^n =', end=' ')
print(power(a, n))