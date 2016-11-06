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
    root = 0


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
    def __init__(self):
        self.head = element_square(CONST.SNAKE_X.value, CONST.SNAKE_Y.value,
                             CONST.SNAKE_THICKNESS.value,
                             CONST.SNAKE_HCOLOR.value)
        self.body = []
        self.body.append(self.head.draw())

        vals.root.bind('<d>',snake_body.right)
        vals.root.bind('<D>',snake_body.right)
        vals.root.bind('<Right>',snake_body.right)
        vals.root.bind('<s>',snake_body.down)
        vals.root.bind('<S>',snake_body.down)
        vals.root.bind('<Down>',snake_body.down)
        vals.root.bind('<a>',snake_body.left)
        vals.root.bind('<A>',snake_body.left)
        vals.root.bind('<Left>',snake_body.left)
        vals.root.bind('<w>',snake_body.up)
        vals.root.bind('<W>',snake_body.up)
        vals.root.bind('<Up>',snake_body.up)

        vals.root.bind('<q>',snake_body.quit)
        vals.root.bind('<e>',snake_body.start)
        vals.root.bind('<Destroy>',snake_body.quit)

    def right(event):
        vals.vector = CONST.RIGHT.value
    def down(event):
        vals.vector = CONST.DOWN.value
    def left(event):
        vals.vector = CONST.LEFT.value
    def up(event):
        vals.vector = CONST.UP.value

    def quit(event):
        vals.quit = 'y'

    def start(event):
        vals.quit = 'n'
        global snake
        i = 0
        while i == 0:
            vals.snake.step('del')
            for x in range(0,20):
                time.sleep(0.05)
                vals.root.update()
                if vals.quit == 'y':
                    i = 1
                    break

    def step(self, add):
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
        self.body.append(self.head.draw()) # Создал новую голову
        vals.canv.itemconfig(self.body[-2],
                             fill=CONST.SNAKE_BCOLOR.value) # Перекрасил старую голову в тело
        if add != 'add':
            vals.canv.delete(self.body[0])
            self.body.pop(0)






def main():
    vals.root = Tk()
    vals.root.title('Программа Змейка на питоне в графике')
    vals.root.geometry('800x600+150+150')

    vals.canv = Canvas(width=740,height=470,bg=CONST.CANVAS_BGCOLOR.value)
    vals.canv.place(x=30, y=100)



    vals.snake = snake_body()
    vals.snake.step('add')
    vals.snake.step('add')
    vals.snake.step('del')
    vals.snake.step('del')
    vals.snake.step('add')
    vals.snake.step('add')

    snake_body.start(1)



    vals.root.mainloop()



if __name__ == '__main__':
    main()


