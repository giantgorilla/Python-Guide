#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Key - Value Pairing 


# In[2]:


fruits = ["banana", "apple"]


# In[3]:


calories = [100, 150]


# In[4]:


fruits[0]


# In[5]:


calories[0]


# In[11]:


fitnessDictionary = {"banana": 100,
                     "apple": 150}


# In[12]:


type(fitnessDictionary)


# In[13]:


#Dictionary key value olduğu için index yoktur.


# In[14]:


fitnessDictionary["banana"]


# In[15]:


fitnessDictionary["apple"]


# In[16]:


fitnessDictionary.keys() #Sadece anahtarları verir.


# In[17]:


fitnessDictionary.values() #Sadece değerleri verir.


# In[24]:


list(fitnessDictionary.values())


# In[27]:


fitnessDictionary["banana"] = 200


# In[28]:


fitnessDictionary


# In[29]:


fitnessDictionary["melon"] = 300


# In[30]:


fitnessDictionary


# In[34]:


fitnessDictionary.get("apple", 0)


# In[37]:


myDictionary = {100: "a", 200: "b", 300: "c"}


# In[38]:


myDictionary[100]


# In[39]:


myDictionary = {"key1": "value1", "key2": "value2", "key3": "value3"}


# In[40]:


myDictionary["key1"]


# In[41]:


myMixedDictionary = {"key1": 100, "key2": 3.14, "key3": [10, 20, 30]}


# In[42]:


myMixedDictionary["key3"]


# In[45]:


lastDictionary = {"k1": 10, "k2": [10, 20, 30, 40, 50], "k3": "string", "k4": {"a": 100, "b": 200}}


# In[48]:


lastDictionary["k2"][2]


# In[49]:


lastDictionary["k4"]["b"]


# In[ ]:




