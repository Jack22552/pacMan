***Pac-Man Reinforcement Learning Agent***

Authors: Jack Salinas, Daron Chen

This project implements a reinforcement learning Pac-Man agent trained using Q-learning to navigate a simplified maze environment. The agent learns to collect pellets while avoiding a ghost that pursues Pac-Man using the A* search algorithm. The project explores how reinforcement learning can develop effective policies in a dynamic game environment where the agent must balance exploration and survival.

**Environment Design**
  The Pac-Man environment was simplified to make reinforcement learning tractable while still providing meaningful challenges.  
  Key simplifications:
  
  - Smaller grid-based maze
  - One ghost agent
  - No power pellets or fruit bonuses
  - Deterministic game mechanics
  
  These constraints allowed us to focus on the interaction between Q-learning and adversarial pathfinding.

**Agent Architecture**
  - Pac-Man Agent
  
  Pac-Man uses a Q-learning algorithm with an epsilon-greedy exploration strategy.
  Key elements:
  
  - State-action Q-table
  - Epsilon-greedy exploration
  - Reward signals for pellet collection and survival
  - Training through repeated game episodes

  - Ghost Agent
    The ghost uses A* pathfinding, recalculating the shortest path to Pac-Man at every step.
    This creates a dynamic adversary that forces the RL agent to learn evasive behavior rather than memorizing patterns.

**Training Setup**
  The RL agent was trained over 100 training batches, tracking:
  - Average score 
  - Epsilon decay (exploration rate)
  
  Two training configurations were tested: 
  - train.py  
  - train2.py
  
  These runs were used to verify that the learning process was consistent and reproducible.

**Results**
  Performance Improvement
  Early training episodes resulted in poor performance as the agent explored the environment.
  Example progression from train.py:
  
  Batch	  Avg Score	  Epsilon
  0	      -4.67	      0.778
  10	    23.12	      0.063
  20	    48.54	      0.005
  30-99	  ~51.10	    0.000
  
  After sufficient training, the agent converged to a near-optimal strategy with consistent high scores.

**Comparison with Baseline**
  We compared the trained agent to a random-movement baseline agent. 
  The trained agent achieved:
  
  - significantly higher average score
  - longer survival time
  - fewer ghost collisions
  
  This demonstrates the effectiveness of reinforcement learning in learning optimal policies within the environment.

**Key Takeaways**
  - Q-learning successfully learned an optimal policy for pellet collection and ghost avoidance.
  - Epsilon decay played a critical role in transitioning from exploration to exploitation.
  - Combining reinforcement learning with adversarial A* pathfinding created a dynamic and challenging training environment.

**Running the Project**
  Example commands:
  
  - python train.py
  - python train2.py
  
  Training progress and performance metrics will be printed during execution.
