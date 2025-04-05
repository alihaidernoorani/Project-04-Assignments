import pygame
import time

# Initialize pygame
pygame.init()

# Set up the canvas size and cell properties
CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 40  # Each grid cell will be 40x40 pixels
ERASER_SIZE = 20  # The eraser will be 20x20 pixels

# Define some colors
BLUE = (0, 0, 225)  # Blue color for the cells
WHITE = (255, 255, 255)  # White color (used for erasing)
PINK = (255, 182, 193)  # PINK color for the eraser

# Set up the screen
screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))
pygame.display.set_caption("Eraser effect in pygame")

# Create a list to store the grid of cells
grid = []

# Populate the grid with rectangles (representing each cell)
for row in range(0, CANVA_HEIGHT, CELL_SIZE):
    for col in range(0, CANVA_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)  # Create a rectangle for each cell
        grid.append((rect, False))  # Store the rectangle and a flag (False = not erased)

# Set up the eraser as a rectangle
eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)  # Initially position the eraser at (200, 200)

# Main game loop
running = True
while running:
    screen.fill(WHITE)  # Fill the screen with white (background color)

    # Get the current position of the mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y)  # Move the eraser to the mouse position

    # Draw the grid of cells
    new_grid = []  # We will store the updated grid here
    for rect, erased in grid:
        # Check if the eraser is colliding with this cell
        if eraser.colliderect(rect):
            erased = True  # Mark this cell as erased (it should be white)

        # Draw the cell (white if erased, blue if not)
        color = WHITE if erased else BLUE
        pygame.draw.rect(screen, color, rect)

        # Add the updated cell (with its erased status) to the new grid
        new_grid.append((rect, erased))

    # Update the grid to reflect the new erased status
    grid = new_grid

    # Draw the eraser on the screen (in pink)
    pygame.draw.rect(screen, PINK, eraser)

    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the loop if the window is closed

    # Update the display and pause briefly to control the frame rate
    pygame.display.flip()
    time.sleep(0.05)

# Quit pygame when the loop ends
pygame.quit()
