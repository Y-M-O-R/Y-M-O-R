import logging
import random

import pygame
from pygame import USEREVENT

# first game finished on the 04/10/2021 started on the 30 September 2021
# does need some tweaks
# change player speed
#
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
# sprite = pygame.image.load('flappyBird.png')

pygame.time.set_timer(USEREVENT + 2, 3000)

dinner = pygame.image.load(r'C:\Users\ryous\PycharmProjects\pythonProject\pygameTest\img\10.png')
rect = dinner.get_rect()


# def create_obstacles():
#     aa = random.randrange(500)
#     b = random.randrange(500)
#     # c = random.randrange()
#     # d = random.randrange()
#     pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((450, 50), (50, 250)))


class CreateObstacles(object):
    img = pygame.image.load(r'C:\Users\ryous\PycharmProjects\pythonProject\pygameTest\img\space.png')

    def __init__(self, sx, sy, wwidth, wheight):
        self.x = sx
        self.y = sy
        self.width = wwidth
        self.height = wheight
        self.hitbox = (sx, sy, wwidth, wheight)

    def draw(self, draw_screen):
        self.hitbox = (self.x + 120, self.y + 140, self.width + 60, self.height + 0)
        draw_screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(draw_screen, (255, 0, 0), self.hitbox, 2)


text = 0
textList = []


def redraw_window():
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
        rect.y -= vel + 0.00000000001
    if rect.y < 450:

        for i in range(vel):
            rect.y += 1
    if text > 30 and text // 5 not in textList:
        r = random.randint(1, 254)
        b = random.randint(1, 254)
        g = random.randint(1, 254)
        screen.fill(r, g, b)
    if 100 <= text <= 110:

        r = random.randint(1, 254)
        b = random.randint(1, 254)
        g = random.randint(1, 254)
        for i in range(10):
            j = random.randrange(1, 1920, 10)
            k = random.randrange(1, 1080, 5)
            pygame.draw.circle(screen, [r, g, b], (j, k), 75)
        pygame.display.flip()
    if text // 5 != 0 and text // 5 not in textList:
        textList.append(text // 5)

        for i in range(text // 5):
            obstcspeed += 0.001

    iftrue = redraw_window()
    if iftrue:
        text = 0
    # screen.blit(sprite, (x, y, width, height))
    textsurface = myfont.render(str(text), False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))
    screen.blit(dinner, rect)

    pygame.display.update()
