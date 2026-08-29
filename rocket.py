import pygame
from time import *
pygame.init()
screen=pygame.display.set_mode((600,600))
image=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\rocket.png")
screen.fill("dark blue")
x=225
y=400
pygame.display.update()
screen.blit(image,(x,y))
pygame.display.update()

keys=[False,False,False,False]

while True:
    y+=0.01
    #sleep(0.05)
    screen.blit(image,(x,y))
    pygame.display.update()
    screen.fill("dark blue")
    if keys[0]==True:
        y-=0.05
    if keys[1]==True:
        y+=0.05
    if keys[2]==True:
        x-=0.05
    if keys[3]==True:
        x+=0.05
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_UP:
                keys[0]=True


            elif i.key==pygame.K_DOWN:
                keys[1]=True

            elif i.key==pygame.K_LEFT:
                keys[2]=True

            elif i.key==pygame.K_RIGHT:
                keys[3]=True

        if i.type==pygame.KEYUP:
            if i.key==pygame.K_UP:
                keys[0]=False

            elif i.key==pygame.K_DOWN:
                keys[1]=False
            
            elif i.key==pygame.K_LEFT:
                keys[2]=False

            elif i.key==pygame.K_RIGHT:
                keys[3]=False
            
            print(x,y)

