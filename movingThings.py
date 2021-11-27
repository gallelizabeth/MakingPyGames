import pygame

SIZE = WIDTH, HEIGHT = 800, 600
RADIUS = 20
BLACK = 0, 0, 0
BLUE = 0, 0, 255

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Графический редактор v0.0.0.1')
    screen = pygame.display.set_mode(SIZE)

    running = True
    screen.fill(BLACK)
    while running:  # основной игровой цикл
        for event in pygame.event.get():
            # обработка всех событий
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, BLUE, event.pos, RADIUS)
        # изменения, не зависящие от событий - действий пользователя или таймера
        pygame.display.flip()

    pygame.quit()