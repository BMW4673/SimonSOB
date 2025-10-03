from scipy import stats
from scipy.stats import ttest_1samp
import pandas as pd
import math

#Import data
df=pd.read_excel('HomePrices.xlsx', engine='openpyxl')

print(df.head())

#Calculate moments of price
#1st Moment: Mean
mean_price = df['Price'].mean()

#2nd Moment: Variance
var_price = df['Price'].var()

std_price = df['Price'].std()

#3rd Moment: Skewness
skew_price = stats.skew(df['Price'])

#4th Moment: Kurtosis
kurt_price = stats.kurtosis(df['Price'])

#print Moments
print()
print("Moments of Statistics\n"
    f"- Mean: {mean_price:,.2f}\n",
    f"- Variance: {var_price:,.2f}\n",
    f"- Standard Deviation: {std_price:,.2f}\n",
    f"- Skewness: {skew_price:.4f}\n",
    f"- Kurtosis: {kurt_price:.4f}\n"
)

#A - Home Prices
# Ho is average house prices in this area are equal to or above $150,000
# Ha is average house prices in this are are below $150,000
# Significance level is 5% (how much doubt willing to accept)
# Calculate and explain p-value

#Convert Values
x_bar = mean_price
mu_0 = 150000
s = std_price
n = df['Price'].count()
alpha = 0.05

#T-statistic
t_stat = (x_bar - mu_0) / (s / math.sqrt(n))

#one-tailed p-value (greater than)
p_value = 1 - stats.t.cdf(t_stat, df=n-1)

#Interpreting
if p_value < (alpha):
    print(f"Reject H0 - the average is significantly greater than ${mu_0}\n")
else:
    print(f"Fail to reject H0 - the evidence isn't strong enough\n")

print(
    f"x_bar: {x_bar:,.2f}\n"
    f"mu_0: {mu_0}\n"
    f"s: {s:,.2f}\n"
    f"n: {n}\n"
    f"T-Statistic: {t_stat:,.4f}\n"
    f"p_Value: {p_value:,.10f}\n")
