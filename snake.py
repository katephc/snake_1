import pygame
import random
from os import path

pygame.init()
pygame.mixer.init()
font = pygame.font.SysFont('Times New Roman', 30)
pygame.mixer.music.load('fonovaja_muzika.ogg')
pygame.mixer.music.play()


blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
aqua = (0, 255, 255)
white = (255, 255, 255)

screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')

snake_x = screen_width / 2
snake_y = screen_height / 2

snake_speed = 5
snake_size = 10
snake_length = 1
snake_block = []

fruit_x = 300
fruit_y = 400

speed_x = 0
speed_y = 10

game_over = False

running = True
clock = pygame.time.Clock()

while running:

    if not game_over:
        screen.fill(aqua)

        snake_head = [snake_x, snake_y]
        snake_block.append(snake_head)

        if len(snake_block) > snake_length:
            del snake_block[0]

        for x in snake_block[:-1]:
            if x == snake_head:
                game_over = True

        for block in snake_block:
            pygame.draw.rect(screen, blue, [block[0], block[1], snake_size, snake_size])
        pygame.draw.rect(screen, red, [fruit_x, fruit_y, snake_size, snake_size])

        snake_x += speed_x
        snake_y += speed_y

        if snake_x == fruit_x and snake_y == fruit_y:
            fruit_x = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
            fruit_y = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0
            snake_length += 1

        if (snake_x >= screen_width or snake_x < 0 or
                snake_y >= screen_height or snake_y < 0):
            game_over = True

    else:
        screen.fill(white)
        score = font.render('You scored ' + str(snake_length), False, red)
        screen.blit(score, (10, screen_height / 2 - 100))
        text = font.render('You lost! Press \'Q\' to quit, or Space to play again', False, red)
        screen.blit(text, (10, screen_height / 2))

    pygame.display.flip()
    clock.tick(snake_speed)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_SPACE:
                game_over = False
                snake_x = screen_width / 2
                snake_y = screen_height / 2
                snake_blocks = []
                snake_length = 1
            if event.key == pygame.K_UP:
                speed_x = 0
                speed_y = -10
            if event.key == pygame.K_DOWN:
                speed_x = 0
                speed_y = 10
            if event.key == pygame.K_LEFT:
                speed_y = 0
                speed_x = -10
            if event.key == pygame.K_RIGHT:
                speed_y = 0
                speed_x = 10
        if event.type == pygame.QUIT:
            running = False
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    pygame.time.delay(20)
