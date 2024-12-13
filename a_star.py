"""
[Author]: Rajamanickam S
[Date]: 2024-Dec-13
[Description]: A* algorithm implementation for solving the maze.
"""
import heapq

def a_star(maze, start, goal):
    rows, cols = maze.shape
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    def heuristic(x, y):
        return abs(x - goal[0]) + abs(y - goal[1])  # Manhattan distance

    pq = []
    heapq.heappush(pq, (0, 0, start, None))
    visited = set()
    parents = {}

    while pq:
        f_score, g_score, current, parent = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)
        parents[current] = parent

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1], g_score

        x, y = current
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] == 0:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    new_g_score = g_score + 1
                    heapq.heappush(pq, (new_g_score, new_g_score, neighbor, current))

    return None, float('inf')  # No path found