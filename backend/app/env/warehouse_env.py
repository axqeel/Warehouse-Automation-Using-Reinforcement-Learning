import gymnasium as gym
from gymnasium import spaces
import numpy as np

class WarehouseEnv(gym.Env):
    def __init__(self, grid_size=(20, 20, 5), n_agents=3, n_shelves=5):
        super(WarehouseEnv, self).__init__()
        self.grid_size = grid_size
        self.n_agents = n_agents
        self.n_shelves = n_shelves
        self.action_space = spaces.Discrete(6)  # up, down, left, right, forward, backward
        self.observation_space = spaces.Box(low=0, high=max(grid_size), shape=(n_agents, 3), dtype=np.int32)
        self.reset()

    def reset(self, seed=None, options=None):
        self.agent_positions = np.random.randint(0, self.grid_size[0], (self.n_agents, 3))
        self.shelf_positions = np.random.randint(0, self.grid_size[0], (self.n_shelves, 3))
        return self.agent_positions, {}

    def step(self, actions):
        # actions: list of actions for each agent
        for i, action in enumerate(actions):
            if action == 0:  # up
                self.agent_positions[i][1] = min(self.grid_size[1]-1, self.agent_positions[i][1]+1)
            elif action == 1:  # down
                self.agent_positions[i][1] = max(0, self.agent_positions[i][1]-1)
            elif action == 2:  # left
                self.agent_positions[i][0] = max(0, self.agent_positions[i][0]-1)
            elif action == 3:  # right
                self.agent_positions[i][0] = min(self.grid_size[0]-1, self.agent_positions[i][0]+1)
            elif action == 4:  # up z
                self.agent_positions[i][2] = min(self.grid_size[2]-1, self.agent_positions[i][2]+1)
            elif action == 5:  # down z
                self.agent_positions[i][2] = max(0, self.agent_positions[i][2]-1)
        reward = 0  # Placeholder
        done = False
        info = {}
        return self.agent_positions, reward, done, False, info
