import random, sys
import pygame
from pygame.locals import *

from global_stuff import *
from game import Game
from player import Player
from fontrenderer import FontRenderer
from insectoid import Insectoid
from derpboss import DerpBoss

class GameScreen:
    
    def __init__(self, g, winSurfObj):        
        self.g = g
        self.windowSurfaceObj = winSurfObj

        self.myFontRenderer = FontRenderer()
        self.loadGraphics()

        
        # Load sound effects
        self.soundPlayerShoot = pygame.mixer.Sound('playershoot.wav')
        
        self.playerFrame = 0
        self.playerShootFrame = 0
        self.playerAnimationCounter = 0

    def drawIcon(self,surf,x,y):
        "Shorthand for blitting icons onto the screen."
        self.windowSurfaceObj.blit(surf,(x*ICON_SIZE,y*ICON_SIZE))

    def getSurfaceFromIcons(self,x,y):
        "Shorhand for creating subsurfaces for the icons"
        return self.iconsSurfaceObj.subsurface(pygame.Rect(x*ICON_SIZE,y*ICON_SIZE,ICON_SIZE,ICON_SIZE))

    def loadGraphics(self):
        "Load and scale graphics."
        tempSurfaceObj = pygame.image.load('icons2.png')
        (iconsSizex,iconsSizey) = tempSurfaceObj.get_size()
        self.iconsSurfaceObj = pygame.transform.scale(tempSurfaceObj,(SCALE_FACTOR*iconsSizex,SCALE_FACTOR*iconsSizey))
        
        self.sandyWalkSurfObj = []
        self.sandyShootSurfObj = []
        
        self.sandyWalkSurfObj.append(pygame.transform.scale(pygame.image.load('sandy0.png'),(ICON_SIZE,ICON_SIZE)))
        self.sandyWalkSurfObj.append(pygame.transform.scale(pygame.image.load('sandy1.png'),(ICON_SIZE,ICON_SIZE)))
        self.sandyShootSurfObj.append(pygame.transform.scale(pygame.image.load('sandy2.png'),(ICON_SIZE,ICON_SIZE)))
        self.sandyShootSurfObj.append(pygame.transform.scale(pygame.image.load('sandy3.png'),(ICON_SIZE,ICON_SIZE)))
        
        self.insectoidSurfObj = [self.getSurfaceFromIcons(0,0),
                                 self.getSurfaceFromIcons(1,0),
                                 self.getSurfaceFromIcons(2,0)]
        
        
        self.sandyBigShotSurfObj = self.getSurfaceFromIcons(3,1)
        self.sandySmallShotSurfObj = self.getSurfaceFromIcons(3,2)
        self.skullSurfaceObj = self.getSurfaceFromIcons(4,0)
        self.dirtSurfaceObj = self.getSurfaceFromIcons(0,2)
        self.brickSurfObjs = []
        self.brickSurfObjs.append(self.getSurfaceFromIcons(0,5))
        self.brickSurfObjs.append(self.getSurfaceFromIcons(1,4))
        
        
        self.derpBossSurfObj = []
        self.derpBossSurfObj.append(pygame.transform.scale(pygame.image.load('derpboss0.png'),(ICON_SIZE*2,ICON_SIZE*2)))
        self.derpBossSurfObj.append(pygame.transform.scale(pygame.image.load('derpboss1.png'),(ICON_SIZE*2,ICON_SIZE*2)))
        
    def animate(self):
        self.playerAnimationCounter = (self.playerAnimationCounter + 1) % 600
        if self.g.player.isWalking:
            if (self.playerAnimationCounter % 6 == 0):
                self.playerFrame = 1 - self.playerFrame
        else:
            self.playerFrame = 0
        if (self.playerAnimationCounter % 5 == 0):
            self.playerShootFrame = 1- self.playerShootFrame

        for i in self.g.currentRoom.monsterList:
            i.animCounter = (i.animCounter + 1) % 60
            i.frameNumber = (i.animCounter % (i.numberOfFrames * 4)) /4
        
        
    def render(self):
        offsetx = SCREEN_WIDTH/2 - self.g.player.rect.centerx
        offsety = SCREEN_HEIGHT/2 - self.g.player.rect.centery
        #want to require that
        #0 >= xoffs >= SCREEN_WIDTH - self.g.currentRoom.width
        #0 >= yoffs >= SCREEN_HEIGHT - self.g.currentRoom.height
        offsetx = min(offsetx, 0)
        offsetx = max(SCREEN_WIDTH - self.g.currentRoom.width, offsetx)
        
        offsety = min(offsety, 0)
        offsety = max(SCREEN_HEIGHT -self.g.currentRoom.height, offsety)
        
        self.offset = (offsetx, offsety)
        
        self.animate()

        self.drawScene()
        self.drawObjects()
        self.drawPlayer()

        self.displayScore()
        

    
    def drawObjects(self):
        for i in self.g.currentRoom.monsterList:
            if isinstance(i,Insectoid):
                self.windowSurfaceObj.blit(self.insectoidSurfObj[i.frameNumber], i.rect.move(self.offset))
            elif isinstance(i,DerpBoss):
                self.windowSurfaceObj.blit(self.derpBossSurfObj[i.frameNumber], i.rect.move(self.offset))

        for s in self.g.currentRoom.playerShotList:
            if self.g.player.hasBigWeapon:
                srf = self.sandyBigShotSurfObj
            else:
                srf = self.sandySmallShotSurfObj
            if s.dir == -1:
                srf = pygame.transform.flip(srf, True, False)
            self.windowSurfaceObj.blit(srf, s.rect.move(self.offset))
        
            
    def drawPlayer(self):
        p = self.g.player
        if p.isShooting and self.playerShootFrame == 1 and self.playerAnimationCounter % 5 == 0:
            self.soundPlayerShoot.stop()
            self.soundPlayerShoot.play()
            self.g.spawnShot(p.rect.copy(), p.dir)

        if (not p.canBeHurt) and (self.playerAnimationCounter % 4 < 2):
            return

        if p.isShooting:
            if p.dir == -1:
                self.windowSurfaceObj.blit(self.sandyShootSurfObj[self.playerShootFrame], p.rect.move(self.offset))
            else:
                self.windowSurfaceObj.blit(pygame.transform.flip(self.sandyShootSurfObj[self.playerShootFrame],True,False), p.rect.move(self.offset))
        else:                
            if p.dir == -1:
                self.windowSurfaceObj.blit(self.sandyWalkSurfObj[self.playerFrame], p.rect.move(self.offset))
            else:
                self.windowSurfaceObj.blit(pygame.transform.flip(self.sandyWalkSurfObj[self.playerFrame],True,False), p.rect.move(self.offset))

    def drawScene(self):
        # fill background
        self.windowSurfaceObj.fill(pygame.Color(25,5,5)) #68,124,209))
                

        #if outside, draw tap and update falling items
        #if isOutside:
        for y in range(0,len(self.g.currentRoom)):
            for x in range(0,len(self.g.currentRoom[0])):
                rect = pygame.Rect((x*ICON_SIZE,y*ICON_SIZE), (ICON_SIZE,ICON_SIZE)).move(self.offset)
                if rect.bottom<0 or rect.top >= SCREEN_HEIGHT or rect.left >= SCREEN_WIDTH or rect.right < 0:
                    continue
                if self.g.currentRoom[y][x] == "1":
                    self.windowSurfaceObj.blit(self.brickSurfObjs[0], rect)
                if self.g.currentRoom[y][x] == "2":
                    self.windowSurfaceObj.blit(self.skullSurfaceObj, rect)
                if self.g.currentRoom[y][x] == "3":
                    self.windowSurfaceObj.blit(self.dirtSurfaceObj, rect)


    def displayScore(self):
        charSize = 16
        #print health at top of screen
        self.windowSurfaceObj.fill(pygame.Color(0,0,0),Rect(0,0,16*ICON_SIZE, ICON_SIZE))
        
        #print health
        scoreTextx = ((16*ICON_SIZE/2)-6*charSize)/2
        scoreTexty = 0 
        self.myFontRenderer.render(self.windowSurfaceObj,(scoreTextx,scoreTexty),"HEALTH")
        
        scoreWidth = charSize * len(str(self.g.player.health))
        scorex = ((16*ICON_SIZE/2)-scoreWidth)/2
        scorey = scoreTexty+charSize
        self.myFontRenderer.render(self.windowSurfaceObj,(scorex,scorey),str(self.g.player.health))
        
        #        
        #print FPS
        timeTextx = (16*ICON_SIZE - 3*charSize)/2
        timeTexty = 0
        self.myFontRenderer.render(self.windowSurfaceObj,(timeTextx,timeTexty),"FPS")
    
        ms = self.g.msSinceUpdate
        FPS = str(int(round(1000.0/ms)))
        timeWidth = charSize * len(FPS)
        timeLeftx = (16*ICON_SIZE-timeWidth)/2
        timeLefty = charSize
        self.myFontRenderer.render(self.windowSurfaceObj,(timeLeftx,timeLefty),FPS)
        #
        ##print hiscore
        #hiscoreTextx = 16*ICON_SIZE/2 + ((16*ICON_SIZE/2)-7*charSize)/2
        #hiscoreTexty =0
        #myFontRenderer.render(self.windowSurfaceObj,(hiscoreTextx,hiscoreTexty),"HISCORE")
        #
        #hiscoreWidth = charSize * len(str(hiscore))
        #hiscorex = 16*ICON_SIZE/2+((16*ICON_SIZE/2)-hiscoreWidth)/2
        #hiscorey = hiscoreTexty+charSize
        #myFontRenderer.render(self.windowSurfaceObj,(hiscorex,hiscorey),str(hiscore))
        #
        #draw water bar
        #waterBarx = charSize
        #waterBary = charSize * 2
        #waterBarMaxLength = 16*ICON_SIZE-2*charSize
        #waterBarLength = int(round(waterBarMaxLength * self.player.water/MAX_WATER))
        #waterBarRect = Rect(waterBarx,waterBary, waterBarLength, charSize)
        #windowSurfaceObj.fill(pygame.Color(20,20,240),waterBarRect)
        #pygame.draw.rect(windowSurfaceObj,(210,210,210),Rect(waterBarx,waterBary,waterBarMaxLength,charSize),2)
        
        #draw pellets
        #pelletsPosx = (16*ICON_SIZE-6*charSize)/2
        #pelletsPosy = charSize * 3
        #windowSurfaceObj.blit(pelletSurfaceObj,(pelletsPosx,pelletsPosy-charSize))
        #myFontRenderer.render(windowSurfaceObj,(pelletsPosx+ICON_SIZE,pelletsPosy),"="+str(self.player.pellets))


    
    def showTitleScreen(self):
        "Show title screen and wait for player to press space."
    
        # fill background black
        self.windowSurfaceObj.fill(pygame.Color(0,0,0))
    
        # print some text
        self.myFontRenderer.render(self.windowSurfaceObj, (20,20), "         Sandy returns")
        self.myFontRenderer.render(self.windowSurfaceObj, (20,40), "              in ")
        self.myFontRenderer.render(self.windowSurfaceObj, (20,80), "    :: Project Planetoid ::")
        
        self.myFontRenderer.render(self.windowSurfaceObj, (20,120), "  Keys: Left Right Up Space")
        self.myFontRenderer.render(self.windowSurfaceObj, (20,140),"     Press space to play!")
        
    #    msgSurfaceObj = fontObj.render("Sandy's Sunflowers",False,pygame.Color(20,200,20))
    #    msgRectObj = msgSurfaceObj.get_rect()
    #    msgRectObj.centerx = windowSurfaceObj.get_rect().centerx
    #    msgRectObj.centery = 20
    #    windowSurfaceObj.blit(msgSurfaceObj, msgRectObj)
    
    #    msgSurfaceObj = fontObj.render("Press space to play",False,pygame.Color(20,200,20))
    #    msgRectObj = msgSurfaceObj.get_rect()
    #    msgRectObj.centerx = windowSurfaceObj.get_rect().centerx
    #    msgRectObj.centery = 50
    #    windowSurfaceObj.blit(msgSurfaceObj, msgRectObj)
    
        isWaiting = True
        waitClock = pygame.time.Clock()
        while isWaiting:
            for event in pygame.event.get():
                if event.type == QUIT or event.type==KEYDOWN and event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.type==KEYDOWN:
                    if event.key==K_SPACE:
                        isWaiting = False
            pygame.display.update()
            waitClock.tick(30)


    def showGameOverScreen(self):
        isWaiting = True
        waitClock = pygame.time.Clock()
        counter = 0
        while isWaiting:
            self.drawScene()
            self.displayScore()
            msg="GAME OVER!"
            self.myFontRenderer.render(self.windowSurfaceObj,((SCREEN_WIDTH-len(msg)*16)/2, SCREEN_HEIGHT/2-8), msg)
            counter = min(counter + 1, 120)
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.type==KEYDOWN:
                    if event.key==K_SPACE and counter>=120:
                        isWaiting=False
            pygame.display.update()
            waitClock.tick(FPS)

