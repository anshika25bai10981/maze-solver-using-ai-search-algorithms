import time

def print_maze(maze, path=None, color="\033[93m"):
    RESET = "\033[0m"

    for i in range(len(maze)):
        for j in range(len(maze[0])):

            if path and (i, j) in path:
                print(f"{color}*{RESET}", end=" ")

            elif maze[i][j] == 'S':
                print("\033[92mS\033[0m", end=" ")

            elif maze[i][j] == 'E':
                print("\033[91mE\033[0m", end=" ")

            elif maze[i][j] == '#':
                print("\033[90m#\033[0m", end=" ")

            else:
                print("\033[97m.\033[0m", end=" ")

        print()

def measure(func, maze, start, end):
    start_time = time.time()
    path = func(maze, start, end)
    end_time = time.time()
    return path, end_time - start_time