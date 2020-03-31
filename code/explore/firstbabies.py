import nsfg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def cohen_effect_size(s1, s2):
    mean_diff = s1.mean() - s2.mean()

    s1_count = s1.count()
    s2_count = s2.count()
    weighted_variance = (s1_count * s1.var() + s2_count * s2.var())/(s1_count + s2_count)

    return mean_diff/np.sqrt(weighted_variance)


df = nsfg.ReadFemPreg()

df_live = df[df.outcome == 1]

# use prglngth > 27 weeks, to discard outliers
# df_live = df_live[df_live.prglngth > 27]

df_live['firstbaby'] = (df_live.birthord == 1)

# do first babies arrive late?
# birthordr pivot, avg(preglength)
print("Preg length summary by Birth order", pd.pivot_table(df_live, values=['prglngth'], index='birthord', aggfunc=(np.mean, len)), sep='\n')
print()

print("Preg length summary (First vs Non-First)", pd.pivot_table(df_live, values=['prglngth'], index='firstbaby', aggfunc=(np.mean, len)), sep='\n')
print()

first_prglngth = df_live[df_live.firstbaby].prglngth
others_prglngth = df_live[~df_live.firstbaby].prglngth

print("Cohen effect size PregLength (First vs Non-First)", cohen_effect_size(first_prglngth, others_prglngth), sep='\n')
print()

plt.figure(1)
plt.grid(axis='y', color='r')

plt.hist([first_prglngth, others_prglngth], label=["first", "other"], bins=range(27, 50, 1), histtype='bar', rwidth=0.9)
plt.legend(loc="best")

# do first babies weight different?
print("totalwgt_lb summary by Birth order", pd.pivot_table(df_live, values=['totalwgt_lb'], index='birthord', aggfunc=(np.mean, len)), sep='\n')
print()

print("totalwgt_lb summary (First vs Non-First)", pd.pivot_table(df_live, values=['totalwgt_lb'], index='firstbaby', aggfunc=(np.mean, len)), sep='\n')
print()

first_weight = df_live[df_live.firstbaby].totalwgt_lb
others_weight = df_live[~df_live.firstbaby].totalwgt_lb

print("Cohen effect size Weight (First vs Non-First)", cohen_effect_size(first_weight, others_weight), sep='\n')
print()

plt.figure(2)
plt.grid(axis='y', color='r')

plt.hist([first_weight, others_weight], label=["first", "other"], bins=range(0, 15, 1), histtype='bar', rwidth=0.9)
plt.legend(loc="best")

plt.show()


