import random

# Define the grid size
GRID_SIZE = 10

# Define the number of ships
NUM_SHIPS = 5

# Define the ship symbol
SHIP_SYMBOL = "S"

# Define the hit symbol
HIT_SYMBOL = "X"

# Define the miss symbol
MISS_SYMBOL = "O"

# Create the grid
grid = []
for i in range(GRID_SIZE):
    row = []
    for j in range(GRID_SIZE):
        row.append(" ")
    grid.append(row)

# Place the ships on the grid
for i in range(NUM_SHIPS):
    ship_placed = False
    while not ship_placed:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if grid[x][y] != SHIP_SYMBOL:
            grid[x][y] = SHIP_SYMBOL
            ship_placed = True

