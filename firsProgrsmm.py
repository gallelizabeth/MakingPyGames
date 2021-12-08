import pygame

WIDTH = 5
HEIGHT = 800, 600
BORDER = 10


def draw_square(screen):
    color = pygame.Color(50, 150, 50)
    pygame.draw.rect(screen, color,
                     (20, 20, 100, 100), 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3])
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)
    pygame.draw.rect(screen, (255, 225, 0), (10, 10, 100, 100), 0)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
        draw_square(screen)
    pygame.quit()

