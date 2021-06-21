import pygame
import random
import math

from universal_constants_file import *

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.side = BALL_SIDE
        self.current_ball_speed = 0
        self.current_theta = 0
    def ball_movement(self):
        if self.x + BALL_SIDE < 0:
            return "left side"
        elif self.x > WIDTH:
            return "right side"
        else:
            self.x += (self.current_ball_speed * math.cos(self.current_theta))
            self.y += (self.current_ball_speed * math.sin(self.current_theta))
        
    def draw_ball(self, gameDisplay):
        pygame.draw.rect(gameDisplay, WHITE, pygame.Rect(self.x, self.y, self.side, self.side))
    def initial_ball_movement(self): # To provide the initial push to the ball just after a point scored or at the beginning
        degrees = random.randrange(0, 361, 40) # O is included and 361 is not included
        while 1:
            if(degrees == 0 and degrees == 180 and degrees == 360):
                degrees = random.randrange(0, 361, 20) # O is included and 361 is not included
            else:
                break
        theta = math.radians(degrees)
        self.current_ball_speed = INITIAL_BALL_SPEED
        self.current_theta = theta
        self.ball_movement()


