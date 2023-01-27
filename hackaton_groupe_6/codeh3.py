#!/usr/bin/env python

# les imports standard en premier
from random import randint
import numpy as np

import pygame as pg
from pyganim import PygAnimation

# on initialise pygame et on crée une fenêtre 
pg.init()
jeu = True
black = (0,0,0)
ecran = pg.display.set_mode((1000, 800))
pg.display.set_caption('Donjohn Lennon')
ecran.fill(black)

#message début
message = "Il était une fois, John Lennon, le célèbre membre des Beatles, qui avait quitté la scène pour vivre une vie de hippie, se consacrant à la paix et à l'amour. Il passait ses journées à organiser des manifestations pacifistes et à jouer de la musique pour des causes sociales. / Un jour, alors qu'il participait à une manifestation pour la paix, il rencontra Alban Lafont, le gardien de but du FC Nantes. Ce dernier lui parla d'un donjon caché, rempli d'un trésor incroyable qui pourrait aider à financer des projets pour les moins favorisés. John, intrigué, décida de suivre Alban dans cette aventure./ Mais une fois arrivé dans le donjon, John se rendit compte qu'Alban avait menti, et que le donjon était rempli de pièges et de monstres redoutables. Pire encore, Alban révéla qu'il n'était pas là pour aider les moins favorisés mais pour s'enrichir personnellement./ John, déçu mais déterminé, décida de continuer l'aventure, utilisant ses talents de musicien pour calmer les monstres et sa philosophie pacifiste pour convaincre Alban de changer de voie. Il avança bravement dans les couloirs sombres, luttant contre des hordes de créatures maléfiques..."

# Objet de gestion du temps
clock = pg.time.Clock()

#Importation images
albanlafont = pg.image.load("albanlafont2.png")
johnlennon = pg.image.load("johnlennon.png")
murs = pg.image.load("hippievert.png")
balkanyface = pg.image.load("patrick-balkany.png")
balkanydance1 = pg.image.load("patrickv2.png")
balkanydance2 = pg.image.load("patrickv3.png")

#mise à l'échelle images
albanlafont = pg.transform.scale(albanlafont, (50, 50))
johnlennon = pg.transform.scale(johnlennon, (50, 50))
murs = pg.transform.scale(murs, (50, 50))
balkanydance2 = pg.transform.scale(balkanydance2, (50, 50))
balkanydance1 = pg.transform.scale(balkanydance1, (50, 50))
balkanyface = pg.transform.scale(balkanyface, (50, 50))

# police  
font = pg.font.Font('vinque rg.otf', 30)

etat_balkany = 1

refreshrate = 5

cnt_lvl = 0


    
# pg.init()
# black = (0,0,0)
# ecran = pg.display.set_mode((1000, 800))
# pg.display.set_caption('Donjon Lennon')
for event in pg.event.get():
    if event.type == pg.QUIT:
        pg.quit()

# Dessiner chaque lettre du message
largeur = 30
hauteur = 0
ecran.fill((0, 0, 0))
for i, lettre in enumerate(message):
    clock.tick(20)
    pg.event.get()
    if lettre != '/':
        message_affiche = font.render(lettre, True, (255, 255, 255))
        ecran.blit(message_affiche, (largeur, hauteur))
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

#menu

# ecran.fill(black)
# play_button = pg.draw.rect(screen, (0, 255, 0), (150, 250, 100, 50))
# quit_button = pg.draw.rect(screen, (255, 0, 0), (350, 250, 100, 50))
# play_text = font.render("Jouer", True, (0, 0, 0))
# quit_text = font.render("Quitter", True, (0, 0, 0))
# ecran.blit(play_text, (175, 265))
# ecran.blit(quit_text, (380, 265))

#events
# for event in pg.event.get():
#     if event.type == pg.QUIT:
#         pg.quit()
#     elif event.type == pg.MOUSEBUTTONDOWN:
#         if play_button.collidepoint(event.pos):
while jeu:
    clock.tick(refreshrate)

    ecran.fill(black)

    #les evenements
    for event in pg.event.get():
        if event.type == pg.QUIT:
            jeu = False
        
    
    #le niveau 

    # Dessins
    ecran.blit(albanlafont, (100, 100))
    ecran.blit(johnlennon, (300, 300))
    ecran.blit(murs, (400, 100))
    ecran.blit(balkanyface, (50, 50))
    #ecran.blit(balkanydance1, (50, 100))
    #ecran.blit(balkanydance2, (60, 80))

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
    ecran.blit(score_text, (10, 10))
    ecran.blit(armor_text, (210, 10))
    ecran.blit(moula_text, (410, 10))
    ecran.blit(vie_text, (610, 10))

    

    if etat_balkany == 1:
        ecran.blit(balkanydance1, (100, 100))
        etat_balkany = 2
            
    elif etat_balkany == 2:
        ecran.blit(balkanydance2, (100, 100))
        etat_balkany = 1
    
    #le niveau

    nrom = 2*cnt_lvl + 2
    Ldoor = []

    screen = np.zeros((100, 300))

    def createrom(): #fonction qui crée les délimitations des salles
        Lrom = []
        Lmur = []
        count = nrom
        while count > len(Lmur):
            i, j = randint(20, 80), randint(20,280)
            Lrom.append((i,j))
            lar = randint(2,4)
            lon = randint(5,10)
            
            rom = [(i + h,j + lon) for h in range(lar+1)] + [(i - h,j + lon) for h in range(1,lar+1)]
            rom += ([(i + h,j - lon) for h in range(lar+1)] + [(i - h,j - lon) for h in range(1,lar+1)])
            rom += ([(i + lar,j + h) for h in range(lon+1)] + [(i - lar,j + h) for h in range(1,lon+1)])
            rom += ([(i + lar,j - h) for h in range(lon+1)] + [(i - lar,j - h) for h in range(1,lon+1)])

            for mur in rom:
                if mur in Lmur:
                    Lrom.pop()
                else:
                    Lmur.append(rom)
                    break
        return Lmur

    Lmur = createrom()

    for rom in range(len(Lmur)): #création des murs et des portes

        for mur in Lmur[rom]:
            screen[mur] = 1
        
        door1 = randint(0,len(Lmur[rom])-1)
        screen[Lmur[rom][door1]] = 2
        door2 = randint(0,len(Lmur[rom])-1)

        while door2 == door1:
            door2 = randint(0,len(Lmur[rom])-1)
        
        screen[Lmur[rom][door2]] = 2
        a = Lmur[rom][door1]
        b = Lmur[rom][door2]
        Ldoor.append([a, b])

    def createpath(dep, arr): #crée un chemin entre 2 points en renvoyant une liste de points qui le compose sans passer à l'intérieur des salles
        Lpath = [dep]
        Lpathx = []
        Lpathy = []
        x, y = dep
        a, b = arr
        
        if x < a:
            Lpathx = [(x+i,y) for i in range(1,a-x)]
        elif x>a:
            Lpathx = [(x-i,y) for i in range(1,x-a)]
        if y < b:
            Lpathy = [(x,y+i) for i in range(1,b-y)]
        elif x>a:
            Lpathy = [(x,y-i) for i in range(1,y-b)]
        Lpath = Lpath + Lpathx + Lpathy
        return Lpath

    for rom in range(nrom):
        if rom < (nrom - 1):
            path = createpath(Ldoor[rom][0],Ldoor[rom + 1][1])
        else:
            path = createpath(Ldoor[rom][0],Ldoor[0][1])
        
        for case in path:
            if screen[case] == 1:
                screen[case] = 2

            elif screen[case] == 0:
                screen[case] = 3
    

    
        

    # affichage à la mort
    if vie == 0:
        screen.fill(black)
        gameover_text = font.render("GAME OVER", 1, (255, 255, 255))
        screen.blit(gameover_text, (500, 400))


    pg.display.update()

            # elif quit_button.collidepoint(event.pos):
            #     pg.quit()

    

pg.quit()