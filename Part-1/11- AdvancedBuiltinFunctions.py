#!/usr/bin/env python
# coding: utf-8

# In[1]:


myList = [10, 20, 30, 40, 50, 60, 70]


# In[3]:


for num in myList:
    print(num / 2)


# # Range

# In[5]:


range(50)


# In[6]:


list(range(10))


# In[7]:


for num in list (range(20)):
    print(num * 2)


# In[8]:


list(range(5, 25))


# In[9]:


list(range(5, 25, 2))


# In[10]:


myList = [20, 30, 40, 50, 60]


# In[11]:


for index in range(len(myList)):
    print(index)


# # Enumerate

# In[13]:


for element in enumerate(myList):
    print(element)


# In[15]:


for (index, value) in enumerate(myList):
    print(value)


# # Random

# In[16]:


from random import randint


# In[17]:


randint(0, 100)


# In[18]:


randint(0, 100)


# In[19]:


from random import shuffle #Shuffle = Karıştırmak


# In[20]:


shuffle(myList)


# In[21]:


myList


# In[22]:


myList = [10, 20, 30, 40, 50, 60, 70]


# In[23]:


randint(0, len(myList))


# In[24]:


myList[randint(0, len(myList))]


# # Zip

# In[25]:


foodList = ["apple", "banana", "melon"]
caloriesList = [100, 150, 200]
dayList = ["monday", "tuesday", "wednesday"]


# In[28]:


zippedList = list(zip(foodList, caloriesList, dayList))


# In[29]:


zippedList


# In[30]:


newList = []
myString = "Metallica"

for element in myString:
    newList.append(element)


# In[31]:


newList


# # List Comprehension

# In[32]:


newList = [element for element in myString]


# In[33]:


newList


# In[34]:


numberList = [10, 20, 30, 40, 50, 60]


# In[35]:


newNumberList = [num for num in numberList]


# In[36]:


newNumberList


# In[ ]:




