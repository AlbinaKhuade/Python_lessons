# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import sample

def find_el(num):
    cur_list = sample(range(1, (num+1)*2), k=num)
    print(cur_list)

    new_list = [cur_list[i+1] for i in range(num-1) if cur_list[i+1] > cur_list[i]]
    print(new_list)



find_el(int(input('Введите количество: ')))