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

spacepressed=False
gamestarted=False

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
        if self.starttime<10:
            self.image=fup
        elif self.starttime<15:
            self.image=fdown

        elif self.starttime<20:
            self.image=fstill
           
        else:
            self.starttime=0
        if spacepressed==True and gamestarted==True:
           
            self.rect.y-=3
        if gamestarted==True:
            self.rect.y+=0.5

        print(self.starttime)

class Pipe(pygame.sprite.Sprite):
    def __init__(self,flip):
        super().__init__()
        self.image=pipe
        self.rect=self.image.get_rect()
        if flip==True:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.x=600
            self.rect.y=-100
        else:
            self.rect.x=600
            self.rect.y=250
    def update(self):
        self.rect.x-=1
        if self.rect.right<0:
            self.kill()
             


flappy=Bird()
sprites=pygame.sprite.Group()
pipes=pygame.sprite.Group()
sprites.add(flappy)

flappy.rect.x=50
flappy.rect.y=250


timeinterval=2000   
x=0




clock=pygame.time.Clock()

pipespritecreate=pygame.time.get_ticks()

while True:
    currenttime=pygame.time.get_ticks()
    if currenttime-pipespritecreate>2000:

        pipebottom=Pipe(False)
        pipetop=Pipe(True)
        pipes.add(pipebottom)
        pipes.add(pipetop)
        pipespritecreate=currenttime

    screen.blit(bg,(0,0))
    pipes.draw(screen)
    screen.blit(ground,(x,450))
    flappy.updatebird()
    pipes.update()

    x-=1
    if x<-200:
        x=0

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_SPACE:
                spacepressed=True
                gamestarted=True
        if i.type==pygame.KEYUP:
            if i.key==pygame.K_SPACE:
                spacepressed=False

    sprites.draw(screen)
    
    pygame.display.update()