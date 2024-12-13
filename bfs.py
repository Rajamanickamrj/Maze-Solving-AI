"""
[Author]: Rajamanickam S
[Date]: 2024-Dec-13
[Description]: This module contains the implementation of the Breadth-First Search (BFS) algorithm for solving a maze.
The bfs function takes a maze, start position, and goal position as input and returns the path from the start to the goal along with the total cost of the path.
"""
from collections import deque

def bfs(maze, start, goal):
    rows, cols = maze.shape
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    queue = deque([(start, 0)])  # (current_position, cost)
    visited = set()
    parents = {}

    while queue:
        current, cost = queue.popleft()

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents.get(current)
            return path[::-1], cost

        x, y = current
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] == 0:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    queue.append((neighbor, cost + 1))
                    parents[neighbor] = current

    return None, float('inf')  # No path found