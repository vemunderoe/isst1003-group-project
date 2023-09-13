import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
x = df.iloc[:, 0]
y = df.iloc[:, 1]

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line = slope * x + intercept

plt.plot(x, y, 'o', x, line)
plt.show()