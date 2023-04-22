"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""

import random
n = int(input('Введите количество монет: '))
coinList = []
i = 0
while i <= n:
    coinList.append(random.randint(0, 1))
    i += 1
print(coinList)
countObverse = 0
countReverse = 0
for j in range(0, n):
    if coinList[j] == 0:
        countObverse += 1
    else: countReverse += 1
if countObverse < countReverse:
    print(f'Минимальное количество монет к перевороту {countObverse}')
else:
    print(f'Минимальное количество монет к перевороту {countReverse}')