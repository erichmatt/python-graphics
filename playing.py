import pygame
import sys
import time
pygame.init()
screen = pygame.display.set_mode((640,480))
for x in range (255):
    
    green = x,(255-x),100
    screen.fill(green)
    pygame.display.update()
    time.sleep(.001)

blue = 0,255,0
def shape():
    pygame.draw.arc(screen, blue,(100,100),0,1.0472,5)
    pygame.draw.arc(screen, blue,(50,57.73),0,1.0472,5)
    pygame.draw.arc(screen, blue,(100,100),0,1.0472,5)
    pygame.display.update()
    return

shape()
