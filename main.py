import pygame
import sys
import time
import os

import Bat_class_file, Ball_class_file
from ball_collision import *
from universal_constants_file import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Pong Ball")

UP_WALL = pygame.Rect(0,0,WIDTH,UP_DOWN_BORDER_HEIGHT) # FIXED
DOWN_WALL = pygame.Rect(0, HEIGHT - UP_DOWN_BORDER_HEIGHT, WIDTH, UP_DOWN_BORDER_HEIGHT) # FIXED

# User events
BALL_OFF_SCREEN_LEFT = pygame.USEREVENT + 1
BALL_OFF_SCREEN_RIGHT = pygame.USEREVENT + 2
STALEMATE = pygame.USEREVENT + 3

# Font properties
SCORE_FONT = pygame.font.SysFont("consolas", 20)
WINNER_FONT = pygame.font.SysFont("Comic Sans MS",50)

# Music channels

# argument must be int
channel1 = pygame.mixer.Channel(0) # Background music channel
channel2 = pygame.mixer.Channel(1) # Background music channel

#----------------------code for working on terminal----------
final_path = os.getcwd()
path_list = final_path.split("\\")
# print(final_path)
final_path = final_path + "\\"
if path_list[-1] == "Physics_Pong_Multiplayer" or  path_list[-1] == "Physics_Pong_Multiplayer-master":
    pass
#----------------------code for working on terminal----------

#----------------------code for working on vs code----------
else:
    final_path = os.path.dirname(__file__) + "\\"
    # print(final_path)
#----------------------code for working on vs code----------

BACKGROUND_MUSIC = pygame.mixer.Sound(final_path + "rain_sound.wav")
BACKGROUND_MUSIC.set_volume(0.50)
BALL_HIT_SOUND = pygame.mixer.Sound(final_path + "ball_hit.ogg")
BALL_HIT_SOUND.set_volume(1)

def line_point_collide(left_bat, right_bat, ball):
    if ball.x < left_bat.x + BAT_WIDTH:
        if ((left_bat.y) < (ball.y - BALL_SIDE/2) < (left_bat.y + BAT_HEIGHT)):
            ball.x = left_bat.x + BAT_WIDTH # reset ball position to a moment before 'only if bat hits the ball
            bat_ball_collision(ball) # Changes the angle of incidence to angle of reflection
            channel2.play(BALL_HIT_SOUND)
        else:
            return
    elif ball.x + BALL_SIDE > right_bat.x:
        if ((right_bat.y) < (ball.y - BALL_SIDE/2) < (right_bat.y + BAT_HEIGHT)):
            ball.x = right_bat.x - BALL_SIDE # reset ball position to a moment before 'only if bat hits the ball
            bat_ball_collision(ball) # Changes the angle of incidence to angle of reflection
            channel2.play(BALL_HIT_SOUND)
    else:
        return




def draw_winner(winner_text):
    if winner_text == "PLAYER TO THE LEFT WINS!":
        draw_text = WINNER_FONT.render(winner_text,1,BLUE)
        gameDisplay.blit(draw_text,(WIDTH/2-(draw_text.get_width())/2, HEIGHT/4 -(draw_text.get_height())/2))
    elif winner_text == "PLAYER TO THE RIGHT WINS!":
        draw_text = WINNER_FONT.render(winner_text,1,RED)
        gameDisplay.blit(draw_text,(WIDTH/2-(draw_text.get_width())/2, HEIGHT/4 -(draw_text.get_height())/2))
    pygame.display.update()
    pygame.time.delay(1000*3) # 3 seconds




def draw_display(game_ball, left_bat,right_bat, left_score, right_score):

    gameDisplay.fill(BLACK)

    pygame.draw.line(gameDisplay, YELLOW, (RESTRIANT, 0), (RESTRIANT, HEIGHT), 1)
    pygame.draw.line(gameDisplay, YELLOW, (WIDTH - RESTRIANT, 0),(WIDTH - RESTRIANT, HEIGHT), 1)

    # pygame.draw.line(gameDisplay, YELLOW, (WIDTH/2, 0), (WIDTH/2, HEIGHT), 1)  # Central line if needed.

    left_score_text = SCORE_FONT.render("{}/{}".format(left_score, WINNING_SCORE), 1, ORANGE)
    right_score_text = SCORE_FONT.render("{}/{}".format(right_score, WINNING_SCORE), 1, ORANGE)

    gameDisplay.blit(left_score_text,(20, HEIGHT/2 - (left_score_text.get_height()/2)))
    gameDisplay.blit(right_score_text, (WIDTH - 20 - right_score_text.get_width(), HEIGHT/2 - (right_score_text.get_height()/2)))

    pygame.draw.rect(gameDisplay , GREEN, UP_WALL)
    pygame.draw.rect(gameDisplay, GREEN, DOWN_WALL)
    
    left_bat.left_draw_bat(gameDisplay)
    right_bat.right_draw_bat(gameDisplay)
    game_ball.draw_ball(gameDisplay)    

    pygame.display.update()

channel1.play(BACKGROUND_MUSIC, -1)
def main():
    # Left and Right bats
    # SCORES
    LEFT_SCORE = 0
    RIGHT_SCORE = 0

    LEFT_BAT = Bat_class_file.Bat(RESTRIANT, HEIGHT/2 - BAT_HEIGHT/2) # Initial position
    RIGHT_BAT = Bat_class_file.Bat(WIDTH - RESTRIANT - BAT_WIDTH, HEIGHT/2 - BAT_HEIGHT/2) # Initial position

    GAME_BALL = Ball_class_file.Ball(WIDTH/2 - BALL_SIDE/2, HEIGHT/2 - BALL_SIDE/2)

    draw_display(GAME_BALL, LEFT_BAT,RIGHT_BAT, LEFT_SCORE, RIGHT_SCORE)
    time.sleep(2)
    
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
                LEFT_BAT.y = RIGHT_BAT.y = HEIGHT/2 - BAT_HEIGHT/2 # Bat position reset for taking the ball
                GAME_BALL.initial_ball_movement()
                RIGHT_SCORE += 1
                draw_display(GAME_BALL, LEFT_BAT, RIGHT_BAT, LEFT_SCORE, RIGHT_SCORE)
                time.sleep(DELAY)

            if event.type == BALL_OFF_SCREEN_RIGHT:
                LEFT_BAT.y = RIGHT_BAT.y = HEIGHT/2 - BAT_HEIGHT/2 # Bat position reset for taking the ball
                GAME_BALL.initial_ball_movement()
                LEFT_SCORE += 1
                draw_display(GAME_BALL, LEFT_BAT, RIGHT_BAT, LEFT_SCORE, RIGHT_SCORE)
                time.sleep(DELAY)
            
            if event.type == STALEMATE:
                LEFT_BAT.y = RIGHT_BAT.y = HEIGHT/2 - BAT_HEIGHT/2 # Bat position reset for taking the ball
                GAME_BALL.initial_ball_movement()
                # print("STALEMATE")
                draw_display(GAME_BALL, LEFT_BAT, RIGHT_BAT, LEFT_SCORE, RIGHT_SCORE)
                time.sleep(DELAY)
            winner_text=""
            if LEFT_SCORE >= WINNING_SCORE:
                winner_text = "PLAYER TO THE LEFT WINS!"
            if RIGHT_SCORE >= WINNING_SCORE:
                winner_text = "PLAYER TO THE RIGHT WINS!"

            if winner_text!="":
                draw_winner(winner_text)
                pygame.quit()
                sys.exit(0)
            
            
        Bat_class_file.Bat.bat_movement(keys_pressed, LEFT_BAT, RIGHT_BAT)

        line_point_collide(LEFT_BAT, RIGHT_BAT, GAME_BALL)

        x = GAME_BALL.ball_movement()
            
        if(x == 1):
            pygame.event.post(pygame.event.Event(BALL_OFF_SCREEN_LEFT))
        elif(x == -1):
            pygame.event.post(pygame.event.Event(BALL_OFF_SCREEN_RIGHT))
        elif(x == 10):
            channel2.play(BALL_HIT_SOUND)
            pygame.event.post(pygame.event.Event(STALEMATE))
        elif(x == 7):
            channel2.play(BALL_HIT_SOUND)
        else:
            pass

        draw_display(GAME_BALL, LEFT_BAT, RIGHT_BAT, LEFT_SCORE, RIGHT_SCORE)
    


if __name__=='__main__':
    main()