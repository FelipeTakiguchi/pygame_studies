from pygame import Surface, sprite, time

class Plant(sprite.Sprite):
    def __init__(self, pos=(0, 0)):
        super().__init__()

        self.health = 100
        self.image = Surface((50, 50))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)

        self.range = Surface((1200, 1))
        self.range.fill('red')
        self.range_rect = self.image.get_rect(center=self.rect.center)

    def draw_range(self, screen):
        screen.blit(self.range, self.range_rect.center)

    def recive_damage(self, damage):
        print(self.health)
        self.health -= damage
        time.wait(200)

    def update(self):
        self.destroy()

    def destroy(self):
        if self.health <= 0:
            self.kill()

