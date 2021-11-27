import pygame

SIZE = WIDTH, HEIGHT = 800, 600
BLACK = 0, 0, 0
BLUE = 0, 0, 255

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Графический редактор v0.0.0.2')
    screen = pygame.display.set_mode(SIZE)

    # Создадим второй холст (сохранённые прямоугольники) и будем:
    surface_2 = pygame.Surface(screen.get_size())
    x, y, w, h = 0, 0, 0, 0
    drawing = False  # режим рисования
    # - Копировать второй холст на основной (на экран).
    # Если мы в режиме рисования, то рисовать на экране текущий прямоугольник
    # - При отпускании мыши копировать основной холст(экран) на второй холст:
    # фиксировать изменения. И выключать режим «рисование»
    running = True
    screen.fill(BLACK)
    while running:  # основной игровой цикл
        for event in pygame.event.get():
            # обработка всех событий
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # При нажатии на кнопку мыши — запоминать начальную вершину
                # и включать режим «рисование»
                x, y = event.pos
                drawing = True
            if event.type == pygame.MOUSEMOTION:
                # При движении мыши запоминать ширину и высоту
                if drawing:
                    w = event.pos[0] - x
                    h = event.pos[1] - y
            if event.type == pygame.MOUSEBUTTONUP:
                surface_2.blit(screen, (0, 0))
                # сохранённые = сохранённые + временный
                drawing = False
                x, y, w, h = 0, 0, 0, 0
        # изменения, не зависящие от событий - действий пользователя или таймера
        screen.fill(BLACK)
        # заливка экрана чёрным
        screen.blit(surface_2, (0, 0))
        # рисование всех сохранённых прямоугольников
        if drawing:
            if w != 0 or h != 0:
                pygame.draw.rect(screen, BLUE, (x, y, w, h), 1)
                # рисование временного прямоугольника
        pygame.display.flip()
    pygame.quit()
