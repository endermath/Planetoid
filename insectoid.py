
import pygame
import random

from global_stuff import *
from basicsprite import BasicSprite


class Insectoid(BasicSprite):
    def __init__(self, pos):
        r = pygame.Rect(pos,(ICON_SIZE,ICON_SIZE))
        BasicSprite.__init__(self, r, numberOfFrames=3, health=20, mass=0.6)
        
        self.moveTime = random.randint(100,200)
        self.xspeed = 4.0 * ICON_SIZE / FPS
    
    def bumpedWall(self):
        self.xspeed = - self.xspeed             #bouncing.
    
    def bumpedRoof(self):
        self.yspeed = - self.yspeed * 0.9       #bouncing!
        
    def tick(self, room):
        BasicSprite.tick(self,room)
        self.moveTime -= 1
        if self.moveTime < 0:
            self.moveTime = random.randint(100,200)
            self.yspeed = - 15.0 * ICON_SIZE/FPS            #jump randomly
    