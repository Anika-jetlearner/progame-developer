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
    Ball.vy=u+(acceleration*changetime)
    Ball.y=Ball.y+(u+Ball.vy)*0.5*changetime
    Ball.draw()
    pygame.display.update()
    print(Ball.vy)
    print(Ball.y)
    print(changetime)
    
    
    

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()