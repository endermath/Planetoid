import pygame, sys, random
from pygame.locals import *

from global_stuff import *
from fontrenderer import *
from game import Game
from gamescreen import GameScreen

# Global variables common to both title screen and game loop
hiscore = 0

# Initialize pygame
pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_caption("Planetoid")

# Create a screen
windowSurfaceObj = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.mixer.Sound('background.ogg').play(loops=-1)



#class Flower:
#    height = 1
#    waterMax = 3000.0
#    xpos = 1
#    def __init__(self,xpos):
#        self.xpos = xpos
#        self.height = random.randint(1,4)
#        self.water = max(400.0, random.gauss(1000,250))
#        self.growCounter = 0
#        self.isFinished = False
#
#    def get_rect(self):
#        return Rect(ICON_SIZE*self.xpos, SCREEN_HEIGHT-ICON_SIZE-ICON_SIZE*(self.height+1),
#                    ICON_SIZE, ICON_SIZE*(self.height+1))
#        
#    def grow(self):
#        if not self.isFinished:
#            self.water = self.water-self.height/3
#            if self.water<0:
#                self.isFinished = True
#            else:
#                self.growCounter += self.water/2500.0
#                if self.growCounter > 200:
#                    self.growCounter = 0
#                    self.height += 1
#                    if self.height > SCREEN_HEIGHT/ICON_SIZE-5:
#                        self.isFinished = True
#                        
#            
#    def addWater(self,water):
#        self.water = min(self.water+water, self.waterMax)
#        
#    def draw(self):
#        for s in range(1,self.height+1):
#            drawIcon(flowerstalkSurfaceObj,self.xpos,15-s)    #draw the stalk
#        drawIcon(flowerSurfaceObj,self.xpos,15-(self.height+1))  #draw the flower on top
#        meterRect = Rect(self.xpos*ICON_SIZE, 15*ICON_SIZE+ ICON_SIZE/4, int(round(ICON_SIZE*self.water/self.waterMax)), ICON_SIZE/4)
#        windowSurfaceObj.fill(pygame.Color(20,20,220), meterRect)
#        

#class FallingItem:
#    surf = None
#
#    def __init__(self,xpos,ypos):
#        self.xpos=xpos*ICON_SIZE
#        self.ypos=ypos*ICON_SIZE
#        self.xspeed = random.gauss(0,3)
#        self.yspeed = random.gauss(0,3)
#        self.onFloorCounter = 4*FPS
#        self.isFalling = True
#
#    def get_rect(self):
#        return Rect(self.xpos,self.ypos,ICON_SIZE,ICON_SIZE)
#
#    def fallAndDecideIfTimeToRemove(self):
#        if self.isFalling:
#            self.xpos=self.xpos+self.xspeed
#            if self.xpos > SCREEN_WIDTH-2*ICON_SIZE or self.xpos < ICON_SIZE :
#                self.xspeed = -self.xspeed
#            
#            self.yspeed = self.yspeed + 0.2
#            self.ypos=self.ypos+self.yspeed
#            if self.ypos > SCREEN_HEIGHT-2*ICON_SIZE:
#                self.ypos = SCREEN_HEIGHT-2*ICON_SIZE 
#                self.yspeed = -0.5*self.yspeed
#                if int(round(self.yspeed))==0:
#                    self.ypos = SCREEN_HEIGHT-2*ICON_SIZE
#                    self.isFalling = False
#
#        else:
#            self.onFloorCounter -=1 
#            if self.onFloorCounter<0:
#                return False
#        return True
#
#    def draw(self):
#        if self.ypos<SCREEN_HEIGHT-2*ICON_SIZE or self.onFloorCounter>1*FPS or self.onFloorCounter%4>1:
#            windowSurfaceObj.blit(self.surf,(int(round(self.xpos)),int(round(self.ypos))))
#
#class Skull(FallingItem):
#    surf = skullSurfaceObj
#    def giveBonus(self,p):
#        p.water = p.water/2
#        #soundSkullPickup.play()
#
#class ClockItem(FallingItem):
#    surf = clockSurfaceObj
#    def giveBonus(self,p):
#        p.addScore(7)
#        #soundPickup.play()
#
#class Pellet(FallingItem):
#    surf = pelletSurfaceObj
#    def giveBonus(self,p):
#        p.addScore(7)
#        p.pellets += 1
#        #soundPickup.play()
#
#class FlowerItem(FallingItem):
#    surf = flowerSurfaceObj
#    def giveBonus(self,p):
#        p.addScore(50)
#        #soundPickup.play()
#
#class FlowerStalkItem(FallingItem):
#    surf = flowerstalkSurfaceObj
#    def giveBonus(self,p):
#        p.addScore(25)
#        #soundPickup.play()
#




            
            
while True:
    g = Game()
    gs = GameScreen(g, windowSurfaceObj)
    gs.showTitleScreen()
    while (not g.isGameOver):
        g.update()
        gs.render()
        pygame.display.update()
        fpsClock.tick(FPS)
    gs.showGameOverScreen()
    

