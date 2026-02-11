import pygame
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mega Jump")

# Colors
SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
PLATFORM_COLOR = (100, 200, 100)
PLAYER_COLOR = (255, 100, 100)

# Game Variables
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_width = 30
player_height = 30

vel_y = 0
gravity = 0.5
jump_power = -12

# Platforms: [x, y, width, height]
platforms = [[WIDTH // 2 - 50, HEIGHT - 50, 100, 10]]
for i in range(1, 10):
    platforms.append([random.randint(0, WIDTH - 100), HEIGHT - (i * 70), 100, 10])

score = 0
font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(SKY_BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Player Movement (Left/Right)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += 5

    # 2. Apply Gravity
    vel_y += gravity
    player_y += vel_y

    # 3. Collision with Platforms (Only when falling)
    if vel_y > 0:
        for p in platforms:
            if (player_x + player_width > p[0] and player_x < p[0] + p[2]) and \
                    (player_y + player_height > p[1] and player_y + player_height < p[1] + 15):
                vel_y = jump_power  # Bounce!

    # 4. Scroll Screen (If player goes high)
    if player_y < 200:
        scroll = 200 - player_y
        player_y = 200
        for p in platforms:
            p[1] += scroll
            if p[1] > HEIGHT:
                p[1] = 0 - random.randint(20, 50)
                p[0] = random.randint(0, WIDTH - 100)
                score += 1

    # 5. Game Over
    if player_y > HEIGHT:
        running = False

    # Drawing
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, player_width, player_height))
    for p in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, p)

    score_text = font.render(f"Height: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

print(f"Final Height Reached: {score}")
pygame.quit()