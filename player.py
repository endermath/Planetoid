import pygame
import math

from global_stuff import *


class Player:
    dir = 1
    pellets = 0
    isShooting = False  #true when shooting
    score = 0
    
    def __init__(self, pos):
        self.rect = pygame.Rect(pos, (ICON_SIZE,ICON_SIZE))
        self.xspeed = 0
        self.yspeed = 0
        self.movingRight = False
        self.movingLeft = False
        self.isWalking = False
        self.isFalling = False
    
        self.health = 100
        
        
    def addScore(self,sc):
        self.score +=  sc 
    
    def tick(self, room):       
        
        # calculate new vertical speed (due to gravity)
        self.yspeed = min( self.yspeed + 1.0 * ICON_SIZE/FPS, 20.0 * ICON_SIZE/FPS)

        ## for testing
        ##if self.xspeed !=0:
        ##    self.xspeed = self.xspeed / abs(self.xspeed)
        ##if self.yspeed !=0:
        ##    self.yspeed = self.yspeed / abs(self.yspeed)
        #    
        #
        ## find new position
        #accuracy = ICON_SIZE 
        #cury = self.rec.top
        #dy = int(round(self.yspeed))
        #
        #dottedLine = [int(round(self.xspeed * t / (1.0*accuracy) )) for t in range(1,accuracy+1)  ]
        #restrictedLine = filter(lambda p: canObjectBePlacedAt(p, ), dottedLine)
        #dx = max()
        #
        #t = 1
        #    
        #
        #self.rect.move_ip(dx,dy)
            
            
            
            
        curx = self.rect.left
        cury = self.rect.top
        dx = int(round(self.xspeed))    #desired displacement (but walls might be in the way)
        dy = int(round(self.yspeed))
        if dx != 0:
            t = 0
            dt = 1 if dx>0 else -1
            while abs(t) <= abs(dx):
                if not room.canObjectBePlacedAt(curx + t, cury):
                    #self.xspeed = 0 #bumped into a wall
                    break
                t += dt
            dx = t - dt

        if dy != 0:
            t = 0
            dt = 1 if dy>0 else -1
            while abs(t) <= abs(dy):
                if not room.canObjectBePlacedAt(curx + dx, cury + t):
                    self.yspeed = self.yspeed/2
                    break
                t += dt
            dy = t - dt
        
        self.rect.move_ip(dx,dy)

        # Check if we have air under our feet and update isFalling flag accordingly.
        curx = self.rect.left
        cury = self.rect.top        
        if room.canObjectBePlacedAt(curx, cury+1):
            self.isFalling = True
        else:
            self.isFalling = False

        
        #playableAreaRect = pygame.Rect(ICON_SIZE,0,SCREEN_WIDTH-2*ICON_SIZE,SCREEN_HEIGHT-ICON_SIZE)
        #if self.rect.centerx < 0:
        #    self.rect.centerx = SCREEN_WIDTH-ICON_SIZE
        #else:
        #    self.rect.clamp_ip(playableAreaRect)
        #    
        #if oldy != self.rect.y:
        #    self.isFalling = False
        #    self.yspeed = 0
        
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
        