#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Input the diameter of a circle that is positive and a non-zero integer without error correction
diameter = input ("Please input the diameter of a circle in inches: ")

#Convert diameter to integer
diameter = int(diameter)

#Calculate circumference with pi defined as a variable
pi=3.14159
circumference = diameter * pi 

print("")
print("The circumference of the circle is ", round(circumference,2), " inches.")

#End of Script

