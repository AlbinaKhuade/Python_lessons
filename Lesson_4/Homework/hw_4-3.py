# 3. Задайте последовательность чисел.
#  Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
# Negative value of the number of numbers!
# []

# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

import random

num = int(input('Введите число: '))

def uniq_el(num):
    num_list = []
    for i in range(num):
        num_list.append(random.randrange(10))
    print(num_list)
   
    new_num_list = []
    for k in num_list:
        if num_list.count(k) == 1:
            new_num_list.append(k)
    print(new_num_list)


uniq_el(num)
   
    # new_num_list = []
    # new_num_list[0] = num_list[0]
    # temp = new_num_list[0]
    # for i in range(1, num):
    #     if num_list[i] != temp:
    #         new_num_list[i] = num_list[i]
    #     temp = new_num_list[i]
   
    # new_set = set()
    # for j in range(len(new_num_list)):
    #     new_set.add(new_num_list[j])
    # print(new_set)
   
   
    # new_dict = {}
    # for i in range(len(num_list)):
    #     new_dict[i] = num_list[i]
    # print(new_dict)
   
    # for i in new_dict.values():
    #     print(i)

