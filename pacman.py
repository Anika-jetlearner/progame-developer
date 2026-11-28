import pygame
import random
pygame.init()

screen=pygame.display.set_mode((700,600))
bg=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\bgr1.jpg")
screen.blit(bg,(0,0))
linesverticalleft=[]
linesverticalright=[]
lineshorizontaltop=[]
lineshorizontalbottom=[]

score=0
life=3




class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\pacman.png")
        self.rect=self.image.get_rect()
        self.rect.x=10
        self.rect.y=10
        
    def move(self):
        y=self.rect.y
        x=self.rect.x
        if keys[0]==True:
            self.rect.y-=2
        if keys[1]==True:
            self.rect.y+=2
        if keys[2]==True:
            self.rect.x-=2
        if keys[3]==True:
            self.rect.x+=2
        for i in lineshorizontaltop+lineshorizontalbottom+linesverticalleft+linesverticalright:
            if self.rect.colliderect(i):
                self.rect.y=y
                self.rect.x=x
        pygame.time.wait(10)

    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\coin.jpg")
        self.rect=self.image.get_rect()

class Ghost(pygame.sprite.Sprite):
    def __init__(self,ghostimagefile):
        super().__init__()
        self.image=pygame.image.load(ghostimagefile)
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(0,700)
        self.rect.y=random.randint(0,600)
        self.direc=random.randint(0,3)
    def move(self):
        x=self.rect.x
        y=self.rect.y
        

       

        
            
        if self.direc==0:                    #if 0, up
            self.rect.y-=3
        if self.direc==1:                    #if 1, down
            self.rect.y+=3
        if self.direc==2:                    #if 2, left
            self.rect.x-=3
        if self.direc==3:                    #if 3, right
            self.rect.x+=3              
            


        for i in lineshorizontaltop+lineshorizontalbottom+linesverticalleft+linesverticalright:
            if self.rect.colliderect(i):
                
                self.rect.y=y
                self.rect.x=x
                self.direc=random.randint(0,3)
                

                

    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))



    
def draw_line(xstart,ystart,length,dir, scr):
    print(dir)
    if dir=="up":
        yend=ystart-length
        xend=xstart
        recty=yend
        rectx=xend
        rectwidth=5
        rectheight=length
    elif dir=="down":
        yend=ystart+length
        xend=xstart
        recty=ystart
        rectx=xstart
        rectwidth=5
        rectheight=length
    elif dir=="left":
        yend=ystart
        xend=xstart-length
        recty=yend
        rectx=xend
        rectwidth=length
        rectheight=5
    elif dir=="right":
        yend=ystart
        xend=xstart+length
        recty=ystart
        rectx=xstart
        rectwidth=length 
        rectheight=5
    else:
        print("drawlineerror")

    
    
    line=pygame.draw.line(scr,"black", (xstart,ystart),(xend,yend),5)
    line=pygame.Rect(rectx,recty,rectwidth,rectheight)
    
    return line,xend,yend



def draw_multi_lines(xstart,ystart,lengthlist,dirlist):
    rectlist=[]
    for i in range(len(dirlist)):
       
        if i==0:
            line,xend,yend=draw_line(xstart,ystart,lengthlist[i],dirlist[i],screen)
            rectlist.append(line)
        else:
            line,xend,yend=draw_line(xend,yend,lengthlist[i],dirlist[i],screen)
            rectlist.append(line)
    return rectlist

    
        




    


font=pygame.font.SysFont("Times New Roman",30)


sprites=pygame.sprite.Group()
pacman=Pacman()
ghost=Ghost(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\ghost.png")
ghost1=Ghost(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\ghost1.png")
ghost2=Ghost(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\ghost2.png")
#sprites.add(pacman)


for xi in range(36):
    for yi in range(31):
        coin=Coin()
        coin.rect.x=((xi+0.5)*40)
        coin.rect.y=((yi+0.5)*40)
        sprites.add(coin)

class Wall(pygame.sprite.Sprite):
    def __init__(self,startx,starty,endx,endy):
        super().__init__()
    
      
        self.line=pygame.draw.line(screen, "black", (startx,starty), (endx, endy))



  


keys=[False,False,False,False]
lengthlist=[600,700,600,700,40,285,200,40,160,40,280,360,200]
dirlist=["down","right","up","left","right","down","right","up","left","up","right","down","right"]
dirghost=["up","down","left","right"]
xstart=0
ystart=0

while True:

    
    pacman.move()
    ghost.move()
    ghost1.move()
    ghost2.move()
    screen.blit(bg,(0,0))
    ghost.draw()
    ghost1.draw()
    ghost2.draw()
    text=font.render("Score {}".format(score),True, "black")
    text1=font.render("Life {}".format(life),True,"black")
    screen.blit(text,(580,10))
    screen.blit(text1,(580,40))
    # line = draw_line(43,525,100,"up", screen)
    # lineshorizontalbottom.append(line)
    

    lineshorizontaltop=draw_multi_lines(xstart,ystart,lengthlist,dirlist)
    

        
    pacman.draw()
    for i in sprites:
        if pacman.rect.colliderect(i.rect):
            sprites.remove(i)
            score+=1
    if pacman.rect.colliderect(ghost.rect):
        life-=1
        pacman.rect.y=10
        pacman.rect.x=10

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