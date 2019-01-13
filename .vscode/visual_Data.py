# This file is to visualize the price data, daily return data and the distribution of daily return data
# Before we use data in machine learning, we need to check the data at first.

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/sp500-new.csv")

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=False, sharey=False)
ax1.plot(dataframe["Close"])
ax1.set_title('Price Data')
ax2.plot(dataframe["Return"])
ax2.set_title('Daily Return Data')
ax3.hist(dataframe["Return"], 200, density=True, facecolor='g', alpha=0.75)
ax3.set_title("The distribution of Daily Return")
f.suptitle('Visualize Price and Return Data')
plt.show()