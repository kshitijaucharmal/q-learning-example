import matplotlib.pyplot as plt
import numpy as np 
import random
class Maze:
	def __init__(self):
		self.n_actions, self.n_states = 4, 9
		self.state = self.reset()
		self.reward_table = np.zeros((self.n_states, self.n_actions)) + -0.5
		self.actions = {
			0:-3,#up
			1:3,#down
			2:1,#right
			3:-1#left
		}
		self.reward_table[0, 0], self.reward_table[0, 3] = -10, -10
		self.reward_table[1, 0] = -10
		self.reward_table[2, 2], self.reward_table[2, 0] = -10, -10
		self.reward_table[3, 3] = -10
		self.reward_table[5, 3], self.reward_table[5, 1] = -10, 100
		self.reward_table[6, 3], self.reward_table[6, 1] = -10, -10
		self.reward_table[7, 1], self.reward_table[7, 2] = -10, 100
		self.reward_table[8, 2], self.reward_table[8, 1] = -10, -10
		pass
	def reset(self):
		self.state = int(random.uniform(0, 8))
		return self.state
	def step(self, action):
		done = False
		observation = self.state + self.actions[action]
		if self.reward_table[self.state, action] == 100:
			done = True
		if observation <= 0 or observation >= 9:
			observation = self.state
		reward = self.reward_table[self.state, action]
		return observation, reward, done
	def sample(self):
		action = int(random.uniform(0, 4))
		return action


