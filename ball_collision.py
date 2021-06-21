import math

COUNTER = 0

def wall_ball_collision(ball):
    global COUNTER
    COUNTER += 1
    angle = math.degrees(ball.current_theta)
    angle = 360 - angle
    ball.current_theta = math.radians(angle)
    # print(COUNTER)
    if(COUNTER == 18):
        COUNTER = 0
        return 10
    else:
        return 7

def bat_ball_collision(ball):
    global COUNTER
    COUNTER = 0
    angle = math.degrees(ball.current_theta)
    angle = 180 - angle
    ball.current_theta = math.degrees(angle)
    # print(COUNTER)