import random

def generate_maze(size, obstacle_prob):
    maze = []

    for i in range(size):
        row = []
        for j in range(size):
            if random.random() < obstacle_prob:
                row.append('#')
            else:
                row.append(' ')
        maze.append(row)

    maze[0][0] = 'S'
    maze[size-1][size-1] = 'E'

    return maze

def get_difficulty():
    print("1. Easy (5x5)")
    print("2. Medium (8x8)")
    print("3. Hard (12x12)")

    choice = input("Choose: ")

    if choice == '1':
        return 5, 0.2
    elif choice == '2':
        return 8, 0.3
    else:
        return 12, 0.4

def find_points(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            if maze[i][j] == 'E':
                end = (i, j)
    return start, end