import pygame
import random
class Food:
    def __init__(self):
        self.food_position = []
    def get_food_position(self, qui):
        self.food_position = random.choice(qui.field)
    def draw_food(self,win):
        pygame.draw.rect(win,pygame.Color("Red"),pygame.Rect(self.food_position[0],self.food_position[1],10,10))
