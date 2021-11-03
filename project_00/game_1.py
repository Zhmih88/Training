"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # Загадываем числа

# Колиякство попыток
count = 0

while True:
    count+=1
    predict_numder = int(input("Угадай число от 1 до 100: "))
    
    if predict_numder > number:
        print("Число должно быть меньше!")
    
    elif predict_numder < number:
        print("Число должно быть больше!")
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # Конец игры, выход из цикла