import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as sm
import statsmodels.api as statm
import numpy as np

dat = pd.read_pickle('indian2000.df')

casinoZeroOUT = dat[(dat.pcinc_log > 9.575) & (dat.casino == 0)]
casinoZeroIN = dat[(dat.pcinc_log < 9.575) & (dat.casino == 0)]
casinoOneOUT = dat[(dat.pcinc_log > 9.575) & (dat.casino == 1)]
casinoOneIN = dat[(dat.pcinc_log < 9.575) & (dat.casino == 1)]

print('Number of Outlier "Non-Casino" Tribes: {0}'
	.format(casinoZeroOUT.shape[0]))

print('Number of Non-Outlier "Non-Casino" Tribes: {0}'
	.format(casinoZeroIN.shape[0]))

print('Number of Outlier "Casino" Tribes: {0}'
	.format(casinoOneOUT.shape[0]))

print('Number of Non-Outlier "Casino" Tribes: {0}'
	.format(casinoOneIN.shape[0]))
