import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface: pygame.Surface):
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                cell = self.board[row][column]
                if cell == 0:
                    w = 1
                else:
                    w = 0
                pygame.draw.rect(
                    surface=surface,
                    color=(225, 225, 225),
                    rect=(
                        self.left + self.cell_size * column,
                        self.top + self.cell_size * row,
                        self.cell_size,
                        self.cell_size
                    ),
                    width=w
                )

    def get_cell(self, mouse_pos: tuple[int, int]) -> None:
        x, y = mouse_pos
        if x <= self.left:
            return None
        if y <= self.top:
            return None
        if x >= self.left + self.cell_size * self.width:
            return None
        if y >= self.top + self.cell_size * self.height:
            return None
        column = (x - self.left) // self.cell_size
        row = (x - self.top) // self.cell_size
        return row, column

    def on_click(self, cell_coords: tuple[int, int]):
        print(cell_coords)

    def get_click(self, mouse_pos):
        self.on_click(self.get_cell(mouse_pos))

