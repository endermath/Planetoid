import pygame
from pygame.locals import *

from global_stuff import *
from game import Game
from player import Player
from fontrenderer import FontRenderer

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
        
        
                
        
        
        #wateringCanSurfaceObj = getSurfaceFromIcons(0,0)
        #waterSplashSurfaceObj = getSurfaceFromIcons(1,0)
        #flowerSurfaceObj = getSurfaceFromIcons(2,0)
        ##flowerstalkSurfaceObj = getSurfaceFromIcons(2,1)
        #pelletSurfaceObj = getSurfaceFromIcons(3,0)
        #clockSurfaceObj = getSurfaceFromIcons(4,1)
        #tapSurfaceObj = getSurfaceFromIcons(5,0)
        #tapSplashSurfaceObj = getSurfaceFromIcons(5,1)
        self.sandyShotSurfObj = self.getSurfaceFromIcons(3,1)
        self.skullSurfaceObj = self.getSurfaceFromIcons(4,0)
        self.dirtSurfaceObj = self.getSurfaceFromIcons(0,2)
        self.brickSurfaceObj = self.getSurfaceFromIcons(0,3)
        
    def animate(self):
        self.playerAnimationCounter = (self.playerAnimationCounter + 1) % 60
        if self.g.player.isWalking:
            if (self.playerAnimationCounter % 6 == 0):
                self.playerFrame = 1 - self.playerFrame
        else:
            self.playerFrame = 0
        if (self.playerAnimationCounter % 5 == 0):
            self.playerShootFrame = 1- self.playerShootFrame

        
    def render(self):
        self.drawScene()
        self.drawObjects()
        
        self.animate()
        
        self.drawPlayer()
        self.displayScore()
    
    def drawObjects(self):
        for s in self.g.spriteList:
            if s.dir == 1:
                self.windowSurfaceObj.blit(self.sandyShotSurfObj, s.rect)
            else:
                self.windowSurfaceObj.blit(pygame.transform.flip(self.sandyShotSurfObj, True, False), s.rect)
            
            
    def drawPlayer(self):
        p = self.g.player
        if p.isShooting:
            if p.dir == -1:
                self.windowSurfaceObj.blit(self.sandyShootSurfObj[self.playerShootFrame], p.rect)
            else:
                self.windowSurfaceObj.blit(pygame.transform.flip(self.sandyShootSurfObj[self.playerShootFrame],True,False), p.rect)

            if self.playerShootFrame == 1 and self.playerAnimationCounter % 5 == 0:
                self.soundPlayerShoot.stop()
                self.soundPlayerShoot.play()
                self.g.spawnShot(p.rect.copy(), p.dir)

        else:                
            if p.dir == -1:
                self.windowSurfaceObj.blit(self.sandyWalkSurfObj[self.playerFrame], p.rect)
            else:
                self.windowSurfaceObj.blit(pygame.transform.flip(self.sandyWalkSurfObj[self.playerFrame],True,False), p.rect)

    def drawScene(self):
        # fill background
        self.windowSurfaceObj.fill(pygame.Color(25,5,5)) #68,124,209))
        
        

        #if outside, draw tap and update falling items
        #if isOutside:
        for y in range(0,16):
            for x in range(0,16):
                if self.g.currentRoom[y][x] == "1":
                    self.windowSurfaceObj.blit(self.brickSurfaceObj, (x*ICON_SIZE,y*ICON_SIZE))
                if self.g.currentRoom[y][x] == "2":
                    self.windowSurfaceObj.blit(self.skullSurfaceObj, (x*ICON_SIZE,y*ICON_SIZE))
                if self.g.currentRoom[y][x] == "3":
                    self.windowSurfaceObj.blit(self.dirtSurfaceObj, (x*ICON_SIZE,y*ICON_SIZE))

            #drawIcon(tapSurfaceObj, 16-2,16-3)
            #for f in self.fallingItems:
            #    f.draw()
            #    itemRect = f.get_rect()
            #    if itemRect.colliderect(self.player.rect):
            #        f.giveBonus(self.player)
            #        self.fallingItems.remove(f)

                    
        #if inside, draw flowers
        #else:
        #    # draw bricks and dirt
        #    for y in range(0,16-1):
        #        windowSurfaceObj.blit(brickSurfaceObj, (0,y*ICON_SIZE))
        #        if y<16-3:
        #            windowSurfaceObj.blit(brickSurfaceObj, ((16-1)*ICON_SIZE,y*ICON_SIZE))
        #    for x in range(0,16):
        #        windowSurfaceObj.blit(dirtSurfaceObj, (x*ICON_SIZE, (16-1)*ICON_SIZE))
        #
        #    for f in self.flowers:
        #        f.draw()
        #    for f in self.fallingFlowers:
        #        f.draw()
        #        flowerRect = Rect(int(round(f.xpos)),int(round(f.ypos)),ICON_SIZE,ICON_SIZE)
        #        if flowerRect.colliderect(self.player.rect):
        #            f.giveBonus(self.player)
        #            self.fallingFlowers.remove(f)



    def displayScore(self):
        pass
        #
        #charSize = 16
        ##print score etc at top of screen
        #self.windowSurfaceObj.fill(pygame.Color(0,0,0),Rect(0,0,16*ICON_SIZE,2*ICON_SIZE))
        #
        ##print score
        #scoreTextx = ((16*ICON_SIZE/2)-5*charSize)/2
        #scoreTexty = 0 
        #self.myFontRenderer.render(self.windowSurfaceObj,(scoreTextx,scoreTexty),"SCORE")
        #
        ##global scoreBlinkCounter 
        ##scoreBlinkCounter = scoreBlinkCounter + 1 % FPS
        #if True: #scoreMultiplier==1 or scoreBlinkCounter> FPS/2:
        #    self.myFontRenderer.render(self.windowSurfaceObj,(scoreTextx-2*charSize,scoreTexty),"1*")
        #    scoreWidth = charSize * len(str(self.player.score))
        #    scorex = ((16*ICON_SIZE/2)-scoreWidth)/2
        #    scorey = scoreTexty+charSize
        #    self.myFontRenderer.render(self.windowSurfaceObj,(scorex,scorey),str(self.player.score))
        #        
        ##print time left
        ##timeTextx = (16*ICON_SIZE - 4*charSize)/2
        ##timeTexty = 0
        ##myFontRenderer.render(windowSurfaceObj,(timeTextx,timeTexty),"TIME")
        #
        ##timeWidth = charSize * len("60")
        ##timeLeftx = (16*ICON_SIZE-timeWidth)/2
        ##timeLefty = charSize
        ##myFontRenderer.render(windowSurfaceObj,(timeLeftx,timeLefty),"60")
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
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==KEYDOWN:
                    if event.key==K_SPACE:
                        isWaiting = False
            pygame.display.update()
            waitClock.tick(30)


    def showGameOverScreen(self):
        global hiscore
        delayTime = 3*FPS
        isWaiting = True
        waitClock = pygame.time.Clock()
        while isWaiting:
            #self.updateObjects()
            self.drawScene(self.player.isOutside)
            self.player.tick()
            hiscore = max(hiscore, self.player.score)
            self.displayScore()
            delayTime-=1
            if delayTime<FPS*0.25:
                msg="GAME OVER!"
                myRender(self.windowSurfaceObj,((16*ICON_SIZE-len(msg)*charSize)/2, 2*charSize), msg)
                if delayTime<0:
                    delayTime=FPS*0.45
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==KEYDOWN:
                    if event.key==K_SPACE and delayTime<FPS*0.5:
                        isWaiting=False
            pygame.display.update()
            waitClock.tick(FPS)

