# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20


n = int(input("Enter the value of N: "))
pos1 = int(input("Position one: "))
pos2 = int(input("Position two: "))

num_list = []

for i in range(0, 2*n + 1):
    num_list.append(-n + i)
print(num_list)

if pos1 <= 2*n + 1 and pos1 <= 2*n + 1:
    res = num_list[pos1-1] * num_list[pos2-1]
    print(res)
else:
    print("There are no values for these indexes!")