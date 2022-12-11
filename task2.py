"""

Напишите программу для проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

"""

# подключаем модуль random
import random

# создаем три булевы переменные в которые помещаем значния True или False в случайном порядке
x = bool(random.getrandbits(1))
y = bool(random.getrandbits(1))
z = bool(random.getrandbits(1))
# выводим значения пользователю
print(f'X = {x}, Y = {y}, Z = {z}')
# выводим неравенство пользователю
if not(x or y or z) == (not(x) and not(y) and not(z)):
    print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
else:
    print(f'¬({x} ⋁ {y} ⋁ {z}) != ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
