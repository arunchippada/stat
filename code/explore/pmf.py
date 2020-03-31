import nsfg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def pmf(s):
    count = s.count()
    hist = s.value_counts().sort_index()
    return hist/count

df = nsfg.ReadFemPreg()

df_live = df[df.outcome == 1]

df_live['firstbaby'] = (df_live.birthord == 1)

first_prglngth = df_live[df_live.firstbaby].prglngth
others_prglngth = df_live[~df_live.firstbaby].prglngth

# plot pmf for first vs others using distplot on the same axis
plt.figure(1)
sns.distplot(first_prglngth, bins=range(25, 52, 1), color="skyblue", label="first prglngth")
sns.distplot(others_prglngth, bins=range(25, 52, 1), color="red", label="others prglngth")
plt.legend()

# filtering to specific week range
weeks = np.arange(35, 46)

pmf_first_prglngth = pmf(first_prglngth)
pmf_others_prglngth = pmf(others_prglngth)

zoomed_first = pmf_first_prglngth.reindex(weeks)
zoomed_others = pmf_others_prglngth.reindex(weeks)

# plot pmf for zoomed first vs others using barplot
plt.figure(2)
sns.barplot(zoomed_first.index, zoomed_first.values, color="skyblue", label="first prglngth")
sns.barplot(zoomed_others.index, zoomed_others.values, color="red", label="others prglngth")
plt.legend()

# plot the diff between zoomed
plt.figure(3)
diff = 100 * (zoomed_first - zoomed_others)
sns.barplot(diff.index, diff.values, color="skyblue", label="diff zoomed")

plt.show()