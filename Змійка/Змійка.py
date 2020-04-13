import pygame
import random
from control import Control
from snake import Snake
from food import Food
from qui import Qui
pygame.init()
win = pygame.display.set_mode((441,441))
pygame.display.set_caption("Змійка")
control = Control()
snake = Snake()
qui = Qui()
food = Food()
qui.init_field()
food = Food()
food.get_food_position(qui)


while control.Flag_game:
    # pygame.time.delay(var_speed0)
    control.control()
    win.fill(pygame.Color("Black"))
    snake.snake_die(qui)
    if qui.game == "GAME":
        snake.draw_snake(win)
        food.draw_food(win)
        # qui.socer(win)
    elif qui.game == 'LOSE':
        win.blit(qui.lose,(23,100))
    if snake.run % 700 == 0:
        snake.moove (control)
        snake.chec_win()
        snake.eat(food, qui)
        snake.animation()
    # var_speed += 3
    snake.var_s(food)
    pygame.display.flip()
