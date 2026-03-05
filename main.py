import pygame
import random
import sys

from player import Player
from database import DatabaseManager

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point Collector")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

db = DatabaseManager()

player = Player(400,300)

points = []

def spawn_points():

    for i in range(5):
        x = random.randint(20, WIDTH-20)
        y = random.randint(20, HEIGHT-20)

        points.append(pygame.Rect(x,y,20,20))


spawn_points()

player_name = input("Введите имя игрока: ")

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.move(keys)

    for point in points[:]:

        if player.rect.colliderect(point):

            points.remove(point)
            player.collect_point()

    if len(points) == 0:
        spawn_points()

    if player.score >= 100:

        db.add_score(player_name, player.score)

        print("ПОБЕДА!")

        top = db.get_top_players()

        print("\nТОП ИГРОКОВ")

        for p in top:
            print(p[0], p[1])

        running = False

    screen.fill((0,0,0))

    player.draw(screen)

    for point in points:
        pygame.draw.rect(screen, (255,0,0), point)

    score_text = font.render(f"Score: {player.score}", True, (255,255,255))
    screen.blit(score_text,(10,10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
