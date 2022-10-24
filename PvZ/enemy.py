from pygame import sprite, Surface

class Enemy(sprite.Sprite):
    def __init__(self, pos=(0, 0)):
        super().__init__()
        self.image = Surface((50, 50))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)
        self.damage = 5
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed
        self.destroy()

    def destroy(self):
        if self.rect.x <= 0:
            self.kill()

    def give_damage(self, plant):
        plant.recive_damage(self.damage)