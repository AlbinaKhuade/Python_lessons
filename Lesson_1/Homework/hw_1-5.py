# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# AB = √(xb - xa)2 + (yb - ya)2
# in
# - 3
# - 6
# - 2
# - 1

import math

print('Введите значения координат x и y точки А:')
xa = int(input('Ax = '))
ya = int(input('Ay = '))

print('Введите значения координат x и y точки B:')
xb = int(input('Bx = '))
yb = int(input('By = '))

dist = math.sqrt((xb - xa)**2 + (yb - ya)**2)
print(round(dist, 2 ))