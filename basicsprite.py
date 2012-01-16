
import pygame
import random

from global_stuff import *


class BasicSprite:
    def __init__(self, rect, numberOfFrames=1, health=-1, mass=1.0):
        #graphics related
        self.rect = rect
        self.animCounter = 0
        self.numberOfFrames = numberOfFrames
        self.frameNumber = random.randint(0,self.numberOfFrames-1)        
        
        #physics related
        self.xspeed = 0
        self.yspeed = 0        
        self.mass = mass      # determines effect of gravity (0 = massless)
        self.isFalling = False
        
        #gameplay related
        self.health = health   #-1 = infinite
        self.isAlive = True  # if set to False, will be removed from lists by Game
        
    
    
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.isAlive = False
    
    def bumpedWall(self):
        pass
    
    def bumpedRoof(self):
        #default behaviour is to loose speed (hang for a brief moment in air)
        #before dropping down due to gravity
        self.yspeed = self.yspeed/2

    def tick(self, room):
        "Calculate new position and speed due to speed and gravity and set some flags."
        
        if not self.isAlive:
            return
        
        # calculate new vertical speed (due to gravity)
        self.yspeed = min( self.yspeed + self.mass * ICON_SIZE/FPS, 20.0 * ICON_SIZE/FPS)
        
        dx = int(round(self.xspeed))    #desired displacement (but walls might be in the way)
        dy = int(round(self.yspeed))

        curx = self.rect.left
        cury = self.rect.top
        if dx != 0:
            t = 0
            dt = 1 if dx>0 else -1
            while abs(t) <= abs(dx):
                if not room.canObjectBePlacedAt(curx + t, cury):
                    self.bumpedWall()
                    break
                t += dt
            dx = t - dt

        if dy != 0:
            t = 0
            dt = 1 if dy>0 else -1
            while abs(t) <= abs(dy):
                if not room.canObjectBePlacedAt(curx + dx, cury + t):
                    self.bumpedRoof()
                    break
                t += dt
            dy = t - dt
        
        self.rect.move_ip(dx,dy)

        # Check if we have air under our feet and update isFalling flag accordingly.
        curx = self.rect.left
        cury = self.rect.top        
        if self.mass == 0 or room.canObjectBePlacedAt(curx, cury+1):
            self.isFalling = True
        else:
            self.isFalling = False

        