import nsfg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = nsfg.ReadFemResp()

plt.figure(1)
plt.grid(axis='y', color='r')
plt.hist(df.totincr, bins=range(0, 16, 1), histtype='bar', rwidth=0.9)

plt.figure(2)
plt.grid(axis='y', color='r')
plt.hist(df.age_r, bins=np.arange(min(df.age_r-1), max(df.age_r)+2, 1), histtype='bar', rwidth=0.9)

plt.figure(3)
plt.grid(axis='y', color='r')
plt.hist(df.numfmhh, bins=np.arange(min(df.numfmhh-1), max(df.numfmhh)+2, 1), histtype='bar', rwidth=0.9)

plt.figure(4)
plt.grid(axis='y', color='r')
plt.hist(df.parity, bins=np.arange(min(df.parity-1), max(df.parity)+2, 1), histtype='bar', rwidth=0.9)

plt.show()

