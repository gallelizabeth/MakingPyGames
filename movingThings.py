import pygame

SIZE = WIDTH, HEIGHT = 800, 600
RADIUS = 20

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
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, 'red', (x_pos, HEIGHT // 2), RADIUS)
        x_pos += 1
        pygame.display.flip()

    pygame.quit()
