import nsfg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# weighted table to pmf
def normalize_to_pmf(s):
    sum = s.sum()
    return s.sort_index()/sum

def mean_from_pmf(s):
    items = s.index.to_series()
    contrib = items * s
    return contrib.sum()

df = nsfg.ReadFemResp()

numkdhh = df.numkdhh

numkdhh_freq = numkdhh.value_counts()
numkdhh_freq_pmf = normalize_to_pmf(numkdhh_freq)

numkdhh_size = numkdhh_freq.index.to_series()
numkdhh_size_pmf = normalize_to_pmf(numkdhh_size)

bias_pmf = normalize_to_pmf(numkdhh_size_pmf * numkdhh_freq_pmf)

print("numkdhh mean:", numkdhh.mean(), sep='\n')
print("numkdhh mean from pmf:", mean_from_pmf(numkdhh_freq_pmf), sep='\n')
print("numkdhh bias mean:", mean_from_pmf(bias_pmf), sep='\n')

plt.figure(1)
sns.barplot(numkdhh_freq_pmf.index, numkdhh_freq_pmf.values, color="skyblue", label="freq pmf")
sns.barplot(bias_pmf.index, bias_pmf.values, color="red", label="bias pmf", alpha=0.4)
plt.legend()
plt.show()
