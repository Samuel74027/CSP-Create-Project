###################################################################
#                                                                 #
#               Program 1 - By Yen-Lin Lee                        #
#                last revised: 10/18/21                           #
#           You are died when your health is 0. Invader will      #
#           bounce around the screen. Try to kill all of them!    #
#                                                                 #
###################################################################
#Import library
from ast import Num
import pygame, math, sys
import random

# Screen constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700
BLACK = (0, 0, 0)

#Setup Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Missile Detector')


pygame.init()

#image constants
background = pygame.image.load('./map.png')
background = pygame.transform.scale(background, (1200, 700))


#missle detection 
class Missle():
    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y
        
#
# Game loop
running = True
while running:
    # redraw game Screen
    screen.blit(background, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
