"""
[Author]: Rajamanickam S
[Date]: 2024-Dec-13
[Description]: This module contains the MazeSolverApp class, which is the main application class for the Maze Solver App.
It handles the user interface, maze loading, and solving algorithms.
"""
import tkinter as tk
from tkinter import filedialog, messagebox

from a_star import a_star
from bfs import bfs
from maze import load_maze


class MazeSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver")
        self.maze = None
        self.start = None
        self.goal = None

        # UI Elements
        self.create_ui()

    def create_ui(self):
        # Frame for Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Buttons
        load_button = tk.Button(button_frame, text="Load Maze", command=self.load_maze)
        load_button.grid(row=0, column=0, padx=5)

        solve_a_star_button = tk.Button(button_frame, text="Solve with A*", command=self.solve_a_star)
        solve_a_star_button.grid(row=0, column=1, padx=5)

        solve_bfs_button = tk.Button(button_frame, text="Solve with BFS", command=self.solve_bfs)
        solve_bfs_button.grid(row=0, column=2, padx=5)

        quit_button = tk.Button(button_frame, text="Quit", command=self.root.quit)
        quit_button.grid(row=0, column=3, padx=5)

        # Canvas for Maze Display
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg="white")
        self.canvas.pack(pady=10)

    def load_maze(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                self.maze, self.start, self.goal = load_maze(file_path)
                self.draw_maze()
                messagebox.showinfo("Success", "Maze loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load maze: {e}")

    def draw_maze(self):
        if self.maze is None:
            return

        self.canvas.delete("all")
        rows, cols = self.maze.shape
        cell_width = self.canvas.winfo_width() / cols
        cell_height = self.canvas.winfo_height() / rows

        for i in range(rows):
            for j in range(cols):
                x1, y1 = j * cell_width, i * cell_height
                x2, y2 = x1 + cell_width, y1 + cell_height
                if self.maze[i, j] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                elif (i, j) == self.start:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                elif (i, j) == self.goal:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray")

    def solve_a_star(self):
        if self.maze is None or self.start is None or self.goal is None:
            messagebox.showerror("Error", "No maze loaded.")
            return

        path, cost = a_star(self.maze, self.start, self.goal)
        if path:
            messagebox.showinfo("Success", f"Path found with A*! Cost: {cost}")
            self.highlight_path(path)
        else:
            messagebox.showerror("Error", "No path found!")

    def solve_bfs(self):
        if self.maze is None or self.start is None or self.goal is None:
            messagebox.showerror("Error", "No maze loaded.")
            return

        path, cost = bfs(self.maze, self.start, self.goal)
        if path:
            messagebox.showinfo("Success", f"Path found with BFS! Cost: {cost}")
            self.highlight_path(path)
        else:
            messagebox.showerror("Error", "No path found!")

    def highlight_path(self, path):
        rows, cols = self.maze.shape
        cell_width = self.canvas.winfo_width() / cols
        cell_height = self.canvas.winfo_height() / rows

        for x, y in path:
            x1, y1 = y * cell_width, x * cell_height
            x2, y2 = x1 + cell_width, y1 + cell_height
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")