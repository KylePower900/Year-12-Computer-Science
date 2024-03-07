import Entities as E
import pygame
import Configuration as C
import random
import time
class Battle():
    def __init__(self, heroes, enemies):
        self.heroes = heroes
        self.enemies = enemies
        self.hero_turns = len(heroes)
        self.turn = 'enemy'
        self.enemy_skill = []

    def Battle(self, clicked):
        #Enemy skill selection
        if self.turn == 'enemy':
            self.enemy_skill.clear()
            for enemy in self.enemies:
                self.enemy_skill.append(enemy.abilities[random.randint(0,5)])

            for i in self.enemies:
                i.target = self.heroes[random.randint(0,len(self.heroes)-1)]

            self.turn = 'player'
        
        elif self.turn == 'player':
            if time.time() % 0.5 > 0.25:
                for i in self.enemies:
                    pygame.draw.line(C.SCREEN, C.RED, (i.target.rect.midright), (i.rect.midleft), 10)

            if self.hero_turns == 0:
                self.turn = 'enemy'
                self.hero_turns = len(self.heroes)
                for i in range(0,len(self.enemies)-1):
                    self.enemy_skill[i]
        
            if E.stab.Used(self.enemies, clicked) == True:
                self.hero_turns -= 1

        else:
            print("Battle Function Error")

        for i in self.enemies:
            if i.health <= 0: 
                self.enemies.remove(i)




        


        
            
        
        

battle = Battle(E.party, E.enemies)
