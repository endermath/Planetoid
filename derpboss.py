
import pygame
import random

from global_stuff import *


class DerpBoss:
    def __init__(self, pos):
        self.rect = pygame.Rect(pos,(2*ICON_SIZE,2*ICON_SIZE))
        self.animCounter = 0
        self.frameNumber = random.randint(0,1)
        
        self.health = 150
        
    
    def tick(self):
        pass
    
    def hit(self):
        self.health -= 1