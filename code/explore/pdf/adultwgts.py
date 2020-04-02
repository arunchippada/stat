import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import brfss

def pearsonMedianSkewness(mean, median, std):
    return 3 * (mean - median) / std


df = brfss.ReadBrfss()

weights = df.wtkg2.dropna().sort_values()
weights_size = weights.size

weights_mean = weights.mean()
weights_std = weights.std()
weights_median = weights.median()
print(weights_size)
print(weights_mean)
print(weights_median)
print(weights_std)
print("Pearson skew", pearsonMedianSkewness(weights_mean, weights_median, weights_std), sep='\n')

if 1:
    norm = pd.Series(np.random.normal(size=weights_size)).sort_values()

    # plot weights against normal
    plt.figure(1)
    sns.lineplot(x=norm.values, y=weights.values, lw=1, color="blue", label="Adult weights vs Norm")

    fit_xs = pd.Series([-4.0, 4.0])
    fit_ys = (weights_std * fit_xs) + weights_mean
    sns.lineplot(x=fit_xs.values, y=fit_ys.values, lw=1, color="gray", label="Fit line")

    log_weights = np.log10(weights)
    log_weights_mean = log_weights.mean()
    log_weights_std = log_weights.std()

    # plot log_weights against normal
    plt.figure(2)
    sns.lineplot(x=norm.values, y=log_weights.values, lw=1, color="blue", label="Log of Adult weights vs Norm")

    fit_xs = pd.Series([-4.0, 4.0])
    fit_ys = (log_weights_std * fit_xs) + log_weights_mean
    sns.lineplot(x=fit_xs.values, y=fit_ys.values, lw=1, color="gray", label="Fit line")

if 0:
    # estimated pdf for weights
    kde = stats.gaussian_kde(weights.values)
    estimated_pdf = kde.pdf(weights.values)

    plt.figure(3)
    sns.lineplot(x=weights.values, y=estimated_pdf, lw=1, color="blue", label="Estimated pdf for weights")

plt.legend()
plt.show()
