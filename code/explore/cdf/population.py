import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import populations
import cdf_func as cdf_func


population = populations.ReadData()

population_cdf = cdf_func.cdf(population)
population_freq = cdf_func.freq(population)
population_ccdf = 1 - population_cdf
population_lccdf = np.log10(population_ccdf)
log_x = np.log10(population_lccdf.index)

frame = pd.DataFrame(data={
    'cdf': population_cdf,
    'freq': population_freq
})
# print(frame[600:700])

plt.figure(1)
sns.lineplot(x=population_cdf.index, y=population_cdf.values, lw=1, color="blue", label="Population cdf")

plt.figure(2)
sns.lineplot(x=log_x, y=population_lccdf.values, lw=1, color="blue", label="Population lccdf vs log x")

# normal probability plot for log population
log_population = np.log10(population.sort_values())
norm = pd.Series(np.random.normal(size=log_population.size)).sort_values()

plt.figure(3)
sns.lineplot(x=norm.values, y=log_population.values, lw=1, color="blue", label="Log population vs Norm")

fit_xs = pd.Series([-4.0, 4.0])
fit_ys = (log_population.std() * fit_xs) + log_population.mean()
sns.lineplot(x=fit_xs.values, y=fit_ys.values, lw=1, color="gray", label="Fit line")

plt.legend()
plt.show()

