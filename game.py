import sys
import pygame
from pygame.locals import *

from global_stuff import *

from player import Player
from playershot import PlayerShot
from room import Room

class Game:
    def __init__(self):                
        self.isGameOver=False
        self.player = Player()
        
        self.currentRoom = Room(["1111111111111111",
                            "1010000000000001",
                            "1000000000002001",
                            "1200000011111101",
                            "1110000000000001",
                            "1000000000000001",
                            "1000011110000001",
                            "1000000000000001",
                            "1000000000000001",
                            "1001110000000001",
                            "1000000000000001",
                            "1000111110000021",
                            "1000000000000221",
                            "1000000000111111",
                            "1000000000000001",
                            "3333333111333333"])
        
        self.spriteList = []
                            
        #self.flowers = []
        #self.flowers.append(Flower(random.randint(1,screenSize-2)))

        #self.fallingItems = []
        #self.fallingFlowers = []

        #self.fallSpawnCounter = 60   #delay until next falling item is created
        #self.wateringCounter = 0            #for animating the splashing of water when watering or refilling

    def spawnShot(self, rect, dir):
        self.spriteList.append(PlayerShot(rect,dir))
        
        
    def updateObjects(self):
        for s in self.spriteList:
            s.tick()
            if s.rect.right < 0 or s.rect.left>SCREEN_WIDTH:
                self.spriteList.remove(s)
                
        # falling items
        #for f in self.fallingItems:
        #    if not f.fallAndDecideIfTimeToRemove():
        #        self.fallingItems.remove(f)
        #for f in self.fallingFlowers:
        #    if not f.fallAndDecideIfTimeToRemove():
        #        self.fallingFlowers.remove(f)
                
        #self.fallSpawnCounter -=1
        #if self.fallSpawnCounter<0:
        #    self.fallSpawnCounter = 60+random.randint(0,FPS*2)
        #    pos=random.randint(1,screenSize-3)
        #    self.fallingItems.append(random.choice([ClockItem(pos,0),Pellet(pos,0),Skull(pos,0)]))

        # flowers
        #for f in self.flowers:
        #    f.grow()
        #    if f.isFinished:
        #        self.fallingFlowers.append(FlowerItem(f.xpos, screenSize-2-f.height))
        #        for s in range(0,f.height):
        #            self.fallingFlowers.append(FlowerStalkItem(f.xpos, screenSize-2-s))
        #        self.flowers.remove(f)                   #turn flower into falling pieces!
                
            

                


    def update(self):    
        self.updateObjects()
#        oldRect = self.player.rect.copy()
        #px = self.player.rect.left/ICON_SIZE
        #py = self.player.rect.top/ICON_SIZE
        #dx = 0 if px % ICON_SIZE == 0 else 1
        #dy = 0 if py % ICON_SIZE == 0 else 1
        #twoByTwo = [[self.currentRoom[py][px], self.currentRoom[py][px+dx]],
        #            [self.currentRoom[py+dy][px], self.currentRoom[py+dy][px+dx]]]
        self.player.tick(self.currentRoom)
#        newRect = self.player.rect

        # If player is watering, animate splashing and give water to flower
        #if self.player.watering:
        #    self.wateringCounter = self.wateringCounter-1 % 10
        #    if self.player.water>0:
        #        self.player.water = max(self.player.water-16,0)
        #        for f in self.flowers:
        #            if f.get_rect().colliderect(self.player.rect.move(2*iconSize*self.player.dir,0)):
        #                f.addWater(16)
        #                self.player.addScore(1)
        #        for f in self.fallingItems:
        #            if isinstance(f,Skull) and f.get_rect().colliderect(self.player.rect.move(2*iconSize*self.player.dir,0)):
        #                self.fallingItems.remove(f)
        #                self.player.addScore(20)
        #        if self.wateringCounter%4>1:
        #            windowSurfaceObj.blit(pygame.transform.flip(waterSplashSurfaceObj,(self.player.dir==-1),False),
        #                                  self.player.rect.move(2*self.player.dir*iconSize,0))
        #    else:
        #        self.player.watering=False
        #        #soundRefillWater.stop()
        #
        ## If refilling water at the tap, animate splashing and give player water
        #if self.player.refilling:
        #    self.wateringCounter = self.wateringCounter-1 % 10
        #    #flash water splash below the tap
        #    if self.wateringCounter%2>0:
        #        drawIcon(tapSplashSurfaceObj, screenSize-2,screenSize-2)
        #    self.player.water = min(self.player.water+50,12000.0)
        #
        #
        #hiscore = max(hiscore, self.player.score)
        #

        # take care of events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                if event.key == K_LEFT:
                    self.player.moveLeft() 
                if event.key == K_RIGHT:
                    self.player.moveRight()
                if event.key == K_UP:
                    self.player.jump()
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_SPACE:
                    self.player.isShooting=True
                    
                    
                                #soundRefillWater.play(loops=-1)
                #if event.key==K_RETURN:
                #    if (not self.player.watering) and (not self.player.refilling) and (not self.player.isOutside) and self.player.pellets > 0:
                #        target = self.player.rect.center #dir+round(self.player.rect.centerx/iconSize)
                #        if target[0]/iconSize in range(1,screenSize-2) and not any(f.get_rect().collidepoint(target) for f in self.flowers):
                #            self.flowers.append(Flower(target[0]/iconSize))
                #            self.player.pellets-=1
                #            
                            
            elif event.type==KEYUP:
                if event.key==K_LEFT:
                    self.player.stopLeft()
                if event.key==K_RIGHT:
                    self.player.stopRight()
                if event.key==K_SPACE:
                    self.player.isShooting = False
                    #soundRefillWater.stop()         #stop playing water sound
                    
                
    