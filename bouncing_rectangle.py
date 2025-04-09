class BouncingRectangle:
    def __init__(self, x, y, width, height, speed_x, speed_y, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color

    def update(self, screen_width, screen_height):
        # Update position
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x <= 0 or self.x + self.width >= screen_width:
            self.speed_x *= -1
        if self.y <= 0 or self.y + self.height >= screen_height:
            self.speed_y *= -1

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))