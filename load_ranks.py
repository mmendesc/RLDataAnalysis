import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
pylab.show()

df = pd.read_csv('ranks.csv', delimiter=",", usecols=[1,2,3,4,7,11], header=None,
    names=["playlist",'rank','division','rating','games','player'])

df = df.dropna(how='any')

print(df.shape)
print(df.iloc[4])