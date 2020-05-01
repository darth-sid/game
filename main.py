import os, sys, random, time, pygame
from pygame.locals import *
import pygame.gfxdraw

pygame.init()

size = 320
screen = pygame.display.set_mode((size, size))
screen.fill((0,0,0))

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
