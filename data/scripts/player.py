import pygame
from data.util.utils import load_image

class Player:
    def __init__(self):
        self.img = load_image('player_idle_0.png')
        self.player_pos = [50, 50]
        
    def render(self, screen):
        screen.blit(self.img, (self.player_pos))