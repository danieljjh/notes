# Q-Learning
## explanation
[Demystifying Deep Reinforcement Learning | Computational Neuroscience Lab](http://neuro.cs.ut.ee/demystifying-deep-reinforcement-learning/)

[Dissecting Reinforcement Learning-Part.1](https://mpatacchiola.github.io/blog/2016/12/09/dissecting-reinforcement-learning.html)

[Reinforcement training](https://github.com/aikorea/awesome-rl)

### deep Q-learning algorithm with experience replay:
```
initialize replay memory D
initialize action-value function Q with random weights
observe initial state s
repeat
    select an action a
        with probability ε select a random action
        otherwise select a = argmaxa’Q(s,a’)
    carry out action a
    observe reward r and new state s’
    store experience <s, a, r, s’> in replay memory D

    sample random transitions <ss, aa, rr, ss’> from replay memory D
    calculate target for each minibatch transition
        if ss’ is terminal state then tt = rr
        otherwise tt = rr + γmaxa’Q(ss’, aa’)
    train the Q network using (tt - Q(ss, aa))^2 as loss

    s = s'
until terminated
```

### q-learning example

https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0

https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe


### OpenAI Gym for Trading With DQN OpenAI Baseline
https://github.com/AdrianP-/gym_trading

### Deep Trader
https://github.com/deependersingla/deep_portfolio/blob/master/supervised_learning/lstm_single_stock.py

[stock-Q-learning/QLearner.py at master · xjdeng/stock-Q-learning · GitHub](https://github.com/xjdeng/stock-Q-learning/blob/master/QLearner.py)


[Δ ℚuantitative √ourney | Q-learning with Neural Networks](http://outlace.com/rlpart3.html)



### game example
[用Tensorflow基于Deep Q Learning DQN 玩Flappy Bird - songrotek的专栏        - 博客频道 - CSDN.NET](http://blog.csdn.net/songrotek/article/details/50951537)



### make own gym
[强化学习实战 第一讲 gym学习及二次开发](https://zhuanlan.zhihu.com/p/26985029)


### q-learning path finding
http://www.mnemstudio.org/path-finding-q-learning-tutorial.htm


## Tading

### Trading gym
[Gym and agent for algorithmic stock and cryptocurrency trading - Universe - OpenAI Forum](https://discuss.openai.com/t/gym-and-agent-for-algorithmic-stock-and-cryptocurrency-trading/519)

https://github.com/hackthemarket/gym-trading

### deer  example
http://deer.readthedocs.io/en/latest/user/environments/toy_env_time_series.html

[Deep Q-Learning with Keras and Gym · Keon’s Blog](https://keon.io/deep-q-learning/)

## with Keras
[Using Keras and Deep Q-Network to Play FlappyBird | Ben Lau](https://yanpanlau.github.io/2016/07/10/FlappyBird-Keras.html)

[Reinforcement learning tutorial using Python and Keras - Adventures in Machine Learning](http://adventuresinmachinelearning.com/reinforcement-learning-tutorial-python-keras/)

## Keras-rl
https://github.com/keras-rl/keras-rl