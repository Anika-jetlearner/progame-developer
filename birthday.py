import pygame
import time
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Happy birthday!")
font=pygame.font.SysFont("Times New Roman",17)
text=font.render("Eat lots of cake!",True,"dark blue")
text1=font.render("Have a fun day!",True,"red")
image1=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\birthday cat.jpg")
scaleimage1=pygame.transform.scale(image1,(600,600))
image2=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\birthday bear.jpg")
scaleimage2=pygame.transform.scale(image2,(600,600))
image3=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\birthday penguin.jpg")
scaleimage3=pygame.transform.scale(image3,(600,600))




while True:
    screen.blit(scaleimage1,(0,0))
    pygame.display.update()
    time.sleep(3)
    screen.blit(scaleimage2,(0,0))
    screen.blit(text,(225,500))
    pygame.display.update()
    time.sleep(3)
    screen.blit(scaleimage3,(0,0))
    screen.blit(text1,(225,500))
    pygame.display.update()
    time.sleep(3)


    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()