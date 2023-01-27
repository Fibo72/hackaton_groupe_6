#!/usr/bin/env python

# les imports standard en premier
from random import randint

import pygame as pg

# on initialise pygame et on crée une fenêtre de 400x300 pixels
pg.init()
jeu = True
black = (0,0,0)
screen = pg.display.set_mode((1000, 800))
screen.fill(black)


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

refreshrate = 4

while jeu:
    clock.tick(refreshrate)

    #les evenements
    for event in pg.event.get():
        if event.type == pg.QUIT:
            jeu = False
         
    
    #le niveau 

    # Dessins
    screen.blit(albanlafont, (100, 100))
    screen.blit(johnlennon, (300, 300))
    screen.blit(mur, (400, 100))
    screen.blit(balkanyface, (50, 50))
    screen.blit(balkanydance1, (50, 100))
    screen.blit(balkanydance2, (60, 80))

    score = 1
    armure = 1
    moula = 1
    vie = 1

    # Compteurs graphiques  
    font = pg.font.Font('vinque rg.otf', 30)

    # Créer une image du texte du score
    score_text = font.render("Score: " + str(score), 1, (255, 255, 255))
    armor_text = font.render("Armure: " + str(armure), 1, (255, 255, 255))
    moula_text = font.render("Moula: " + str(moula), 1, (255, 255, 255))
    vie_text = font.render("Vie: " + str(vie), 1, (255, 255, 255))

    # Dessiner l'image du score à l'écran
    screen.blit(score_text, (10, 10))
    screen.blit(armor_text, (210, 10))
    screen.blit(moula_text, (410, 10))
    screen.blit(vie_text, (610, 10))

    #affichage à la mort
    gameover_text = font.render("GAME OVER", 1, (255, 255, 255))
    screen.blit(score_text, (500, 400))

    pg.display.update()

pg.quit()