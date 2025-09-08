#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scipy.stats import norm

mu = 0.08 #mean return
sigma = 0.20 #STD DEV
investment = 100000


# In[4]:


# A. Probability of a positive return
p_positive = 1-norm.cdf(0,mu, sigma)
print("A. P(Profit > 0%) =", round(p_positive, 4))


# In[6]:


# B. Probability between -12% and 28%
p_between = norm.cdf(0.28, mu, sigma) - norm.cdf(-0.12, mu, sigma)
print("B. P(-12% , Return < 28%) = ", round(p_between, 4))


# In[12]:


# C. Probability of >48% return
p_above_48 = 1-norm.cdf(0.48, mu, sigma)
print("C. P(Return > 48%) =", round(p_above_48,4))


# In[32]:


# D. Value at Risk at 2%
z_2 = norm.ppf(0.02, mu, sigma)
VaR_2 = investment * -z_2
print("D. 2% VaR =", round(VaR_2, 2), "USD")


# In[26]:


# E. Required mean if 2% VaR = $10,000
#We want norm.ppf(0.01, mu, sigma) = -0.10
from scipy.optimize import fsolve

def solve_mu(mu):
    return norm.ppf(0.02, mu, sigma) + 0.10

mu_needed = fsolve(solve_mu, 0.08)[0]
print("E. Required Mean Return =", round(mu_needed), 4)


# In[ ]:




