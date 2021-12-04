import random
import sys

import pygame

pygame.init()
# display
screen = pygame.display.set_mode((960, 640))
screen_rect = screen.get_rect()

# test rect
test_rect1 = pygame.Rect((screen_rect.x, 0, screen_rect.w, 100))
test_rect2 = pygame.Rect((screen_rect.x, 100, screen_rect.w, 100))
test_rect3 = pygame.Rect((screen_rect.x, 200, screen_rect.w, 100))
test_rect4 = pygame.Rect((screen_rect.x, 300, screen_rect.w, 100))
test_rect5 = pygame.Rect((screen_rect.x, 400, screen_rect.w, 100))
test_rect6 = pygame.Rect((screen_rect.x, 500, screen_rect.w, 100))
test_rect7 = pygame.Rect((screen_rect.x, 600, screen_rect.w, 100))

test_rect_list = [test_rect1, test_rect2, test_rect3, test_rect4]

# Z variable for 3d illusion
DDZ = 4
DZ = 0
Z = 0
posz = 0





class Texture: # todo change texture shade depending on z
    def __init__(self):
        self.texture_pos = 0

    def texture_switch(self):
        if self.texture_pos == 0:
            colour = (255, 255, 255)
            colour2 = (0,0,0)
        elif self.texture_pos == 1:
            colour = (0, 0, 0)
            colour2 = (255, 255, 255)
            self.texture_pos = 0
        return colour, colour2

texture_postion = Texture()
def redraw():  # redraws screen in game loop
    screen.fill((230, 230, 230))
    colour, colour2 = texture_postion.texture_switch()

    pygame.draw.rect(screen, (colour), test_rect1)
    pygame.draw.rect(screen, (colour2), test_rect2)
    pygame.draw.rect(screen, (colour), test_rect3)
    pygame.draw.rect(screen, (colour2), test_rect4)
    pygame.draw.rect(screen, (colour), test_rect5)
    pygame.draw.rect(screen, (colour2), test_rect6)
    pygame.draw.rect(screen, (colour), test_rect7)

    pygame.display.flip()
def user_input():
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_UP]:
        texture_postion.texture_pos += 1
    if True:
        if userInput[pygame.K_UP]:
            texture_postion.texture_pos += 1


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        user_input()
        redraw()


main()
