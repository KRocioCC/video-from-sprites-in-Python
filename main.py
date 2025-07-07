import pygame, sys

class StoryTeller(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []

        screen_width = 560
        screen_height = 680
        
        for i in range(1, 67 ):
            image = pygame.image.load(f'sprites/{i}.png')
            image = pygame.transform.scale(image, (screen_width, screen_height))
            self.sprites.append(image)
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        self.image_timer = 0
        self.image_duration = 250

    def start_story(self):
        self.image_timer = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.image_timer > self.image_duration:
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = len(self.sprites) - 1

            self.image_timer = pygame.time.get_ticks()

        self.image = self.sprites[self.current_sprite]

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

screen_width = 560
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Viaje al Cañón del Valle de las Ánimas")

moving_sprites = pygame.sprite.Group()
story = StoryTeller(0, 0)
moving_sprites.add(story)

pygame.mixer.music.load("relato.mp3")
pygame.mixer.music.play(-1, 0, 0)
story.start_story()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()

    pygame.display.flip()
    clock.tick(60)
