import math

def wall_ball_collision(ball):
    angle = math.degrees(ball.current_theta)
    angle = 360 - angle
    if(angle < 20):
        angle = 45
    ball.current_theta = math.radians(angle)


def bat_ball_collision(ball):
    angle = math.degrees(ball.current_theta)
    angle = 180 - angle
    if(angle < 20):
        angle = 45
    ball.current_theta = math.degrees(angle)