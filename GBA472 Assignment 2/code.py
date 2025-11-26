import pandas as pd
import statsmodels.api as sm

# Load dataset from the local directory
df = pd.read_csv('data.csv')

# Add BET Performer with unknown sale price and BDI
bet_performer = {
    'Sale Date': 'Jan-08',  # 1997 build with 11-year age implies 2008 sale year
    'Vessel Name': 'BET Performer',
    'Sale Price_USD_millions': 'Unknown',
    'Year Built': 1997,
    'Age_at_Sale_years': 11,
    'Deadweight_000_tons': 172.0,  # 172,000 DWT expressed in thousand tons
    'Trailing1yrAvgMonthlyBDI': None
}
new_row = pd.DataFrame(
    [[bet_performer[col] for col in df.columns]],
    columns=df.columns
)
df = pd.concat([df, new_row], ignore_index=True)

# ---------------------------------------------------------
# Minimal regression and prediction workflow
# ---------------------------------------------------------

# Convert necessary columns to numeric
df_clean = df.copy()
df_clean = df_clean[df_clean['Sale Price_USD_millions'] != 'Unknown']
df_clean = df_clean.astype({
    'Sale Price_USD_millions': float,
    'Deadweight_000_tons': float,
    'Age_at_Sale_years': float,
    'Trailing1yrAvgMonthlyBDI': float
})

# Build regression
X = df_clean[['Deadweight_000_tons', 'Age_at_Sale_years', 'Trailing1yrAvgMonthlyBDI']]
X = sm.add_constant(X)
y = df_clean['Sale Price_USD_millions']

# (c) Model fit: how well the three factors jointly explain ship prices
model = sm.OLS(y, X).fit()
print("\n=== MODEL SUMMARY (MINIMAL) ===")
print(model.summary())

# ---------------------------------------------------------
# BET Performer prediction (BDI hardcoded from table)
# ---------------------------------------------------------

dwt_bet = 172.0
age_bet = 11
bdi_bet = 10526   # From Jan-08 table

X_new = pd.DataFrame({
    'const': [1],
    'Deadweight_000_tons': [dwt_bet],
    'Age_at_Sale_years': [age_bet],
    'Trailing1yrAvgMonthlyBDI': [bdi_bet]
})

# (d) Predicted price for BET Performer + 95% CI and 95% PI
pred = model.get_prediction(X_new).summary_frame(alpha=0.05)

print("\n=== BET PERFORMER PREDICTION ===")
print(pred)

# ---------------------------------------------------------
# Scenario analysis (point predictions only)
# ---------------------------------------------------------

# (e) Scenario analysis: age change, DWT change, and BDI change (point predictions only)
# 1. Age = 6
X_age6 = X_new.copy()
X_age6['Age_at_Sale_years'] = 6
price_age6 = model.predict(X_age6)[0]

# 2. DWT = 152
X_dwt152 = X_new.copy()
X_dwt152['Deadweight_000_tons'] = 152.0
price_dwt152 = model.predict(X_dwt152)[0]

# 3. BDI = 30% lower
X_bdi_low = X_new.copy()
X_bdi_low['Trailing1yrAvgMonthlyBDI'] = bdi_bet * 0.70
price_bdi_low = model.predict(X_bdi_low)[0]

print("\n=== SCENARIO ANALYSIS (POINT PREDICTIONS) ===")
print(f"If 5 years younger (age 6): {price_age6:.2f}M")
print(f"If 20k DWT smaller (152k): {price_dwt152:.2f}M")
print(f"If BDI 30% lower: {price_bdi_low:.2f}M")
