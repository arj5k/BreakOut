import pygame
import random
pygame.init()#hi

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()


class Player(pygame.Rect):
    def __init__(self,x,y):
        super().__init__(x,y,100,25) # arbitrary values TODO tweak
        self.vx = 0
    def draw(self):
        pygame.draw.rect(screen, 'orange', self, 0) #fill
        pygame.draw.rect(screen, 'black', self, 1) #outline
    def update(self):
        self.x+=self.vx
        if self.x <0:
            self.x = 0
        elif self.x + self.width > screen.get_width():
            self.x = screen.get_width()-self.width

class Ball(pygame.Rect):
    def __init__(self, x, y, diameter):
        super().__init__(x, y, diameter, diameter)
        self.vx = random.randint(3, 4) * random.choice([1, -1])
        self.vy = 8#random.randint(3, 4) # TODO tweak?

    def draw(self):
        pygame.draw.rect(screen, 'white', self, 0)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if player.colliderect(self):
            self.vy *= -1
            self.y = player.y - self.width
            diff = (ball.x + ball.w/2) - (player.x + player.w/2)
            self.vx += diff//10
        if (self.x < 0):
            self.vx *= -1
        if (self.x + ball.width > screen.get_width()):
            self.vx *= -1
        if (self.y < 0):
            self.vy *= -1
        if (self.y + ball.width > screen.get_height()):
            self.reset()
    def reset(self):
        self.x = int(screen.get_width()/2) - 10
        self.y = int(screen.get_height()/2) + 20

BRICK_WIDTH = 75
BRICK_HEIGHT = 25
class Brick(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x,y,BRICK_WIDTH,BRICK_HEIGHT)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    def draw(self):
        pygame.draw.rect(screen, self.color, self, 0, border_radius = 8)
        pygame.draw.rect(screen, 'black', self, 2, border_radius = 8)
    def update(self, ball):
        if(self.colliderect(ball)):
            if(self.x<(ball.x+ball.width) and ball.x<(self.x+BRICK_WIDTH)):
                ball.vy*=-1
            if((ball.y+ball.width)>self.y +1 and ball.y+1<(self.y+BRICK_HEIGHT)):
                ball.vx*=-1
            bricks.remove(self)


bricks = []
ball = Ball(screen.get_width()/2 - 10, screen.get_height()/2 +20, 20)
player = Player(screen.get_width()/2-50, screen.get_height()-50)
for y in range(10, 250, BRICK_HEIGHT+2):
    for x in range(5, screen.get_width()-BRICK_WIDTH, BRICK_WIDTH+2):
        bricks.append(Brick(x,y))
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.vx += -10
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.vx += 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame. K_a:
                player.vx += 10
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
               player.vx -= 10
    # Do logical updates here.
    player.update()
    ball.update()
    for brick in bricks:
        brick.update(ball)
    screen.fill("grey")
    # Render the graphics here.

    player.draw()
    ball.draw()
    for brick in bricks:
        brick.draw()
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
