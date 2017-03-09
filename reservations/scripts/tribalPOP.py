import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as sm
import statsmodels.api as statm
import numpy as np

dat = pd.read_pickle('indian2000.df')

casinoZeroOUT = dat[(dat.pcinc_log > 9.575) & (dat.casino == 0)].mean()
casinoZeroIN = dat[(dat.pcinc_log < 9.575) & (dat.casino == 0)].mean()
casinoOneOUT = dat[(dat.pcinc_log > 9.575) & (dat.casino == 1)].mean()
casinoOneIN = dat[(dat.pcinc_log < 9.575) & (dat.casino == 1)].mean()

print('Average Population of Outlier "Non-Casino" Tribes: {0}'
        .format("%.0f" % casinoZeroOUT['pop']))

print('Average Population of Non-outlier "Non-Casino" Tribes: {0}'
	.format("%.0f" % casinoZeroIN['pop']))

print('Average Population of Outlier "Casino" Tribes: {0}'
	.format("%.0f" % casinoOneOUT['pop']))

print('Average Population of Non-Outlier "Casino" Tribes: {0}'
        .format("%.0f" % casinoOneIN['pop']))
