import sys
import pygame
import random
import json

with open('battle_city_map.json') as f:
    map_layout = json.load(f)


def lerp(a, b, t):
    return (1 - t) * a + t * b


def round_8(num):
    return round(num / 8) * 8


def round_4(num):
    return round(num / 4) * 4


def get_matrix_subset(matrix, px, py):
    """ Retorna uma submatriz da matriz 'matrix' que está contida no retângulo
        definido pelos pontos 'px' (superior esquerdo) e 'py' (inferior direito).

        Args:
            matrix (list): uma matriz representada como uma lista de listas.
            px (tuple): as coordenadas do ponto superior esquerdo (linha, coluna).
            py (tuple): as coordenadas do ponto inferior direito (linha, coluna).

        Returns:
            list: uma submatriz representada como uma lista de listas.
    """
    start_row, start_col = px
    end_row, end_col = py

    # Garante que start_row <= end_row e start_col <= end_col
    if start_row > end_row:
        start_row, end_row = end_row, start_row
    if start_col > end_col:
        start_col, end_col = end_col, start_col

    # Extrai a submatriz definida pelo retângulo
    return [row[start_col:end_col+1] for row in matrix[start_row:end_row+1]]


def newCollision(p1x, p1y, p2x, p2y):
    p1x = round_4(p1x)
    p1y = round_4(p1y)
    p2x = round_4(p2x)
    p2y = round_4(p2y)

    p1 = (p1y, p1x)
    p2 = (p2y, p2x)

    map_hovered = get_matrix_subset(map_layout, p1, p2)
    print(map_hovered)


def colision(axis, direction, positionX, positionY):
    if (axis == 'x'):
        positionX = round_8(positionX)
        positionY = round_8(positionY)
        xC = int((positionX+(playerSpd*direction)) / 8)
        yC = int((positionY) / 8)
    else:
        xC = int((positionX) / 8)
        yC = int((positionY+(playerSpd*direction)) / 8)
    try:
        map_layout[yC][xC]
        if map_layout[yC][xC] == 1:
            return True
        else:
            return False
    except:
        return False


def destroyBrick(axis, direction, positionX, positionY, shoot):
    if (axis == 'x'):
        positionX = round_8(positionX)
        positionY = round_8(positionY)
        xC = int((positionX+(playerSpd*direction)) / 8)
        yC = int((positionY) / 8)
    else:
        xC = int((positionX) / 8)
        yC = int((positionY+(playerSpd*direction)) / 8)
    try:
        if map_layout[yC][xC] == 1:
            if axis == 'x':
                map_layout[yC][xC] = 0
                map_layout[yC-1][xC] = 0
                map_layout[yC+1][xC] = 0
                map_layout[yC-2][xC] = 0
                index_ = shoots.index(shoot)
                shoots.remove(shoot)
            else:
                map_layout[yC][xC] = 0
                map_layout[yC][xC-1] = 0
                map_layout[yC][xC+1] = 0
                map_layout[yC][xC+2] = 0
                index_ = shoots.index(shoot)
                shoots.remove(shoot)
    except:
        None


def shooting(x, y, dir, objs, owner, col):
    if dir == 'left' or dir == 'up':
        axis = -1
    else:
        axis = 1

    if dir == 'left' or dir == 'right':
        y += rect_size/2
    else:
        x += rect_size/2
    objs.append({
        'x': x,
        'y': y,
        'direction': dir,
        'axis': axis,
        'owner': owner,
        'colision': col
    })


# Initialize Pygame
pygame.init()

# Set the window size
window_size = (416, 416)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Battle city clone")

# Set up the game clock
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 24)


# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (150, 75, 0)

# Set the starting position of the rectangle
rect_x = 1
rect_y = 1
playerSpd = 1
alive = True
direction = 'none'
walking = False
newPosition = 0
distance = 0
xC = 0
yC = 0
rect_size = 28
aimDir = 'left'
delay = 100

shoots = [
]
shootSpd = 2

# Set the movement speed of the rectangle

# Run the game loop
while True:
    delay += 1
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the game state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        aimDir = 'left'
        if (rect_x - playerSpd > 0 and colision('x', -1, rect_x, rect_y) == False):
            rect_x -= playerSpd
    if keys[pygame.K_RIGHT]:
        aimDir = 'right'
        if (rect_x + playerSpd < 416-rect_size and colision('x', 1, rect_x+rect_size, rect_y) == False):
            rect_x += playerSpd
    if keys[pygame.K_UP]:
        aimDir = 'up'
        if (rect_y - playerSpd > 0 and colision('y', -1, rect_x, rect_y) == False and colision('y', -1, rect_x, rect_y) == False):
            rect_y -= playerSpd
    if keys[pygame.K_DOWN]:
        aimDir = 'down'
        if (rect_y + playerSpd < 416-rect_size and colision('y', 1, rect_x, rect_y+rect_size) == False and colision('y', 1, rect_x+rect_size, rect_y+rect_size) == False):
            rect_y += playerSpd

        if colision('y', 1, rect_x, rect_y+rect_size) == False:
            newCollision(rect_x, rect_y, rect_x+rect_size, rect_y+rect_size)

    if keys[pygame.K_z] and delay > 25:
        if aimDir == 'left' or aimDir == 'right':
            sC = 'x'
        else:
            sC = 'y'
        shooting(rect_x, rect_y, aimDir, shoots, 'player', sC)
        delay = 0
    if keys[pygame.K_r]:
        print('test')

    # Draw the game

    screen.fill(black)

    for y in range(len(map_layout)):
        for x in range(len(map_layout[y])):
            if map_layout[y][x] == 1:
                pygame.draw.rect(screen, red, (
                    x*8, y*8, 8, 8))

    for shoot in shoots:
        pygame.draw.rect(screen, white, (
            shoot['x'], shoot['y'], 8, 8))
        if shoot['direction'] == 'left' or shoot['direction'] == 'right':
            shoot['x'] += shootSpd*shoot['axis']
        else:
            shoot['y'] += shootSpd*shoot['axis']

        destroyBrick(shoot['colision'], shoot['axis'],
                     shoot['x'], shoot['y'], shoot)

        if shoot['x'] < -8 or shoot['x'] > 424:
            shoots.remove(shoot)
        if shoot['y'] < -8 or shoot['y'] > 424:
            shoots.remove(shoot)

    pygame.draw.rect(screen, white, (rect_x, rect_y, rect_size, rect_size))
    # Update the window
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
