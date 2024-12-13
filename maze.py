"""
[Author]: Rajamanickam S
[Date]: 2024-Dec-13
[Description]: This module contains the main logic for loading a maze from a file.
It reads the maze data from a text file, parses it, and returns the maze, start position, and goal position.
"""
import numpy as np

def load_maze(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    maze = []
    start = goal = None
    for i, line in enumerate(lines):
        row = []
        for j, char in enumerate(line.strip()):
            if char == "S":
                start = (i, j)
                row.append(0)
            elif char == "G":
                goal = (i, j)
                row.append(0)
            elif char == "1":
                row.append(1)
            else:
                row.append(0)
        maze.append(row)
    if not start or not goal:
        raise ValueError("Maze must have a start (S) and goal (G) position.")
    return np.array(maze), start, goal