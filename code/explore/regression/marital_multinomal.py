import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import nsfg

df = nsfg.ReadFemResp(dct_file="../../2002FemResp.dct", dat_file="../../2002FemResp.dat.gz")

print(df[['caseid', 'age_r', 'race', 'educat', 'totincr', 'rmarital']].head(10))
print(df.rmarital.value_counts())

model = smf.mnlogit('rmarital ~ age_r + C(race) + educat + totincr', data=df)
results = model.fit()
print(results.summary())

new = pd.DataFrame([[25, 1, 10, 11]], columns=['age_r', 'race', 'educat', 'totincr'])
print("when race is black", results.predict(new), sep='\n')

new = pd.DataFrame([[25, 2, 10, 11]], columns=['age_r', 'race', 'educat', 'totincr'])
print("when race is white", results.predict(new), sep='\n')
