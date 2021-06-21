import pygame

from universal_constants_file import *

class Bat:
    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_bat(self, gameDisplay):
        pygame.draw.rect(gameDisplay, WHITE, pygame.Rect(self.x, self.y, self.width, self.height))
    
    @staticmethod
    def bat_movement(keys_pressed, left_bat, right_bat):
        
        if keys_pressed[pygame.K_w] and left_bat.y > 0 + UP_DOWN_BORDER_HEIGHT:
            left_bat.y -= BAT_Y_SPEED
        if keys_pressed[pygame.K_a] and left_bat.x > 0:
            left_bat.x -= BAT_X_SPEED
        if keys_pressed[pygame.K_s] and left_bat.y + BAT_HEIGHT + UP_DOWN_BORDER_HEIGHT < HEIGHT:
            left_bat.y += BAT_Y_SPEED
        if keys_pressed[pygame.K_d] and left_bat.x + BAT_WIDTH < BAT_X_RESTRIANT:
            left_bat.x += BAT_X_SPEED

        if keys_pressed[pygame.K_UP] and right_bat.y > 0 + UP_DOWN_BORDER_HEIGHT:
            right_bat.y -= BAT_Y_SPEED
        if keys_pressed[pygame.K_LEFT] and right_bat.x > WIDTH - BAT_X_RESTRIANT:
            right_bat.x -= BAT_X_SPEED
        if keys_pressed[pygame.K_DOWN] and right_bat.y + BAT_HEIGHT + UP_DOWN_BORDER_HEIGHT < HEIGHT:
            right_bat.y += BAT_Y_SPEED
        if keys_pressed[pygame.K_RIGHT] and right_bat.x + BAT_WIDTH < WIDTH:
            right_bat.x += BAT_X_SPEED
