# Environment.py for PacMan
from random import choice
from agent2 import a_star_search

class PacmanEnv:
    def __init__(self, rows=5, cols=5):
        self.rows = rows
        self.cols = cols
        self.actions = [0, 1, 2, 3]  # 0 = up, 1 = left, 2 = down, 3 = right
        self.reset()

    def reset(self):
        # Initialize grid: 1 = pellet, 2 = wall, 0 = empty
        self.grid = [[1 for _ in range(self.cols)] for _ in range(self.rows)]

        # Hardcoded walls to create a simple maze
        self.grid[1][2] = 2
        self.grid[3][2] = 2

        # Set initial Pac-Man and ghost positions
        self.pacman = (0, 0)
        self.ghosts = [(self.rows - 1, self.cols - 1)]

        # Pac-Man eats the starting pellet
        r, c = self.pacman
        self.grid[r][c] = 0

        # Count total pellets for win condition
        self.total_pellets = sum(cell == 1 for row in self.grid for cell in row)

        return self.state()

    def state(self):
        """
        Returns a tuple representing the full game state:
        - Flattened grid (0, 1, 2 values)
        - Pac-Man's index in the flattened grid
        - Tuple of ghost indices
        """
        flat_grid = tuple(cell for row in self.grid for cell in row)
        pac_index = self.pacman[0] * self.cols + self.pacman[1]
        ghost_indices = tuple(g[0] * self.cols + g[1] for g in self.ghosts)
        return (flat_grid, pac_index, ghost_indices)

    def step(self, action):
        """
        Executes one step of the game:
        - Moves Pac-Man
        - Collects pellets
        - Moves ghosts using A* search
        - Returns (reward, new_state, done)
        """
        r, c = self.pacman
        new_r, new_c = r, c

        # Compute next position based on action
        if action == 0 and r > 0: new_r -= 1      # up
        elif action == 1 and c > 0: new_c -= 1    # left
        elif action == 2 and r < self.rows - 1: new_r += 1  # down
        elif action == 3 and c < self.cols - 1: new_c += 1  # right

        # Only move if not a wall
        if self.grid[new_r][new_c] != 2:
            self.pacman = (new_r, new_c)

        reward = -0.1  # Small penalty per step to encourage shorter paths
        done = False

        # Pellet collection
        r, c = self.pacman
        if self.grid[r][c] == 1:
            reward += 2
            self.grid[r][c] = 0
            self.total_pellets -= 1

        # Move each ghost one step toward Pac-Man using A*
        new_ghosts = []
        for ghost_pos in self.ghosts:
            next_pos = a_star_search(ghost_pos, self.pacman, self)
            new_ghosts.append(next_pos)
        self.ghosts = new_ghosts

        # Check for collision with ghost
        if self.pacman in self.ghosts:
            reward -= 10
            done = True
        elif self.total_pellets == 0:
            reward += 10  # Win condition
            done = True

        return reward, self.state(), done