#!/usr/bin/env python

# les imports standard en premier
from random import randint

import pygame as pg
from pyganim import PygAnimation

# on initialise pygame et on crée une fenêtre 
pg.init()
jeu = True
black = (0,0,0)
screen = pg.display.set_mode((1000, 800))
pg.display.set_caption('Donjon Lennon')
screen.fill(black)

#message début
message = "Il était une fois, John Lennon, le célèbre membre des Beatles, qui avait quitté la scène pour vivre une vie de hippie, se consacrant à la paix et à l'amour. Il passait ses journées à organiser des manifestations pacifistes et à jouer de la musique pour des causes sociales. / Un jour, alors qu'il participait à une manifestation pour la paix, il rencontra Alban Lafont, le gardien de but du FC Nantes. Ce dernier lui parla d'un donjon caché, rempli d'un trésor incroyable qui pourrait aider à financer des projets pour les moins favorisés. John, intrigué, décida de suivre Alban dans cette aventure./ Mais une fois arrivé dans le donjon, John se rendit compte qu'Alban avait menti, et que le donjon était rempli de pièges et de monstres redoutables. Pire encore, Alban révéla qu'il n'était pas là pour aider les moins favorisés mais pour s'enrichir personnellement./ John, déçu mais déterminé, décida de continuer l'aventure, utilisant ses talents de musicien pour calmer les monstres et sa philosophie pacifiste pour convaincre Alban de changer de voie. Il avança bravement dans les couloirs sombres, luttant contre des hordes de créatures maléfiques..."

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

# police  
font = pg.font.Font('vinque rg.otf', 30)

etat_balkany = 1

refreshrate = 5


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    # Dessiner chaque lettre du message
    largeur = 30
    hauteur = 0
    screen.fill((0, 0, 0))
    for i, lettre in enumerate(message):
        clock.tick(20)
        pg.event.get()
        if lettre != '/':
            message_affiche = font.render(lettre, True, (255, 255, 255))
            screen.blit(message_affiche, (largeur, hauteur))
            largeur += font.size(lettre)[0]
            if largeur >= 950 :
                hauteur += 30
                largeur = 10
        else:
            hauteur += 70
            largeur = 30
        pg.display.update()
        #pg.time.wait(100)  # Attendre 100ms avant d'afficher la prochaine lettre
    pg.time.wait(5000) #avant de commencer le menu

    while jeu:
        clock.tick(refreshrate)

        screen.fill(black)

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
        #screen.blit(balkanydance1, (50, 100))
        #screen.blit(balkanydance2, (60, 80))

        score = 1
        armure = 1
        moula = 1
        vie = 1

        

        # textes compteurs
        score_text = font.render("Score: " + str(score), 1, (255, 255, 255))
        armor_text = font.render("Armure: " + str(armure), 1, (255, 255, 255))
        moula_text = font.render("Moula: " + str(moula), 1, (255, 255, 255))
        vie_text = font.render("Vie: " + str(vie), 1, (255, 255, 255))

        # affichage compteurs
        screen.blit(score_text, (10, 10))
        screen.blit(armor_text, (210, 10))
        screen.blit(moula_text, (410, 10))
        screen.blit(vie_text, (610, 10))

        

        if etat_balkany == 1:
            screen.blit(balkanydance1, (100, 100))
            etat_balkany = 2
                
        elif etat_balkany == 2:
            screen.blit(balkanydance2, (100, 100))
            etat_balkany = 1
        
                


        

        # affichage à la mort
        #gameover_text = font.render("GAME OVER", 1, (255, 255, 255))
        #screen.blit(gameover_text, (500, 400))


        pg.display.update()

    pg.quit()