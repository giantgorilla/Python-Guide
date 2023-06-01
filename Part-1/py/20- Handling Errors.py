#!/usr/bin/env python
# coding: utf-8

# # Try - Except

# In[1]:


while True:
    
    try:
        myAge = int(input("Enter Your Age: "))
        break
    except ValueError: 
        print("Enter Your Age!:")
    else: 
        print("Else Executed")
    finally:
        print("Finally")

