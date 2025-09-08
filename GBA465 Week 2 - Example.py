#!/usr/bin/env python
# coding: utf-8

# In[5]:


#-------------------------
#Starter File
#-------------------------

#Input the user's name
myName = input ("What is your name? ")

#Input the user's favorite ice cream flavor
myFavoriteIceCreamFlavor = input (myName + ", what is your favorite ice cream flavor? ")

#Input the user's preferred number of ice cream scoops
myPreferredNumberofScoops = input (myName + ", how many scoops of " + myFavoriteIceCreamFlavor + " do you prefer on your ice cream cone?")

#Convert myPreferredNumberofScoops from a string to an integer
myPreferredNumberofScoops = int(myPreferredNumberofScoops)

#Input the number of times the user eats ice cream for dessert in a week
numberofDessertsInAWeek = input(myName + ", how many times do you eat ice cream in a week? ")

#Convert numberofDessertsInAWeek from a string to an integer
numberofDessertsInAWeek = int(numberofDessertsInAWeek)

#Calculate the total number of ice cream scoops the user eats in a week
totalNumberofScoops = myPreferredNumberofScoops & numberofDessertsInAWeek

#Output the information to the screen
print( )
print (myName + ", your favorite dessert is " + str(myPreferredNumberofScoops) + " scoops of " + myFavoriteIceCreamFlavor + "ice cream one a cone.")
print ("In one week, you eat " + (totalNumberofScoops) + " scoops of " + myFavoriteIceCreamFlavor + " ice cream." )


# In[ ]:




