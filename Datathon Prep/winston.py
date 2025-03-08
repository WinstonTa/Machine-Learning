"""Winston's Python File"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\08 Skillset\Programming\Machine-Learning\Datathon Prep\train.csv')
print(df.head())

# compare if all YearStart and all YearEnd values are the same
print((df['YearStart'] == df['YearEnd']).all())
