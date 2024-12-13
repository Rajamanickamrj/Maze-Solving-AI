"""
[Author]: Rajamanickam S
[Date]: 2024-Dec-13
[Description]: This module contains the main logic for loading a maze from a file.
It reads the maze data from a text file, parses it, and returns the maze, start position, and goal position.
"""
import matplotlib.pyplot as plt
import numpy as np

def visualize_path(maze, path):
    maze_copy = np.copy(maze)
    for x, y in path:
        maze_copy[x, y] = 0.5  # Mark path in the maze

    plt.imshow(maze_copy, cmap="gray")
    plt.title("Maze with Shortest Path")
    plt.show()