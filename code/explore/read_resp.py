import thinkstats2

dct = thinkstats2.ReadStataDct('E:\\scripts\\python\\thinkstat\\ThinkStats2\\code\\explore\\2002FemResp.dct')
df = dct.ReadFixedWidth('E:\\scripts\\python\\thinkstat\\ThinkStats2\\code\\explore\\2002FemResp.dat.gz', compression='gzip', nrows=None)

print(df.head(10))

print("Age dist", df.age_r.value_counts().sort_index(), sep='\n')
print()

print("Caseid 1 age", df[df.caseid == 1].age_r, sep='\n')
print()
