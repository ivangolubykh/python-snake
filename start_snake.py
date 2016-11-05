#!/usr/bin/python3
# coding: utf-8

from tkinter import *
import time
import random


'''
 Перед началом создания программы провёл сравнения скорости
работы при использовании глобальных переменных и собственного 
класса
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


def element_square(x, y, d, canv):
    # координата центра квадрата и его сторона
    if (d % 2) == 0:
        d +=1 # сторону квадрата делаю нечётной
    x = x - (d // 2) # координата левой грани квадрата
    y = y - (d // 2) # координата верхней грани квадрата
    rect = canv.create_rectangle(x, y, x+d, y+d, fill="red", width=2)
    return rect


def main():
    root = Tk()
    root.title('Программа Змейка на питоне в графике')
    root.geometry('800x600+150+150')

    canv = Canvas(width=740,height=470,bg='#bfcff1')
    canv.place(x=30, y=100)



    # turtle.onkey(pres_key_w,"w")
    # turtle.listen()

    element_square(10, 50, 15, canv)

    root.mainloop()





if __name__ == '__main__':
    main()


