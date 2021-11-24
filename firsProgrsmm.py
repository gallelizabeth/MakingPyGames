import pygame

SIZE = WIDTH, HEIGHT = 800, 600
BORDER = 10


def draw(screen: pygame.Surface):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello World", True, (255, 255, 100))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(
        surface=screen,
        color=(0, 255, 0),
        rect=(
            text_x - BORDER,
            text_y - BORDER,
            text.get_width() + BORDER * 2,
            text.get_height() + BORDER * 2
         ),
        width=1,
    )


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
        draw(screen)
        draw_square(screen)
    pygame.quit()

