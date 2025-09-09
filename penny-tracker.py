#!/usr/bin/env python
# coding: utf-8

# In[111]:


#Penny Tracker

#Define initial variables
myName = input("Please enter your name")
numPenniesInBank = 200000

#Output
print((myName)+"'s", "Bank Account: ",(numPenniesInBank),"pennies")

#Data Analyst Average Salary
salaryInDollars = 124800

#Calculate hourly rate in pennies
hourlyRateInPennies = round(salaryInDollars * 100,2)

#Output
print((myName)+"'s", "Salary: ",(hourlyRateInPennies), "pennies per hour")

#Hard Work
numHoursWorked = 8

#Calculate hourly rate per day in pennies
numPenniesEarned = hourlyRateInPennies * numHoursWorked

#Add to Bank Account
numPenniesEarned = numPenniesEarned + numPenniesInBank

#Output
print("Pennies Earned Today: ",numPenniesEarned)
print((myName)+"'s", "Bank Account: ", (numPenniesInBank))


# In[ ]:




