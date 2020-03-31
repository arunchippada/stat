import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import explore.cdf_func as cdf_func


def std_err_exp(n):
    errors = []
    for _ in range(1000):
        # Lambda = 2 implies scale = 1/2
        # expon = stats.expon(loc=0, scale=1/2)
        # sample = pd.Series(expon.rvs(size=n))

        expon = np.random.exponential(1/2, n)
        sample = pd.Series(expon)

        mean = sample.mean()
        lambdabar = 1/mean
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


std_err_exp(10)
if 0:
    std_errors = []
    sample_sizes = range(10, 100, 10)
    for i in sample_sizes:
        std_errors.append(std_err_exp(i))

    plt.figure(2)
    sns.lineplot(x=sample_sizes, y=std_errors, lw=1, color="blue", label="std error for increasing sample size")
    plt.show()

