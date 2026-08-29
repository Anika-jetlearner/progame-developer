import pygame
import random
pygame.init()
screen=pygame.display.set_mode((800,600))




class Shapes:
    def __init__(self,rectx,recty,circx,circy):
        self.rectx=rectx
        self.recty=recty
        self.circx=circx
        self.circy=circy

        

    def drawrect(self):
        pygame.draw.rect(screen,"red",(self.rectx,self.recty,200,100))

    def drawcirc(self):
        pygame.draw.circle(screen,"blue",(self.circx,self.circy),50)

    def drawcircpos(self):
        pygame.draw.circle(screen,"yellow",(mouse),100)

rectangle=Shapes(50,50,0,0)
circle=Shapes(0,0,50,50)
circlepos=Shapes(0,0,0,0)

pygame.display.update()


while True:
    mouse=pygame.mouse.get_pos()
    print(mouse)
    for i in pygame.event.get():

        if i.type==pygame.MOUSEBUTTONDOWN:
            circlepos.drawcircpos()
            pygame.display.update()


        if i.type==pygame.QUIT:
            pygame.quit()

        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_r:
                rectangle.rectx=random.randint(0,800)
                rectangle.recty=random.randint(0,600)
                rectangle.drawrect()
                pygame.display.update()

        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_c:
                circle.circx=random.randint(0,800)
                circle.circy=random.randint(0,600)
                circle.drawcirc()
                pygame.display.update()
