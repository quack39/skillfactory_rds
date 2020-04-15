#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v3(number):
 
    count = 1 
    my_li = [x for x in range(1,101)]
    min_num = 0                           # задаём левую границу
    max_num = len(my_li)                     # задаём правую границу равную длине списка
    while min_num < max_num:                 # сравниваем границы 
        count = count + 1
        average = (min_num + max_num)//2     # получаем среднее значение
        if average < number:              # сравниваем среднее значение с загаданным числом
            min_num = average +1          # присваиваем нижней границе среднее значение + 1 и отправляем на сравнение в блок while подвинув нижнюю границу
        else:                             # в этом блоке присваем верхней границе среднее значение и отправляем на сравнение в блок while подвинув верхнюю границу
            max_num=average
    return(count)
# Проверяем
score_game(game_core_v3)

