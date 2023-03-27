import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# Define the class for the fruit
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -25)
        self.speed = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -25)
            self.speed = random.randrange(1, 5)

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the caption of the window
pygame.display.set_caption('Catch the Fruit')

# Create a sprite group for the fruit
fruit_group = pygame.sprite.Group()

# Create some fruit and add them to the group
for i in range(10):
    fruit = Fruit()
    fruit_group.add(fruit)

# Set the font and size for the score display
font = pygame.font.Font(None, 36)

# Initialize the score
score = 0

# Set the clock
clock = pygame.time.Clock()

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on a fruit
            pos = pygame.mouse.get_pos()
            fruit_list = pygame.sprite.spritecollide(
                None, fruit_group, False, pygame.sprite.collide_rect)
            if fruit_list:
                score += 1
                fruit_list[0].rect.x = random.randrange(
                    SCREEN_WIDTH - fruit_list[0].rect.width)
                fruit_list[0].rect.y = random.randrange(-100, -25)
                fruit_list[0].speed = random.randrange(1, 5)

    # Update the sprites
    fruit_group.update()

    # Fill the background
    screen.fill(BLACK)

    # Draw the sprites
    fruit_group.draw(screen)

    # Draw the score
    score_text = font.render('Score: {}'.format(score), True, WHITE)
    screen.blit(score_text, [10, 10])

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
