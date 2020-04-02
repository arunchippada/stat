import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# blue man group: 177.8 cm to 185.42 cm
men_ht = stats.norm(loc=178, scale=7.7)
blue_start = men_ht.cdf(177.8)
blue_end = men_ht.cdf(185.42)

# 34.27%
print("percent of men for the blue man group height range", blue_end - blue_start, sep='\n')
print()

# if human height is pareto
ht_pareto = stats.pareto(b=1.7, scale=1)

# cdf for ht_pareto
x = np.linspace(start=1, stop=8, num=100)
ht_pareto_cdf = ht_pareto.cdf(x)

plt.figure(1)
sns.lineplot(x=x, y=ht_pareto_cdf, lw=1, color="blue", label="cdf for height pareto")

ht_pareto_mean = ht_pareto.mean()
ht_pareto_median = ht_pareto.median()

print("height pareto mean", ht_pareto_mean, sep='\n')
print("height pareto median", ht_pareto_median, sep='\n')

ht_pareto_mean_cdf = ht_pareto.cdf(ht_pareto_mean)
# 77.87%
print("Fraction shorter than mean", ht_pareto_mean_cdf, sep='\n')

ht_pareto_1km_cdf = ht_pareto.cdf(1000)
fraction = 1 - ht_pareto_1km_cdf
# 7.943282347211422e-06
print("Fraction greater than 1km", fraction, sep='\n')
# 55603
print("#People greater than 1km", fraction * 7 * 1000000000, sep='\n')

# Heights at specific cdf values
ppf_0 = ht_pareto.ppf(0)
ppf_1 = ht_pareto.ppf(1)
cdf_7_billion = 1 - (1/(7 * 1000000000))
ht_7_billion = ht_pareto.ppf(cdf_7_billion)

print("ppf0", ppf_0, sep='\n')
print("ppf1", ppf_1, sep='\n')
# 618.34 km
print("Height at 7 billion", ht_7_billion, sep='\n')
print()

# rvs = pd.Series(ht_pareto.rvs(size=10000))
# print(rvs.sort_values())


plt.legend()
plt.show()
