import pygame


class Player:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 40, 40)

        self.color = (0, 255, 0)

        self.speed = 5

        self.score = 0

    def move(self, keys):

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Ограничение по экрану
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > 800:
            self.rect.right = 800

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > 600:
            self.rect.bottom = 600

    def collect_point(self):

        self.score += 10

    def draw(self, screen):

        pygame.draw.rect(screen, self.color, self.rect)
