import pygame, sys, random
from pygame.locals import *

from global_stuff import *
from fontrenderer import *
from game import Game
from gamescreen import GameScreen
from insectoid import Insectoid
from player import Player
from derpboss import DerpBoss

# Global variables common to both title screen and game loop
hiscore = 0

# Initialize pygame
pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_caption("Planetoid")

# Create a screen
windowSurfaceObj = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN | DOUBLEBUF | HWSURFACE )

pygame.mixer.Sound('background.ogg').play(loops=-1)

# Initialize sounds
Insectoid.hitSound = pygame.mixer.Sound('insectoidhit.wav')
DerpBoss.hitSound = pygame.mixer.Sound('insectoidhit.wav')
Player.hurtSound = pygame.mixer.Sound('playerhurt.wav')


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
        g.update(fpsClock.tick_busy_loop())
        gs.render()
        pygame.display.flip()
    gs.showGameOverScreen()
    

