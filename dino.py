import pygame
from random import randint

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_HEIGHT = SCREEN_HEIGHT - 70
FPS = 30

# Load and set the icon
icon = pygame.image.load('dino.png')
pygame.display.set_icon(icon)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Game")

# Clock
clock = pygame.time.Clock()

# Dinosaur class
class Dinosaur:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.color = BLACK
        self.rect = pygame.Rect(50, GROUND_HEIGHT - self.height, self.width, self.height)
        self.jump = False
        self.jump_speed = 20  
        self.gravity = 1.5  
        self.jump_velocity = 0

    def update(self):
        if self.jump:
            self.jump_velocity -= self.gravity
            self.rect.y -= self.jump_velocity
            if self.rect.y >= GROUND_HEIGHT - self.height:
                self.rect.y = GROUND_HEIGHT - self.height
                self.jump = False
                self.jump_velocity = 0
        else:
            if self.rect.y < GROUND_HEIGHT - self.height:
                self.rect.y += self.gravity

    def jump_action(self):
        if not self.jump:
            self.jump = True
            self.jump_velocity = self.jump_speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Obstacle class
class Obstacle:
    def __init__(self):
        self.width = 30
        self.height = 60
        self.color = BLACK
        self.rect = pygame.Rect(SCREEN_WIDTH, GROUND_HEIGHT - self.height, self.width, self.height)
        self.speed = 10

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < -self.width:
            self.rect.x = SCREEN_WIDTH + randint(0, 200)  # Randomize respawn position

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Ground class
class Ground:
    def __init__(self):
        self.color = BLACK
        self.rect = pygame.Rect(0, GROUND_HEIGHT, SCREEN_WIDTH, 70)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Main game loop
def main():
    running = True
    dino = Dinosaur()
    obstacles = [Obstacle()]
    ground = Ground()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump_action()

        screen.fill(WHITE)
        ground.draw(screen)

        dino.update()
        dino.draw(screen)

        for obstacle in obstacles:
            obstacle.update()
            obstacle.draw(screen)
            if dino.rect.colliderect(obstacle.rect):
                running = False

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
