# imports
import pygame
import os
from .Enemies import Enemy

# create a an empty list for Orge2
Robot_images = []


# add image for the Orge2
for x in range(10):
    string = str(x)
    Robot_images.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/Rofence/Robot", "Robot_00" + string + ".png")), (50, 50)))


# create a class for orge while inherit properties from Enemy File
class Orge2(Enemy):

    # define the details of the orge
    def __init__(self):
        super().__init__()
        self.maxHP = 3
        self.health = self.maxHP
        self.money = 8
        self.imgs = Robot_images[:]