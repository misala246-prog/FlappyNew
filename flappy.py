import pygame
import random
import sys

pygame.init()

# Screen
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# Load images
bg = pygame.image.load("bg.png")
bird_img = pygame.image.load("bird.png")
pipe_img = pygame.image.load("pipe.png")

bird_img = pygame.transform.scale(bird_img, (50, 35))
pipe_img = pygame.transform.scale(pipe_img, (80, 500))
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# Sound
hit = pygame.mixer.Sound("hit.wav")

# Bird
bird_x = 50
bird_y = 250
bird_vel = 0
gravity = 0.5

# Pipes
pipe_gap = 150
pipe_x = WIDTH
pipe_y = random.randint(-300, -100)
pipe_speed = 3

score = 0
font = pygame.font.SysFont("Arial", 32)

def draw():
    screen.blit(bg, (0, 0))
    screen.blit(bird_img, (bird_x, bird_y))
    screen.blit(pipe_img, (pipe_x, pipe_y))
    screen.blit(pipe_img, (pipe_x, pipe_y + 500 + pipe_gap))
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            bird_vel = -8

    bird_vel += gravity
    bird_y += bird_vel

    pipe_x -= pipe_speed
    if pipe_x < -80:
        pipe_x = WIDTH
        pipe_y = random.randint(-300, -100)
        score += 1

    bird_rect = pygame.Rect(bird_x, bird_y, 50, 35)
    top_pipe = pygame.Rect(pipe_x, pipe_y, 80, 500)
    bottom_pipe = pygame.Rect(pipe_x, pipe_y + 500 + pipe_gap, 80, 500)

    if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
        hit.play()
        pygame.time.delay(500)
        bird_y = 250
        bird_vel = 0
        pipe_x = WIDTH
        score = 0

    if bird_y > HEIGHT or bird_y < 0:
        bird_y = 250
        bird_vel = 0
        pipe_x = WIDTH
        score = 0

    draw()

pygame.quit()
sys.exit()