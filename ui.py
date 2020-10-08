from pygame.locals import *
import pygame
import time


from astar import read_maze, get_path_astart
from config import CONFIG

WINDOWS_WIDTH = CONFIG["UI"]["WINDOWS_WIDTH"]
WINDOWS_HEIGHT = CONFIG["UI"]["WINDOWS_HEIGHT"]


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_to(self, maze_coordonates, maze_size):
        """
        moves the player from the 1 unit grid to the pixel Ui grid
        """
        x_unit_size = WINDOWS_WIDTH // maze_size[0]
        y_unit_size = WINDOWS_HEIGHT // maze_size[1]

        self.x = maze_coordonates[0] * x_unit_size
        self.y = maze_coordonates[1] * y_unit_size

    def display(self, display_surf, maze_size):
        """
        displayes the player on the curent possition
        """
        x_unit_size = WINDOWS_WIDTH // maze_size[0]
        y_unit_size = WINDOWS_HEIGHT // maze_size[1]

        player_surf = pygame.image.load("player.png").convert()
        player_surf = pygame.transform.scale(player_surf, (x_unit_size, y_unit_size))
        display_surf.blit(player_surf, (self.x, self.y))


class Maze:
    def __init__(self):
        self.maze = read_maze()
        self.size = (len(self.maze[0]), len(self.maze))
        self.solution = get_path_astart(
            self.maze, CONFIG["MAZE"]["START"], CONFIG["MAZE"]["END"]
        )

    def draw(self, display_surf):
        """
        draw the 1 grid maze in relations woth window boundaries
        """
        x_unit_size = WINDOWS_WIDTH // self.size[0]
        y_unit_size = WINDOWS_HEIGHT // self.size[1]

        block_surf = pygame.image.load("block.jpg").convert()
        block_surf = pygame.transform.scale(block_surf, (x_unit_size, y_unit_size))

        for x in range(self.size[0]):
            for y in range(self.size[1]):

                if self.maze[y][x] == 1:
                    display_surf.blit(block_surf, (x * x_unit_size, y * y_unit_size))

    def get_size(self):
        return self.size


class App:
    player = 0

    def __init__(self):
        self.player = Player()
        self.maze = Maze()
        self.maze_size = self.maze.get_size()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            (WINDOWS_WIDTH, WINDOWS_HEIGHT), pygame.HWSURFACE
        )
        pygame.display.set_caption("Pygame maze with A*!")

    def on_render(self, poz):
        time.sleep(CONFIG["UI"]["SLEEP"])

        self._display_surf.fill((0, 0, 0))

        self.player.move_to(poz, self.maze_size)
        self.player.display(self._display_surf, self.maze_size)

        self.maze.draw(self._display_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.maze.solution is None:
            exit()

        self.on_init()
        print(self.maze.solution)

        while 1:
            for poz in self.maze.solution:
                pygame.event.pump()
                keys = pygame.key.get_pressed()
                if keys[K_ESCAPE]:
                    pygame.quit()

                self.on_render(poz)

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
