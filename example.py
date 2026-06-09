"""
TODO:
    fix
        lag
        quit

    td
        hold movement

    new
        music!
            https://www.geeksforgeeks.org/python/python-playing-audio-file-in-pygame/

"""

import time
import pygame
from debug import debug
import colors as c
#import sys

pygame.init()
clock = pygame.time.Clock()

HEIGHT = 640
WIDTH = 640
window = (HEIGHT, WIDTH)
# Height & Width for single block
SHEIGHT = HEIGHT / 16
SWIDTH = WIDTH / 16

screen = pygame.display.set_mode(window)
background = pygame.Surface(window)
green_img = pygame.image.load("assets/green.png").convert()
red_img = pygame.image.load("assets/red.png").convert()
wall_bump_audio = pygame.mixer.Sound("assets/martial-arts-fast-punch.wav")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

Yelx = 200
Yely = 200

green_img = pygame.transform.scale(
    green_img, (green_img.get_width() * 2, green_img.get_height() * 2)
)

red_img = pygame.transform.scale(
    red_img, (red_img.get_width() * 2, red_img.get_height() * 2)
)


# pygame.draw.rect(background, (0, 255, 255), (20, 20, 20 , 20))
# pygame.draw.rect(background, (255,0,  255), (120, 120, 50 , 50))
screen.blit(background, (0, 0))
screen.fill(c.WHITE)
pygame.display.update()
running = True
x = 0

prev_time = time.time_ns()
delta_time = 0.1

moving = False

# sound = pygame.mixer.Sound("clank.wav")

cycle = 0
FPS = 30

OOPS = False

while running:

    clock.tick(FPS)
    # Comute delta time
    now = time.time_ns()
    dt = now - prev_time
    # print(f"{now} - {prev_time} = {dt}")
    prev_time = now
    # pygame.display.flip()
    # if cycle == 0:
    # print(f"Clock: {clock.get_rawtime()}")
    for row in range(0, int(HEIGHT / SHEIGHT)):
        for col in range(0, int(WIDTH / SWIDTH)):
            if (x + row + col) % 2 == 0:
                # print(f"EVEN:  {x} {r} {c}")
                screen.blit(green_img, (row * SHEIGHT, col * SWIDTH))
                screen.blit(red_img, (row * SHEIGHT, (col + 1) * SWIDTH))
            else:
                # print(f"ODD:  {x} {r} {c}")
                screen.blit(red_img, (row * SHEIGHT, col * SWIDTH))
                screen.blit(green_img, (row * SHEIGHT, (col + 1) * SWIDTH))

    pygame.draw.rect(screen, c.YELLOW, (Yelx+2, Yely+2, SHEIGHT - 4, SWIDTH - 4))
    cycle = 0
    x = 1 if x == 0 else 0

    #    screen.blit(potato_img, (x, 30))
    #
    #    hitbox = pygame.Rect(x, 30, potato_img.get_width(), potato_img.get_height())
    #
    #    mpos = pygame.mouse.get_pos()
    #
    #    target = pygame.Rect(300, 0, 160, 280)
    #    collision = hitbox.colliderect(target)
    #    m_collision = target.collidepoint(mpos)
    #    pygame.draw.rect(screen, (255 * collision, 255 * m_collision, 0), target)
    #
    #    if moving:
    #        x += 50 * delta_time
    #
    #    text = font.render('Hello World!', True, (0, 0, 0))
    #    screen.blit(text, (300, 100))
    #
    for event in pygame.event.get():
        print(f"Event: {event}")
        if event.type == pygame.QUIT:
            running = False

        # wasd move w,s,a,d
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if Yely >= SHEIGHT:
                    Yely -= SHEIGHT
                else:
                    OOPS = True
                moving = True
            if event.key == pygame.K_s:
                if Yely <= HEIGHT - 2*SHEIGHT:
                    Yely += SHEIGHT
                else:
                    OOPS = True
                moving = True
            if event.key == pygame.K_a:
                if Yelx >= SWIDTH:
                    Yelx -= SWIDTH
                else:
                    OOPS = True
                moving = True
            if event.key == pygame.K_d:
                if Yelx <= WIDTH - 2*SWIDTH:
                    Yelx += SWIDTH
                else:
                    OOPS = True
                moving = True
            if OOPS:
                wall_bump_audio.play()
                OOPS = False
            if event.key in [pygame.K_q,  pygame.K_ESCAPE]:
                running = False

            # if event.key == pygame.K_f:
            #    sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving = False

    #
    delta_time = clock.tick(60) / 100
    delta_time = max(0.001, min(0.1, delta_time))

    cycle = (cycle + 1) % 100
    debug(f"Location: {Yelx}, {Yely}")
    pygame.display.update()
    clock.tick(FPS/8)
    # print(cycle)

# sys.exit()
pygame.display.quit()
pygame.quit()
