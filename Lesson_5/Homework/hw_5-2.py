# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

# f = open('file.txt', 'r')
# data = f.read() + ' '
# f.close()

from os import path
from itertools import groupby

def file_encode(f_name_in, f_name_encode):   # функция кодирования текста в файл text_code_words.txt
    data_in = open(f_name_in, 'r')
    
    new_list = list(data_in.read())
    new_list_num = []   # список из цифр (количества встречаемых букв)
    count = 1
    for i in range(len(new_list)-1):
        if new_list[i] == new_list[i+1]:
            count += 1
        else:
            new_list_num.append(count)
            count = 1
    new_list_num.append(count)
   
    new_list_letter = [i for i, j in groupby(new_list)]   # список из букв

    new_list_encode = []

    for i in range(len(new_list_letter)):
        new_list_encode.append(str(new_list_num[i]) + new_list_letter[i])

    data_encode = open(f_name_encode, 'w')
    data_encode.writelines(new_list_encode)

    data_in.close()
    data_encode.close()


def file_decode(f_name_decode):       # функция декодирования текста из файла text_code_words.txt
    data_decode = open(f_name_decode, 'r')
    new_list = list(data_decode.read())

    num_list = [] #список из чисел
    let_list = [] #список из букв
    num = ''
    for char in new_list:
        if char.isdigit():
            num += char
        else:
            if num != '':
                num_list.append(int(num))
                let_list.append(char)
                num = ''

    a = ''
    for e in range(len(num_list)):
        a += (num_list[e] * let_list[e])
    print(a)



file_name_in = input('Enter the name of the file with the text: ')
if path.exists(file_name_in):
    
    file_name_code = input('Enter the file name to record: ')
    file_encode(file_name_in, file_name_code)

    file_name_decode = input('Enter the name of the file to decode: ')
    if path.exists(file_name_decode):
        file_decode(file_name_decode)
    else:
        print('No such file exists')
else:
    print('No such file exists')





