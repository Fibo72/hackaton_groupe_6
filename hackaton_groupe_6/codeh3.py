#!/usr/bin/env python

# les imports standard en premier
from random import randint

import pygame as pg

# on initialise pygame et on crée une fenêtre de 400x300 pixels
pg.init()
jeu = True
black = (0,0,0)
screen = pg.display.set_mode((400, 300))
screen.fill(black)
snake = [
    (10, 15),
    (11, 15),
    (12, 15),
]
tete = snake[-1]
direction = ['r', 'l', 'u', 'd']
direction0 = 'r'
direction1 = 'r'
count = 0
fruit = (randint(0,39), randint(0,29))
c = 3

# Objet de gestion du temps
clock = pg.time.Clock()

#Importation images
albanlafont = pg.image.load("albanlafont2.png")
johnlennon = pg.image.load("johnlennon.png")
mur = pg.image.load("hippievert.png")
balkanyface = pg.image.load("patrick-balkany.png")
balkanydance1 = pg.image.load("patrickv2.png")
balkanydance2 = pg.image.load("patrickv3.png")

#mise à l'échelle images
albanlafont = pg.transform.scale(albanlafont, (10, 10))
johnlennon = pg.transform.scale(johnlennon, (10, 10))
mur = pg.transform.scale(mur, (10, 10))
balkanydance2 = pg.transform.scale(balkanydance2, (10, 10))
balkanydance1 = pg.transform.scale(balkanydance1, (10, 10))
balkanyface = pg.transform.scale(balkanyface, (10, 10))

while jeu:
    clock.tick(c)

    #les evenements
    for event in pg.event.get():
         direction1 = direction0
         if event.type == 769:
            if event.key == 113:
                jeu = False
            elif event.key == 108: #l
                 direction0 = 'r'
            
            elif event.key == 106: #j
                direction0 = 'l'
            
            elif event.key == 107: #k
                direction0 = 'd'
            
            elif event.key == 105: #i
                direction0 = 'u'
    
    #le niveau 
    screen.fill(black)
    for i in range(40):
        for j in range(30):
            if (i + j) % 2 == 0:
                rect = pg.Rect(i*10, j*10, 10, 10)
                color1 = (150, 200, 0) # vert
                pg.draw.rect(screen, color1, rect)
    
    #le fruit
    if fruit in snake:
        fruit = (randint(0,39), randint(0,29))
    a,b = fruit
    rect = pg.Rect(a*10, b*10, 10, 10)
    color2 = (0, 0, 255) # bleu
    pg.draw.rect(screen, color2, rect)
    pg.display.update()

   #le mouvement
    tete = snake[-1]
    x,y = tete
    if direction0 == 'r':
        x += 1
    elif direction0 == 'l':
        x -= 1
    elif direction0 == 'd':
        y += 1
    elif direction0 == 'u':
        y -= 1
    if (x,y) == fruit:
        snake = snake + [(x,y)]
        fruit = (randint(0,39),randint(0,29))
        count += 1
        c += 1
    else:
        snake = snake[1:] + [(x,y)]

    #le serpent
    for i, j in snake:
        rect = pg.Rect(i*10, j*10, 10, 10)
        black = (0,0,0) # noir
        pg.draw.rect(screen, black, rect )
    
    #condition de defaite:
    if (x>=40) or (x<0) or (y>=30) or (y<0):
        jeu = False
    if tete in snake[:-2]:
        jeu = False
    if direction0 == 'r' and direction1 == 'l':
        jeu = False
    if direction0 == 'l' and direction1 == 'r':
        jeu = False
    if direction0 == 'u' and direction1 == 'd':
        jeu = False
    if direction0 == 'd' and direction1 == 'u':
        jeu = False

    # Dessiner l'image du personnage à l'écran
    screen.blit(albanlafont, (100, 100))
    screen.blit(johnlennon, (300, 300))
    screen.blit(mur, (400, 100))
    screen.blit(balkanyface, (50, 50))
    screen.blit(balkanydance1, (50, 100))
    screen.blit(balkanydance2, (60, 80))


    pg.display.update()
print('Game Over, score =',count)
pg.quit()