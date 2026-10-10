import pygame
pygame.init()
screen=pygame.display.set_mode((700,600))
bg=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\bgr1.jpg")
screen.blit(bg,(0,0))

class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\pacman.png")
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

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\coin.jpg")
        self.rect=self.image.get_rect()
    





sprites=pygame.sprite.Group()
pacman=Pacman()
sprites.add(pacman)

for xi in range(36):
    for yi in range(31):
        coin=Coin()
        coin.rect.x=((xi+1)*40)
        coin.rect.y=((yi+1)*40)
        sprites.add(coin)

keys=[False,False,False,False]

while True:
    
    pacman.move()
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