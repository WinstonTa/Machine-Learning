"""Mindy's Python File"""
# Import the modules, read the dataset and create a Pandas DataFrame.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mall_df = pd.read_csv("https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/Mall_Customers.csv")

# Print the first five records
mall_df.head()