import sys
import pygame
import random
import json

with open('battle_city_map.json') as f:
    map_layout = json.load(f)


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


# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (150, 75, 0)

# Set the starting position of the rectangle
rect_x = 1
rect_y = 1
playerSpd = 1
direction = 'x'
walking = False
rect_size = 28
aimDir = 'left'
delay = 100

walls = []

shoots = [
]
shootSpd = 2


class Player():
    def __init__(self, x, y, spd, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.spd = spd
        self.color = color

    def draw(self):
        rect = pygame.draw.rect(
            screen, self.color, (self.x, self.y, self.size, self.size))
        return rect

    def move(self, direction, axis):
        isPossible = self.can_move(direction, self.spd, axis)
        if (isPossible == True):
            if (direction == 'x'):
                self.x += self.spd*axis
            else:
                self.y += self.spd*axis

    def can_move(self, direction, axis):
        if (direction == 'x'):
            playerCollision = pygame.Rect(
                self.x+self.spd*axis, self.y, self.size, self.size)
        else:
            playerCollision = pygame.Rect(
                self.x, self.y+self.spd*axis, self.size, self.size)

        for wall in walls:
            if (playerCollision.colliderect(wall)):
                return False
        return True


class Wall():
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((8, 8))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x * 8
        self.rect.y = y * 8


player = Player(0, 0, 32, playerSpd, white)

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
        player.move('x', -1)

    if keys[pygame.K_RIGHT]:
        aimDir = 'right'
        player.move('x', 1)

    if keys[pygame.K_UP]:
        aimDir = 'up'
        player.move('y', -1)

    if keys[pygame.K_DOWN]:
        aimDir = 'down'
        player.move('y', 1)

    if keys[pygame.K_z] and delay > 25:
        if aimDir == 'left' or aimDir == 'right':
            sC = 'x'
        else:
            sC = 'y'
        delay = 0
    if keys[pygame.K_r]:
        print('test')

    # Draw the game
    screen.fill(black)
    player_rect = player.draw()

    wall_surface = pygame.Surface(window_size)

    wall_group = pygame.sprite.Group()

    for y in range(len(map_layout)):
        for x in range(len(map_layout[y])):
            if map_layout[y][x] == 1:
                wall = Wall(x, y)
                wall_group.add(wall)
                walls.append(pygame.Rect(x*8, y*8, 8, 8))
    wall_group.update()
    wall_group.draw(screen)
    # Update the window
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
