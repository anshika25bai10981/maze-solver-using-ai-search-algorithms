from maze import generate_maze, get_difficulty, find_points
from bfs import bfs
from dfs import dfs
from best_first import best_first
from astar import astar
from utils import print_maze, measure

# Difficulty
size, prob = get_difficulty()

# Ensure solvable maze
while True:
    maze = generate_maze(size, prob)
    start, end = find_points(maze)
    if bfs(maze, start, end):
        break

print("\nGenerated Maze:\n")
print_maze(maze)

print("\nChoose Algorithm(s):")
print("1. BFS")
print("2. DFS")
print("3. Best First Search")
print("4. A*")
print("5. All")

choices = input("Enter choice/choices (e.g., 1,2,3,4 or 5): ").split(',')

algo_map = {
    "1": ("BFS", bfs, "\033[93m"),
    "2": ("DFS", dfs, "\033[94m"),
    "3": ("BestFS", best_first, "\033[96m"),
    "4": ("A*", astar, "\033[95m")
}

selected_algos = []

if "5" in choices:
    selected_algos = list(algo_map.values())
else:
    for ch in choices:
        ch = ch.strip()
        if ch in algo_map:
            selected_algos.append(algo_map[ch])

if not selected_algos:
    print("No valid selection!")
    exit()

results = {}

# Run algorithms
for name, algo, color in selected_algos:
    path, t = measure(algo, maze, start, end)
    results[name] = (len(path) if path else 0, t)

    print(f"\n{name} Solution:")
    print_maze(maze, path, color)
    print(f"Steps: {len(path)} | Time: {t:.6f} sec")

print("\n=== Comparison Chart ===")
for algo in results:
    steps, t = results[algo]
    bar = "#" * steps
    print(f"{algo:8} | Steps: {steps:2} | Time: {t:.6f} | {bar}")


best_algo = min(results, key=lambda x: results[x][0])
fastest_algo = min(results, key=lambda x: results[x][1])

print(f"\n🏆 Shortest Path: {best_algo}")
print(f"⚡ Fastest: {fastest_algo}")