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


df = nsfg.ReadFemPreg(dct_file="../../2002FemPreg.dct", dat_file="../../2002FemPreg.dat.gz")

df_live = df[(df.outcome == 1) & np.isfinite(df.agepreg) & np.isfinite(df.totalwgt_lb)]

# get slope, intercept, rvalue etc for baby's birthwgt as a func of mother's age
slope, intercept, r_value, p_value, std_err = stats.linregress(df_live.agepreg, df_live.totalwgt_lb)

print("slope = %s, intercept = %s, r_value = %s, p_value = %s, std_err = %s" %
      (slope, intercept, r_value, p_value, std_err),
      sep=' ')
print()

# cross validate rvalue with pearson
print("Pearson =", pearson(df_live.agepreg, df_live.totalwgt_lb), sep=' ')
print()

sns.set(color_codes=True)

plt.figure(1)
sns.lmplot(x="agepreg", y="totalwgt_lb", data=df_live)
plt.show()

