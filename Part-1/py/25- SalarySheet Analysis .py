#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 


# In[2]:


import pandas as pd 


# In[3]:


data = pd.read_excel("SalarySheet.xlsx")


# In[4]:


data.shape #Data has how much row and columns 


# In[5]:


data.describe() #Mathematics Operations


# In[11]:


mean_salary = data["Salary"].mean()


# In[12]:


mean_salary


# In[13]:


department_group = data.groupby("Department")


# In[14]:


department_group.mean()


# In[16]:


title_group = data.groupby("Title")


# In[18]:


title_group.mean()


# In[22]:


data.loc[data["Department"] == "Software Development"].groupby("Title").mean()


# In[23]:


data.loc[data["Department"] == "Finance"].groupby("Title").mean()


# In[24]:


data.loc[data["Department"] == "Software Development"].groupby("Title").describe()


# In[25]:


data.loc[data["Department"] == "Marketing"].groupby("Title").describe()


# In[ ]:




