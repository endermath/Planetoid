import sys
import pygame
from pygame.locals import *

from global_stuff import *

from player import Player
from playershot import PlayerShot
from room import Room
from insectoid import Insectoid
from derpboss import DerpBoss

class Game:
    def __init__(self):                
        self.isGameOver=False

        self.soundInsectoidHit = pygame.mixer.Sound('insectoidhit.wav')
        self.soundPlayerHurt = pygame.mixer.Sound('playerhurt.wav')

        self.verticalTop1Room = \
                           ["1111111111111111",
                            "1000000000000001",
                            "1000020000200001",
                            "1001111111111001",
                            "1000000000000001",
                            "1000000000000001",
                            "1111110000000001",
                            "1111111000000001",
                            "1000000000011001",
                            "1000000000000001",
                            "1000000110000001",
                            "1111100000000001",
                            "1000000000111111",
                            "1000000000000001",
                            "1011110000000001",
                            "1010000000000001"]
        
        self.verticalMid1Room = \
                           ["1000000000110001",
                            "1000000001100001",
                            "1000000000000001",
                            "1110000110000001",
                            "1000000000000001",
                            "1000011000011001",
                            "1200000000000001",
                            "1100000000000001",
                            "1110011110000001",
                            "1000000000000001",
                            "1000000111111101",
                            "1000000000000001",
                            "1000100000111111",
                            "1000000000000001",
                            "1011110000000001",
                            "1010000000000001"]
        

        self.verticalBottom1Room = \
                           ["1010001110000021",
                            "1010000000000201",
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
                            "1000000000001111",
                            "3333331111333333"]

        insectList = [Insectoid((ICON_SIZE*4, ICON_SIZE*35)),
                      Insectoid((ICON_SIZE*12, ICON_SIZE*34))]
        
        self.derpBoss = DerpBoss((ICON_SIZE*8,ICON_SIZE*10))
        
        self.currentRoom=Room(self.verticalTop1Room+self.verticalMid1Room * 3+self.verticalBottom1Room,
                              insectList)

        self.player = Player((self.currentRoom.width/2,self.currentRoom.height-2*ICON_SIZE))


        self.testRoom = Room(["11111111111111111111",
                            "10000000000000010001",
                            "10000000000000010001",
                            "10000000000000000001",
                            "10000000000000000001",
                            "10000000000000010001",
                            "10111111111100010001",
                            "10100000000000010001",
                            "10100000000000210001",
                            "10100000000002010001",
                            "10000000000020010001",
                            "12000000111111010001",
                            "11100000000000010001",
                            "10000000000000010001",
                            "10000111100000010001",
                            "10000000000000010001",
                            "10000000000000010001",
                            "10011100000000010001",
                            "10000000000000010001",
                            "10001111100000210001",
                            "10000000000002210001",
                            "10000000001111110001",
                            "10000000000000000001",
                            "33333331113333333333"], [])
        
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
            if s.rect.right < 0 or s.rect.left>self.currentRoom.width:
                self.spriteList.remove(s)
        
        for i in self.currentRoom.insectoidList:
            i.tick()
                


    def checkCollisions(self):
        for i in self.currentRoom.insectoidList:
            if i.rect.colliderect(self.player.rect):
                self.player.hit()
                self.soundPlayerHurt.play()
            
            for s in self.spriteList:
                if i.rect.colliderect(s.rect):
                    i.hit()
                    self.soundInsectoidHit.play()
                    if i.health <= 0:
                        self.currentRoom.insectoidList.remove(i)

        for s in self.spriteList:    
            if self.derpBoss.rect.colliderect(s.rect):
                self.derpBoss.hit()
                self.soundInsectoidHit.play()
                #if self.derpBoss.health <= 0:
                    
            
    def update(self):    
        self.updateObjects()
        self.player.tick(self.currentRoom)

        self.checkCollisions()

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
                    
                            
            elif event.type==KEYUP:
                if event.key==K_LEFT:
                    self.player.stopLeft()
                if event.key==K_RIGHT:
                    self.player.stopRight()
                if event.key==K_SPACE:
                    self.player.isShooting = False
                    
                
    