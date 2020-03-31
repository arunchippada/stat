import thinkstats2
import pandas as pd
import numpy as np

dct = thinkstats2.ReadStataDct('E:\\scripts\\python\\thinkstat\\ThinkStats2\\code\\explore\\2002FemPreg.dct')
df = dct.ReadFixedWidth('E:\\scripts\\python\\thinkstat\\ThinkStats2\\code\\explore\\2002FemPreg.dat.gz', compression='gzip', nrows=None)

print("CaseId distribution:", df.caseid.value_counts(), sep='\n')
print()

print("Head:", df.head(10), sep='\n')
print()

print(df.loc[:, ['caseid', 'birthord']])

print("PrgLength dist", df.prglngth.value_counts().sort_index(), sep='\n')
print()

df['birthwgt_kg'] = df.birthwgt_lb * 0.45
print("Mean birthwgt kg:", df.birthwgt_kg.mean(), sep='\n')
print()

print("PrgLengths for case 2298", df.loc[df.caseid == 2298, 'prglngth'], sep='\n')
print()

print("PrgLengths for case 2298. another way", df[df.caseid == 2298].prglngth, sep='\n')
print()

print("Case id 5012 preg info", df.loc[df.caseid == 5012, ['birthord', 'outcome', 'birthwgt_lb']], sep='\n')
print()

# do first babies arrive late
# birthordr pivot, avg(preglength)
# use prglngth > 27 weeks, to discard outliers
print("Preg length dist by Birth order", pd.pivot_table(df[df.prglngth > 27], values=['prglngth'], index='birthord', aggfunc=(np.mean, len)), sep='\n')
print()


