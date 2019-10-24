import matplotlib.pyplot as plt
import pandas as pd
#import pylab as pl
import numpy as np
#%matplotlib inline

df = pd.read_csv("FuelConsumption.csv")

# take a look at the dataset
df.head()
df.describe()