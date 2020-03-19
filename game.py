import numpy as np
import files
import random
env = files.Maze()

# parameters 
alpha = 0.1
gamma = 0.6
epsilon = 0.1
q_table = np.zeros([env.n_states, env.n_actions])
episodes = 1000
for i in range(episodes + 1):
	state = env.reset()
	epochs, penalties, reward = 0, 0, 0
	done = False
	while not done:
		if random.uniform(0, 1) < epsilon:
			action = env.sample()
		else:
			action = np.argmax(q_table[state])
		next_state, reward, done = env.step(action)

		old_value = q_table[state, action]
		next_max = np.max(q_table[next_state])

		new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
		q_table[state, action] = new_value

		state = next_state
		epochs += 1
		if reward == -10:
			penalties += 1
		pass
	if i % 100 == 0:
		print("Episode: "+str(i))
print q_table