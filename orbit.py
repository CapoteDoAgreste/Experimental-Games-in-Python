import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Top-Down Car Control")

# Define colors
black = (0, 0, 0)
red = (255, 0, 0)
color = (255, 255, 255)

# Define a rectangle
# Example rectangle position and size


# Define the car class


class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.car_image = pygame.Surface((20, 40), pygame.SRCALPHA)
        pygame.draw.rect(self.car_image, red, (0, 0, 20, 40))

    def update(self):
        # moving the car using curvature calc
        self.x += self.speed * math.sin(math.radians(self.angle))
        self.y -= self.speed * math.cos(math.radians(self.angle))

        # print(car.speed)

    def draw(self):
        rotated_car = pygame.transform.rotate(self.car_image, self.angle * -1)
        new_rect = rotated_car.get_rect(
            center=self.car_image.get_rect(topleft=(self.x, self.y)).center)
        window.blit(rotated_car, new_rect.topleft)
        return new_rect

    # stearing wheel simulation
    def steering(self, modifier):
        if (abs(modifier) >= 0.2):
            car.angle += modifier
            steering_angle
        # print(modifier)

    def accelerate(self, direction, car_gear):
        match(car_gear):
            case 1:
                if (abs(car.speed) <= 1.5):
                    car.speed += 0.2*direction
            case 2:
                if (abs(car.speed) <= 3):
                    car.speed += 0.2*direction
            case 3:
                if (abs(car.speed) <= 4.5):
                    car.speed += 0.2*direction
            case 4:
                if (abs(car.speed) <= 6):
                    car.speed += 0.2*direction
            case 5:
                if (abs(car.speed) <= 7.5):
                    car.speed += 0.2*direction


# Create a car object
car = Car(width // 2, height // 2)
steering_angle = 0
steering_speed = 0.1
gear = 1

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)  # Limit the frame rate to 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        car.accelerate(1, gear)
    if keys[pygame.K_DOWN]:
        car.accelerate(-1, gear)
    if keys[pygame.K_LEFT]:
        if (steering_angle-1 >= -2 and car.speed != 0):
            steering_angle -= (steering_speed*car.speed)/7.5
    if keys[pygame.K_RIGHT]:
        if (steering_angle-1 <= 2 and car.speed != 0):
            steering_angle += (steering_speed*car.speed)/7.5

    if keys[pygame.K_1]:
        gear = 1
    if keys[pygame.K_2]:
        gear = 2
    if keys[pygame.K_3]:
        gear = 3
    if keys[pygame.K_4]:
        gear = 4
    if keys[pygame.K_5]:
        gear = 5
    if keys[pygame.K_6]:
        gear = 6

    # creating acc
    if (car.speed > 0):
        car.speed -= 0.1
        if (car.speed < 0):
            car.speed = 0
    else:
        car.speed += 0.1
        if (car.speed > 0):
            car.speed = 0

    if (car.speed == 0):
        steering_angle = 0

    car.steering(steering_angle)

    # Update the car's position and speed
    car.update()

    # Clear the window
    window.fill(black)

    car_rect = car.draw()  # Get the car's bounding rectangle

    # Check for collision between car and rectangle
    rectangle = pygame.Rect(40, 40, 100, 100)

    pygame.draw.rect(window, red, (40, 40, 100, 100))
    if car_rect.colliderect(rectangle):
        print("Car collided with rectangle!")
    else:
        print("not coliding")

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
