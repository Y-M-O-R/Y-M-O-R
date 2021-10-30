import pygame

pygame.init()


screen = pygame.display.set_mode((750, 750))
sprite_cont = {'x': 0, 'y': 0}


def quit_game():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


# sprite = pygame.draw.rect(screen, (23, 250, 250), rect)
sprite = pygame.image.load('edoidretsa.png')
rect = sprite.get_rect()
vel = 5
obstacle = pygame.Rect(300, 200, 80, 80)

a = True
run = True
while run:
    quit_game()
    screen.fill((72, 79, 71))
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT]:
        rect.x -= vel
    if userInput[pygame.K_RIGHT]:
        rect.x += vel

    if userInput[pygame.K_UP]:
        rect.y -= vel

    if userInput[pygame.K_DOWN]:
        rect.y += vel

    screen.blit(sprite, rect)
    if a:

        if int(vel) < 750:
            for i in range(2):
                m = obstacle = pygame.Rect(vel, 200, 80, 80)

                ac = pygame.draw.rect(screen, (0, 0, 0), m, 4)

    if rect.colliderect(obstacle):
        pygame.draw.rect(screen, (255, 0, 0), rect, 4)
        obstacle = pygame.Rect(0, 0, 0, 0)
        a = False
    # pygame.display.flip()
    pygame.display.update()

pygame.quit()
