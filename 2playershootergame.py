import pygame
pygame.init()
screen=pygame.display.set_mode((1000,700))
background=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\background.png")
screen.blit(background,(0,0))
bulletredcreated=False
bulletyelcreated=False
spaceshipred=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\rocketred.png")
spaceshipyellow=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\rocketyellow.png")
bulletred=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\bulletred.jpg")
bulletyellow=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\bulletyellow.jpg")
spaceshipwidth=51
spaceshipheight=62
redrect=pygame.Rect(850,350,spaceshipwidth,spaceshipheight)
yelrect=pygame.Rect(100,350,spaceshipwidth,spaceshipheight)
bulredrect=pygame.Rect(0,0,26,8)
bulyelrect=pygame.Rect(0,0,26,8)

class rocket:
    
    def drawred(self):
        screen.blit(spaceshipred,(redrect.x,redrect.y))
        #pygame.display.update()
    def drawyel(self):
        screen.blit(spaceshipyellow,(yelrect.x,yelrect.y))
        #pygame.display.update()
   
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
            
    if keysred[1]==True and redrect.y<650:
            redrect.y+=1
    if keysred[2]==True and redrect.x>495:
            redrect.x-=1
    if keysred[3]==True and redrect.x<950:
            redrect.x+=1

def moveyellow(keysyellow):
    if keysyellow[pygame.K_w]==True and yelrect.y>0:
            yelrect.y-=1
            
    if keysyellow[pygame.K_s]==True and yelrect.y<650:
            yelrect.y+=1
    if keysyellow[pygame.K_a]==True and yelrect.x>0:
            yelrect.x-=1
    if keysyellow[pygame.K_d]==True and yelrect.x<429:
            yelrect.x+=1


healthyel=5
healthred=5
font=pygame.font.SysFont("Times New Roman",30)
font1=pygame.font.SysFont("Times New Roman",15)




keysred=[False,False,False,False]
keysyellow=[False,False,False,False]





while healthyel>-1 and healthred>-1:
    screen.blit(background,(0,0))
    text=font.render("Health:{}".format(healthyel),True,"dark blue")
    text1=font.render("Health:{}".format(healthred),True,"dark blue")
    end=font1.render("before you play again, the winner gets one last shot at hitting the enemy!",True,"purple")
    
    pygame.draw.rect(screen,"white",(480,0,12,700))
    screen.blit(text,(180,100))
    if bulletredcreated==True:
        screen.blit(bulletred,(bulredrect.x,bulredrect.y))
    if bulletyelcreated==True:
        screen.blit(bulletyellow,(bulyelrect.x,bulyelrect.y))
    screen.blit(text1,(700,100))

    if healthyel==0:
        redwin=font.render("RED WINS",True,"red")
        screen.blit(redwin,(422,250))
        screen.blit(end,(250,300))
    if healthred==0:
        yelwin=font.render("YELLOW WINS",True,"yellow")
        screen.blit(yelwin,(200,250))
        screen.blit(end,(250,300))
    
    
    red.drawred()
    yellow.drawyel()
    
   

    movered(keysred)
    
    keypress=pygame.key.get_pressed()
    moveyellow(keypress)
    if bulletyelcreated==True:
       
        if bulyelrect.colliderect(redrect):
          
            healthred-=1
            bulletyelcreated=False


        bulyelrect.x+=15
        if bulyelrect.x>1045:
            bulletyelcreated=False

    if bulletredcreated==True:
        if bulredrect.colliderect(yelrect):
             print("collidered")
             healthyel-=1
             bulletredcreated=False

        bulredrect.x-=15
        if bulredrect.x<-30:
            bulletredcreated=False
    
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_f:
                 if bulletyelcreated==False:
                      bulletyelcreated=True
                      bulyelrect.x=yelrect.x
                      bulyelrect.y=yelrect.y
            if i.key==pygame.K_RCTRL:
                if bulletredcreated==False:
                    bulletredcreated=True
                    bulredrect.x=redrect.x
                    bulredrect.y=redrect.y

            
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
    pygame.display.update()
               
                
            