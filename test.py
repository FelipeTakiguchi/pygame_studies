import pygame
from numpy import subtract

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
GAME_NAME = 'Teste'

size = [SCREEN_WIDTH, SCREEN_HEIGHT]

def set_speed(value, speed ):
    if value < 0: return speed
    elif value > 0: return speed * -1
    elif value == 0: return 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=(0, 200))

    def update(self):
        pass



class ReachPoint:  
    def __init__(self, wanted_pos, speed=5):
        self.wanted_pos = wanted_pos
        self.speed = speed 
    
    def update(self, object):
        self.pos = object.rect.topleft
        self.difference = tuple(subtract(self.pos, self.wanted_pos))
        self.x = set_speed(self.difference[0], self.speed)
        self.y = set_speed(self.difference[1], self.speed)
    

    def move_object(self, object):
        
        if object.rect.top == self.wanted_pos:
            return True

        self.update(object)
        pos = object.rect.topleft
        dif = tuple(subtract(pos, self.wanted_pos))

        x = set_speed(dif[0], self.speed)
        y = set_speed(dif[1], self.speed)

        # print(object.rect.topleft, self.wanted_pos)
        object.rect.move_ip(x, y)    
        if object.rect.topleft == self.wanted_pos:
            self.reaching_point = True
            
        return False

class mapPoint:
    def __init__(self) -> None:
        pass
    #TODO mapa de controle dos reachPoints    
    


class Game():
    def __init__(self):
        self.game_over = False

        self.speed = 5
        self.enemy = Enemy()
        self.enemy_group = pygame.sprite.Group()
        
        self.started = False
        self.reachedPointA = False
        self.reachedPointB = False
        self.reachedPointC = False


        self.enemy_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_timer, 1000)

        self.pointA = ReachPoint((200, 200))
        self.pointB = ReachPoint((200, 600))    
        self.pointC = ReachPoint((600, 600))

        

        self.enemy_group.add(self.enemy)



    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return True
            if event.type == pygame.MOUSEBUTTONDOWN: pass

            if not self.game_over: 
                if event.type == self.enemy_timer:
                    self.enemy_group.add(Enemy())
                
    def run_logic(self):
        pass


        # for obj in self.enemy_group:
        #     if self.pointA.move_object(obj) and not gotoNext:
                

        

        # if not self.started:
        #     self.enemy.rect.move_ip(5, 0)
        #     if self.enemy.rect.x == 200: 
        #         self.reachedPointA = True
        #         self.started = True

        # if self.reachedPointA:
        #     self.enemy.rect.move_ip(0, 5)
        #     if self.enemy.rect.y >= 600: 
        #         self.reachedPointB = True
        #         self.reachedPointA = False

        # if self.reachedPointB:
        #     self.enemy.rect.move_ip(5, 0)
        #     if self.enemy.rect.x >= 600: 
        #         self.reachedPointC = True
        #         self.reachedPointB = False

        # if self.reachedPointC:
        #     self.enemy.rect.move_ip(0, -5)
        #     if self.enemy.rect.y <= 200:
        #         self.reachedPointC = False

            

    def display_frame(self, screen):
        screen.fill('Black')
        if not self.game_over:
            self.enemy_group.draw(screen)


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