import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import nsfg

df = nsfg.ReadFemPreg(dct_file="../../2002FemPreg.dct", dat_file="../../2002FemPreg.dat.gz")

df_live = df[(df.outcome == 1) & (df.prglngth > 30)]
df_live['boy'] = (df_live.babysex == 1).astype(int)

model = smf.logit('boy ~ agepreg', data=df_live)
results = model.fit()
print(results.summary())

endog = pd.DataFrame(model.endog, columns=[model.endog_names])
exog = pd.DataFrame(model.exog, columns=[model.exog_names])

print(endog.head(10))
print(exog.head(10))