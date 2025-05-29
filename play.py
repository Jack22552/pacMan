# GUI for simplified Pac-Man game
import pygame
from environment import PacmanEnv
from pickle import load

# Initialize environment and reset game
env = PacmanEnv()
state = env.reset()
intent = None

# Load trained agent from file
with open("trained_pacman_agent.pkl", "rb") as file:
    agent = load(file)

# Display settings
CELL_SIZE = 60
pygame.init()
display = pygame.display.set_mode([env.cols * CELL_SIZE, env.rows * CELL_SIZE])
font = pygame.font.SysFont("Segoe UI Symbol", 30)

# Main game loop
displaying = True
terminal = False
while displaying:
    action = -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            displaying = False
        elif event.type == pygame.KEYDOWN and not terminal:
            # Use trained agent to act
            if event.key == pygame.K_SPACE:
                action = agent.choose(state, env.actions)
            # Manual controls (optional for debugging)
            elif event.key == pygame.K_UP:
                action = 0
            elif event.key == pygame.K_LEFT:
                action = 1
            elif event.key == pygame.K_DOWN:
                action = 2
            elif event.key == pygame.K_RIGHT:
                action = 3

    if action in env.actions:
        intent = env.pacman, action
        reward, state, terminal = env.step(action)
        print(f"Action: {action}, Reward: {reward}, Terminal: {terminal}")

    # Draw background
    display.fill((0, 0, 0))

    # Draw grid
    for r in range(env.rows):
        for c in range(env.cols):
            x, y = c * CELL_SIZE, r * CELL_SIZE
            pygame.draw.rect(display, (40, 40, 40), pygame.Rect(x, y, CELL_SIZE, CELL_SIZE), width=1)

            # Walls (light blue)
            if env.grid[r][c] == 2:
                pygame.draw.rect(display, (0, 191, 255), pygame.Rect(x, y, CELL_SIZE, CELL_SIZE))

            # Pellets (white dots)
            if env.grid[r][c] == 1:
                pygame.draw.circle(display, (255, 255, 255), (x + CELL_SIZE // 2, y + CELL_SIZE // 2), 6)

    # Draw ghosts (red)
    for gr, gc in env.ghosts:
        gx, gy = gc * CELL_SIZE + CELL_SIZE // 4, gr * CELL_SIZE + CELL_SIZE // 4
        pygame.draw.circle(display, (255, 0, 0), (gx + 10, gy + 10), 15)

    # Draw Pac-Man (yellow)
    pr, pc = env.pacman
    px, py = pc * CELL_SIZE + CELL_SIZE // 2, pr * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(display, (255, 255, 0), (px, py), 20)

    pygame.display.flip()

pygame.quit()