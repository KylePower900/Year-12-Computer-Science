import pygame
import Configuration as C
import time
#Base class Entity
class Entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.hover_rect = pygame.rect.Rect((0,0),(300,100))
        self.hover = False

#Derived Class Hero
class Hero(Entity):
    def __init__(self, name, health, abilities):
        super().__init__(name, health)
        self.dimensions = (300,125)
        self.abilities = abilities
        self.surface = pygame.surface.Surface(self.dimensions)
        self.surface.fill(C.BLACK)
        self.rect = self.surface.get_rect()
        self.picture = pygame.surface.Surface((self.rect.width * 1/6, self.rect.width * 1/6))
        self.picture.fill(C.WHITE)
        self.incoming_attack = None
        self.attacker = None



        #Stats

    def Draw(self, screen, position):
        #Drawing coordinates
        self.rect.midleft = (C.SCREEN_WIDTH * 1/10, (C.SCREEN_HEIGHT * 5/6) * (1/(len(party)+1)) * (position + 1))
        screen.blit(self.surface, self.rect.topleft)
        
        #Health display of 10x10 pixels
        total_rows = int((self.max_health/10) + 1)
        rows = total_rows # 3

        while rows != 0:
            if rows != 1:
                health_row = 10
            else:
                health_row = self.max_health % 10
            for i in range(health_row):
                health_rect = pygame.rect.Rect(((self.rect.width/(health_row * 2))*((1/3) + i) + 1/2 * self.rect.width),
                                               ((self.rect.height/(total_rows+1))*(rows) ),
                                                (0.5 * self.rect.width * (1/8) * (1/3)),
                                                (0.5 * self.rect.width * (1/8) * (1/3))
                                                )
                pygame.draw.rect(self.surface, C.GREY, health_rect)
                if self.health > ((total_rows-rows)*10 + i):
                    pygame.draw.rect(self.surface, C.RED, health_rect)


            rows -=1

        screen.blit(self.surface, self.rect.topleft)
        
        #Drawing Icon
        self.picture_rect = self.picture.get_rect()
        self.picture_rect.center = (self.rect.left + self.rect.width * 1/6, self.rect.top + self.rect.height/2)
        screen.blit(self.picture, self.picture_rect)

    def Hover(self,screen):
        mousepos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousepos):
            self.hover = True
            if mousepos[0] < C.SCREEN_WIDTH/2:
                if mousepos[1] < C.SCREEN_HEIGHT/2:
                    self.hover_rect.topleft = mousepos
                else:
                    self.hover_rect.bottomleft = mousepos
            else:
                if mousepos[1] < C.SCREEN_HEIGHT/2:
                    self.hover_rect.topright = mousepos
                else:
                    self.hover_rect.bottomright = mousepos
        else:
            self.hover = False
        if self.hover == True:
            pygame.draw.rect(screen, C.GREEN, self.hover_rect)
            for i in range(len(self.abilities)):
                self.abilities[i].rect.center = (self.hover_rect.left + self.hover_rect.width/7 * (i+1) , self.hover_rect.top+ self.hover_rect.height * 3/4)
                pygame.draw.rect(screen, self.abilities[i].colour, self.abilities[i].rect)

    def IncomingAttack(self, attacker, attack):
        self.incoming_attack = attack
        self.attacker = attacker

#Derived Class Monster
class Monster(Entity):
    def __init__(self, name, health,abilities):
        super().__init__(name, health)
        self.dimensions = (300,100)
        self.abilities = abilities
        self.surface = pygame.surface.Surface(self.dimensions)
        self.surface.fill((0,0,0))
        self.rect = self.surface.get_rect()

        self.picture = pygame.surface.Surface((self.rect.width * 1/6, self.rect.width * 1/6))
        self.picture.fill(C.WHITE)

        self.target = None

    def Draw(self, screen, position):
        #Drawing coordinates
        self.rect.midright = (C.SCREEN_WIDTH * 9/10, (C.SCREEN_HEIGHT * 5/6) * (1/(len(enemies)+1)) * (position + 1))
        screen.blit(self.surface, self.rect.topleft)

        #Health display of 10x10 pixels
        total_rows = int((self.max_health/10) + 1)
        rows = total_rows # 3

        while rows != 0:
            if rows != 1:
                health_row = 10
            else:
                health_row = self.max_health % 10
            for i in range(health_row):
                health_rect = pygame.rect.Rect(((self.rect.width/(health_row * 2))*((1/3) + i) + 1/2 * self.rect.width),
                                               ((self.rect.height/(total_rows+1))*(rows) ),
                                                (0.5 * self.rect.width * (1/8) * (1/3)),
                                                (0.5 * self.rect.width * (1/8) * (1/3))
                                                )
                pygame.draw.rect(self.surface, C.GREY, health_rect)
                if self.health > ((total_rows-rows)*10 + i):
                    pygame.draw.rect(self.surface, C.RED, health_rect)
            rows -=1
        screen.blit(self.surface, self.rect.topleft)
        
        #Drawing Icon
        self.picture_rect = self.picture.get_rect()
        self.picture_rect.center = (self.rect.left + self.rect.width * 1/6, self.rect.top + self.rect.height/2)
        screen.blit(self.picture, self.picture_rect)

    def Hover(self,screen):
        mousepos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousepos):
            self.hover = True
            if mousepos[0] < C.SCREEN_WIDTH/2:
                if mousepos[1] < C.SCREEN_HEIGHT/2:
                    self.hover_rect.topleft = mousepos
                else:
                    self.hover_rect.bottomleft = mousepos
            else:
                if mousepos[1] < C.SCREEN_HEIGHT/2:
                    self.hover_rect.topright = mousepos
                else:
                    self.hover_rect.bottomright = mousepos
        else:
            self.hover = False
        if self.hover == True:
            pygame.draw.rect(screen, C.GREEN, self.hover_rect)
            for i in range(len(self.abilities)):
                self.abilities[i].rect.center = (self.hover_rect.left + self.hover_rect.width/7 * (i+1) , self.hover_rect.top+ self.hover_rect.height * 3/4)
                pygame.draw.rect(screen, self.abilities[i].colour, self.abilities[i].rect)

class Skill:
    def __init__(self, name):
        self.name = name
        self.rect = pygame.rect.Rect((0,0),(20,20))

class AttackSkill(Skill):
    def __init__(self, name, damage, colour):
        super().__init__(name)
        self.damage = damage
        self.colour = colour

    def Used(self, enemies, clicked):
        mousepos = pygame.mouse.get_pos()
        for i in enemies:
            if i.rect.collidepoint(mousepos) and clicked == True:
                i.health -= self.damage
                print("health taken from " + i.name)
                return True
        
    def Reverse(self, target, hero_turns):
        target.health += self.damage
        hero_turns += 1

class SkillBar:
    def __init__(self):
        self.surface = pygame.surface.Surface((C.SCREEN_WIDTH, C.SCREEN_HEIGHT/6))
        self.rect = self.surface.get_rect()
        self.rect.topleft = (0, C.SCREEN_HEIGHT * 5/6)
        self.colour = C.BLUE
        self.skill_roll = []

    def Draw(self, screen):
        pygame.draw.rect(self.surface, C.BLUE, (0,0, self.rect.width, self.rect.height))
        for i in range(len(self.skill_roll)):
            


            skill_surface = pygame.surface.Surface((self.rect.height/2, self.rect.height/2))
            skill_rect = skill_surface.get_rect()
            skill_rect.center = ((self.rect.width/(len(self.skill_roll)+1))*(i+1), self.rect.height/2)



            pygame.draw.rect(self.surface, self.skill_roll[i-1].colour, skill_rect)
        screen.blit(self.surface, self.rect)
            


hero_skillbar = SkillBar()

background = [hero_skillbar]

strike = AttackSkill('Strike', 1, C.GREY)
stab = AttackSkill('Stab', 2, C.BLACK)
riposte = AttackSkill('Riposte', 3, C.BLUE)


hero1 = Hero('Hero', 15, [strike, stab, riposte, strike, strike, strike])
hero2 = Hero('Hero2', 5, [strike])
hero3 = Hero('Hero3', 3, [strike])


enemy1 = Monster('Monster', 25, [strike, strike, stab, strike, strike, strike])
enemy2 = Monster('Monster', 17, [strike, strike, stab, strike, strike, strike])

hero_skillbar.skill_roll.append(stab)
hero_skillbar.skill_roll.append(stab)
hero_skillbar.skill_roll.append(strike)
hero_skillbar.skill_roll.append(strike)
hero_skillbar.skill_roll.append(strike)
hero_skillbar.skill_roll.append(strike)

party = [hero1, hero2]

enemies = [enemy1, enemy2]