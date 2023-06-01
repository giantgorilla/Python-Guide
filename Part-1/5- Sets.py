#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Unique Elements, Unordered - Her bir elemandan 1 tane olabilir.


# In[2]:


myList = [10, 20, 30, 10, 20, 40, 10, 20, 40]


# In[3]:


len(myList)


# In[4]:


myList


# In[5]:


mySet = set(myList)


# In[6]:


mySet


# In[7]:


mySet = {10, 20, 30, 10, 20, 40, 10, 20, 40}


# In[8]:


mySet


# In[9]:


mySet.add(10)


# In[10]:


mySet


# In[11]:


mySet.add(50)


# In[12]:


mySet


# In[13]:


mySet2 = {30, 40, 50, 60, 70}


# In[14]:


mySet


# In[15]:


mySet2


# In[16]:


mySet.union(mySet2) #Union = Birleştirmek için kullanılır.


# In[17]:


mySet.intersection(mySet2) #Intersection = Kesişim için kullanılır.


# In[23]:


countryList = ["de", "fr", "tr", "fr", "tr", "tr", "de", "nl", "de", "tr"]


# In[24]:


len(set(countryList))


# In[25]:


emptySet = set()


# In[26]:


type(emptySet)


# In[27]:


len(emptySet)


# In[29]:


emptySet.add(10)
emptySet.add(10)
emptySet.add(10)
emptySet.add(20)
emptySet.add(30)


# In[30]:


emptySet


# In[31]:


emptyList = list()


# In[32]:


emptyList.append(10)
emptyList.append(20)
emptyList.append(30)


# In[33]:


emptyList


# In[34]:


emptyDictionary = dict()


# In[35]:


emptyDictionary["a"] = 10
emptyDictionary["b"] = 20


# In[36]:


emptyDictionary


# In[ ]:




