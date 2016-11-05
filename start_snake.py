#!/usr/bin/python3
# coding: utf-8

# import turtle
import time
# import random

'''
 Перед началом создания программы провёл сравнения скорости
работы при использовании глобальных переменных и собственного класса
с набором своих переменных.
 Провожу тест для изменения значения глобальной переменной и переменной
 из своего класса 100000000 раз (100М раз).
Результат:
 global -> от 19.62 до 20.70 сек
 class  -> от 19.81 до 21.02 сек

GLOBAL:
    start = time.time()
    def sum():
        global k
        k += 1
    k = 0
    i = 0
    while (i < 100000000):
        sum()
        i += 1
    print(str(k) + ' - ' + str((time.time() - start)) )

CLASS:
    start = time.time()
    class glob():
        k=0;
    test = glob()
    i = 0
    while (i < 100000000):
        test.k += 1
        i += 1
    print(str(test.k) + ' - ' + str((time.time() - start)) )

ВЫВОД:
 Погрешность в пределах статистики, но вроде глобальная переменная чуть
быстрее.
'''




