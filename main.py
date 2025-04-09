import pygame
import math
import colorsys
import random
from bouncing_rectangle import BouncingRectangle

# ONE COMMENT

def create_fractal_music_pattern(width=1000, height=600):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Fractal Music Visualizer")
    clock = pygame.time.Clock()
    
    # Create particles and bouncing rectangle
    particles = [(random.randint(0, width), random.randint(0, height)) for _ in range(100)]
    rectangle = BouncingRectangle(
        x=width//2,
        y=height//2,
        width=50,
        height=30,
        speed_x=5,
        speed_y=4,
        color=(255, 0, 0)
    )
    angle = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))
        angle += 0.02
        
        # Update and draw rectangle
        rectangle.update(width, height)
        rectangle.draw(screen)
        
        for i, (x, y) in enumerate(particles):
            # ... existing code ...
            hue = (x + y + angle * 50) / 1000 % 1
            color = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1, 1))
            
            new_x = (x + math.sin(angle + i * 0.1) * 2) % width
            new_y = (y + math.cos(angle * 2 + i * 0.1) * 2) % height
            
            if i > 0:
                prev_x, prev_y = particles[i-1]
                pygame.draw.line(screen, color, (prev_x, prev_y), (new_x, new_y), 2)
            
            particles[i] = (new_x, new_y)
            pygame.draw.circle(screen, color, (int(new_x), int(new_y)), 3)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    create_fractal_music_pattern()