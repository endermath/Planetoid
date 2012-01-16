import pygame
import math

from global_stuff import *
from basicsprite import BasicSprite

class Player(BasicSprite):
    dir = 1
    pellets = 0
    isShooting = False  #true when shooting
    score = 0
    
    def __init__(self, pos):
        r = pygame.Rect(pos,(ICON_SIZE,ICON_SIZE))
        BasicSprite.__init__(self, r, health=100, mass=1.0)

        # graphics related
        self.movingRight = False
        self.movingLeft = False
        self.isWalking = False
    
        
        
    def addScore(self,sc):
        self.score +=  sc 
    
    def tick(self, room):       
        BasicSprite.tick(self, room)
        
    def stopLeft(self):
        self.movingLeft = False
        if not self.movingRight:
            self.xspeed = 0
            self.isWalking = False
            
    def stopRight(self):
        self.movingRight = False
        if not self.movingLeft:
            self.xspeed = 0
            self.isWalking = False

    def moveLeft(self):
        self.isWalking = True
        self.movingLeft = True
        self.movingRight = False
        self.xspeed = -8.0*ICON_SIZE/FPS
        #if self.isFalling:
        #    self.xspeed = self.xspeed * 0.5
        if not self.isShooting:
            self.dir = -1
        
    def moveRight(self):
        self.isWalking = True
        self.movingRight = True
        self.movingLeft = False
        self.xspeed = 8.0*ICON_SIZE/FPS
        #if self.isFalling:
        #    self.xspeed = self.xspeed * 0.5
        if not self.isShooting:
            self.dir = 1
        
    def jump(self):
        if self.isFalling:
            return              #can't jump in the air!
        self.yspeed = - 20.0 * ICON_SIZE/FPS
        
    def hit(self):
        self.health -= 1
        