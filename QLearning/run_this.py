"""
Reinforcement learning maze example.
Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].
This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.
View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from maze_env import Maze
from RL_brain import QLearningTable


def update():
    best_episode=0
    best_step=0
    for episode in range(1000):
        # initial observation
        observation = env.reset()
        step=0
        
        
        while True:
            step+=1
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))
            
            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action,step)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_
            

            # break while loop when end of this episode
            if done:
                print('episode:',episode,'total_step:',step)
                if best_step==0 or step<best_step:
                    best_step=step
                    best_episode=episode
                elif best_step>step:
                    best_step=step
                    best_episode=episode
                    
                break
        if episode>100:
            RL.change_epsilon()

    # end of game
    print('game over')
    print("最佳成績：Episode{},{}STEP".format(best_episode,best_step))
    
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()