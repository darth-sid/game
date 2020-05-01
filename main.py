import os, sys, random, time, pygame
from pygame.locals import *
import pygame.gfxdraw

pygame.init()
pygame.font.init()

Black = (0,0,0)
Yellow = (255,225,0)
Brown = (139,69,19)

started = False
X='x'
Y='y'
xvec = 6
yvec = 6 
days = 0

size = 320
screen = pygame.display.set_mode((size, size))
screen.fill(Black)

running = True


class Butter(pygame.sprite.Sprite):
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
    def pos(self, xy):
        if xy == X:
            return self.rect.x
        elif xy == Y:
            return self.rect.y

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
    def follow(self, target):
        self.rect.x = target[0]-40
    def pos(self, xy):
        if xy == X:
            return self.rect.x
        elif xy == Y:
            return self.rect.y

class Button(pygame.sprite.Sprite):
    def __init__(self, text, border, font, color, hover_color, x, y):
        pygame.sprite.Sprite.__init__(self)

        #default text
        self.txt = font.render(text, True, color)

        #hover text
        self.hover_txt = font.render(text, True, hover_color)
        
        #colors
        self.color = color
        self.hover_color = hover_color
        #border
        self.border = border

        #button surface
        self.image = pygame.Surface((self.txt.get_width()+(2*self.border),self.txt.get_height()+(2*self.border)))

        #color and setup
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        #location
        self.rect.x = x-self.txt.get_width()/2
        self.rect.y = y-self.txt.get_height()/2     
        self.interior = pygame.draw.rect(self.image, Black, (self.border,self.border,self.txt.get_width(),self.txt.get_height()))
        
        self.image.blit(self.txt ,(self.border,self.border))

    #returns boolean for whether the mouse is over the button or not
    def mouse_detect(self):
        pos = pygame.mouse.get_pos()
        #-------------------------------------------------
        mouse_over_button = (pos[0] > self.rect.x and pos[0] < self.rect.x + self.txt.get_width()+2*self.border and pos[1] > self.rect.y and pos[1] < self.rect.y + self.txt.get_height()+2*self.border)
        #-------------------------------------------------

        if mouse_over_button:
            self.image.fill(self.hover_color)
            self.interior = pygame.draw.rect(self.image, Black, (self.border,self.border,self.txt.get_width(),self.txt.get_height()))

            self.image.blit(self.hover_txt ,(self.border,self.border))

            return True
        else:
            self.image.fill(self.color)
            self.interior = pygame.draw.rect(self.image, Black, (self.border,self.border,self.txt.get_width(),self.txt.get_height()))
            self.image.blit(self.txt ,(self.border,self.border))
            return False

boton = Button('Start', 4, pygame.font.SysFont("sfnstextcondense", 32), (255,255,0), (255, 125, 0),160,240)
butter = Butter()
bageht = Bread()

menusprites = pygame.sprite.Group((boton))
sprites=pygame.sprite.Group((butter,bageht))
while running:
    if started:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                
#    if key[K_RIGHT]:
#        bageht.move(1)
#    if key[K_LEFT]:
#        bageht.move(-1)

    #roof detection
        if butter.pos(Y) <= 0:
            yvec = yvec * -1

	#wall detection
        if butter.pos(X) <= 0 or butter.pos(X) >= size-40:
            xvec = xvec * -1

        butter.move(xvec,yvec)

        bageht.follow(pygame.mouse.get_pos())
        if pygame.mouse.get_pos()[0] > bageht.pos(X):
            vel = 'r'
        elif pygame.mouse.get_pos()[0] < bageht.pos(X):
            vel = 'l'

        if butter.pos(X) >= bageht.pos(X) and butter.pos(X) <= bageht.pos(X)+80:
            aligned = True
        elif butter.pos(X)+40 >= bageht.pos(X) and butter.pos(X)+40 <= bageht.pos(X)+80:
            aligned = True
        else:
            aligned = False
        if butter.pos(Y)+20 >= bageht.pos(Y) and aligned:
            yvec = yvec * -1
            days += 1
            if vel == "r":
                xvec += 2
            elif vel == "l":
                xvec -= 2

        if butter.pos(Y) >= 340:
            running = False

        screen.fill(Black)
        sprites.draw(screen)
        pygame.display.flip()
    else:
        key = pygame.key.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            else:
                click = False

        if boton.mouse_detect() and click:
            started = True
        
        font = pygame.font.SysFont("sfnstextcondensed", 32)
        text = font.render("Keep Butter Alive!", True, (255, 255, 0))
        screen.fill(Black)
        menusprites.draw(screen)
        screen.blit(text,(160 - text.get_width() // 2, 80 - text.get_height() // 2))
        pygame.display.flip()
