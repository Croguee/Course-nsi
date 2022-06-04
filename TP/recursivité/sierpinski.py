#!/usr/bin/python
# coding: utf-8

import pygame
import sys
import time

A = (0,0)
B = (800,0)
C = (400,600)
coord = (A,B,C)

pygame.init()

white   = (255, 255, 255)
blue     = (0, 0, 255)
black =(0,0,0)
size = [800,800]

fenetre = pygame.display.set_mode(size)
fenetre.fill(white)
# voir https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon
pygame.draw.polygon(fenetre, blue, ((0,0),(800,0),(400,600)),0)


def milieu(A, B):
    xm = (A[0] + B[0])//2
    ym = (A[1] + B[1])//2
    return (xm, ym)
    
    
def sierpinski(n, coord):
    if n >=0:
        E = milieu(coord[0], coord[1])
        F = milieu(coord[1], coord[2])
        G = milieu(coord[2], coord[0]) 
        
        pygame.draw.polygon(fenetre, white, (E,F,G), 0)
        
        pygame.display.flip()
        time.sleep(0.05)
        sierpinski(n-1, (coord[0], E, G))
        sierpinski(n-1, (E, coord[1], F))
        sierpinski(n-1, (G, F, coord[2]))
        
sierpinski(7, coord)


# Boucle infinie qui attend l'événement QUIT pour terminer le programme
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()













