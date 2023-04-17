import sys
import pygame
import random


def lerp(a, b, t):
    return (1 - t) * a + t * b


def round_to_multiple_of_32(num):
    return round(num / 32) * 32


def colision(axis, direction, positionX, positionY):
    print(positionX)
    print(positionY)
    xC = int(positionX / 32)
    yC = int(positionX / 32)
    print(map_layout[yC+(1*direction)][xC])
    if (axis == 'x'):
        if map_layout[yC][xC+(1*direction)] == 1:
            return True
        else:
            return False
    else:
        if map_layout[yC+(1*direction)][xC] == 1:
            return True
        else:
            return False


# Initialize Pygame
pygame.init()

# Set the window size
window_size = (640, 480)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Zen Snake")

# Set up the game clock
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 24)

map_layout = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (150, 75, 0)

# Set the starting position of the rectangle
rect_x = 128
rect_y = 128
playerSpd = 0.2
alive = True
direction = 'none'
walking = False
newPosition = 0
distance = 0
xC = 0
yC = 0

# Set the movement speed of the rectangle

# Run the game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the game state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and walking == False and colision('x', -1, rect_x, rect_y) == False:
        direction = 'left'
        newPosition = rect_x - 32
        walking = True
    if keys[pygame.K_RIGHT] and walking == False and colision('x', 1, rect_x, rect_y) == False:
        direction = 'right'
        newPosition = rect_x + 32
        walking = True
    if keys[pygame.K_UP] and walking == False and colision('y', -1, rect_x, rect_y) == False:
        direction = 'up'
        newPosition = rect_y - 32
        walking = True
    if keys[pygame.K_DOWN] and walking == False and colision('y', 1, rect_x, rect_y) == False:
        direction = 'down'
        newPosition = rect_y + 32
        walking = True
    if keys[pygame.K_r]:
        print('test')

    if walking:

        if direction == 'left' or direction == 'right':
            rect_x = lerp(rect_x, newPosition, playerSpd)
            distance = rect_x - newPosition
        if direction == 'up' or direction == 'down':
            rect_y = lerp(rect_y, newPosition, playerSpd)
            distance = rect_y - newPosition

        if distance < 0:
            distance *= -1
        if (distance < 0.001):
            walking = False
            direction = 'none'
            rect_x = round_to_multiple_of_32(rect_x)
            rect_y = round_to_multiple_of_32(rect_y)

    # Draw the game

    screen.fill(black)

    for y in range(len(map_layout)):
        for x in range(len(map_layout[y])):
            if map_layout[y][x] == 1:
                pygame.draw.rect(screen, red, (
                    x*32, y*32, 32, 32))

    pygame.draw.rect(screen, white, (rect_x, rect_y, 32, 32))
    # Update the window
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
