# agent2.py GHOST
from heapq import heappush, heappop

def a_star_search(start, goal, env):
    """
    Finds the next step from `start` to `goal` using A*.
    Returns the next position (row, col) toward the goal, or start if no path found.
    """
    rows, cols = env.rows, env.cols
    walls = set((r, c) for r in range(rows) for c in range(cols) if env.grid[r][c] == 2)

    # Heuristic: Manhattan distance
    def heuristic(pos):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    # Neighboring positions (up, down, left, right)
    def get_neighbors(pos):
        r, c = pos
        neighbors = []
        if r > 0 and (r - 1, c) not in walls: neighbors.append((r - 1, c))
        if r < rows - 1 and (r + 1, c) not in walls: neighbors.append((r + 1, c))
        if c > 0 and (r, c - 1) not in walls: neighbors.append((r, c - 1))
        if c < cols - 1 and (r, c + 1) not in walls: neighbors.append((r, c + 1))
        return neighbors

    # Priority queue for frontier: (estimated total cost, cost so far, position, path)
    open_set = []
    heappush(open_set, (heuristic(start), 0, start, [start]))
    visited = set()

    while open_set:
        est_total, cost, current, path = heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path[1] if len(path) > 1 else start  # Return next step

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_cost = cost + 1
                heappush(open_set, (new_cost + heuristic(neighbor), new_cost, neighbor, path + [neighbor]))

    return start  # No path found