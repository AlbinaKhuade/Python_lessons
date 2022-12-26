# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011


def dec_in_bin (num):
    num_list = []
    while num > 0:
        num_list.append(num % 2)
        num //= 2
    print(num_list)
    new_list = []
    for i in range(len(num_list)):
        new_list.append(num_list[len(num_list)-1-i])
    print(*new_list, sep="")

dec_in_bin(int(input('Введите число: ')))