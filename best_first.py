import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def best_first(maze, start, end):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        _, (x, y), path = heapq.heappop(pq)

        if (x, y) == end:
            return path

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] != '#':
                    h = heuristic((nx, ny), end)
                    heapq.heappush(pq, (h, (nx, ny), path + [(nx, ny)]))
    return None