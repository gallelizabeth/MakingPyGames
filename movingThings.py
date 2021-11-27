import pygame

SIZE = WIDTH, HEIGHT = 800, 600
RADIUS = 20
BLACK = 0, 0, 0
RED = 255, 0, 0
FPS = 60  # кадров в секунду

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    running = True
    x_pos = 0
    v = 100  # пикселей в секунду
    clock = pygame.time.Clock()
    while running:  # основной игровой цикл
        for event in pygame.event.get():
            # обработка всех событий
            if event.type == pygame.QUIT:
                running = False
        # изменения, не зависящие от событий - действий пользователя или таймера
        screen.fill(BLACK)
        pygame.draw.circle(screen, RED, (x_pos, HEIGHT // 2), RADIUS)
        x_pos += v * clock.tick(FPS) / 1000
        # clock.tick() - время от начала работы программы в миллисекундах
        # x = v * t (в секундах)
        if x_pos > WIDTH or x_pos < 0:
            v *= -1  # изменить направление
        pygame.display.flip()

    pygame.quit()