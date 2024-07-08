import pygame, sys
from data.util.utils import load_image
from data.scripts.player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 560))
        self.display = pygame.Surface((400, 280))
        self.clock = pygame.time.Clock()
        
        self.assets = {'background': load_image('Background.png')}
        self.player = Player()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.display.blit(self.assets['background'], (0, 0))
                   
            self.player.render(self.display)
            
            self.screen.blit(pygame.transform.scale(self.display, (800, 560)), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            
Game().run()