import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.speed = 5
        self.score = 0

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0,128,255), self.rect)

    def collect_point(self):
        self.score += 10

    def reset_score(self):
        self.score = 0
