# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# in
# 54
# out
# [2, 3, 3, 3]

# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

# in
# 650
# out
# [2, 5, 5, 13]

num = int(input('Введите натуральное число N: '))

def find_prime_factors(num):
    list_prime_fact = []
    i = 2
    while i * i <= num:
        while num % i == 0:
            list_prime_fact.append(i)
            num /= i
        i += 1

    if (num != 1):
        list_prime_fact.append(round(num, None))
    print(list_prime_fact)

find_prime_factors(num)

