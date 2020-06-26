import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import brfss


def print_stats(x, y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    print("slope = %s, intercept = %s, r_value = %s, p_value = %s, std_err = %s" %
          (slope, intercept, r_value, p_value, std_err),
          sep=' ')
    print()

    print("coefficient of determination =", np.power(r_value, 2), sep=' ')
    print()
    return slope, intercept


df = brfss.ReadBrfss(filename="..\..\CDBRFS08.ASC.gz")
df = df.dropna()

df['log_wgt'] = np.log10(df.wtkg2)

df_sample = df[0:10]
print(df_sample)

# get slope, intercept, rvalue etc for adult wgt as a func of hgt
print_stats(df.htm3, df.wtkg2)

# get slope, intercept, rvalue etc for log of adult wgt as a func of hgt
slope, intercept = print_stats(df.htm3, df.log_wgt)
reg_logwgts = slope * df.htm3 + intercept
inv_transform_logwgts = np.power(10, reg_logwgts.values)

sns.set(color_codes=True)

plt.figure(1)
sns.lmplot(x="htm3", y="wtkg2", data=df)
sns.lineplot(x=df.htm3.values, y=inv_transform_logwgts, lw=1, color="green")

plt.figure(2)
sns.lmplot(x="htm3", y="log_wgt", data=df)

plt.show()


