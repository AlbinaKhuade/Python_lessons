# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

def sum_number (amount):
    num_list = sample(range(1, (amount+1)*2), k=amount)
    print(num_list)
    new_list = []
    for i in range(amount//2):
        new_list.append(num_list[i]*num_list[amount-1-i])

    if amount % 2 != 0:
        new_list.append(num_list[amount//2])
    print(new_list)

    

sum_number(int(input('Введите количество чисел: ')))