import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import hinc
import hinc2
import cdf_func as cdf_func

def pearsonMedianSkewness(mean, median, std):
    return 3 * (mean - median) / std


df = hinc.ReadData()
df['log_income'] = np.log10(df.income)
# print(df)

if 0:
    plt.figure(1)
    sns.lineplot(x=df.income.values, y=df.ps.values, lw=1, color="blue", label="Household Income cdf")

    income_ccdf = 1 - df.ps
    income_lccdf = np.log10(income_ccdf)
    log_income = np.log10(df.income)

    plt.figure(2)
    sns.lineplot(x=log_income.values, y=df.ps.values, lw=1, color="blue", label="Household Income cdf vs log income")

    # check for pareto
    plt.figure(3)
    sns.lineplot(x=log_income.values, y=income_lccdf.values, lw=1, color="blue", label="Household Income lccdf vs log income")

    plt.legend()
    plt.show()

log_sample = pd.Series(hinc2.InterpolateSample(df))
sample = np.power(10, log_sample)
median = sample.median()
mean = sample.mean()
std = sample.std()

print("median", median, "mean", mean, "std", std, sep=' ')
print("pearson skew", pearsonMedianSkewness(mean, median, std), sep=' ')

cdf_mean = cdf_func.cdf(sample, mean)
print("fraction below mean", cdf_mean, sep=' ')