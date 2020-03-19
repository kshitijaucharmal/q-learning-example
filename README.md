# q-learning-example
this repository is where i will post every progress i make in learning machine learning or more specifically, Q Learning.
The first files i uploaded are files.py and game.py
The "files.py" file contains the game which is a 9x9 grid with the player's position random and 
the goal being the lower right box
it has 9 states, starting from 0, and 4 actions, namely -
0 - up
1 - down
2 - right
3 - left
the goal is to reach the goal quickly, as 0.5 penalty is given for each action
the goal reaching state has 100 reward, while going beyond limits has -10 reward, not changing the currnet state.
The "game.py" file has an example run of the program, which is not working yet (i have 2gb ram :P)
