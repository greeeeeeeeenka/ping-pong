from pygame import *

clock = time.Clock()
FPS = 90

main_win = display.set_mode((600,500))

display.set_caption('pinpong')

run = True
finish = False

back = (150,205,205)

main_win.fill(back)
font.init()
font1 = font.SysFont(None, 36)

text_left_win = font1.render('ИГРОК СЛЕВА ПОБЕЖДАЕТ!',1,(0,200,0))

text_right_win = font1.render('ИГРОК СПРАВА ПОБЕЖДАЕТ!',1,(0,200,0))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    def reset(self):
        main_win.blit(self.image,(self.rect.x, self.rect.y))
    # def collidepoint(self, player_x, player_y):
    #     return self.rect.collidepoint(player_x, player_y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 295:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 295:
            self.rect.y += self.speed

player_left = Player('5.png', 10, 150, 50, 200, 7)

player_right = Player('5.png', 540, 150, 50, 200, 7)

ball = GameSprite('222.png', 280, 230, 40, 40, 7)

flag = False

speed_x = 5
speed_y = 5

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False 
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                flag = True       
    if finish != True:
        main_win.fill(back)

        player_left.reset()
        player_left.update_l()

        player_right.reset()
        player_right.update_r()

        ball.reset()
        if flag:

            ball.reset()

            ball.rect.x += speed_x
            ball.rect.y += speed_y
            # if ball.rect.y < w0:
            #     speed_y *= -1
            if ball.rect.y > 460 or ball.rect.y < 0:
                speed_y *= -1

            if ball.rect.x > 560:
                main_win.blit(text_left_win,(120,200))
                finish = True

            if ball.rect.x < 0:
                main_win.blit(text_right_win,(120,200))  
                finish = True          

            if ball.rect.x > 560 or ball.rect.x < 0:
                speed_x *= -1

            if ball.colliderect(player_left.rect):
                # speed_y *= -1
                speed_x *= -1

            if ball.colliderect(player_right.rect):
                # speed_y *= -1  
                speed_x *= -1



            # if ball.rect == player_left.rect:
            #     speed_y *= -1
            # if ball.rect == player_right.rect:
            #     speed_y *= -1
        
            

            # ball.rect.x += ball.speed
            # ball.rect.y += ball.speed
            # if ball.rect.y(player_left.rect or player_right.rect):
            #     ball.speed *= -1
            # if ball.rect.y < 0:
            #     ball.speed *= -1
            # if ball.rect.x > 425 or ball.rect.x < 25:
            #     ball.speed *= -1

    display.update()
    clock.tick(FPS)