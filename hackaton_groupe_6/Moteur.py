import pygame as pg
import random

clock = pg.time.Clock()
c = 1
jeu = True
pos = (0, 0)
HP = 10
Armor = 5
Ad = 2
Ap = 0

cafard = {'HP' : 5, 'Armor' : 5, 'Rm' : 2, 'Ad' : 3, 'Ap' : 1, 'trend' : 0.75}
LAFOOOON = {'HP' : 100, 'Armor' : 100, 'Rm' : 100, 'Ad' : 100, 'Ap' : 100, 'trend' : 0.5}
ratz = {'HP' : 5, 'Armor' : 2, 'Rm' : 5, 'Ad' : 1, 'Ap' : 3, 'trend' : 0.25}
BALKANY = {'HP' : 80, 'Armor' : 35, 'Rm' : 45, 'Ad' :5, 'Ap' : 35, 'trend' : 0.15}

class Character:
    def __init__(self, HP = 10, Armor = 5, Rm = 5, Ad = 2, Ap = 0, trend = 0.5):
        self.HP = HP
        self.Armor = Armor
        self.Rm = Rm
        self.Ad = Ad
        self.Ap = Ap
        self.trend = trend



        

class John_Lennon:
        def __init__(self, pos, inventory = {'potion' : 0, 'moula' : 10}, HP = 10, Armor = 5, Rm = 5, Ad = 2, Ap = 0):
            self.HP = HP
            self.inventory = inventory
            self.Armor = Armor
            self.Rm = Rm
            self.Ad = Ad
            self.Ap = Ap
            self.pos = pos
        
        def avance(self, dir, map):
            if dir == 0 and map[self.pos[1] + 1][self.pos[0]] not in ['|', '-']:
                return (self.pos[0], self.pos[1] + 1)
            elif dir == 1 and map[self.pos[1]][self.pos[0] + 1] not in ['|', '-']:
                return (self.pos[0] + 1, self.pos[1])
            elif dir == 2 and map[self.pos[1] - 1][self.pos[0]] not in ['|', '-']:
                return (self.pos[0], self.pos[1] - 1)
            elif dir == 3 and map[self.pos[1]][self.pos[0] - 1] not in ['|', '-']:
                return (self.pos[0] - 1, self.pos[1])
            else:
                return self.pos
        
        def combat(self, ennemy):
            while self.HP > 0:
                action = None
                while action == None:
                    clock.tick(c)
                    for event in pg.event.get():

                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_a:
                                action = "attack"
                            if event.key == pg.K_m:
                                action = "magic"
                            if event.key == pg.K_p:
                                action = 'potion'
                        if event.type == pg.QUIT:
                            global jeu
                            jeu = False
                            break

                
                if action == "attack":
                    ennemy.HP = ennemy.HP - int(self.Ad / ennemy.Armor) - 1
                    acted = True
                elif action == "magic":
                    ennemy.HP = ennemy.HP - int(self.Ap / ennemy.Rm) - 1
                    acted = True
                elif action == 'potion':
                    if self.inventory['potion'] > 0:
                        self.inventory['potion'] += -1
                        self.HP += 20
                        acted = True
                if acted:
                    if ennemy.Hp > 0:
                        k = random.random()
                        if k < ennemy.trend:
                            ennemy_action = "attack"
                        else:
                            ennemy_action = "magic"
                        
                        if ennemy_action == "attack":
                            self.HP = self.HP - int(ennemy.Ad / self.Armor) - 1
                        elif action == "magic":
                            self.HP = self.HP - int(ennemy.Ap / self.Rm) - 1
                    else:
                        return True
            return False
        
        def interact(self, map):
            thing = map[self.position[1]][self.position[0]]
            if thing == 'P':#potion
                self.inventory['potion'] += 1
            elif thing == 'S':#long sword
                self.Ad += 5
            elif thing == 'A':#cloth armor
                self.Armor += 5
            elif thing == 'T':#amplifiyng tome
                self.Ap += 5
            elif thing == 'C':#null-magic Tome
                self.Rm += 5
            elif thing == 't':#Thune
                self.inventory['moula'] += 5
            elif thing == 'c':
                ennemy = Character(**cafard)
                self.combat(ennemy)
            elif thing == 'r':
                ennemy == Character(**ratz)
                self.combat(ennemy)
            elif thing == 'B':
                ennemy = Character(**BALKANY)
                self.combat(ennemy)
            elif thing == 'L':#LAFOOOON
                ennemy = Character(**LAFOOOON)
                self.combat(ennemy)

        def shop(self):
            buy = True
            while buy:
                item = None
                while item == None:
                        clock.tick(c)
                        for event in pg.event.get():

                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_s:
                                    item = "long sword"
                                if event.key == pg.K_t:
                                    item = "amplifying tome"
                                if event.key == pg.K_c:
                                    item = 'null-magic cape'
                                if event.key == pg.K_a:
                                    item = 'cloth armor'
                                if event.key == pg.K_p:
                                    item = 'potion'
                                if event.key == pg.K_q:
                                    item = 0
                                    buy = False
                            if event.type == pg.QUIT:
                                global jeu
                                jeu = False
                                break
                if item == "long sword" and self.inventory['moula'] >= 5:
                    self.inventory['moula'] += -5
                    self.Ad += 5
                elif item == "null-magic cape" and self.inventory['moula'] >= 5:
                    self.inventory['moula'] += -5
                    self.Rm += 5
                elif item == "cloth armor" and self.inventory['moula'] >= 5:
                    self.inventory['moula'] += -5
                    self.Armor += 5
                elif item == "amplifying tome" and self.inventory['moula'] >= 5:
                    self.inventory['moula'] += -5
                    self.Ap += 5
                elif item == "potion" and self.inventory['moula'] >= 5:
                    self.inventory['moula'] += -5
                    self.inventory['potion'] += 1

        def inventaire(self):
            inventory = True
            while inventory:
                item = None
                while item == None:
                        clock.tick(c)
                        for event in pg.event.get():

                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_p:
                                    item = 'potion'
                                if event.key == pg.K_q:
                                    item = 0
                                    inventory = False
                            if event.type == pg.QUIT:
                                global jeu
                                jeu = False
                                break
                if item == "potion" and self.inventory['potion'] >= 1:
                    self.inventory['potion'] += -1
                    self.HP += 20
