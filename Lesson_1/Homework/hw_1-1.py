# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input())

if n >= 1 and n <= 5:
    print(f'- {n} -> этот день является рабочим днем')
elif n >= 6 and n <= 7:
    print(f'- {n} -> этот день является выходным днем')
else:
    print(f'- {n} -> такого дня недели не существует!')