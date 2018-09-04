#!/usr/bin/env python3

import pygame, sys
from pygame.locals import *

pygame.init()

x = int (input('Which size do you want for x? '))	#read the input from the keyboard 
y = int (input('Which size do you want for y? '))

screen = pygame.display.set_mode((x,y))			#set the size of the screen

clock = pygame.time.Clock()
screen.fill((255,255,255))				#fill the screen with the color of white

startx=int (x - x/2)					#calculate the number of the startpoint at the begining
starty=int (y - y/2)

while 1:
    clock.tick(60)
    pygame.draw.circle(screen, (0,0,0), (startx,starty),2)  #define the screen, the startpoint at the begining and the depth of the line
    pygame.display.update()
    key=pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:startx+=1				#define the regtions of the input from the keyboard
    if key[pygame.K_LEFT]:startx-=1 
    if key[pygame.K_UP]:starty-=1 
    if key[pygame.K_DOWN]:starty+=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            screen.fill((255,255,255))
