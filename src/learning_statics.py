import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sample_number = 1000

for i in range(3):
  sample = [np.random.randn(sample_number)]
  plt.subplot(2,2,i+1)
  plt.hist(sample,bins=10,range=(-5,5),histtype='bar')

plt.show()