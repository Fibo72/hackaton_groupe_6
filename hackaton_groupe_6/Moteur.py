import pygame as pg
import random

screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
c = 1
jeu = True
pos = (0, 0)
HP = 10
Armor = 5
Ad = 2
Ap = 0


class Character:
    def __init__(self, HP = 10, Armor = 5, Rm = 5, Ad = 2, Ap = 0, trend = 0.5):
        self.HP = HP
        self.Armor = Armor
        self.Rm = Rm
        self.Ad = Ad
        self.Ap = Ap
        self.trend = trend



        

class John_Lennon(Character):
        def __init__(self, pos, inventory = {'potion' : 0}, HP = 10, Armor = 5, Rm = 5, Ad = 2, Ap = 0):
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
                            if event.type == pg.QUIT:
                                global jeu
                                jeu = False
                                break

                
                if action == "attack":
                    ennemy.HP = ennemy.HP - int(self.Ad / ennemy.Armor) - 1
                elif action == "magic":
                    ennemy.HP = ennemy.HP - int(self.Ap / ennemy.Rm) - 1
                
                if ennemy.Hp > 0:
                    k = random.random()
                    if k > ennemy.trend:
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
            if thing == 'P':
                self.inventory['potion'] += 1
            elif thing == 'AL':
                ennemy = Character()
                self.combat(ennemy)


