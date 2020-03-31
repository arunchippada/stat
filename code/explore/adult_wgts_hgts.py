import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import brfss
import explore.cdf_func as cdf_func


def jitter(s, r):
    n = len(s)
    return s + np.random.uniform(-r, r, n)


df = brfss.ReadBrfss()

if 0:
    height_freq = cdf_func.freq(df.htm3)
    weight_freq = cdf_func.freq(df.wtkg2)

    print(height_freq)
    print(weight_freq)

plt.figure(1)
sns.scatterplot(x='htm3', y='wtkg2', data=df, label="Adult Height vs Weight")

plt.figure(2)

# add jitter to height
df['jitter_hgt'] = jitter(df.htm3, 1.3)

# use transparency (alpha) to highlight overlapping points
sns.scatterplot(x='jitter_hgt', y='wtkg2', data=df, label="Jitter Height vs Weight", alpha=0.2)

plt.figure(3)
# hexbin
sns.jointplot(x='jitter_hgt', y='wtkg2', data=df, kind='hex', color='k', label="Jitter Height vs Weight")

plt.legend()
plt.show()

print(df)
