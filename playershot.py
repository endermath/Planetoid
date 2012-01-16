import pygame

from global_stuff import *

class PlayerShot:
    
    def __init__(self, rect, dir):
        self.rect = rect
        self.dir = dir
        self.xspeed = dir * 20.0 * ICON_SIZE/FPS
        self.yspeed = 0
        
    def tick(self):
        self.rect.move_ip(int(round(self.xspeed)), int(round(self.yspeed)))