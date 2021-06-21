import pygame

import Bat_class_file, Ball_class_file
from universal_constants_file import *

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))

UP_WALL = pygame.Rect(0,0,WIDTH,UP_DOWN_BORDER_HEIGHT) # FIXED
DOWN_WALL = pygame.Rect(0,HEIGHT - UP_DOWN_BORDER_HEIGHT,WIDTH,UP_DOWN_BORDER_HEIGHT) # FIXED

# User events

BALL_OFF_SCREEN_LEFT = pygame.USEREVENT + 1
BALL_OFF_SCREEN_RIGHT = pygame.USEREVENT + 2


def draw_display(game_ball, left_bat,right_bat):

    gameDisplay.fill(BLACK)

    pygame.draw.line(gameDisplay, RED, (BAT_X_RESTRIANT, 0), (BAT_X_RESTRIANT, HEIGHT), 1)
    pygame.draw.line(gameDisplay, RED,(WIDTH-BAT_X_RESTRIANT, 0),(WIDTH-BAT_X_RESTRIANT, HEIGHT), 1)

    # pygame.draw.line(gameDisplay, BLUE, (WIDTH/2, 0), (WIDTH/2, HEIGHT), 1)  # Central line if needed.

    pygame.draw.rect(gameDisplay , GREEN, UP_WALL)
    pygame.draw.rect(gameDisplay, GREEN, DOWN_WALL)
    
    left_bat.draw_bat(gameDisplay)
    right_bat.draw_bat(gameDisplay)
    game_ball.draw_ball(gameDisplay)    

    pygame.display.update()

def main():
    # Left and Right bats
    LEFT_BAT = Bat_class_file.Bat(BAT_X_RESTRIANT/2 - BAT_WIDTH/2, HEIGHT/2 - BAT_HEIGHT/2, BAT_WIDTH, BAT_HEIGHT) # Initial position
    RIGHT_BAT = Bat_class_file.Bat(WIDTH - BAT_X_RESTRIANT/2 - BAT_WIDTH/2, HEIGHT/2 - BAT_HEIGHT/2, BAT_WIDTH, BAT_HEIGHT) # Initial position
    GAME_BALL = Ball_class_file.Ball(WIDTH/2 - BALL_SIDE/2, HEIGHT/2 - BALL_SIDE/2)
    
    clock = pygame.time.Clock()
    running = True

    GAME_BALL.initial_ball_movement() #Initial push at the start of the game
    while running: # Game loop
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == BALL_OFF_SCREEN_LEFT:
                print("left side")
            if event.type == BALL_OFF_SCREEN_RIGHT:
                print("right side")
            
        Bat_class_file.Bat.bat_movement(keys_pressed, LEFT_BAT, RIGHT_BAT)

        x = GAME_BALL.ball_movement()
        
        if(x == "left side"):
            pygame.event.post(pygame.event.Event(BALL_OFF_SCREEN_LEFT))
        elif(x == "right side"):
            pygame.event.post(pygame.event.Event(BALL_OFF_SCREEN_RIGHT))

        draw_display(GAME_BALL, LEFT_BAT, RIGHT_BAT)

    pygame.quit()


if __name__=='__main__':
    main()