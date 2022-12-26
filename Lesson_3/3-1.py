# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

from random import sample

def find_number (amount, user_number):
    new_list = sample(range(1, (amount+1)*2), k=amount)
    print(new_list)
    if user_number in new_list:
        return 'ДА'
    return 'НЕТ'

result = find_number(int(input('Введите количество: ')),
                     int(input('Введите число: ')))

print(result)
