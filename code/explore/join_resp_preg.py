import thinkstats2
import pandas as pd

dct_resp = thinkstats2.ReadStataDct('E:\\scripts\\python\\thinkstat\\ThinkStats2\\code\\explore\\2002FemResp.dct')
resp = dct_resp.ReadFixedWidth('E:\\scripts\\python\\thinkstat\\ThinkStats2\\code\\explore\\2002FemResp.dat.gz', compression='gzip', nrows=None)

dct_preg = thinkstats2.ReadStataDct('E:\\scripts\\python\\thinkstat\\ThinkStats2\\code\\explore\\2002FemPreg.dct')
preg = dct_preg.ReadFixedWidth('E:\\scripts\\python\\thinkstat\\ThinkStats2\\code\\explore\\2002FemPreg.dat.gz', compression='gzip', nrows=None)

join = pd.merge(resp, preg, on="caseid", suffixes=('_resp', '_preg'))

npreg = join[['caseid', 'pregnum_resp', 'pregnum_preg', 'pregordr', 'outcome']].sort_values(by=["caseid", "pregordr"])

print(npreg)
