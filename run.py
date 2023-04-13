from random import randint

# GRID_SIZE = 10
NUM_SHIPS = 5
SHIP_SYMBOL = "S"
HIT_SYMBOL = "X"
MISS_SYMBOL = "O"

while True:
    try:
        GRID_SIZE = int(input("Enter the grid size (between 5 and 20): "))
        if GRID_SIZE < 5 or GRID_SIZE > 20:
            raise ValueError()
        break
    except ValueError():
        print("Invalid input. Please enter an integer between 5 and 20.")

grid = []
for i in range(GRID_SIZE):
    row = []
    for j in range(GRID_SIZE):
        row.append(" ")
    grid.append(row)

for i in range(NUM_SHIPS):
    ship_placed = False
    while not ship_placed:
        x = randint(0, GRID_SIZE - 1)
        y = randint(0, GRID_SIZE - 1)
        if grid[x][y] != SHIP_SYMBOL:
            grid[x][y] = SHIP_SYMBOL
            ship_placed = True

print(
    """
    ********************************
    Welcome to the Battleships Game
    Number of ships: 5
    Number of shots: 10
    O - Missed shot
    X - Hit
    Enter your shots below the table
    ********************************
    """)


def display_grid():
    """
    display function to print the grid
    """
    print("   " + " ".join(str(i) for i in range(GRID_SIZE)))
    print(" + " + "-" * (GRID_SIZE * 2 - 1) + " + ")
    for index in range(GRID_SIZE):
        print("{:2d}|".format(index), end="")
        for jcol in range(GRID_SIZE):
            if grid[index][jcol] == SHIP_SYMBOL:
                print(" ", end="")
            else:
                print(grid[index][jcol], end="")
            print(" ", end="")
        print("|")
    print(" + " + "-" * (GRID_SIZE * 2 - 1) + " + ")


def is_valid_shot(xval, yval):
    """
    function to check if the shot is valid
    """
    return xval >= 0 and xval < GRID_SIZE and yval >= 0 and yval < GRID_SIZE


def count_hit_ships(board):
    """
    function to count the hit ships
    """
    count = 0
    for rowval in board:
        for column in rowval:
            if column == "X":
                count += 1
    return count


def final_result():
    """
    function to print the final grid with hits, miss and ships
    """
    print("  " + " ".join(str(i) for i in range(GRID_SIZE)))
    print(" + " + "-" * (GRID_SIZE * 2 - 1) + " + ")
    for index in range(GRID_SIZE):
        print("{:2d}|".format(index), end="")
        for jcol in range(GRID_SIZE):
            print(grid[index][jcol], end="")
            print(" ", end="")
        print("|")
    print(" + " + "-" * (GRID_SIZE * 2 - 1) + " + ")


num_turns = 0
win = False
while num_turns < 10:
    display_grid()
    print("Enter the x and y coordinates of your shot (separated by a space):")
    try:
        x, y = map(int, input().split())
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")
        continue
    if not is_valid_shot(x, y):
        print("Invalid shot. Please enter a shot within the grid.")
        continue
    if grid[x][y] == HIT_SYMBOL or grid[x][y] == MISS_SYMBOL:
        print("You have already fired at this position.")
        continue
    if grid[x][y] == SHIP_SYMBOL:
        print("Hit!")
        grid[x][y] = HIT_SYMBOL
    else:
        print("Miss!")
        grid[x][y] = MISS_SYMBOL
    num_turns += 1
    num_ships_remaining = sum(row.count(SHIP_SYMBOL) for row in grid)
    if num_ships_remaining == 0:
        print("Congratulations! You have sunk all the ships", num_turns,)
        win = True
        break
    else:
        print("You have " + str(10-num_turns) + " shoots left")

if (not win):
    print("FAILED! You could not sink all the ships in given shots. Try again")
    final_result()
    print("You sunk "+str(count_hit_ships(grid)) +
          " ship(s) out of " + str(NUM_SHIPS)+" ships"
          " 'S'=enemy ship(s)"
          " Click 'Run program' at the top left if you want to play again.")
