# Spacewalk

import pygame

WIDTH = 800
HEIGHT = 600

player_x = 600
player_y = 350

ship_x = 550
ship_y = 300

def draw():
    screen.blit(images.backdrop, (0,0))  # X, Y from top left => down right
    screen.blit(images.mars, (50, 50))
    screen.blit(images.astronaut, (player_x, player_y))
    screen.blit(images.ship, (ship_x, ship_y))

def game_loop():
    global player_x, player_y

    # keyboard listeners

    if keyboard.right:
        player_x += 5
    elif keyboard.left:
        player_x -= 5
    elif keyboard.up:
        player_y -= 5
    elif keyboard.down:
        player_y += 5

clock.schedule_interval(game_loop, 0.03)
