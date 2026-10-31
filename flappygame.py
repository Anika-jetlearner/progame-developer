import pygame
import time
pygame.init()

bg=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\bagr.png")
bg=pygame.transform.scale(bg,(650,600))
fstill=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\flappystill.png")
fup=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\flappyup.png")
fdown=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\flappydown.png")
ground=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\groundbg.png")
pipe=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\pipe.png")
screen=pygame.display.set_mode((650,600))

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=fstill
        self.image2=fup
        self.image3=fdown
        self.starttime=0
        self.timelimit=5
        self.rect=self.image.get_rect()

    def updatebird(self):
       
        self.starttime+=1
        if self.starttime>5:
            self.image=fup
        elif self.starttime>10:
            self.image=fdown
            self.starttime=0
        else:
             self.image=fstill
        print(self.starttime)
             


flappy=Bird()
sprites=pygame.sprite.Group()
sprites.add(flappy)

flappy.rect.x=50
flappy.rect.y=250


    
x=0







while True:
    screen.blit(bg,(0,0))
    screen.blit(ground,(x,450))
    flappy.updatebird()
    x-=1
    if x<-150:
        x=0

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    sprites.draw(screen)
    pygame.display.update()