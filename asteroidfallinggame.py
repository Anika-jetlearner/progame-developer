import pygame
import random
import time
pygame.init()
screen=pygame.display.set_mode((800,600))



screen.fill("dark blue")
font=pygame.font.SysFont("Times New Roman",30)







pygame.display.update()

keys=[False,False]
class Rocket:
    def __init__(self):
        self.height=141
        self.width=79
        self.rocrect=pygame.Rect(400,460,self.width,self.height)
        self.img=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\rocket.png")
        screen.blit(self.img,(400,460))



    def draw(self):
        screen.blit(self.img,(self.rocrect.x,self.rocrect.y))
        pygame.display.update()

    def move(self):
        if keys[0]==True and rocket.rocrect.x>0:
            self.rocrect.x-=0.7
        if keys[1]==True and rocket.rocrect.x<700:
            self.rocrect.x+=0.7

class Asteroid:
    def __init__(self):
        self.speed=1
        self.x=400.0
        self.y=50.0
        self.asteroidheight=110
        self.asteroidwidth=110
        self.astrect=pygame.Rect(350,50,self.asteroidwidth,self.asteroidheight)
        self.astimg=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\asteroid.png")
        screen.blit(self.astimg,(self.x,self.y))

    def draw(self):
        screen.blit(self.astimg,(self.astrect.x,self.astrect.y))

    def move(self):
        self.astrect.y+=self.speed
        if self.astrect.y>600:
            self.astrect.x=random.randint(0,800)
            self.astrect.y=50
            self.speed+=1
            self.draw()

        if self.astrect.colliderect(rocket.rocrect):
                text=font.render("GAME OVER",True,"black")
                screen.blit(text,(400,300))
                pygame.time.wait(1000)
        
              

        
    

rocket=Rocket()
ast=Asteroid()

while True:
    screen.fill("dark blue")
    ast.draw()
    rocket.draw()
    rocket.move()
    ast.move()
   
    pygame.time.wait(10)

    
    


    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_LEFT:
                keys[0]=True
            elif i.key==pygame.K_RIGHT:
                keys[1]=True

        if i.type==pygame.KEYUP:
            if i.key==pygame.K_LEFT:
                keys[0]=False
            elif i.key==pygame.K_RIGHT:
                keys[1]=False
        pygame.display.update()