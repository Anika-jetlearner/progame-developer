import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
class Circle:
    def __init__(self,colour,radius,position,width):
        self.colour=colour
        self.radius=radius
        self.position=position
        self.width=width
    def draw(self):
        pygame.draw.circle(screen,self.colour,self.position,self.radius,self.width)
    def increase(self):
        self.radius+=5
        self.draw()
circle=Circle("red",50,(400,300),20)


while True:
    for i in pygame.event.get():
        if i.type==pygame.MOUSEBUTTONDOWN:
            circle.draw()
            pygame.display.update()
        if i.type==pygame.MOUSEBUTTONUP:
            circle.increase()
            pygame.display.update()

        if i.type==pygame.QUIT:
            pygame.quit()