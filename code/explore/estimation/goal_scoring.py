import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import cdf_func as cdf_func


GAME_TIME = 90


def simulate_game(lam):
    goals = []
    cur_game_time = 0
    expon = stats.expon(loc=0, scale=1/lam)

    while cur_game_time < GAME_TIME:
        goal_interval = expon.rvs(size=1)[0]
        cur_game_time += goal_interval
        if cur_game_time <= GAME_TIME:
            goals.append(goal_interval)

    return len(goals)


def error_dist(lam):
    errors = []
    for _ in range(1000):
        g = simulate_game(lam)
        lambdabar = g/GAME_TIME
        errors.append(lambdabar - 2)

    error_dist = pd.Series(errors)

    if 1:
        percentile_5 = error_dist.quantile(q=0.05)
        percentile_95 = error_dist.quantile(q=0.95)
        print(percentile_5, error_dist.quantile(q=0.5), percentile_95)
        print("confidence interval = ", percentile_95 - percentile_5)

        cdf = cdf_func.cdf(error_dist)
        plt.figure(1)
        sns.lineplot(x=cdf.index, y=cdf.values, lw=1, color="blue", label="error distribution cdf")
        plt.show()

    return error_dist.std()


print(error_dist(1/10))