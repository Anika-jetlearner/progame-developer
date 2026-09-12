import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
cat1=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\catstanding.png")
screen.fill("light blue")
catwidth=81
catheight=59
x=400
y=300

catrect=pygame.Rect(400,200,catwidth,catheight)
pygame.display.update()

class Cat:
    def draw(self):
        screen.blit(cat1,(catrect.x,catrect.y))
        pygame.display.update

cat=Cat()

    

keys=[False,False,False,False]


def move():
    global cat1,x,y
    if keys[0]==True:
         cat1=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\catwalking.png")
         catrect.y-=1
                    
    if keys[1]==True:
        cat1=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\catwalking.png")
        catrect.y+=1
    if keys[2]==True:
        cat1=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\catwalking.png")
        catrect.x-=1
    if keys[3]==True:
        cat1=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\catwalking.png")
        catrect.x+=1






while True:
    cat.draw()
    pygame.display.update()
    screen.fill("light blue")
    pygame.display.update
    keypress=pygame.key.get_pressed()
    move()
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
                cat1=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\catstanding.png")


            elif i.key==pygame.K_DOWN:
                keys[1]=False
                cat1=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\catstanding.png")
            
            elif i.key==pygame.K_LEFT:
                keys[2]=False
                cat1=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\catstanding.png")

            elif i.key==pygame.K_RIGHT:
                keys[3]=False
                cat1=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\catstanding.png")
                