import nsfg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = nsfg.ReadFemPreg()

birthweight_dist = df.birthwgt_lb.value_counts().sort_index()

plt.figure(1)
birthweight_dist.plot(kind='bar')

# plot using plt hist
plt.figure(2)
plt.grid(axis='y', color='r')

hist_bins = np.arange(min(df.birthwgt_lb), max(df.birthwgt_lb)+1, 1)
plt.xticks(hist_bins)
plt.hist(df.birthwgt_lb, bins=hist_bins, histtype='bar', rwidth=0.9)

plt.figure(3)
plt.hist(df.birthwgt_oz, bins=20, histtype='bar', rwidth=0.9)

plt.figure(4)
plt.grid(axis='y', color='r')
plt.hist(df.agepreg, bins=np.arange(min(df.agepreg), max(df.agepreg)+1, 1), histtype='bar', rwidth=0.9)

plt.figure(5)
plt.grid(axis='y', color='r')
plt.hist(df.prglngth, bins=np.arange(min(df.prglngth), max(df.prglngth)+1, 1), histtype='bar', rwidth=0.9)

plt.show()