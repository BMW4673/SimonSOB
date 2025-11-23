import pandas as pd
import statsmodels.api as sm

# Load dataset
df = pd.read_csv('GBA472 Assignment 2/data.csv')

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

# Save a formatted copy
df.to_csv('GBA472 Assignment 2/data_formatted.csv', index=False)

# Preview formatted data
#print(df.head())
