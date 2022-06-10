from unicodedata import name
import pygame
import random
import math
from pygame import mixer


# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("background.jpg")

# Background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Player
player_image = pygame.image.load("arcade-game.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy

enemy_image = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemy_image.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(5)
    

# Bullet
bullet_image = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 1
bulletY_change = 1
currentX = 0
bullet_state = "ready"
# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Functions
def game_over_text():
    game_over = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over, (200, 250))


def show_score(x,y):
    score_value = font.render("Score : " + str(score), True, (255,255,255))
    screen.blit(score_value, (x, y))
def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image,(x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                 playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0
    screen.fill((148, 87, 235))
    # Background image
    screen.blit(background, (0,0))
    playerX += playerX_change
    

    # Boundries for player
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 735

    # Boundries for enemy
    for i in range(num_of_enemies):

        # Game over
        if enemyY[i] > 200:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= 736:
            enemyX[i] = 735
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play(1)
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bullet_state is "ready":
        bulletX = playerX
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bullet_sound = mixer.Sound("laser.wav")
        bullet_sound.play()
        bulletY -= bulletY_change
        if bulletY <= 0:
            bullet_state = "ready"
            bulletY = 480
    # Collision
   


    player(playerX, playerY)
    show_score(textX, textY)
    
    pygame.display.update()
