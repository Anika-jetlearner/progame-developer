import pygame
pygame.init()


class Cars:
    def __init__(self):
        self.brand=""
        self.speed=260
    def details(self):
        self.brand=input("what is the brand?")
    def display(self):
        print("the brand is",self.brand)
        print("the speed is",self.speed,"kmph")

    def accelerate(self):
        self.speed+=10
        print("Vrooooooooooom")

car1=Cars()
car1.details()
car1.display()
car1.accelerate()
car1.accelerate()
car1.display()

