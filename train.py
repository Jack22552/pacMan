# train.py
from environment import PacmanEnv
from agent1 import QLearner
import matplotlib.pyplot as plt
from pickle import dump

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
