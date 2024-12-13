"""
[Author]: Rajamanickam S
[Date]: 2024-Dec-13
[Description]: This is the main entry point of the Maze Solver App.
It creates the main application window and sets up the Maze Solver App.
The app is then run in the main loop of the Tkinter event loop.
"""
from ui.ui import MazeSolverApp
import tkinter as tk

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()

    # Set up the Maze Solver App
    app = MazeSolverApp(root)

    # Run the Tkinter main loop
    root.mainloop()