import pygame
pygame.init()
screen=pygame.display.set_mode((1000,700))
background=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\background.png")
screen.blit(background,(0,0))
bulletredcreated=False
spaceshipred=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\rocketred.png")
spaceshipyellow=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\rocketyellow.png")
bulletred=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\bulletred.jpg")
spaceshipwidth=51
spaceshipheight=62
redrect=pygame.Rect(850,350,spaceshipwidth,spaceshipheight)
class rocket:
    def __init__(self):
        # self.x=850
        # self.y=350
        

        self.x1=100
        self.y1=350
    def drawred(self):
        screen.blit(spaceshipred,(redrect.x,redrect.y))
        pygame.display.update()
    def drawyel(self):
        screen.blit(spaceshipyellow,(self.x1,self.y1))
        pygame.display.update()
   
class bullet:
    def __init__(self):
        self.x=850
        self.y=350

        self.x1=100
        self.y1=350
    def drawred(self):
        screen.blit(spaceshipred,(self.x,self.y))
        pygame.display.update()
    def drawyel(self):
        screen.blit(spaceshipyellow,(self.x1,self.y1))
        pygame.display.update()



red=rocket()
yellow=rocket()

def movered(keysred):
    if keysred[0]==True and redrect.y>0:
            redrect.y-=1
            
    if keysred[1]==True and red.y<650:
            red.y+=1
    if keysred[2]==True and red.x>490:
            red.x-=1
    if keysred[3]==True and red.x<950:
            red.x+=1

def moveyellow(keysyellow):
    if keysyellow[pygame.K_w]==True and yellow.y1>0:
            yellow.y1-=1
            
    if keysyellow[pygame.K_s]==True and yellow.y1<650:
            yellow.y1+=1
    if keysyellow[pygame.K_a]==True and yellow.x1>0:
            yellow.x1-=1
    if keysyellow[pygame.K_d]==True and yellow.x1<480:
            yellow.x1+=1


health=10
health1=10
font=pygame.font.SysFont("Times New Roman",30)




keysred=[False,False,False,False]
keysyellow=[False,False,False,False]





while True:
    text=font.render("Health:{}".format(health),True,"dark blue")
    text1=font.render("Health:{}".format(health1),True,"dark blue")
    pygame.draw.rect(screen,"white",(480,0,12,700))
    screen.blit(text,(180,100))
    screen.blit(bulletred,(red.x,red.y))
    screen.blit(text,(700,100))
    screen.blit(spaceshipred,(red.x,red.y))
    screen.blit(spaceshipyellow,(yellow.x1,yellow.y1))
    pygame.display.update()
    red.drawred()
    pygame.display.update()
    screen.blit(background,(0,0))

    movered(keysred)
    
    keypress=pygame.key.get_pressed()
    moveyellow(keypress)
    if bulletredcreated==True:
         bulletred.y-=15
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_RSHIFT:
                bulletredcreated=True
            
            if i.key==pygame.K_UP:
                keysred[0]=True
        
        
            elif i.key==pygame.K_DOWN:
                keysred[1]=True

            elif i.key==pygame.K_LEFT:
                keysred[2]=True

            elif i.key==pygame.K_RIGHT:
                keysred[3]=True
        
        if i.type==pygame.KEYUP:
            if i.key==pygame.K_UP:
                keysred[0]=False

            elif i.key==pygame.K_DOWN:
                keysred[1]=False
            
            elif i.key==pygame.K_LEFT:
                keysred[2]=False

            elif i.key==pygame.K_RIGHT:
                keysred[3]=False
            
               
                
            