# 1. Вычислить число c заданной точностью d

# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

from decimal import Decimal

num = input('Enter a real number: ')
acc = input('Enter the required accuracy: ')

def accuracy(num, acc):
    new_num = Decimal(num)
    new_num =new_num.quantize(Decimal(acc))
    print(new_num)

accuracy(num, acc)
