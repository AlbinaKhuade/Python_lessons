# 1
# fluffy = open("test1.txt", "r", encoding="utf-8")
# print(fluffy.read().split("\n"))
# fluffy.close()

# 2
# fluffy = open("test1.txt", "r", encoding="utf-8")
# print(fluffy.readlines()) # возвращает 1 строку
# print(fluffy.readlines()) # возвращает 2ую строку
# print(fluffy.readlines())
# fluffy.close()

#3
# fluffy = open("test1.txt", "r", encoding="utf-8")
# for i in fluffy:
#     print(i, end="")
# fluffy.close()

#4
# fluffy = open("test1.txt", "r", encoding="utf-8")
# print([i.strip() for i in fluffy])
# fluffy.close()

#5
fluffy = open("test1.txt", "r", encoding="utf-8")
print(*[i for i in fluffy], sep="")
fluffy.close()