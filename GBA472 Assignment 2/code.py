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
    'Trailing1yrAvgMonthlyBDI': 'Unknown'
}
new_row = pd.DataFrame(
    [[bet_performer[col] for col in df.columns]],
    columns=df.columns
)
df = pd.concat([df, new_row], ignore_index=True)

# Find vessel closest to BET Performer by DWT (exclude BET Performer itself)
target_dwt = bet_performer['Deadweight_000_tons']
df_numeric = df.copy()
df_numeric = df_numeric[df_numeric['Vessel Name'] != 'BET Performer']
df_numeric['DWT_diff'] = (df_numeric['Deadweight_000_tons'] - target_dwt).abs()
closest = df_numeric.loc[df_numeric['DWT_diff'].idxmin()]

# --- Minimal Regression Block for Variation Explained ---
df_reg = df_numeric.copy()
df_reg = df_reg[(df_reg['Sale Price_USD_millions'] != 'Unknown') & (df_reg['Trailing1yrAvgMonthlyBDI'] != 'Unknown')]

df_reg = df_reg.astype({
    'Sale Price_USD_millions': float,
    'Deadweight_000_tons': float,
    'Age_at_Sale_years': float,
    'Trailing1yrAvgMonthlyBDI': float
})

X = df_reg[['Deadweight_000_tons', 'Age_at_Sale_years', 'Trailing1yrAvgMonthlyBDI']]
X = sm.add_constant(X)
y = df_reg['Sale Price_USD_millions']

model = sm.OLS(y, X).fit()
print("\nModel Fit Statistics:")
print(f"  R-squared: {model.rsquared:.4f}")
print(f"  Adjusted R-squared: {model.rsquared_adj:.4f}\n")
# --- End Regression Block ---

# --- Partial R² for each regressor ---
n = model.nobs
k = len(model.params) - 1  # number of predictors

print("Partial R² for each regressor:")
for var in model.params.index:
    if var == 'const':
        continue
    t = model.tvalues[var]
    partial_r2 = (t**2) / (t**2 + (n - k - 1))
    print(f"  {var}: {partial_r2:.4f}")

# --- End Partial R² ---

# --- Prediction and Intervals for BET Performer (only if BDI known) ---
import numpy as np
from scipy import stats

# Check if BET Performer has numeric BDI and Sale Price missing
bet = df[df['Vessel Name'] == 'BET Performer'].iloc[0]

try:
    dwt_bet = float(bet['Deadweight_000_tons'])
    age_bet = float(bet['Age_at_Sale_years'])
    bdi_bet = float(bet['Trailing1yrAvgMonthlyBDI'])

    X_new = pd.DataFrame({
        'const': [1],
        'Deadweight_000_tons': [dwt_bet],
        'Age_at_Sale_years': [age_bet],
        'Trailing1yrAvgMonthlyBDI': [bdi_bet]
    })

    pred = model.get_prediction(X_new)
    summary = pred.summary_frame(alpha=0.05)

    print("\n--- Prediction for BET Performer ---")
    print(f"Predicted Price: {summary['mean'].iloc[0]:.2f} million USD")
    print(f"95% CI for mean price: [{summary['mean_ci_lower'].iloc[0]:.2f}, {summary['mean_ci_upper'].iloc[0]:.2f}]")
    print(f"95% Prediction Interval: [{summary['obs_ci_lower'].iloc[0]:.2f}, {summary['obs_ci_upper'].iloc[0]:.2f}]")

except:
    print("\nBET Performer prediction skipped (BDI missing). Add numeric BDI to enable prediction.")
# --- End Prediction Block ---

# Format dataset
# - Sale Date as month-year (e.g., Jan-07)
df['Sale Date'] = pd.to_datetime(df['Sale Date'], format='%b-%y', errors='coerce').dt.strftime('%b-%y')

# - Sale Price as USD millions with currency marker
def format_price(v):
    try:
        return f"${float(v):,.1f}M"
    except (TypeError, ValueError):
        return "Unknown"
df['Sale Price_USD_millions'] = df['Sale Price_USD_millions'].apply(format_price)

# - Deadweight as thousand tons with a unit suffix
def format_dwt(v):
    try:
        return f"{float(v):,.1f}k tons"
    except (TypeError, ValueError):
        return "Unknown"
df['Deadweight_000_tons'] = df['Deadweight_000_tons'].apply(format_dwt)

# - Capesize index (Trailing1yrAvgMonthlyBDI) with thousands separator
def format_bdi(v):
    try:
        return f"{int(v):,}"
    except (TypeError, ValueError):
        return "Unknown"
df['Trailing1yrAvgMonthlyBDI'] = df['Trailing1yrAvgMonthlyBDI'].apply(format_bdi)

# Report closest vessel details after headers, spaced from other content
closest_formatted = df[df['Vessel Name'] == closest['Vessel Name']].iloc[0]
print("\nClosest vessel by DWT to BET Performer:")
print(
    f"  Name: {closest_formatted['Vessel Name']}\n"
    f"  Tonnage: {closest_formatted['Deadweight_000_tons']}\n"
    f"  Build Year: {closest_formatted['Year Built']}\n"
    f"  Sale Amount: {closest_formatted['Sale Price_USD_millions']}\n"
)

# Save a formatted copy next to the source file
df.to_csv('data_formatted.csv', index=False)

# Preview formatted data
#print(df.head())
