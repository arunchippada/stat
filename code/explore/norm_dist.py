import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nsfg
import explore.cdf_func as cdf_func

df = nsfg.ReadFemPreg()

df_live = df[df.outcome == 1]

birthwgt = df_live.totalwgt_lb.dropna().sort_values()
birthwgt_size = birthwgt.size
birthwgt_mean = birthwgt.mean()
birthwgt_std = birthwgt.std()

print(birthwgt_mean)
print(birthwgt_std)

norm = pd.Series(np.random.normal(size=birthwgt_size)).sort_values()

plt.figure(1)
sns.lineplot(x=norm.values, y=birthwgt.values, lw=1, color="blue", label="Birthwgt vs Norm")

fit_xs = pd.Series([-4.0, 4.0])
fit_ys = (birthwgt_std * fit_xs) + birthwgt_mean
sns.lineplot(x=fit_xs.values, y=fit_ys.values, lw=1, color="gray", label="Fit line")

plt.legend()
plt.show()

