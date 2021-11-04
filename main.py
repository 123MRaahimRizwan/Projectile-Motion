"""
Project : Projectile Motion Physics Simulator
@author : M.Raahim Rizwan
Credit : https://www.youtube.com/watch?v=_gDOz7E6HVM
"""

# Importing the libraries
import pygame
import math

# Initializing pygame
pygame.init()

# Game constants
WIDTH = 1200
HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (37, 6, 117)

# Pygame window setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Motion")

# Creating ball class


class Ball:
    def __init__(self, x, y, radius, color):
        """
        Initializing ball class with some attributes.
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        """
        Drawing the ball on the screen.
        """
        pygame.draw.circle(win, BLACK, (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x, self.y),
                           self.radius - 1)  # for outline

    @staticmethod
    def ballPath(startx, starty, power, angle, time):
        """
        Finding the ball path according to projectile motion.
        """
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distance_X = velx * time
        distance_Y = (vely * time) + ((-4.9 * (time) ** 2) / 2)

        new_X = round(distance_X + startx)
        new_Y = round(starty - distance_Y)

        return (new_X, new_Y)


def redrawWindow():
    """
    Drawing all the stuff on the screen and updating it.
    """
    WIN.fill((95, 146, 227))
    ball.draw(WIN)
    pygame.draw.line(WIN, DARK_BLUE, line[0], line[1])

    pygame.display.update()


def findAngle(pos):
    """
    Finds the angle.
    """
    X = ball.x
    Y = ball.y
    # Horrible math part starts here
    try:
        angle = math.atan((Y - pos[1]) / (X - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < Y and pos[0] > X:
        angle = abs(angle)

    elif pos[1] < Y and pos[0] < X:
        angle = math.pi - angle

    elif pos[1] > Y and pos[0] < X:
        angle = math.pi + abs(angle)

    elif pos[1] > Y and pos[0] > X:
        angle = (math.pi * 2) - angle

    return angle


# Object
ball = Ball(300, 494, 5, WHITE)

x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False

# Main game loop
run = True
while run:
    if shoot:
        if ball.y < 500 - ball.radius:
            time += 0.05
            position = ball.ballPath(x, y, power, angle, time)
            ball.x = position[0]
            ball.y = position[1]
        else:
            shoot = False
            ball.y = 494

    pos = pygame.mouse.get_pos()
    line = [(ball.x, ball.y), pos]
    redrawWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shoot == False:
                shoot = True
                x = ball.x
                y = ball.y
                time = 0
                power = math.sqrt(
                    (line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2)/8
                angle = findAngle(pos)

pygame.quit()
