import pygame
import math


def lerp(a, b, t):
    return (1 - t) * a + t * b


def getAngle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    angle_radians = math.atan2(dy, dx)
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees


# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Square Orbit")

# Define colors
black = (0, 0, 0)
red = (255, 0, 0)
color = (255, 255, 255)

# Define a rectangle
# Example rectangle position and size


class playerCell:
    def __init__(self, x, y, sizeX, sizeY, color):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.color = color
        self.angle = 0
        self.image = pygame.Surface((20, 40), pygame.SRCALPHA)
        self.moving = False
        self.mass = 1
        self.spdY = 10
        pygame.draw.rect(self.image, color, (0, 0, self.sizeX, self.sizeY))

    def draw(self):
        rotated_cell = pygame.transform.rotate(self.image, self.angle * -1)
        new_rect = rotated_cell.get_rect(
            center=self.image.get_rect(topleft=(self.x, self.y)).center)
        window.blit(rotated_cell, new_rect.topleft)
        return new_rect

    def move(self):
        if self.moving:
            self.x += (10*self.mass) * math.sin(math.radians(getAngle(self.x,
                                                                      self.y, mouse_pos[0], mouse_pos[1])))
            self.y -= (self.spdY*self.mass) * math.cos(math.radians(getAngle(self.x,
                                                                             self.y, mouse_pos[0], mouse_pos[1])))

            if (self.y >= mouse_pos[1]):
                self.spdY -= 0.1
            else:
                self.spdY += 0.1

    def update(self):
        self.move()
        self.draw()


player = playerCell(width//2, height//2, 20, 20, red)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)  # Limit the frame rate to 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                player.moving = True
                print("Mouse position:", mouse_pos, player.moving)

    # Clear the window
    window.fill(black)
    player.update()

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
