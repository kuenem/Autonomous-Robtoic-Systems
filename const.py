import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Dimensions of Board
WIDTH = HEIGHT = int(0.8 * screen_height)
# Extra Space for labels
EXTRA_SPACE = int(0.05 * WIDTH)
# Dimensions of Screen (includes space for extra UI elements)
SCREEN_WIDTH = int(WIDTH + (2/7) * WIDTH + 2 * EXTRA_SPACE)
SCREEN_HEIGHT = int(HEIGHT + 2 * EXTRA_SPACE)

EXTRA_WIDTH = (2/7) * WIDTH

# Field dimensions
ROWS = 9
COLS = 9
SQSIZE = WIDTH // COLS

PIECE_VALUE = 1
SCALING = 10

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WOOD = (161, 102, 47)
TIMBER = (96, 80, 71)
OAK = (216, 181, 137)
GREY = (50, 50, 50)
LIGHT_GREY = (180, 180, 180)
LIGHT_GREEN = (234, 235, 200)
DARK_GREEN = (119, 154, 88)
YELLOWISCH = (244, 247, 116)
YELLOVISCH = (172, 195, 51)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)