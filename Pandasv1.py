# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 09:08:19 2017

USes pandas package to display specific stock and plot it

@author: Ferhat
"""

from datetime import datetime    
import pandas_datareader as pdr
from datetime import datetime
import matplotlib.pyplot as plt


ibm = pdr.get_data_yahoo(symbols='IBM', start=datetime(2000, 1, 1), end=datetime(2012, 1, 1))
print(ibm['Adj Close'])
plt.plot(ibm['Adj Close'])