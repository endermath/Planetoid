
import math

from global_stuff import *

class Room:
    def __init__(self, array, monList):
        self.array = array
        self.width = len(array[0])*ICON_SIZE
        self.height = len(array)*ICON_SIZE
        
        self.monsterList = monList
        self.playerShotList = []

    def __getitem__(self, key):
        return self.array[key]
    
    def __len__(self):
        return len(self.array)
    
    def canObjectBePlacedAt(self, nx, ny):
        x1 = int(math.floor(nx/(1.0*ICON_SIZE)))
        x2 = int(math.ceil(nx/(1.0*ICON_SIZE)))
        y1 = int(math.floor(ny/(1.0*ICON_SIZE)))
        y2 = int(math.ceil(ny/(1.0*ICON_SIZE)))
        room = self.array
        return room[y1][x1] == "0" and room[y2][x1] == "0" and room[y1][x2] == "0" and room[y2][x2] == "0"
