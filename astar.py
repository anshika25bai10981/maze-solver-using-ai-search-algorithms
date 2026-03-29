import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, end):
    pq = [(0, 0, start, [start])]  # (f, g, node, path)
    visited = set()

    while pq:
        f, g, (x, y), path = heapq.heappop(pq)

        if (x, y) == end:
            return path

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] != '#':
                    g_new = g + 1
                    h = heuristic((nx, ny), end)
                    f_new = g_new + h
                    heapq.heappush(pq, (f_new, g_new, (nx, ny), path + [(nx, ny)]))
    return None