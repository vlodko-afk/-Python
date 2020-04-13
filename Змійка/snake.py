import pygame
from qui import Qui
qui = Qui()
class Snake:
    def __init__(self):
        self.head = [45,45]
        self.body = [[45,45],[34,45]]
        self.run = 0
        self.k = 0
    def moove(self,control):
        if control.flag_direction == "RIGHT":
            self.head[0] += 11
        elif  control.flag_direction == "LEFT":
            self.head[0] -= 11
        elif  control.flag_direction == "UP":
            self.head[1] -= 11
        elif  control.flag_direction == "DOWN":
            self.head[1] += 11
    def animation(self):
        self.body.insert(0,list(self.head))
        self.body.pop()

    def draw_snake(self,win):
        for segment in self.body:
            pygame.draw.rect(win,pygame.Color("Green"),pygame.Rect(segment[0],segment[1],10,10))
    def  snake_die(self,qui):
        if self.head in  self.body[1:]:
            qui.draw_lose()

    def eat (self,food,qui):
        if self.head == food.food_position:
            self.body.append([food.food_position])
            food.get_food_position(qui)
    def var_s(self,food):
        if len(self.body) <= 5:
            self.run += 1
        elif len(self.body) > 5 and len(self.body) <= 20:
            self.run += 3
        elif len(self.body) > 20 and len(self.body) <= 100:
            self.run += 3.5
        elif len(self.body) > 100:
            self.run += 4
    def chec_win(self):
        if self.head[0] > 440:
            self.head[0] = 1
        elif self.head[0] < 1:
            self.head[0] = 441
        elif self.head[1] > 440:
            self.head[1] = 1
        elif self.head[1] < 1:
            self.head[1] = 441
