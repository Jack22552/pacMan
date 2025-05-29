# train2.py
from environment import PacmanEnv
from agent1 import QLearner
import matplotlib.pyplot as plt
from pickle import dump, load

# Initialize environment and agent
env = PacmanEnv()
agent = QLearner(alpha=0.1, gamma=0.99, epsilon=1.0, decay=0.995)

batches = 100  # Number of training batches
episodes_per_batch = 50  # Episodes per batch

scores = []  # Tracks score (total reward) per batch

# Run training batches
for batch in range(batches):
    total_score = 0

    for _ in range(episodes_per_batch):
        s = env.reset()  # Reset environment to initial state
        done = False
        episode_reward = 0

        while not done:
            a = agent.choose(s, env.actions)  # Select action from agent
            r, sp, done = env.step(a)  # Take a step in the environment
            agent.update(s, a, r, sp, env.actions, done)  # Update agent based on experience
            s = sp  # Update state
            episode_reward += r  # Accumulate reward for the episode

        total_score += episode_reward  # Accumulate total score for this batch

    avg_score = total_score / episodes_per_batch  # Calculate average score for this batch
    scores.append(avg_score)  # Store average score for later plotting

    # Print progress
    print(f"Batch {batch}: Avg Score = {avg_score:.2f}, Epsilon = {agent.epsilon:.3f}")

# Save the trained agent
with open("trained_pacman_agent.pkl", "wb") as f:
    dump(agent, f)

# Plot learning curve
plt.plot(scores)
plt.xlabel("Batch")
plt.ylabel("Average Score")
plt.title("Pac-Man Agent Learning Curve")
plt.show()

# Load the trained agent and test ghost behavior
with open("trained_pacman_agent.pkl", "rb") as f:
    trained_agent = load(f)

# Testing the agent's performance against the ghost
def test_ghost_efficiency(env, agent, episodes=100):
    caught_count = 0
    steps_without_caught = 0
    total_steps = 0

    for _ in range(episodes):
        s = env.reset()
        done = False
        while not done:
            a = agent.choose(s, env.actions)  # Agent chooses an action
            r, sp, done = env.step(a)  # Take step and update environment
            s = sp  # Update state
            total_steps += 1

            # If the agent is caught by the ghost, increment caught count
            if r < 0 and done:
                caught_count += 1
                steps_without_caught = 0
            else:
                steps_without_caught += 1

    print(f"Total steps: {total_steps}")
    print(f"Steps without getting caught: {steps_without_caught}")
    print(f"Number of times caught by ghost: {caught_count} out of {episodes}")

# Test ghost efficiency
test_ghost_efficiency(env, trained_agent)