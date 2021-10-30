import pygame
import logging
import time
import random

from pygame import USEREVENT

pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
myfont = pygame.font.SysFont('VARSITY', 30)
logging.basicConfig(filename='flappyLog', level=logging.INFO)

# initialize and set screen
pygame.init()

screen = pygame.display.set_mode((500, 500))

# adds option to quit

# set player x,y velocity
x, y = 50, 450
width, height = 40, 60
vel = 5
# game loop
run = True
sprite = pygame.image.load('flappyBird.png')

pygame.time.set_timer(USEREVENT + 2, 3000)

dinner = pygame.image.load('10.png')
rect = dinner.get_rect()


# def create_obstacles():
#     aa = random.randrange(500)
#     b = random.randrange(500)
#     # c = random.randrange()
#     # d = random.randrange()
#     pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((450, 50), (50, 250)))


class CreateObstacles(object):
    img = pygame.image.load('space.png')

    def __init__(self, x, y, wwidth, wheight):
        self.x = x
        self.y = y
        self.width = wwidth
        self.height = wheight
        self.hitbox = (x, y, wwidth, wheight)

    def draw(self, screen):
        self.hitbox = (self.x +120, self.y +140, self.width + 60, self.height + 0)
        screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


text = 0
textList=[]

def redrawWindow():
    for objectts in objects:
        objectts.draw(screen)
        if rect.colliderect(objectts.hitbox):
            pygame.draw.rect(screen, (255, 0, 28), rect, 4)
            return True


objects = []

obstcspeed = 1.4
while run:
    screen.fill((176, 176, 176))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        if event.type == USEREVENT + 2:
            yaxis = random.randint(0, 230)
            objects.append(CreateObstacles(500, yaxis, 0, 64))

    for k in objects:

        k.x -= obstcspeed
        if k.x < -k.width * -1:
            logging.info(f'object.x < -object.width* -1: {k.x} < {-k.width * -1}')
            objects.pop(objects.index(k))
            text += 1

    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_DOWN] and rect.y < 500 - height - vel:
        rect.y += vel
    if userInput[pygame.K_UP] and rect.y > vel:
        rect.y -= vel + vel
    if rect.y < 450:

        for i in range(vel):
            rect.y += 1
    if text>30 and text//5 not in textList:

        r = random.randint(1, 254)
        b = random.randint(1, 254)
        g = random.randint(1, 254)
        screen.fill(r,g,b)
    if 100 <= text <= 110:

        r = random.randint(1, 254)
        b = random.randint(1, 254)
        g = random.randint(1, 254)
        for i in range(10):
            j = random.randrange(1, 1920, 10)
            k = random.randrange(1, 1080, 5)
            pygame.draw.circle(screen, [r, g, b], (j, k), 75)
        pygame.display.flip()
    if text // 5 != 0 and text//5 not in textList:
        textList.append(text//5)

        for i in range(text // 5):
            obstcspeed += 0.001
            print(text//5,obstcspeed)


    iftrue = redrawWindow()
    if iftrue:
        text = 0
    # screen.blit(sprite, (x, y, width, height))
    textsurface = myfont.render(str(text), False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))
    screen.blit(dinner, rect)


    pygame.display.update()

for i in objects:
    print(i)
