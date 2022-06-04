#!/usr/bin/python
# coding: utf-8

import pygame
import sys
import time

length = 800

A = (0,0)
B = (length,0)
C = (length, length)
D = (0, length)
points = (A, B ,C ,D)

pygame.init()

white   = (255, 255, 255)
blue     = (0, 0, 255)
black =(0,0,0)
size = [length,length]

fenetre = pygame.display.set_mode(size)
fenetre.fill(white)
# voir https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon
pygame.draw.polygon(fenetre, blue, (A, B, C, D))



def sierpinski(points):
#    if n >=0: 

        E = (B[0]/3, B[1])
        F = (2*B[0]/3, B[1])
        G = (F[0], 2*D[1]/3) 
        H = (E[0], G[1]) 
        
        pygame.draw.polygon(fenetre, white, (E,F,G,H))
        pygame.display.flip()
#        time.sleep(0.05)
#        sierpinski(n-1, (coord[0], F, G, H))
#        sierpinski(n-1, (E, coord[1], G, H))
#        sierpinski(n-1, (E, F, coord[2], H))
#        sierpinski(n-1, (E, F, G, coord[3]))
        
sierpinski(points)

pygame.display.flip()

# Boucle infinie qui attend l'événement QUIT pour terminer le programme
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


