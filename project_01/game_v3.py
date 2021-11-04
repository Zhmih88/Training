import numpy as np

def random_predict(number:int=1) ->int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        Число попыток
    """
    count = 0
    number_up=100
    number_down=1
    
    while True:
        count+=1
        predict_number = np.random.randint(number_down, number_up+1) # Предполагаемое число
        if number < predict_number: # Сужаем область поиска
            number_up=predict_number
        elif number > predict_number:
            number_down = predict_number
        else:
            break # Выход из цикла, если он угадал
    return (count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш подход

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return (score)

# RUN
score_game(random_predict)