import nsfg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def freq(s):
    return s.value_counts().sort_index()

def pmf(s):
    count = s.count()
    hist = s.value_counts().sort_index()
    return hist/count

def cdf_series(s):
    return pmf(s).cumsum()

def cdf(s, x = None):
    c = cdf_series(s)

    if x is None:
        return c

    i = c.index.get_loc(x, method="pad")
    return c.iloc[i]


if __name__ == "__main__":
    df = nsfg.ReadFemPreg()
    cdf_prglength = cdf(df.prglngth)

    # plot cdf for prglength
    plt.figure(1)
    sns.lineplot(x=cdf_prglength.index, y=cdf_prglength.values, lw=1, color="blue", label="CDF for prglngth")

    # birthwgt first vs others
    df_first = df[df.birthord == 1]
    df_others = df[df.birthord != 1]
    first_wgt_cdf = cdf(df_first.totalwgt_lb)
    others_wgt_cdf = cdf(df_others.totalwgt_lb)

    # cdf for a specific weight
    print(cdf(df_first.totalwgt_lb, 5.4))

    plt.figure(2)
    sns.lineplot(x=first_wgt_cdf.index, y=first_wgt_cdf.values, lw=1, color="blue", label="First weight CDF")
    sns.lineplot(x=others_wgt_cdf.index, y=others_wgt_cdf.values, lw=1, color="red", label="Others weight CDF")

    # pmf for first_wgt
    first_wgt_pmf = pmf(df_first.totalwgt_lb)
    plt.figure(3)
    sns.lineplot(x=first_wgt_pmf.index, y=first_wgt_pmf.values, lw=1, color="blue", label="First weight PMF")

    plt.legend()
    plt.show()
