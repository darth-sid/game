import os, sys, random, time, pygame
from pygame.locals import *
import pygame.gfxdraw

pygame.init()

Black = (0,0,0)
Yellow = (255,225,0)
Brown = (139,69,19)

size = 320
screen = pygame.display.set_mode((size, size))
screen.fill(Black)

running = True


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size/6,size/16))
        self.image.fill((Yellow))
        self.rect = self.image.get_rect()
        self.rect.x = size/2
        self.rect.y = 1
    def move(self,xvec,yvec):
        self.rect.x += xvec
        self.rect.y += yvec

class Bread(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80,20))
        self.image.fill(Brown)
        self.rect = self.image.get_rect()
        self.rect.x = size/2 - 40
        self.rect.y = size - 50
    def move(self, vec):
        self.rect.x += vec
        
ball = Ball()
bageht = Bread()

sprites=pygame.sprite.Group((ball,bageht))
while running:
    key = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    
    if key[K_RIGHT]:
        bageht.move(1)
    if key[K_LEFT]:
        bageht.move(-1)
    ball.move(0,1)

    screen.fill(Black)
    sprites.draw(screen)
    pygame.display.flip()
