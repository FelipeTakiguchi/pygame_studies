import pygame
from plant import Plant
from enemy import Enemy

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
GAME_NAME = 'Plants vz Zombies'

size = [SCREEN_WIDTH, SCREEN_HEIGHT]


class Game():
    def __init__(self):
        self.game_over = False

        self.sprite_group = pygame.sprite.Group()
        self.plant_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()

        for i in range(5):
            plant = Plant((200, 125 * (i + 1)))
            self.plant_group.add(plant)
            self.sprite_group.add(plant)

        for i in range(5):
            enemy = Enemy((1000, 125 * (i + 1)))
            self.enemy_group.add(enemy)
            self.sprite_group.add(enemy)


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return True


    def run_logic(self):
        if not self.game_over:
            for enemy in self.enemy_group:
                collide_plant = pygame.sprite.spritecollide(enemy, self.plant_group, False)

                if collide_plant:
                    enemy.speed = 0
                    enemy.give_damage(collide_plant[0])
                else:
                    enemy.speed = 5

    def display_frame(self, screen):
        screen.fill('Black')
        if not self.game_over:
            self.sprite_group.draw(screen)
            self.sprite_group.update()

            for plant in self.plant_group:
                plant.draw_range(screen=screen)


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
