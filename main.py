import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
player_image = pygame.image.load("arcade-game.png")
playerX = 370
playerY = 480


def player(x, y):
    screen.blit(player_image, (x, y))


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow pressed")
            if event.key == pygame.K_RIGHT:
                print("Right arrow pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("Left arrow released")
            if event.key == pygame.K_RIGHT:
                print("Right arrow released")
    screen.fill((148, 87, 235))

    player(playerX, playerY)
    pygame.display.update()
