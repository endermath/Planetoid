
import pygame
import random

from global_stuff import *


class Insectoid:
    def __init__(self, pos):
        self.rect = pygame.Rect(pos,(ICON_SIZE,ICON_SIZE))
        self.animCounter = 0
        self.frameNumber = random.randint(0,2)
        
        self.health = 20
        
    
    def tick(self):
        pass
    
    def hit(self):
        self.health -= 1