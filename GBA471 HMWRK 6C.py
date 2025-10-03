from scipy.stats import t
import pandas as pd
import math

print(f"GBA 471 Homework 6 - Part 3\n")

#Import data
df=pd.read_excel('Salaries.xlsx', engine='openpyxl')

print(df.head())

#Calculate difference in sample mean of salaried by gender
mean_Male = df[df['Gender'] == 'male']['Salary'].mean()
mean_Female = df[df['Gender'] != 'male']['Salary'].mean()
difference = mean_Male - mean_Female

#Calculate the standard error (SE) and T-Statistic
std_male = df[df['Gender'] == 'male']['Salary'].std()
std_female = df[df['Gender'] == 'female']['Salary'].std()

n_male = df[df['Gender'] == 'male'].shape[0]    
n_female = df[df['Gender'] == 'female'].shape[0]

se = ((std_male**2)/n_male + (std_female**2)/n_female)**0.5

#Test statistic (shifed by 10,000)
t_stat = (difference - 10000) / se

#Calculate p-value
df_denom = (((std_male**2)/n_male + (std_female**2)/n_female)**2)
df_num = ((std_male**2)/n_male)**2 / (n_male - 1) + ((std_female**2)/n_female)**2 / (n_female - 1)
df_welch = df_denom / df_num

p_value = 1 - t.cdf(t_stat, df=df_welch)

print()
print(f'Difference of gender salary averages: {difference:.2f}\n'
      f'Standard Error: {se:.2f}\n'
      f'Degrees of freedom from Welch-Satterthwaite approximation: {df_welch:.2f}\n'
      f'Test statistic: {t_stat:,.2f}\n'
      f'P Value: {p_value:,.2f}\n')

if p_value > 0.05:
    print('p_value < 5% chance, thus reject the null - there is evidence women make more than $10k less.\n')
else:
    print('p_value >= 5% chance, thus fail to reject the null - there is not strong evidence women make more than $10k less.\n')
