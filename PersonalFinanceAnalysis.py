#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


# In[2]:


# paths
ROOT = Path.cwd()
DATA_DIR = ROOT / "data"
CONFIG_DIR = ROOT / "config"
REPORTS_DIR = ROOT / "reports"

#validate folders
for d in [DATA_DIR, CONFIG_DIR, REPORTS_DIR]:
    d.mkdir(exist_ok=True, parents=True)

#nicer pandas number formattingNot
pd.options.display.float_format = '{:,.2f}'.format

#point to data folder
DATA_DIR = Path.cwd() / "data"

#file handling
raw_path = Path.cwd() / "data" / "transactions.csv"
raw =  pd.read_csv(raw_path)

#list everything inside
for f in DATA_DIR.glob ("*"):
    print (f.name)

#list folders
print ("setup complete")
print ("data folder:", DATA_DIR)


# In[12]:


#test file
df_preview = pd.read_csv(DATA_DIR / "Transactions.csv")
df_preview.head()


# #rename columns to lower case
# df = raw.rename(columns={
#     'Date': 'date',
#     'Amount': 'amount',
#     'Card': 'card',
#     'Category': 'category',
#     'Description': 'description'
# })
# 
# #convert data types
# df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date
# df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# In[15]:


#define amount variable
amount = df['amount']

print(f"rows: {len(df):,}")

#Moments
print("Moments")
print("step 1 - ", f"mean: {amount.mean():.2f}")
print("step 2 - ", f"variance: {amount.var(ddof=1):.2f}") #sample variance
print("step 3 - ", f"skewness: {stats.skew(amount):.2f}") # >0 means right skew
print("step 4 - ", f"kurtosis: {stats.kurtosis(amount, fisher=True):.2f}") # 0 ~ normal, >0 heavy tails


# In[ ]:





# In[ ]:





# In[ ]:




