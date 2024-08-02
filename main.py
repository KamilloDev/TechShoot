import pygame, sys
from data.scripts.utils import load_image, load_images, Animation
from data.scripts.entity import Player
from data.scripts.tilemap import Tilemap


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 560))
        self.display = pygame.Surface((400, 280))
        self.clock = pygame.time.Clock()
    
       
        """'players': load_images('data/images')"""
        
        # def path = 'data/images/'
        self.assets = {'background': load_image('Background.png'),
                       'icon': load_image('player_idle_0.png'),
                       'grass': load_images('tiles/grass'),
                       'decor': load_images('tiles/decor'),
                       'large_decor': load_images('tiles/large_decor'),
                       'stone': load_images('tiles/stone'),
                       'player': load_image('player_idle_0.png'),
                       'player/idle': Animation(load_images('entities/player'))}
        
        
        self.tilemap = Tilemap(self, tile_size=16)
        self.tilemap.load('Map.json')
        
        self.player = Player(self, [200, 50], [19, 27])
        self.keys = {'left': False, 'right': False}
        
        self.movement = [False, False]
        
        self.scroll = [0, 0]
        
        pygame.display.set_icon(self.assets['icon'])
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
            
            pygame.display.set_caption(f'TechShoot | Fps: {str(int(self.clock.get_fps()))}')
            
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            self.render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            
            self.display.blit(self.assets['background'], (0, 0))
            self.tilemap.render(self.display, offset=self.render_scroll)
            
            self.player.update(self.tilemap, self.movement)
            self.player.render(self.display)
            
            
            self.screen.blit(pygame.transform.scale(self.display, (800, 560)), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            
Game().run()