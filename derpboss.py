
import pygame
import random

from global_stuff import *
from basicsprite import BasicSprite

class DerpBoss(BasicSprite):
    def __init__(self, pos):
        r = pygame.Rect(pos,(2*ICON_SIZE,2*ICON_SIZE))
        BasicSprite.__init__(self, r, health=150, mass=2.0, numberOfFrames=2)
        
        self.waitTime = random.randint(300,500)
        
    def tick(self, room):
        BasicSprite.tick(self, room)
        if not self.isFalling:
            self.waitTime -= 1
            if self.waitTime < 0:
                self.waitTime = random.randint(300,500)
                self.yspeed = -1.0*random.randint(20,30) * ICON_SIZE / FPS
                self.xspeed = 1.0*random.randint(-3,3) * ICON_SIZE / FPS
            
