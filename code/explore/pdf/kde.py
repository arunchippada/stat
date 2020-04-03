import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import math

# normal sample for women heights
mean = 163
std = math.sqrt(52.8)
norm = stats.norm(loc=mean, scale=std)
sample = pd.Series(norm.rvs(size=500)).sort_values()

sample_pdf = norm.pdf(sample.values)
sample_cdf = norm.cdf(sample.values)

kde = stats.gaussian_kde(sample.values)
estimated_pdf = kde.pdf(sample.values)

frame = pd.DataFrame(data={
    'spdf': sample_pdf,
    'epdf': estimated_pdf,
    'scdf': sample_cdf
}, index=sample.values)

print(frame)
low = sample.iat[0]
high = sample.iat[499]
integral = kde.integrate_box_1d(low, high)
print(integral)

plt.figure(1)
sns.lineplot(x=sample.values, y=sample_pdf, lw=1, color="blue", label="sample pdf for women heights")
sns.lineplot(x=sample.values, y=estimated_pdf, lw=1, color="red", label="estimated pdf for women heights")

# sample1 = pd.Series([random.gauss(mean, std) for i in range(500)])
# print(sample1.sort_values())

plt.legend()
plt.show()