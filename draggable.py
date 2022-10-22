from pygame import sprite, mouse


class Draggable(sprite.Sprite):
    def __init__(self, component):
        super().__init__()
        self.component = component
        self.image = self.component.image
        self.rect = self.component.rect
        self.isDragging = False

    def update(self):
        if self.isDragging:
            self.component.rect.center = mouse.get_pos()
