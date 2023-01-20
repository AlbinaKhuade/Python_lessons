# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect



from random import sample

def words_list(num, word='абв'):
    # w_list = []     ---------- далее на 32 строке это же записываем через Comprehension
    # for i in range(num):
    #     m = sample(word, k=3)
    #     w_list.append(''.join(m))

    w_list = [''.join(sample(word, k=3)) for i in range(num)]  

    # w_str = ''   ----------- пыталась преобразовать список в строку, но решила это сделать в выводе
    # for e in range(len(w_list)):
    #     w_str = w_str + w_list[e] + ' '
    # return w_str

    return w_list


def new_words_list(w_list, delete_word):
    # new_w_list = []     ---------- далее на 48 строке это же записываем через Comprehension
    # for i in range(len(w_list)):
    #     if w_list[i] != delete_word:
    #         new_w_list.append(w_list[i])

    new_w_list = [i for i in w_list if i != delete_word]
    return new_w_list

n = int(input('Введите количество: '))

if n > 0:
    u = words_list(n)
    print(*u)
    del_w = input('\nВведите слово, которое необходимо удалить: ')
    n = new_words_list(u, del_w)

    if u == n:
        print('Такого слова нет в списке!')
    else:
        print(*n)
else:
    print("Введите число больше 0")