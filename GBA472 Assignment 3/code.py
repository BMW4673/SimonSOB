import pandas as pd
import numpy
import statsmodels.api as sm

# Load dataset from the local directory
df = pd.read_excel('GBA472 Assignment 3/Store24Data.xlsx')  # pandas uses read_excel for Excel files

# Format Table
df_clean = df.copy()

df_clean = df_clean.astype({
    'Store': int,  
    'Sales': float,
    'Profit': int,
    'MTenure': float,
    'Visibility': int,
    'PedCount': int,
    'Res': bool,
    'Hours24': bool
})
df_clean['Res'] = df_clean['Res'].apply(lambda x: 1 if x > 0 else 0)
df_clean['Hours24'] = df_clean['Hours24'].apply(lambda x: 1 if x > 0 else 0)

# Formatting for Display and Print
df_display = df_clean.copy()
df_display['Sales'] = df_display['Sales'].apply(lambda x: f"${x:,.2f}")
df_display['Profit'] = df_display['Profit'].apply(lambda x: f"${x:,.2f}")
#print(df_display.head())

# Question 1: Regression of Profit on all explantory variables
X = df_clean[['MTenure', 'CTenure', 'Visibility', 'PedCount', 'Res', 'Hours24']]
X = sm.add_constant(X)
y = df_clean['Profit']

model = sm.OLS(y, X).fit() 
print(model.summary())