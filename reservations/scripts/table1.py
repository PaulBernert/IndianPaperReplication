import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as sm
import statsmodels.api as statm
import numpy as np

dat = pd.read_pickle('indian2000.df')

our_data = {'above':dat[dat['pcinc_log'] >= 9.575],
            'below':dat[dat['pcinc_log'] < 9.575],}

fig = plt.figure()
plt.title('LN Per-Capita Income vs Casino Binary Variable')
plt.scatter(our_data['above']['casino'],our_data['above']['pcinc_log'], color='red')
plt.scatter(our_data['below']['casino'],our_data['below']['pcinc_log'], color='blue')
plt.axhline(y=9.575,linewidth=1, ls='dashed', color='grey')
plt.ylabel('LN PCINC')
txt = '''
    LN Average Per-Capita Income for 'Casino Tribes': {0}
    LN Average Per-Capita Income for 'Non-Casino Tribes': {1}'''.format("%.3f" % dat[dat.casino == 0].pcinc_log.mean(),"%.3f" % dat[dat.casino==1].pcinc_log.mean())
fig.text(0.10,0.00,txt)
plt.xlim((-1.00,2.00))
plt.show()
