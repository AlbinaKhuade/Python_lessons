# 3. На вход программе подается число n.
#    Программа печатает численный треугольник.
#    Используем вложенные циклы.

n = int(input('Введите число: '))

for i in range(1, n + 1):
    for k in range(i):
        print(i, end='')
    print()