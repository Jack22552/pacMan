Reinforcement Learning Pac-Man Project
Jack Salinas, Daron Chen

Introduction:
This report presents a detailed summary of our implementation, experimentation, and evaluation of the experimental work we undertook for our Artificial Intelligence project. In this project, we were able to train a reinforcement-learning (RL) based Pac-Man agent to successfully navigate a small maze, collect pellets, and evade A* guided ghosts.

Project Summary:
The game environment was designed as a minimalistic Pac-Man world where several details were omitted. The key simplifications included:
A smaller grid size.
A single ghost agent.
No use of power pellets or fruit bonuses.
The Pac-Man agent used a Q-learning agent with epsilon-greedy exploration. The ghosts used A* search that dynamically recalculated the shortest path to Pac-Man on every turn.

Experimental Setup:
We trained the RL agent using 100 total training batches while tracking average scores and "epsilon" values as part of the performance assessment. We implemented and performed two training runs (train.py and train2.py) that had similar configurations (to verify the approach was consistent and robust).

Results:
Initial Performance: During the early episodes of both training runs, both agents displayed poor performance, resulting in negative average scores due to getting eaten by the ghost too often and inefficient pellet collection. 
Improvement Trend: With training, and increases to the epsilon decrease (less exploration), the agent demonstrated progressively more optimal behavior in training runs, consistently avoiding ghosts and collecting pellets.
Score Plateau: By batch 30, performance leveled off, with agents achieving an average score near 51.10 (most likely a max score), suggesting the agents have converged.

Example Data Points from train.py:
Batch 0: Avg Score = -4.67, Epsilon = 0.778
Batch 10: Avg Score = 23.12, Epsilon = 0.063
Batch 20: Avg Score = 48.54, Epsilon = 0.005
Batch 30-99: Avg Score consistently = 51.10, Epsilon = 0.000

Example Data Points from train2.py:
Batch 0: Avg Score = -4.50
Batch 14: Avg Score = 35.15
Batch 16: Avg Score = 42.49
Batch 17-30+: Scores consistently above 44.0

Ghost Behavior and Impact:
The use of A*-powered ghosts provided the agent with random and dynamic challenges. Since the ghosts were recalculating shortest paths once every move, Pac-Man was forced to learn evasive behavior rather than memorizing fixed patterns, which enabled him to generalize and develop a stronger policy across different game states.

Comparative Evaluation:
We also evaluated the trained Q-learning agent against a baseline agent that used a random movement policy. The trained agent achieved:
Higher average score (up to ~51.10)
Longer survival time
Fewer ghost collisions

Conclusions:
Using reinforcement learning (for Pac-Man) and the A* search algorithm (for the ghost AI) produced a successful and fun game agent. The Q-learning algorithm converged to an optimal policy for the game environment. The epsilon decay method was important in limiting the exploration area and transitions to exploitation. Overall, this project proved effective in utilizing traditional RL and pathfinding algorithms in game AI. Our agent learned not only how to move optimally, but also how to respond to real-time threats, enabling it to get consistent high scores.

