import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

class Shapes:
    def __init__(self,dimension,colour):
        self.dimension=dimension
        self.colour=colour
    def draw(self):
        pygame.draw.rect(screen,self.colour,self.dimension)

rectangle=Shapes((400,300,200,100),"white")
rectangle.draw()
pygame.display.update()
        
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()