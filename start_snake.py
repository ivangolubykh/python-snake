#!/usr/bin/python3
# coding: utf-8

from tkinter import *
from enum import Enum
import time
import random


class CONST(Enum): # Список возможных направлений движения и других констант
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4
    SNAKE_X = 370 # Координата старта змеи
    SNAKE_Y = 235 # Координата старта змеи
    SNAKE_HCOLOR = 'red' # Цвет головы змейки
    SNAKE_BCOLOR = 'green' # Цвет тела змейки
    CANVAS_BGCOLOR = '#bfcff1' # Цвет фона холста
    SNAKE_THICKNESS = 10 # Толщина тела змейки


class vals: # список изменяемых глобальных объектов/переменных
    vector = CONST.RIGHT.value # Текущее направление движения
    quit = 'n'
    canv = 0
    snake = 0


class element_square: # Рисую квадратик со стороной d и центром x,y
    def __init__(self, x, y, d, color):
        self.x = x
        self.y = y
        self.d = d
        self.color = color
        if (self.d % 2) == 0:
            self.d +=1 # сторону квадрата делаю нечётной

    def draw(self):
        x = self.x - (self.d // 2) # координата левой грани квадрата
        y = self.y - (self.d // 2) # координата верхней грани квадрата
        return vals.canv.create_rectangle(x, y, x + self.d, y + self.d, fill=self.color, width=2)


class snake_body: # Двигать тело змеюки в текущую сторону на 1 шаг
# При этом тело может увеличиться (add='add') в размерах или нет
    def __init__(self, window):
        self.window = window
        self.head = element_square(CONST.SNAKE_X.value, CONST.SNAKE_Y.value,
                             CONST.SNAKE_THICKNESS.value,
                             CONST.SNAKE_HCOLOR.value)
        self.body = []
        self.body.append({'id': self.head.draw(), 'x': CONST.SNAKE_X.value,
                        'y': CONST.SNAKE_Y.value})
        self.step('add')
        self.step('add')
        self.step('add')
        self.step('add')

        self.window.bind('<d>',snake_body.right)
        self.window.bind('<D>',snake_body.right)
        self.window.bind('<Right>',snake_body.right)
        self.window.bind('<s>',snake_body.down)
        self.window.bind('<S>',snake_body.down)
        self.window.bind('<Down>',snake_body.down)
        self.window.bind('<a>',snake_body.left)
        self.window.bind('<A>',snake_body.left)
        self.window.bind('<Left>',snake_body.left)
        self.window.bind('<w>',snake_body.up)
        self.window.bind('<W>',snake_body.up)
        self.window.bind('<Up>',snake_body.up)

        self.window.bind('<q>',self.quit)
        self.window.bind('<e>',self.move)
        self.window.bind('<Destroy>',self.quit)

    # обработчики клавиш изменения направления движения:
    def right(event):
        vals.vector = CONST.RIGHT.value
    def down(event):
        vals.vector = CONST.DOWN.value
    def left(event):
        vals.vector = CONST.LEFT.value
    def up(event):
        vals.vector = CONST.UP.value

    def quit(self, event): # Возможность остановить змейку (пауза)
        vals.quit = 'y'

    def move(self, event):
        if vals.quit != 'n':
            self.start()

    def start(self): # бесконечный цикл движения змейки
        vals.quit = 'n'
        i = 0
        while i == 0:
            self.step('del')
            for x in range(0,20):
                time.sleep(0.05)
                self.window.update()
                if vals.quit == 'y':
                    i = 1
                    break

    def step(self, add): # Двигать тело змеюки в текущую сторону на 1 шаг
        # При этом тело может увеличиться (add='add') в размерах или нет
        if vals.vector == CONST.RIGHT.value:
            deltax = CONST.SNAKE_THICKNESS.value
            deltay = 0
        elif vals.vector == CONST.DOWN.value:
            deltax = 0
            deltay = CONST.SNAKE_THICKNESS.value
        elif vals.vector == CONST.LEFT.value:
            deltax = -CONST.SNAKE_THICKNESS.value
            deltay = 0
        elif vals.vector == CONST.UP.value:
            deltax = 0
            deltay = -CONST.SNAKE_THICKNESS.value
        self.head.x += deltax
        self.head.y += deltay
        self.head = element_square(self.head.x, self.head.y,
                             CONST.SNAKE_THICKNESS.value,
                             CONST.SNAKE_HCOLOR.value)
        self.body.append({'id': self.head.draw(), 'x': self.head.x, 'y': self.head.y}) # Создал новую голову
        vals.canv.itemconfig(self.body[-2]['id'],
                             fill=CONST.SNAKE_BCOLOR.value) # Перекрасил старую голову в тело
        if add != 'add':
            vals.canv.delete(self.body[0]['id'])
            self.body.pop(0)





def main():
    root = Tk()
    root.title('Программа Змейка на питоне в графике')
    root.geometry('800x600+150+150')

    vals.canv = Canvas(width=740,height=470,bg=CONST.CANVAS_BGCOLOR.value)
    vals.canv.place(x=30, y=100)



    vals.snake = snake_body(root)
    vals.snake.start()



    root.mainloop()



if __name__ == '__main__':
    main()


