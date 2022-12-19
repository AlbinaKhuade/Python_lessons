# 6. Пример проверки ложности утверждения
# (x ≡ z ) ∨ (x → (y ∧ z))

print("x y z")
for x in range(2):   #2 - т.к. всегодва состояния 0 и 1
    for y in range(2):
        for z in range(2):
            if not(x == z or x <= y and z):
                print(x, y, z)