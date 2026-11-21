import pygame
pygame.init()
screen=pygame.display.set_mode((700,600))
bg=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\bgr1.jpg")
screen.blit(bg,(0,0))
linesverticalleft=[]
linesverticalright=[]
lineshorizontaltop=[]
lineshorizontalbottom=[]
score=0




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
lengthlist=[600,370,35,320,35,400,35,60,120]
dirlist=["down","right","up","left","up","right","down","right","up"]
xstart=0
ystart=0

while True:

    
    pacman.move()
    screen.blit(bg,(0,0))
    text=font.render("Score {}".format(score),True, "black")
    screen.blit(text,(580,10))
    # line = draw_line(43,525,100,"up", screen)
    # lineshorizontalbottom.append(line)
    

    lineshorizontaltop=draw_multi_lines(xstart,ystart,lengthlist,dirlist)
    
    #line=
    #pygame.draw.line(screen,"black",(43,525),(200,525),5)
    # line=pygame.Rect(43,524,157,5)
    # line1=pygame.draw.line(screen,"black", (43,485),(200,485),5)
    # line1=pygame.Rect(43,486,157,5)
    # line2=pygame.draw.line(screen, "black", (45,485),(45,300),5)
    # line2=pygame.Rect(45,300,5,185)
    # line3=pygame.draw.line(screen,"black", (2.5,600), (2.5,0),5)
    # line3=pygame.Rect(2.5,0,5,600)
    # line4=pygame.draw.line(screen,"black", (45,560),(45,527),5)
    # line4=pygame.Rect(45,527,5,33)
    # line5=pygame.draw.line(screen,"black",(43,560),(200,560),5)
    # line5=pygame.Rect(43,560,157,5)

   
    # lineshorizontalbottom.append(line)
    # lineshorizontaltop.append(line1)
    # linesverticalright.append(line2)
    # linesverticalleft.append(line3)
    # linesverticalright.append(line4)
    
    
    # for i in lineshorizontalbottom:
    #     if pacman.rect.colliderect(i):
    #         if pacman.rect.bottom>i.top:
    #             pacman.rect.bottom=i.top
    # for i in lineshorizontaltop:
    #     if pacman.rect.colliderect(i):
    #         if pacman.rect.top>i.bottom:
    #             pacman.rect.top=i.bottom


    # for i in linesverticalright:
    #     if pacman.rect.colliderect(i):
    #         if pacman.rect.right>i.left:
    #             pacman.rect.right=i.left
    # for i in linesverticalleft:
    #     if pacman.rect.colliderect(i):
    #         if pacman.rect.left<i.right:
    #             pacman.rect.left=i.right
        
    pacman.draw()
    for i in sprites:
        if pacman.rect.colliderect(i.rect):
            sprites.remove(i)
            score+=1
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