import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Create raindrop list
drops = [{"x": random.randint(0, WIDTH), "y": random.randint(-HEIGHT, 0), "speed": random.uniform(3, 8)} for _ in range(100)]

running = True
while running:
    pygame.time.delay(20)
    win.fill((0, 0, 0))

    for drop in drops:
        drop["y"] += drop["speed"]
        if drop["y"] > HEIGHT:
            drop["y"] = random.randint(-HEIGHT, 0)
        pygame.draw.line(win, (0, 0, 255), (drop["x"], drop["y"]), (drop["x"], drop["y"] + 10))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
