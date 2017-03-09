import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as sm
import numpy as np

dat = pd.read_csv('Indian2000Data.csv', index_col=0)

dat['pcinc_log'] = np.log(dat['pcinc'])
dat['pcinc_co_log'] = np.log(dat['pcinc_co'])

dat['unempl_co_log'] = np.log(dat['unempl_co'])

dat['pop'] = np.exp(dat['logpop'])

dat.to_pickle('indian2000.df')
