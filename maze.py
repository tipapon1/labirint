from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3,  wall_x, wall_y,  wall_width, wall_height ):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))





class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed





mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()




win_width = 700
win_height = 500



window = display.set_mode((win_width, win_height))
display.set_caption('Лабаиринт')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))


clock = time.Clock()
FPS = 60


finish = False

player = Player("hero.png", 10, 400, 4)
monster = Enemy("cyborg.png", 620, 280, 2)
treasure = GameSprite("treasure.png", 580, 420, 0)
W1 = Wall(154, 205, 50, 100, 20, 450, 10)
W2 = Wall(154, 205, 50, 100, 480, 350, 10)
W3 = Wall(154, 205, 50, 100, 20, 10,380)

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!' , True, (255, 215, 0))
lose = font.render('YOU LOSE', True, (255, 0, 0))
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        player.reset()
        player.update()
        monster.reset()
        monster.update()
        W1.draw_wall()
        W2.draw_wall()
        W3.draw_wall()
        treasure.reset()
        if sprite.collide_rect(player, treasure):
            window.blit(win, (200, 200))
            treasure = True
            money.play()
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, W1) or sprite.collide_rect(player, W2) or sprite.collide_rect(player, W3):
            window.blit(lose, (200,200))
            finish = True
            kick.play()

       

    display.update()
    clock.tick(FPS)
