import random
import math
import pygame

from global_stuff import *
from basicsprite import BasicSprite

class Player(BasicSprite):
    
    hurtSound = None
    
    def __init__(self, pos):
        r = pygame.Rect(pos,(ICON_SIZE,ICON_SIZE))
        BasicSprite.__init__(self, r, health=15, mass=1.0)

        # graphics related
        self.movingRight = False
        self.movingLeft = False
        self.isWalking = False
        self.dir = 1
        
        # gameplay related
        self.canBeHurt = True
        self.hurtCounter = 0
        self.isShooting = False  #true when shooting
        self.score = 0
        self.hasBigWeapon = False

    
        
        
    def addScore(self,sc):
        self.score +=  sc 
    
    def tick(self, room):       
        BasicSprite.tick(self, room)
        if not self.canBeHurt:
            self.hurtCounter -= 1
            if self.hurtCounter < 0:
                self.canBeHurt = True
        
    def hit(self):
        if self.canBeHurt:
            BasicSprite.hit(self)
            self.canBeHurt = False
            self.hurtCounter = 40
            self.xspeed = - self.xspeed
            self.yspeed = 0 #random.gauss(-10,2) - self.yspeed
            Player.hurtSound.play()
        
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
        
        #if not self.isShooting:
        self.dir = -1
        
    def moveRight(self):
        self.isWalking = True
        self.movingRight = True
        self.movingLeft = False
        self.xspeed = 8.0*ICON_SIZE/FPS
        #if self.isFalling:
        #    self.xspeed = self.xspeed * 0.5
        
        
        #if not self.isShooting:
        self.dir = 1
        
    def jump(self):
        if self.isFalling:
            return              #can't jump in the air!
        self.yspeed = - 20.0 * ICON_SIZE/FPS
        
