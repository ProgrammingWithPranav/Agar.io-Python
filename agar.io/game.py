import pygame
import os
from _thread import  *
pygame.font.init()

#constants
PLAYER_RADIUS = 10
START_VEL = 9
BALL_RADIUS = 5

WIDTH, HEIGHT = 1000, 700

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agar.io By Programming with Pranav")

NAME_FONT = pygame.font.SysFont("comicsans", 20)
TIME_FONT = pygame.font.SysFont("comicsans", 30)
SCORE_FONT = pygame.font.SysFont("comicsans", 26)

COLORS = [(255,0,0), (255, 128, 0), (255,255,0), (128,255,0),(0,255,0),(0,255,128),(0,255,255),(0, 128, 255), (0,0,255), (0,0,255), (128,0,255),(255,0,255), (255,0,128),(128,128,128), (0,0,0)]

#functions
def convert_time(time):
    if type(time) == str:
        return t
    if int(time) < 60:
        return str(t) + "s"

    else:
        minutes = (t // 60)
        seconds = (t % 60)

        if int(seconds) < 10:
            seconds = "0" + seconds
        
        return minutes + ":" + seconds

def redraw_window():
    WIN.fill((255,255,255))

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        redraw_window()

main()


