import pygame
from data.util.utils import load_image

class Player:
    def __init__(self, pos):
        self.player = load_image('player_idle_0.png')
        self.p_rect = self.player.get_rect()
        self.player_pos = pos
        self.velocity = [0, 0]
        self.gravity = 0.2
        
    def apply_gravity(self, keys):
        self.velocity[1] += self.gravity 
        self.player_pos[1] += self.velocity[1]
        self.player_pos[0] += self.velocity[0]

        if self.velocity[0] != 0:
            self.velocity[0] -= 0.1
        elif self.velocity[0] != 0:
            self.velocity[0] += 0.1
        
        if keys['left']:
            self.velocity[0] -= 0.5
        if keys['right']:
            self.velocity[0] += 0.5

    def jump(self):
        self.velocity[1] = -2

        
    def render(self, display):
        display.blit(self.player, (self.player_pos))