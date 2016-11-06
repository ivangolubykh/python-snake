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
    def __init__(self, x, y, d, color, canv):
        self.x = x
        self.y = y
        self.d = d
        self.color = color
        self.canv = canv
        if (self.d % 2) == 0:
            self.d +=1 # сторону квадрата делаю нечётной

    def draw(self):
        x = self.x - (self.d // 2) # координата левой грани квадрата
        y = self.y - (self.d // 2) # координата верхней грани квадрата
        self.object = self.canv.create_rectangle(x, y, x + self.d, y + self.d, fill=self.color, width=2)


class snake_body:
    def __init__(self, x, y, bloks, thickness, color, canv):
        self.x = x
        self.y = y
        self.bloks = bloks
        self.thickness = thickness # толщина блока тела
        self.color = color
        self.canv = canv
        self.body = []
        
    def draw(self):
        for i in range(0,len(self.body)):
            x = self.body[i].x - (self.thickness // 2) # координата левой грани квадрата
            y = self.body[i].y - (self.thickness // 2) # координата верхней грани квадрата
            self.body[i] = self.canv.create_rectangle(x, y, x + self.thickness, y + self.thickness, fill=self.color, width=2)


class horiz_body(snake_body):
    def __init__(self, x, y, bloks, thickness, color, canv):
        super().__init__(x, y, bloks, thickness, color, canv)
        for i in range(0,self.bloks):
            self.body.append(element_square(self.x + i * self.thickness, self.y, self.thickness, self.color, self.canv))


class vert_body(snake_body):
    def __init__(self, x, y, bloks, thickness, color, canv):
        super().__init__(x, y, bloks, thickness, color, canv)
        for i in range(0,self.bloks):
            self.body.append(element_square(self.x, self.y + i * self.thickness, self.thickness, self.color, self.canv))





def main():
    canvasbgcolor = '#bfcff1' # Цвет фона холста
    snake_head_color = 'red' # Цвет головы змейки
    snake_body_color = 'green' # Цвет тела змейки
    snake_thickness = 10 # Толщина тела змейки
    root = Tk()
    root.title('Программа Змейка на питоне в графике')
    root.geometry('800x600+150+150')

    canv = Canvas(width=740,height=470,bg=canvasbgcolor)
    canv.place(x=30, y=100)



    hbody1 = horiz_body(30, 200, 15, snake_thickness, snake_body_color, canv)
    hbody1.draw()

    vbody1 = vert_body(330, 200, 15, snake_thickness, snake_body_color, canv)
    vbody1.draw()



    root.mainloop()


if __name__ == '__main__':
    main()


