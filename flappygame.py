import pygame
pygame.init()

bg=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\bagr.png")
bg=pygame.transform.scale(bg,(650,600))
fstill=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\flappystill.png")
fup=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\flappyup.png")
fdown=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\flappydown.png")
ground=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\groundbg.png")
pipe=pygame.image.load(r"C:\Users\Anika\OneDrive\Desktop\Python gamedeveloper course\Progame developer\images\pipe.png")
screen=pygame.display.set_mode((650,600))










while True:
    screen.blit(bg,(0,0))
    screen.blit(ground,(0,450))
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()