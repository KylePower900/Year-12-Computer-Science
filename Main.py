import pygame
import Configuration as C
import Entities as E
import Battle as B
import random
pygame.init()

C.SCREEN.fill(C.WHITE)

def Display(clicked):
    #Background first
    for i in E.background:
        i.Draw(C.SCREEN)

    for i in range(len(E.party)):
        E.party[i].Draw(C.SCREEN, i)
    
    for i in range(len(E.enemies)):
        E.enemies[i].Draw(C.SCREEN,i)

    for i in E.party:
        i.Hover(C.SCREEN)
        
    for i in E.enemies:
        i.Hover(C.SCREEN)

class Game:
    def __init__(self):
        self.running = True
        self.clicked = False
        self.screen_colour = C.WHITE        
        
    def Main(self):
        while self.running:  
            self.clicked = False
            pygame.time.Clock().tick(200)
            C.SCREEN.fill(self.screen_colour)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    self.running = False
                elif i.type == pygame.MOUSEBUTTONUP:
                    self.clicked = True

            B.battle.Battle(self.clicked)
            Display(self.clicked)


            pygame.display.update()

game = Game()
game.Main()