#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Input the diameter of a circle that is positive and a non-zero integer without error correction
diameter = int(input ("Please input the diameter of a circle in inches: "))

#Calculate circumference with pi defined as a variable
pi=3.14159
circumference = diameter * pi 
circumference = round(circumference,2)
print("")
print("The circumference of the circle is ", str(circumference), " inches.")

#End of Script

