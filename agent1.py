# agent1.py PACMAN
from collections import defaultdict
from random import random, choice

class QLearner:
    def __init__(self, alpha=0.1, gamma=0.99, epsilon=1.0, decay=0.995):
        self.alpha = alpha          # Learning rate
        self.gamma = gamma          # Discount factor
        self.epsilon = epsilon      # Exploration rate
        self.decay = decay          # Epsilon decay
        self.q = defaultdict(float) # Q-table, defaults to 0 for unseen (state, action)

    def choose(self, state, actions):
        """
        Choose an action using epsilon-greedy strategy.
        """
        if random() < self.epsilon:
            return choice(actions)
        else:
            return max(actions, key=lambda a: self.q[(state, a)])

    def update(self, s, a, r, sp, actions, terminal):
        """
        Q-learning update rule.
        """
        if terminal:
            target = r
            self.epsilon *= self.decay
        else:
            future = max(self.q[(sp, ap)] for ap in actions)
            target = r + self.gamma * future

        self.q[(s, a)] = (1 - self.alpha) * self.q[(s, a)] + self.alpha * target