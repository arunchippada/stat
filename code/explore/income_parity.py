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


df = nsfg.ReadFemResp()

high_income_parity = df[df.totincr == 14].parity
others_parity = df[df.totincr != 14].parity

# aggregate stats
print("High Income parity avg = {avg}, count = {count}, max = {max}, min = {min}".format(
    avg=high_income_parity.mean(),
    count=high_income_parity.count(),
    max=high_income_parity.max(),
    min=high_income_parity.min()))

print("Others parity avg = {avg}, count = {count}, max = {max}, min = {min}".format(
    avg=others_parity.mean(),
    count=others_parity.count(),
    max=others_parity.max(),
    min=others_parity.min()))
print()

# cohen effect size
print("Cohen effect size", cohen_effect_size(high_income_parity, others_parity), sep='\n')
print()

# histogram comparison
plt.figure(1)
plt.grid(axis='y', color='r')

plt.hist([high_income_parity, others_parity], label=["high income", "others"],
         bins=range(0, 20, 1), histtype='bar', rwidth=0.9)
plt.legend(loc="best")

plt.show()
