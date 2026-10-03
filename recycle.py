import pygame
import random
import time
pygame.init()
screen=pygame.display.set_mode((800,600))

bg=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\bgr.png")
bg=pygame.transform.scale(bg,(800,600))
screen.blit(bg,(0,0))


class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\bin.png")
        self.image=pygame.transform.scale(self.image,(30,50))
        self.rect=self.image.get_rect()
    def move(self):
        if keys[0]==True:
            self.rect.y-=2
        if keys[1]==True: 
            self.rect.y+=2
        if keys[2]==True:
            self.rect.x-=2
        if keys[3]==True:
            self.rect.x+=2
        pygame.time.wait(10)

recycleimgs=[r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\paper bag.png",r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\wooden box.png",r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\pencil.png"]


class Recycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(random.choice(recycleimgs))
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()

sprites=pygame.sprite.Group()
recycle=pygame.sprite.Group()

for i in range(51):
    rec=Recycle()
    rec.rect.x=random.randint(0,800)
    rec.rect.y=random.randint(0,600)
    sprites.add(rec)
    recycle.add(rec)

    


bin=Bin()
sprites.add(bin)

keys=[False,False,False,False]






while True:
    bin.move()
    screen.blit(bg,(0,0))
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
    sprites.draw(screen)
    pygame.display.update()