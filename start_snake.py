#!/usr/bin/python3
# coding: utf-8
'''
 Игра разработана Голубых Иваном Борисовичем.
 Официальный сайт игры:
 https://github.com/ivangolubykh/python-snake
'''


from tkinter import *
from enum import Enum
import time
import random

class python_snake: # Двигать тело змеюки в текущую сторону на 1 шаг
# При этом тело может увеличиться (add='add') в размерах или нет
    def __init__(self, window, canv_x, canv_y, canv_width, canv_height):
        self.__started = 1
        self.__spped = 10
        self.__window = window
        self.__canv_x = canv_x
        self.__canv_y = canv_y
        self.canv_width = canv_width
        self.canv_height = canv_height
        self.__snake_x = self.canv_width // 2 # Координата старта змеи
        self.__snake_y = self.canv_height // 2 # Координата старта змеи
        self.canv = Canvas(self.__window, width=self.canv_width,
                                height=self.canv_height,
                                bg=self.CONST.CANVAS_BGCOLOR.value)
        self.canv.place(x=self.__canv_x, y=self.__canv_y)
        self.create_head_food()

        self.__window.bind('<d>',self.right)
        self.__window.bind('<D>',self.right)
        self.__window.bind('<Right>',self.right)
        self.__window.bind('<s>',self.down)
        self.__window.bind('<S>',self.down)
        self.__window.bind('<Down>',self.down)
        self.__window.bind('<a>',self.left)
        self.__window.bind('<A>',self.left)
        self.__window.bind('<Left>',self.left)
        self.__window.bind('<w>',self.up)
        self.__window.bind('<W>',self.up)
        self.__window.bind('<Up>',self.up)

        self.__window.bind('<e>',self.move)
        self.__window.bind('<q>',self.quit)
        self.__window.bind('<Destroy>',self.quit)
        self.__window.bind('<plus>',self.speed_key)
        self.__window.bind('<minus>',self.speed_key)
        self.__window.bind('<KP_Add>',self.speed_key) # Клавиша + на боковой клаве
        self.__window.bind('<KP_Subtract>',self.speed_key) # Клавиша - на боковой клаве
        # self.__window.bind('<KeyPress>',self.speed_key) # print(event.keysym) Вычислит нажатую клавишу
        

    class CONST(Enum): # Список возможных направлений движения и других констант
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        UP = 4
        SNAKE_HCOLOR = 'red' # Цвет головы змейки
        SNAKE_BCOLOR = 'green' # Цвет тела змейки
        CANVAS_BGCOLOR = '#bfcff1' # Цвет фона холста
        SNAKE_THICKNESS = 11 # Толщина тела змейки (нечётное число)
        FOOD_THICKNESS = 15 # Толщина еды (нечётное число)
        FOOD_COLOR = '#aced95' # Цвет тела еды
        EXPLOSIVE = 15 # Диаметр взрыва при столкновении змеи с препятствием (нечётное число)
        EXPLOSIVE_BORD = 10 # толщина контура взрыва при столкновении змеи с препятствием
        EXPLOSIVE_BCOLOR = '#ff9999' # Цвет тела взрыва
        EXPLOSIVE_CCOLOR = '#881a1a' # Цвет контура взрыва


    # обработчики клавиш изменения направления движения:
    def right(self, event):
        self.__vector = self.CONST.RIGHT.value
    def down(self, event):
        self.__vector = self.CONST.DOWN.value
    def left(self, event):
        self.__vector = self.CONST.LEFT.value
    def up(self, event):
        self.__vector = self.CONST.UP.value

    def speed_key(self, event):
        # print(event.keysym)
        if event.keysym == 'KP_Add' or event.keysym == 'plus' :
            self.speed('+')
        elif event.keysym == 'KP_Subtract' or event.keysym == 'minus' :
            self.speed('-')

    def create_head_food(self):
        rand_vect=random.randint(1,4)
        if rand_vect == 1:
            self.__vector = self.CONST.RIGHT.value
        elif rand_vect == 2:
            self.__vector = self.CONST.DOWN.value
        elif rand_vect == 3:
            self.__vector = self.CONST.LEFT.value
        else:
            self.__vector = self.CONST.UP.value
        self.head = self.element_square(self, self.__snake_x,
                             self.__snake_y,
                             self.CONST.SNAKE_THICKNESS.value,
                             self.CONST.SNAKE_HCOLOR.value)
        self.food.add(self)
        self.body = []
        self.body.append({'id': self.head.draw(),
                        'x': self.__snake_x,
                        'y': self.__snake_y})
        self.step('add')
        self.step('add')
        self.step('add')
        self.step('add')

    def speed(self, way):
        if way == '+' and self.__spped > 1:
            self.__spped -= 1
        elif way == '-' and self.__spped < 20:
            self.__spped += 1

    def reload(self):
        self.quit = 'n'
        self.__started = 1
        self.__spped = 10
        self.canv.delete('all')
        del self.body
        self.body = []
        self.create_head_food()
        self.start()

    def quit(self, event): # Возможность остановить змейку (пауза)
        self.quit = 'y'

    def move(self, event):
        if self.quit != 'n':
            self.start()

    def start(self): # Бесконечный цикл движения змейки
        if self.__started == 1:
            self.quit = 'n'
            i = 0
            add = 'del'
            while i == 0:
                self.step(add)
                if self.food.eat(self) == 1:
                    add = 'add'
                    self.speed('+')
                elif add == 'add':
                    add = 'del'
                if self.bump_wall() == 'the end':
                    break
                if self.bump_body() == 'the end':
                    break
                for x in range(1, (self.__spped + 1) ):
                    time.sleep(0.05)
                    self.__window.update()
                    if self.quit == 'y':
                        i = 1
                        break

    def bump_wall(self): # Проверка на столкновение со стеной
        __head_x = self.body[-1]['x']
        __head_y = self.body[-1]['y']
        if ( (__head_x < ( (self.CONST.SNAKE_THICKNESS.value // 2) + 1 ) )
              or (__head_y < ( (self.CONST.SNAKE_THICKNESS.value // 2) + 1 ) )
              or (__head_x > ( self.canv_width
                         - (self.CONST.SNAKE_THICKNESS.value // 2) + 1 ) )
              or (__head_y > ( self.canv_height
                         - (self.CONST.SNAKE_THICKNESS.value // 2) + 1 ) ) ):
            self.explosive()
            return 'the end'
        else:
            return 0

    def bump_body(self): # Проверка на столкновение с телом змеи
        __head_x = self.body[-1]['x']
        __head_y = self.body[-1]['y']
        bump = 0
        for i in range(0, (len(self.body) - 1) ):
            if ( (__head_x == self.body[i]['x'])
                  and (__head_y == self.body[i]['y']) ):
                self.explosive()
                bump = 'the end'
        return bump

    def explosive(self):
        self.__started = 0
        self.canv.create_oval( (self.body[-1]['x'] 
                               - self.CONST.EXPLOSIVE.value),
                               (self.body[-1]['y'] 
                               - self.CONST.EXPLOSIVE.value),
                               (self.body[-1]['x'] 
                               + self.CONST.EXPLOSIVE.value),
                               (self.body[-1]['y'] 
                               + self.CONST.EXPLOSIVE.value),
                               fill=self.CONST.EXPLOSIVE_BCOLOR.value,
                               outline=self.CONST.EXPLOSIVE_CCOLOR.value,
                               width=self.CONST.EXPLOSIVE_BORD.value)

    def step(self, add): # Двигать тело змеюки в текущую сторону на 1 шаг
        # При этом тело может увеличиться (add='add') в размерах или нет
        if self.__vector == self.CONST.RIGHT.value:
            deltax = self.CONST.SNAKE_THICKNESS.value
            deltay = 0
        elif self.__vector == self.CONST.DOWN.value:
            deltax = 0
            deltay = self.CONST.SNAKE_THICKNESS.value
        elif self.__vector == self.CONST.LEFT.value:
            deltax = -self.CONST.SNAKE_THICKNESS.value
            deltay = 0
        elif self.__vector == self.CONST.UP.value:
            deltax = 0
            deltay = -self.CONST.SNAKE_THICKNESS.value
        self.head.x += deltax
        self.head.y += deltay
        self.head = self.element_square(self, self.head.x, self.head.y,
                             self.CONST.SNAKE_THICKNESS.value,
                             self.CONST.SNAKE_HCOLOR.value)
        self.body.append({'id': self.head.draw(), 'x': self.head.x, 
                          'y': self.head.y}) # Создал новую голову
        self.canv.itemconfig(self.body[-2]['id'],
                             fill=self.CONST.SNAKE_BCOLOR.value) # Перекрасил старую голову в тело
        if add != 'add':
            self.canv.delete(self.body[0]['id'])
            self.body.pop(0)


    class food:
        def add(self):
            self.food.x = random.randint(self.CONST.FOOD_THICKNESS.value
                                     // 2, self.canv_width
                                     - self.CONST.FOOD_THICKNESS.value // 2)
            self.food.y = random.randint(self.CONST.FOOD_THICKNESS.value 
                                     // 2, self.canv_height
                                     - self.CONST.FOOD_THICKNESS.value // 2)
            self.food.body = self.element_square(self, self.food.x,
                                       self.food.y,
                                       self.CONST.FOOD_THICKNESS.value,
                                       self.CONST.FOOD_COLOR.value)
            self.food.id = self.food.body.draw()

        def eat(self):
            head_x = self.body[-1]['x']
            head_y = self.body[-1]['y']
            eat = 0
            if ( (head_x
                     + self.CONST.SNAKE_THICKNESS.value // 2 > (self.food.x
                                - self.CONST.FOOD_THICKNESS.value // 2) )
                     and (head_x
                     - self.CONST.SNAKE_THICKNESS.value // 2 < (self.food.x
                                + self.CONST.FOOD_THICKNESS.value // 2) )
                     and (head_y
                     + self.CONST.SNAKE_THICKNESS.value // 2 > (self.food.y
                                - self.CONST.FOOD_THICKNESS.value // 2) )
                     and (head_y
                     - self.CONST.SNAKE_THICKNESS.value // 2 < (self.food.y
                                + self.CONST.FOOD_THICKNESS.value // 2) ) ):
                self.canv.delete(self.food.id)
                self.food.add(self)
                eat = 1
            return eat


    class element_square: # Рисую квадратик со стороной d и центром x,y
        def __init__(self, self_glob, x, y, d, color):
            self.self_glob = self_glob
            self.x = x
            self.y = y
            self.d = d
            self.color = color
            if (self.d % 2) == 0:
                self.d +=1 # сторону квадрата делаю нечётной

        def draw(self):
            x = self.x - (self.d // 2) # координата левой грани квадрата
            y = self.y - (self.d // 2) # координата верхней грани квадрата
            return self.self_glob.canv.create_rectangle(x, y, x + self.d,
                                                       y + self.d,
                                                       fill=self.color,
                                                       width=2)



def main():
    image1_data='''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'''
    image2_data='''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'''

    def button_press(a):
        reload_button['image']=reload_button_img2
        snake.reload()

    def button_unpress(a):
        reload_button['image']=reload_button_img1

    root = Tk()
    root.title('Программа Змейка на питоне в графике')
    root.geometry('800x600+150+150')

    frame = Frame(root, width=740, height=90, bg='#f2ffe0')
    frame.place(x=30, y=5)
    text = Label(root, text='''Игра Змейка написана на Python 3 Голубых Иваном Борисовичем в ноябре 2016 года для
тренировки и демонстрации навыков работы с Git и Python 3. Правила: Змейка должна кушать
зелёные плоды. При съедании плода, скорость змейки возрастает. Скорость можно
отрегулировать вручную клавишами "+" и "-". Нельзя выползать за границы поля и есть себя.
Официальный сайт игры: https://github.com/ivangolubykh/python-snake''',
                  bg='#f2ffe0', width=79)
    text.place(x=30, y=10)
    reload_button_img1=PhotoImage(data = image1_data)
    reload_button = Label(image=reload_button_img1, bg='#f2ffe0')
    reload_button.place(x=675, y=13)
    reload_button_img2=PhotoImage(data = image2_data)
    reload_button.bind('<Button-1>',button_press)
    reload_button.bind('<ButtonRelease-1>',button_unpress)

    snake = python_snake(root, 30, 100, 740, 470)
    snake.start()

    root.mainloop()



if __name__ == '__main__':
    main()
