import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
acceleration=2000
clock=pygame.time.Clock()

#boing=pygame.mixer.Sound(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\boing.mp3")


class ball:
    def __init__(self,radius,colour,x,y,vx,vy):
        self.vx=vx
        self.vy=vy
        self.radius=radius
        self.colour=colour
        self.position=(x,y)
        self.x=x
        self.y=y

        #self.vx1=vx1
        #self.vy1=vy1
        #self.radius1=radius1
        #self.colour1=colour1
        #self.position1=(x1,y1)
        #self.x1=x1
        #self.y1=y1
    def draw(self):
        pygame.draw.circle(screen,self.colour,self.position,self.radius)

Ball=ball(50,"blue",100,100,100,0)
Ball.draw()
Ball2=ball(30,"red",700,100,100,0)
Ball2.draw()

pygame.display.update()

while True:
    changetime=clock.tick(60)/1000
    u=Ball.vy
    u1=Ball2.vy
    Ball2.x=Ball2.x+Ball2.vx*changetime
    Ball.x=Ball.x+Ball.vx*changetime
    if Ball.x+Ball.radius>800 or Ball.x-Ball.radius<0:
        Ball.vx*=-1
       
    if Ball2.x+Ball2.radius>800 or Ball2.x-Ball2.radius<0:
        Ball2.vx*=-1
        
    Ball2.vy=u1+(acceleration*changetime)
    Ball.vy=u+(acceleration*changetime)
    Ball.y=Ball.y+(u+Ball.vy)*0.5*changetime
    Ball2.y=Ball2.y+(u1+Ball2.vy)*0.5*changetime
    if Ball.y+Ball.radius>600:
        Ball.y=600-Ball.radius
        Ball.vy=-u*0.9
        #boing.play()
    if Ball2.y+Ball2.radius>600:
            Ball2.y=600-Ball2.radius
            Ball2.vy=-u1*0.9
            #boing.play()
        
    Ball.position=(Ball.x,Ball.y)
    Ball2.position=(Ball2.x,Ball2.y)
    screen.fill("black")
    Ball.draw()
    Ball2.draw()
    pygame.display.update()
   
    
    
    

    for i in pygame.event.get():
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_SPACE:
                Ball.vy=-500

            if i.key==pygame.K_UP:
                Ball2.vy=-500
        if i.type==pygame.QUIT:
            pygame.quit()