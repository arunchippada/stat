import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import nsfg

df = nsfg.ReadFemResp(dct_file="../../2002FemResp.dct", dat_file="../../2002FemResp.dat.gz")
df['age2'] = df.age_r ** 2;
df['age3'] = df.age_r ** 3;
df.numbabes.replace([97], np.nan, inplace=True)

print(df[['caseid', 'age_r', 'age2', 'age3', 'race', 'hieduc', 'educat', 'rscreenrace', 'totincr', 'numbabes']].head(10))
# print(df.numbabes.value_counts())

model = smf.poisson('numbabes ~ age_r + C(race) + educat + totincr', data=df)
results = model.fit()
print(results.summary())

new = pd.DataFrame([[35, 1, 16, 14]], columns=['age_r', 'race', 'educat', 'totincr'])
print(results.predict(new))
