import pygame
from global_stuff import *


class FontRenderer:
    def __init__(self):
        tempSurfaceObj = pygame.image.load('font.png')
        (fontSizex,fontSizey) = tempSurfaceObj.get_size()
        self.fontSurfaceObj = pygame.transform.scale(tempSurfaceObj,(SCALE_FACTOR*fontSizex,SCALE_FACTOR*fontSizey))
        self.charSize = 8*SCALE_FACTOR
        self.fontmap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ:1234567890' =!*"

    def render(self,surf,pos,text):
        "Renders a text message on screen using the custom font."
        (posx,posy)=pos
        text=text.upper()
        for char in text:
            charSurf = self.fontSurfaceObj.subsurface(pygame.Rect(self.fontmap.index(char)*self.charSize,0,self.charSize,self.charSize))
            surf.blit(charSurf,(posx,posy))
            posx+=self.charSize
