import pygame

WINDOW_SIZES = {
    "small": (1080, 720),
    "medium": (1200, 800),
    "large": (1440, 960),
}

ASPECT_RATIO = WINDOW_SIZES["medium"]
WINDOW_WIDTH = ASPECT_RATIO[0]
WINDOW_HEIGHT = ASPECT_RATIO[1]
PADDING_SIZE = 0.05
EDGE_PADDINGS = WINDOW_HEIGHT * PADDING_SIZE
GAME_SQUARE_SIZE = WINDOW_HEIGHT - 2 * EDGE_PADDINGS


class UI:
    def __init__(self, gameWorld):
        self.gameWorld = gameWorld
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.blockSize = GAME_SQUARE_SIZE // self.gameWorld.size

    def draw_ui(self):
        self.screen.fill("black")
        self.draw_blocks()

    def draw_hud(self):
        self.screen.fill("black")
        self.display_score()

        pygame.draw.line(
            self.screen,
            "white",
            (EDGE_PADDINGS, EDGE_PADDINGS),
            (EDGE_PADDINGS + GAME_SQUARE_SIZE, EDGE_PADDINGS),
        )
        pygame.draw.line(
            self.screen,
            "white",
            (EDGE_PADDINGS, EDGE_PADDINGS),
            (EDGE_PADDINGS, EDGE_PADDINGS + GAME_SQUARE_SIZE),
        )
        pygame.draw.line(
            self.screen,
            "white",
            (EDGE_PADDINGS + GAME_SQUARE_SIZE, EDGE_PADDINGS + GAME_SQUARE_SIZE),
            (EDGE_PADDINGS + GAME_SQUARE_SIZE, EDGE_PADDINGS),
        )
        pygame.draw.line(
            self.screen,
            "white",
            (EDGE_PADDINGS + GAME_SQUARE_SIZE, EDGE_PADDINGS + GAME_SQUARE_SIZE),
            (EDGE_PADDINGS, EDGE_PADDINGS + GAME_SQUARE_SIZE),
        )
        pygame.draw.line(
            self.screen,
            "white",
            (2 * EDGE_PADDINGS + GAME_SQUARE_SIZE, EDGE_PADDINGS),
            (WINDOW_WIDTH - EDGE_PADDINGS, EDGE_PADDINGS),
        )
        pygame.draw.line(
            self.screen,
            "white",
            (2 * EDGE_PADDINGS + GAME_SQUARE_SIZE, EDGE_PADDINGS),
            (2 * EDGE_PADDINGS + GAME_SQUARE_SIZE, EDGE_PADDINGS + GAME_SQUARE_SIZE),
        )
        pygame.draw.line(
            self.screen,
            "white",
            (WINDOW_WIDTH - EDGE_PADDINGS, EDGE_PADDINGS + GAME_SQUARE_SIZE),
            (WINDOW_WIDTH - EDGE_PADDINGS, EDGE_PADDINGS),
        )
        pygame.draw.line(
            self.screen,
            "white",
            (WINDOW_WIDTH - EDGE_PADDINGS, EDGE_PADDINGS + GAME_SQUARE_SIZE),
            (2 * EDGE_PADDINGS + GAME_SQUARE_SIZE, EDGE_PADDINGS + GAME_SQUARE_SIZE),
        )

    def draw_blocks(self):
        for rowIndex, row in enumerate(self.gameWorld.gridWorld):
            for ColumnIndex, value in enumerate(row):
                if value == 1:
                    x, y = self.grid_to_pixel(rowIndex, ColumnIndex)
                    pygame.draw.rect(
                        self.screen,
                        "white",
                        pygame.Rect(x, y, self.blockSize, self.blockSize),
                    )
                elif value == 2:
                    x, y = self.grid_to_pixel(rowIndex, ColumnIndex)
                    pygame.draw.rect(
                        self.screen,
                        "red",
                        pygame.Rect(x, y, self.blockSize, self.blockSize),
                    )

    def draw_instructions(self):
        insntructionFont = pygame.font.SysFont("monospace", 30, italic=True)
        insntructionText = "Press Enter or Space to Start"
        insntructionTextSurface = insntructionFont.render(
            insntructionText, True, (255, 255, 255)
        )

        self.screen.blit(
            insntructionTextSurface,
            (
                EDGE_PADDINGS
                + GAME_SQUARE_SIZE // 2
                - insntructionTextSurface.get_width() // 2,
                EDGE_PADDINGS
                + GAME_SQUARE_SIZE // 2
                - insntructionTextSurface.get_height() // 2,
            ),
        )

    def grid_to_pixel(self, row, column):
        x = column * self.blockSize
        y = row * self.blockSize
        return (x + EDGE_PADDINGS, y + EDGE_PADDINGS)

    def display_score(self):
        titleFont = pygame.font.SysFont("arial", 45, italic=True)
        titleText = "Snake Game"
        titleTextSurface = titleFont.render(titleText, True, (255, 255, 255))

        scoreFont = pygame.font.SysFont("monospace", 35)
        scoreText = f"Score : {self.gameWorld.score}"
        scoreTextSurface = scoreFont.render(scoreText, True, (255, 255, 255))

        stepsTakenFont = pygame.font.SysFont("monospace", 25)
        stepsTakenText = f"Steps Taken : {self.gameWorld.stepsTaken}"
        stepsTakenTextSurface = stepsTakenFont.render(
            stepsTakenText, True, (255, 255, 255)
        )

        self.screen.blit(
            titleTextSurface, (3 * EDGE_PADDINGS + GAME_SQUARE_SIZE, 2 * EDGE_PADDINGS)
        )
        self.screen.blit(
            scoreTextSurface,
            (
                3 * EDGE_PADDINGS + GAME_SQUARE_SIZE,
                3 * EDGE_PADDINGS + titleTextSurface.get_height(),
            ),
        )
        self.screen.blit(
            stepsTakenTextSurface,
            (
                3 * EDGE_PADDINGS + GAME_SQUARE_SIZE,
                4 * EDGE_PADDINGS
                + titleTextSurface.get_height()
                + scoreTextSurface.get_height(),
            ),
        )


# (EDGE_PADDINGS, EDGE_PADDINGS)                  (EDGE_PADDINGS + GAME_SQUARE_SIZE, EDGE_PADDINGS)

# (EDGE_PADDINGS, EDGE_PADDINGS + GAME_SQUARE_SIZE)   (EDGE_PADDINGS + GAME_SQUARE_SIZE, EDGE_PADDINGS + GAME_SQUARE_SIZE)

# (2*EDGE_PADDINGS + GAME_SQUARE_SIZE, EDGE_PADDINGS)                   (WINDOW_WIDTH - EDGE_PADDINGS, EDGE_PADDINGS)

# (2*EDGE_PADDINGS + GAME_SQUARE_SIZE, EDGE_PADDINGS + GAME_SQUARE_SIZE)  (WINDOW_WIDTH - EDGE_PADDINGS, EDGE_PADDINGS + GAME_SQUARE_SIZE)
