import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import analytic
import explore.cdf_func as cdf_func
import scipy.stats as stats


df = analytic.ReadBabyBoom()

plt.figure(1)
sns.lineplot(x=df.index, y=df.minutes, lw=1, color="blue", label="Time of birth")

inter_arrival = df.minutes.diff()

inter_arrival_cdf = cdf_func.cdf(inter_arrival)

plt.figure(2)
sns.lineplot(x=inter_arrival_cdf.index, y=inter_arrival_cdf.values, lw=1, color="blue", label="Interarrival cdf")

inter_arrival_freq = cdf_func.freq(inter_arrival)
inter_arrival_ccdf = 1 - inter_arrival_cdf
inter_arrival_lccdf = np.log10(inter_arrival_ccdf)
inter_arrival_pmf = cdf_func.pmf(inter_arrival)

plt.figure(3)
sns.lineplot(x=inter_arrival_cdf.index, y=inter_arrival_ccdf.values, lw=1, color="blue", label="Interarrival ccdf")

plt.figure(4)
sns.lineplot(x=inter_arrival_cdf.index, y=inter_arrival_lccdf.values, lw=1, color="blue", label="Interarrival lccdf")

plt.figure(5)
sns.lineplot(x=inter_arrival_pmf.index, y=inter_arrival_pmf.values, lw=1, color="blue", label="Interarrival pmf")

frame = pd.DataFrame(data={
    'cdf': inter_arrival_cdf,
    'freq': inter_arrival_freq,
    'ccdf': inter_arrival_ccdf,
    'lccdf': inter_arrival_lccdf},
    index=inter_arrival_cdf.index)
# print(frame)

# plot exponential dist samples against the interarrival samples
inter_arrival_x = inter_arrival.sort_values().dropna()
expon = stats.expon(scale=33)
expon_rvs = pd.Series(expon.rvs(size=43)).sort_values()

plt.figure(6)
sns.lineplot(x=inter_arrival_x.values, y=expon_rvs.values, lw=1, color="blue", label="exponential dist vs interarrival")

plt.legend()
plt.show()
