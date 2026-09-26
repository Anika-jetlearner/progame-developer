import pygame
import time
import random
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("light blue")
clock=pygame.time.Clock()

class Bee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\bee.png")
        self.rect=self.image.get_rect()
    def update(self):
        if keys[0]==True and self.rect.y>0:
            self.rect.y-=1
        if keys[1]==True and self.rect.y<550:
            self.rect.y+=1
        if keys[2]==True and self.rect.x>0:
            self.rect.x-=1
        if keys[3]==True and self.rect.x<550:
            self.rect.x+=1


class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.image=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\catstanding.png")
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(0,600)
        self.rect.y=random.randint(0,600)
        




bees=pygame.sprite.Group()
bee=Bee()
bees.add(bee)

keys=[False,False,False,False]

while True:
    clock.tick(80)
    screen.fill("light blue")
    bees.update()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_UP:
                keys[0]=True
            if i.key==pygame.K_DOWN:
                keys[1]=True
            if i.key==pygame.K_LEFT:
                keys[2]=True
            if i.key==pygame.K_RIGHT:
                keys[3]=True
        if i.type==pygame.KEYUP:
            if i.key==pygame.K_UP:
                keys[0]=False
            if i.key==pygame.K_DOWN:
                keys[1]=False
            if i.key==pygame.K_LEFT:
                keys[2]=False
            if i.key==pygame.K_RIGHT:
                keys[3]=False


    bees.draw(screen)
    pygame.display.update()




