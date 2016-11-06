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


class element_square:
    def __init__(self, x, y, d, canv):
        self.x = x
        self.y = y
        self.d = d
        self.canv = canv
        if (self.d % 2) == 0:
            self.d +=1 # сторону квадрата делаю нечётной
        self.x = self.x - (self.d // 2) # координата левой грани квадрата
        self.y = self.y - (self.d // 2) # координата верхней грани квадрата
        self.object = canv.create_rectangle(self.x, self.y, self.x + self.d, self.y + self.d, fill='red', width=2)


def main():
    canvasbgcolor='#bfcff1'
    root = Tk()
    root.title('Программа Змейка на питоне в графике')
    root.geometry('800x600+150+150')

    canv = Canvas(width=740,height=470,bg=canvasbgcolor)
    canv.place(x=30, y=100)


    element_square1 = element_square(30, 150, 10, canv)




    root.mainloop()


if __name__ == '__main__':
    main()


