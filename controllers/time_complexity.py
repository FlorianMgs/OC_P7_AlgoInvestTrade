import numpy as np
import matplotlib.pyplot as plt
from controllers.datasets import create_actions
from controllers.bruteforce import launch_bruteforce
from controllers.optimized import launch_optimized


path = './data/datasets/base_dataset.csv'
actions = create_actions(path)


def get_exec_times(bruteforce: bool):
    x = []
    y = []
    i = 1
    while i < len(actions):
        if bruteforce:
            exec_time = launch_bruteforce(actions[:i])
        else:
            exec_time = launch_optimized(actions[:i])
        x.append(i)
        y.append(exec_time)
        i += 1
    if bruteforce:
        create_figure(x, y, bruteforce=True)
    else:
        create_figure(x, y, bruteforce=False)


def create_figure(x: list, y: list, bruteforce: bool):
    x = np.array(x)
    y = np.array(y)
    if bruteforce:
        plt.plot(x, y, color="red")
        plt.xticks(range(1, 21, 1))
        plt.title("Time complexity - Bruteforce algorithm")
        plt.xlabel("Number of actions")
        plt.ylabel("Execution time (s)")
    else:
        plt.scatter(x, y, color="red")
        linear_model = np.polyfit(x, y, 1)
        linear_model_fn = np.poly1d(linear_model)
        x_s = np.arange(0, 20)
        plt.plot(x_s, linear_model_fn(x_s),color="green")
        plt.xticks(range(1, 21, 1))
        plt.title("Time complexity - Optimized algorithm")
        plt.xlabel("Number of actions")
        plt.ylabel("Execution time (ms)")
    plt.show()
