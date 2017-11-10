import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
pylab.show()
df= pd.read_csv('stats.csv', delimiter=",", usecols=[1,2,3,4,5,6,7,11], header=None,
  names=['wins','goals','goal_ratio','saves','shots','assists','mvps','player'])
df = df.dropna(how='any')
# x = df['wins']
# y1 = df['mvps']
# y2 = df['goals']

# plt.plot(x,y1,'g-')
# plt.plot(x,y2,'b-')
# plt.show()

print(df.shape)
print(df)
