import pandas as pd
import statsmodels.formula.api as sm
import numpy as np 

dat = pd.read_pickle('indian2000.df')

res = sm.ols(formula='pcinc_log ~ FC + HC + pcinc_co_log + unempl_co_log + logdist + logruggedness + logresarea_sqkm + ea_v5 + ea_v30 + ea_v32 + ea_v66 + logpop + popadultshare + casino', data=dat).fit()

print(res.summary())
