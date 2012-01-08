# Constants of the game
FPS=60            #frames per second
SCALE_FACTOR=2

ICON_SIZE = 16 * SCALE_FACTOR
SCREEN_WIDTH = 16 * ICON_SIZE
SCREEN_HEIGHT = 16 * ICON_SIZE

def signum(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
    