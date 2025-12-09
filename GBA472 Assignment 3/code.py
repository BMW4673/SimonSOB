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


# Formatting for Display
df_display = df_clean.copy()
df_display['Sales'] = df_display['Sales'].apply(lambda x: f"${x:,.2f}")
df_display['Profit'] = df_display['Profit'].apply(lambda x: f"${x:,.2f}")


print(df_display.head())
