import pygame
import random
import time
pygame.init()
screen=pygame.display.set_mode((600,500))
background=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\background.png")
screen.blit(background,(0,0))
#bee=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\bee.png")

pygame.display.update()

class Bee:
    def __init__(self):
        self.height=64
        self.width=64
        self.beerect=pygame.Rect(100,100,self.width,self.height)
        self.img=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\bee.png")
        screen.blit(self.img,(100,100))

    def draw(self):
        screen.blit(self.img,(self.beerect.x,self.beerect.y))
        #pygame.display.update()
        
    def move(self):
        if keys[0]==True and self.beerect.y>0:
            self.beerect.y-=1
        if keys[1]==True and self.beerect.y<450:
            self.beerect.y+=1
        if keys[2]==True and self.beerect.x>0:
            self.beerect.x-=1
        if keys[3]==True and self.beerect.x<550:
            self.beerect.x+=1
        pygame.time.wait(10)

class Flower:
    def __init__(self):
        self.x=random.randint(0,600)
        self.y=random.randint(0,500)
        self.width=64
        self.height=64
        self.florect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.imgf=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\flower.png")
        screen.blit(self.imgf,(self.x,self.y))
    def draw(self):
        screen.blit(self.imgf,(self.florect.x,self.florect.y))
        

keys=[False,False,False,False]



bee=Bee()
flo=Flower()
while True:
    screen.blit(background,(0,0))
    bee.draw()
    #flo.draw()
    bee.move()
    
    flo.draw()
    if bee.beerect.colliderect(flo.florect):
        print("collision")
        flo.florect.x=random.randint(0,600)
        flo.florect.y=random.randint(0,500)
        flo.draw()
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
    pygame.display.update()

        
