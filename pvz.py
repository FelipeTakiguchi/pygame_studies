import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
GAME_NAME = 'Plants vz Zombies'

size = [SCREEN_WIDTH, SCREEN_HEIGHT]

class Plant(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft=(200, 200))


class Game():
    def __init__(self):
        self.game_over = False

        self.plant = Plant()
        self.sprite_group = pygame.sprite.Group()

        self.sprite_group.add(self.plant)


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return True


    def run_logic(self):
        if not self.game_over: pass


    def display_frame(self, screen):
        screen.fill('Black')
        if not self.game_over:
            self.sprite_group.draw(screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption(GAME_NAME)

    done = False
    clock = pygame.time.Clock()

    game = Game()

    while not done:

        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()