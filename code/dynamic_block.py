import pygame
from settings import *


class DynamicBlock(pygame.sprite.Sprite):
    def __init__(self, pos, group, size):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.fill("black")

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)

    def move(self, y):
        # self.pos.y = forced_vibrations(w, time)
        self.pos.y = y

        self.rect.bottom = int((self.pos.y + 1) * ((680 - 100) / (1 + 1)) + 100)

    def move_2(self, y):
        self.pos.y = y

        try:
            self.rect.bottom = int((self.pos.y + 5) * ((600 - 100) / (5 + 5)) + 0)
        except:
            print("Nieskończoność")
