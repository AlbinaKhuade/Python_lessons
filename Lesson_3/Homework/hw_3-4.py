# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform, sample

def diff_max_min(num):
    num_list = []
    diff = 0
    for i in range(num):
        num_list.append(round(uniform(1, num), 2))
    print(num_list)

    max = min = num_list[0] % 1
    
    for i in range(num):
        if num_list[i] % 1 > max:
            max = num_list[i] % 1
        elif num_list[i] % 1 < min:
            min = num_list[i] % 1
    diff = max - min
    print(f'Min: {round(min, 2)}, Max: {round(max, 2)}, Difference: {round(diff, 2)}')
    
    

diff_max_min(int(input('Введите количество чисел: ')))