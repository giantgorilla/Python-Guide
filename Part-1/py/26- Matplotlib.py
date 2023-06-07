#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


age_list = [20, 25, 30, 35, 40, 45, 50, 55, 60]


# In[11]:


weight_list = [70, 75, 73, 85, 89, 90, 75, 84, 90]


# In[12]:


age_list_numpy = np.array(age_list)
weight_list_numpy = np.array(weight_list)


# In[13]:


age_list_numpy


# In[14]:


weight_list_numpy


# In[26]:


plt.plot(age_list_numpy, weight_list_numpy, "g") #Neyi çizdireceğimiz parametre olarak verilir.
plt.xlabel("Age")
plt.ylabel("Weight")
plt.show()


# In[27]:


np_list = np.linspace(0, 15, 20)


# In[28]:


np_list


# In[29]:


np_list2 = np_list ** 3


# In[30]:


np_list2


# In[34]:


plt.plot(np_list, np_list2, "y--")


# In[35]:


plt.subplot(1, 2, 1) #1 row, 2columns 1.graph
plt.plot(np_list, np_list2, "r--")

plt.subplot(1,2,2)
plt.plot(np_list2, np_list, "g*")


# In[51]:


fig = plt.figure()
axes = fig.add_axes([1, 1, 0.6, 0.6])
axes.plot(np_list, np_list2)
axes.set_xlabel("X Data")
axes.set_ylabel("Y Data")
axes.set_title("X-Y Data")


# In[57]:


fig2 = plt.figure()

axes2 = fig2.add_axes([0.1, 0.1, 0.9, 0.9])
axes2.plot(np_list, np_list2)
axes2.set_xlabel("X Data Small")
axes2.set_ylabel("Y Data Small")
axes2.set_title("Small Graph")

fig3 = plt.figure()

axes3 = fig2.add_axes([0.3, 0.4, 0.3, 0.3])
axes3.plot(np_list, np_list2)
axes3.set_xlabel("X Data Large")
axes3.set_ylabel("Y Data Large")
axes3.set_title("Large Graph")


# In[62]:


(fig, axes) = plt.subplots()
np_list3 = np.linspace(0, 15, 20)
np_list4 = np_list3 + 3
axes.plot(np_list3, np_list4)
axes.plot(np_list4, np_list3)


# In[65]:


(fig, axes) = plt.subplots()
axes.plot(np_list3, np_list3 + 2, color = "r", linewidth = 2.4)
axes.plot(np_list3, np_list3 + 3, color = "g", linewidth = 1.4)
axes.plot(np_list3, np_list3 + 4, color = "b", linewidth = 3.4, linestyle = "--")


# In[68]:


fig.savefig("myfig.png", dpi = 200)


# # Histogram

# In[66]:


n_numpy = np.random.randint(0, 100, 40)


# In[67]:


plt.hist(n_numpy)


# In[ ]:




