import nsfg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


def pearson(s1, s2):
    n = s1.count()
    mean_s1 = s1.mean()
    mean_s2 = s2.mean()

    cov = ((s1 - mean_s1).dot(s2 - mean_s2))/n
    return cov/(s1.std() * s2.std())


def spearman(s1, s2):
    return pearson(s1.rank(), s2.rank())


df = nsfg.ReadFemPreg(dct_file="../2002FemPreg.dct", dat_file="../2002FemPreg.dat.gz")

df_live = df[(df.outcome == 1) & np.isfinite(df.agepreg) & np.isfinite(df.totalwgt_lb)]

plt.figure(1)
sns.scatterplot(x='agepreg', y='totalwgt_lb', data=df_live, label="Baby weight vs mother's age")

plt.figure(2)
# use transparency (alpha) to highlight overlapping points
sns.scatterplot(x='agepreg', y='totalwgt_lb', data=df_live, label="Baby weight vs mother's age", alpha=0.2)

plt.figure(3)
# hexbin
sns.jointplot(x='agepreg', y='totalwgt_lb', data=df_live, kind='hex', color='k', label="Baby weight vs mother's age")

# percentiles of wgt for agepreg bins
indices = np.digitize(df_live.agepreg, np.arange(15, 50, 5))
groups = df_live.groupby(indices)

plt.figure(5)

sns.lineplot(x=groups['agepreg'].mean(), y=groups['totalwgt_lb'].quantile(q=0.25), lw=1, color="green", label="25th percentile wgt vs avg age")
sns.lineplot(x=groups['agepreg'].mean(), y=groups['totalwgt_lb'].quantile(q=0.5), lw=1, color="blue", label="50th percentile wgt vs avg age")
sns.lineplot(x=groups['agepreg'].mean(), y=groups['totalwgt_lb'].quantile(q=0.75), lw=1, color="red", label="75th percentile wgt vs avg age")
sns.lineplot(x=groups['agepreg'].mean(), y=groups['totalwgt_lb'].quantile(q=0.9), lw=1, color="orange", label="90th percentile wgt vs avg age")

plt.show()

print("Pearson =", pearson(df_live.agepreg, df_live.totalwgt_lb), sep=' ')
print()

print("Spearman =", spearman(df_live.agepreg, df_live.totalwgt_lb), sep=' ')
print()




