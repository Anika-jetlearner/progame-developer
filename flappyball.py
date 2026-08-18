import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
acceleration=2000
clock=pygame.time.Clock()
class ball:
    def __init__(self,radius,colour,x,y,vx,vy):
        self.vx=vx
        self.vy=vy
        self.radius=radius
        self.colour=colour
        self.position=(x,y)
        self.x=x
        self.y=y
    def draw(self):
        pygame.draw.circle(screen,self.colour,self.position,self.radius)

Ball=ball(50,"blue",100,100,100,0)
Ball.draw()

pygame.display.update()

while True:
    changetime=clock.tick(60)/1000
    u=Ball.vy
    Ball.x=Ball.x+Ball.vx*changetime
    if Ball.x+Ball.radius>800 or Ball.x-Ball.radius<0:
        Ball.vx*=-1
    Ball.vy=u+(acceleration*changetime)
    Ball.y=Ball.y+(u+Ball.vy)*0.5*changetime
    if Ball.y+Ball.radius>600:
        Ball.y=600-Ball.radius
        Ball.vy=-u*0.9
        
    Ball.position=(Ball.x,Ball.y)
    screen.fill("black")
    Ball.draw()
    pygame.display.update()
    print(Ball.vy)
    print(Ball.y)
    print(changetime)
    
    
    

    for i in pygame.event.get():
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_SPACE:
                Ball.vy=-500
        if i.type==pygame.QUIT:
            pygame.quit()