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


def input_screen():

    name = ""
    input_active = True

    while input_active:

        screen.fill((0, 0, 0))

        title = font.render(
            "Введите имя и нажмите Enter",
            True,
            (255, 255, 255)
        )

        screen.blit(title, (200, 200))

        name_text = font.render(
            name,
            True,
            (255, 255, 0)
        )

        screen.blit(name_text, (300, 260))

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    input_active = False

                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]

                else:
                    if len(name) < 12:
                        name += event.unicode

    return name


def show_results(top_players, message):

    show = True

    while show:

        screen.fill((0, 0, 0))

        title = font.render(
            message,
            True,
            (255, 255, 255)
        )

        screen.blit(title, (300, 50))

        subtitle = font.render(
            "ТОП ИГРОКОВ",
            True,
            (255, 255, 0)
        )

        screen.blit(subtitle, (300, 120))

        y = 180

        for p in top_players:

            text = font.render(
                f"{p[0]} - {p[1]}",
                True,
                (255, 255, 255)
            )

            screen.blit(text, (300, y))

            y += 40

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                show = False



player_name = input_screen()

player = Player(400, 300)

points = []


def spawn_points(count=5):

    for i in range(count):

        x = random.randint(20, WIDTH - 20)
        y = random.randint(20, HEIGHT - 20)

        points.append(pygame.Rect(x, y, 20, 20))


spawn_points()


game_time = 30
start_ticks = pygame.time.get_ticks()

running = True

while running:

    seconds = (
        pygame.time.get_ticks() - start_ticks
    ) // 1000

    time_left = game_time - seconds

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

        top = db.get_top_players()

        show_results(top, "ПОБЕДА!")

        running = False


    if time_left <= 0:

        db.add_score(player_name, player.score)

        top = db.get_top_players()

        show_results(top, "ПРОИГРЫШ!")

        running = False

    screen.fill((0, 0, 0))

    player.draw(screen)

    for point in points:
        pygame.draw.rect(screen, (255, 0, 0), point)

    score_text = font.render(
        f"Score: {player.score}",
        True,
        (255, 255, 255)
    )

    screen.blit(score_text, (10, 10))

    timer_text = font.render(
        f"Time: {time_left}",
        True,
        (255, 255, 255)
    )

    screen.blit(timer_text, (650, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

db.close()

sys.exit()
