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

print('Average LN Per-Capita Income of Outlier "Non-Casino" Tribes: {0}'
        .format("%.3f" % casinoZeroOUT['pcinc_log']))

print('Average LN Per-Capita Income of Non-outlier "Non-Casino" Tribes: {0}'
        .format("%.3f" % casinoZeroIN['pcinc_log']))

print('Average LN Per-Capita Income of Outlier "Casino" Tribes: {0}'
        .format("%.3f" % casinoOneOUT['pcinc_log']))

print('Average LN Per-Capita Income of Non-Outlier "Casino" Tribes: {0}'
        .format("%.3f" % casinoOneIN['pcinc_log']))

