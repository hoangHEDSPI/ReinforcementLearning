import os
import sys
import numpy as np
from gridworld import GridworldEnv

env = GridworldEnv()
def policy_eval(policy, env, discount_factor = 1.0, theta = 0.00001):

