import pygame, sys
from data.util.utils import load_image, load_images
from data.scripts.player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 560))
        self.display = pygame.Surface((400, 280))
        self.clock = pygame.time.Clock()
        
        self.keys = {'left': False,
                     'right': False}
        
        """'players': load_images('data/images')"""
        
        self.assets = {'background': load_image('Background.png'),
                       'icon': load_image('player_idle_0.png')}
        
        self.player = Player([50, 50])
        
        pygame.display.set_icon(self.assets['icon'])
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.keys['left'] = True
                    if event.key == pygame.K_d:
                        self.keys['right'] = True
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.keys['left'] = False
                    if event.key == pygame.K_d:
                        self.keys['right'] = False
            
            pygame.display.set_caption(f'TechShoot | Fps: {str(int(self.clock.get_fps()))}')
            
            self.display.blit(self.assets['background'], (0, 0))
                   
            self.player.apply_gravity(self.keys)
            self.player.render(self.display)
            
            
            self.screen.blit(pygame.transform.scale(self.display, (800, 560)), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            
Game().run()