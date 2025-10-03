from scipy import stats
from scipy.stats import ttest_1samp
import pandas as pd
import math

print(f"GBA 471 Homework 6 - A\n")

#Import data
df=pd.read_excel('HomePrices.xlsx', engine='openpyxl')

print(df.head())

#Calculate moments of price
#1st Moment: Mean
#2nd Moment: Variance
#3rd Moment: Skewness
#4th Moment: Kurtosis
mean_price = df['Price'].mean()
var_price = df['Price'].var()
std_price = df['Price'].std()
skew_price = stats.skew(df['Price'])
kurt_price = stats.kurtosis(df['Price'])

#print Moments
print()
print("Price - Moments of Statistics\n"
    f"- Mean: {mean_price:,.2f}\n",
    f"- Variance: {var_price:,.2f}\n",
    f"- Standard Deviation: {std_price:,.2f}\n",
    f"- Skewness: {skew_price:.4f}\n",
    f"- Kurtosis: {kurt_price:.4f}\n"
)

#A - Home Prices
print("Null is average house prices in this area are at most $150,000\n")
print("Alternative is average house prices in this are above $150,000\n")
# Significance level is 5% (how much doubt willing to accept)
# Calculate and explain p-value

#Convert Values
x_bar_price = mean_price
mu_0_price = 150000
s_price = std_price
n_price = df['Price'].count()
alpha_price = 0.05

#T-statistic
t_stat_price = (x_bar_price - mu_0_price) / (s_price / math.sqrt(n_price))

#one-tailed p-value (greater than)
p_value_price = 1 - stats.t.cdf(t_stat_price, df=n_price-1)

#Interpreting
if p_value_price < (alpha_price):
    print(f"Reject H0 - the average is significantly greater than ${mu_0_price}\n")
else:
    print(f"Fail to reject H0 - the evidence isn't strong enough\n")

print(
    f"x_bar: {x_bar_price:.2f}\n"
    f"mu_0: {mu_0_price}\n"
    f"s: {s_price:.2f}\n"
    f"n: {n_price}\n"
    f"T-Statistic: {t_stat_price:.4f}\n"
    f"p_Value: {p_value_price:.4f}\n")

##########################################

print("GBA471 Homework 6 - B\n")

#Calculate moments of price
#1st Moment: Mean
mean_sqft = df['Living Area'].mean()

#2nd Moment: Variance
var_sqft = df['Living Area'].var()

std_sqft = df['Living Area'].std()

#3rd Moment: Skewness
skew_sqft = stats.skew(df['Living Area'])

#4th Moment: Kurtosis
kurt_sqft = stats.kurtosis(df['Living Area'])

#print Moments
print()
print("Living Area - Moments of Statistics\n"
    f"- Mean: {mean_sqft:,.2f}\n",
    f"- Variance: {var_sqft:,.2f}\n",
    f"- Standard Deviation: {std_sqft:,.2f}\n",
    f"- Skewness: {skew_sqft:.4f}\n",
    f"- Kurtosis: {kurt_sqft:.4f}\n"
)

#B - Living Area
print("Null is average house living area in this area are at most 1800 sqft\n")
print("Alternative is average house living area in this are above 1800 sqft\n")
# Significance level is 5% (how much doubt willing to accept)
# Calculate and explain p-value

#Convert Values
x_bar_sqft = mean_sqft
mu_0_sqft = 1800
s_sqft = std_sqft
n_sqft = df['Living Area'].count()
alpha_sqft = 0.05

#T-statistic
t_stat_sqft = (x_bar_sqft - mu_0_sqft) / (s_sqft / math.sqrt(n_sqft))

#one-tailed p-value (greater than)
p_value_sqft = 1 - stats.t.cdf(t_stat_sqft, df=n_sqft-1)

#Interpreting
if p_value_sqft < (alpha_sqft):
    print(f"Reject H0 - the average is significantly greater than {mu_0_sqft}\n")
else:
    print(f"Fail to reject H0 - the evidence isn't strong enough\n")

print(
    f"x_bar: {x_bar_sqft:,.2f}\n"
    f"mu_0: {mu_0_sqft}\n"
    f"s: {s_sqft:,.2f}\n"
    f"n: {n_sqft}\n"
    f"T-Statistic: {t_stat_sqft:,.4f}\n"
    f"p_Value: {p_value_sqft:,.10f}\n")