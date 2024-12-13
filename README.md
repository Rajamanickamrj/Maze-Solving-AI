# Maze-Solving-AI

## Overview
The Maze-Solving-AI project is designed to implement a computer algorithm capable of automatically solving mazes using well-known pathfinding techniques. The AI identifies the shortest path from a designated start point to an endpoint within a maze, considering constraints such as obstacles and dead ends.

## Features
- **Pathfinding Algorithms**: Implements algorithms such as:
  - A* (A-Star)
  - Dijkstra's Algorithm
  - Breadth-First Search (BFS)
- **Maze Representation**: Supports representation of mazes in grid form.
- **Optimal Pathfinding**: Ensures the AI navigates through the maze efficiently, finding the shortest path.
- **Visualization**: Offers visualization of the maze-solving process 

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Rajamanickamrj/Maze-Solving-AI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Maze-Solving-AI
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Prepare a maze as an input file (e.g., `.txt`) or dynamically generate one within the project.
2. Specify the desired pathfinding algorithm.
3. Run the program:
   ```bash
   python main.py
   ```
4. The output will display the shortest path (graphical representation).

## Technologies Used
- **Python 3.12.6**: Core programming language used for implementation.
- **Libraries**:
  - `tkinter`: UI framework 
  - `NumPy`: For efficient computations.
  - `Matplotlib`: For visualizations (if integrated).
  -  All are mentioned on `requirements.txt`.

## Algorithms Overview
1. **A* (A-Star)**:
   - Combines heuristics and cost functions to find the shortest path efficiently.
2. **Dijkstra’s Algorithm**:
   - Guarantees the shortest path by exploring all nodes systematically.
3. **Breadth-First Search (BFS)**:
   - Explores all possible paths in a breadth-first manner. Guarantees shortest path in unweighted graphs.

## Example Input/Output
### Input
A simple maze can be structured as a grid where:
- `0` represents a free space.
- `1` represents an obstacle.
- `S` represents the start point.
- `G` represents the endpoint.

Example:
```plaintext
S 0 1 0 0
0 1 0 1 0
0 0 0 1 G
0 1 0 0 0
```

### Output
Visualization of the shortest path:
```plaintext
Path: [(0,0), (1,0), (2,0), (2,1), (2,4)]
```

## Future Enhancements
- Adding support for 3D mazes.

## Contributing
Contributions to improve the project are always welcome. To get started:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add descriptive message"
   ```
4. Push the branch and create a Pull Request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Credits
- Algorithms and concepts inspired by standard pathfinding techniques.
- Python third-party libraries for added functionality, as listed in the requirements file.

## Contact
For questions or collaborations, feel free to reach out at [rjnick@yahoo.com].