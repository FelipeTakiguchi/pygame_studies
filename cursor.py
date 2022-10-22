from pygame import sprite, image, transform, mouse, locals


def change_size(image, size, angle=0):
    return transform.rotozoom(image, angle, size)

def image_load(path):
    return image.load(path).convert_alpha()

class Cursor(sprite.Sprite):
    def __init__(self, size=0.25):
        super().__init__()  

        self.size = size
        self.isHovering = False
        self.isClicking = False
        self.object_dragged = None

        # Sprites 
        self.cursor_1 = change_size(image_load('graphics/cursor/cursor_1.png'), self.size)
        self.cursor_2 = change_size(image_load('graphics/cursor/cursor_2.png'), self.size)
        
        self.cursor_hold_1 = change_size(image_load('graphics/cursor/cursor_hold_1.png'), self.size)
        self.cursor_hold_2 = change_size(image_load('graphics/cursor/cursor_hold_2.png'), self.size)
        
        self.cursor = [self.cursor_1, self.cursor_2, self.cursor_hold_2, self.cursor_hold_1]
        self.index = 0
        
        self.image = self.cursor[self.index]
        self.rect = self.image.get_rect()

    def update(self):
        self.image = self.cursor[self.index]
        self.rect.center = mouse.get_pos()

        if self.isHovering and not self.isClicking:
            self.index = 2
        
        
    def mouse_click(self, event):
        if event.type == locals.MOUSEBUTTONDOWN:
            self.isClicking = True
            
            if self.isHovering:
                self.index = 3
            else:
                self.index = 1       
        if event.type == locals.MOUSEBUTTONUP:
            self.isClicking = False
            self.object_dragged.isDragging = False
            self.index = 0
        

    def mouse_interact(self, event, object_list):
        if event.type == locals.MOUSEMOTION:
            for object in object_list:
                if object.rect.collidepoint(mouse.get_pos()):
                    self.isHovering = True
                    self.object_dragged = object
                    
                    if self.isClicking:
                        object.isDragging = True
                    break
                else:
                    self.isHovering = False
                    self.index = 0
                    
                    object.isDragging = False
                

