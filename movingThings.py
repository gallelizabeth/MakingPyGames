from random import randint

import pygame

SIZE = WIDTH, HEIGHT = 800, 600
RADIUS = 20
BLACK = 0, 0, 0
WHITE = 255, 255, 255


def draw(surface: pygame.Surface):
    surface.fill(BLACK)
    for i in range(10_000):
        surface.fill(WHITE, (randint(0, WIDTH), randint(0, HEIGHT), 1, 1))


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    x_pos = 0

    running = True
    while running:  # основной игровой цикл
        for event in pygame.event.get():
            # обработка всех событий
            if event.type == pygame.QUIT:
                running = False
        # изменения, не зависящие от событий - действий пользователя или таймера
        draw(screen)
        pygame.display.flip()

    pygame.quit()