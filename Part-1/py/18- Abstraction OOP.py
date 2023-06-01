#!/usr/bin/env python
# coding: utf-8

# # Abstraction - Soyutlama

# In[13]:


from abc import ABC, abstractmethod


# In[18]:


class Car(ABC):
    
    @abstractmethod
    def maxSpeed(self):
        pass


# In[19]:


#myCar = Car()


# In[22]:


class Tesla(Car):
    
    def maxSpeed(self):
        print("200 KM/H")


# In[23]:


tesla = Tesla()


# In[24]:


tesla.maxSpeed()


# In[25]:


class Mercedes(Car):
    
    def maxSpeed(self):
        print("250 KM/H")


# In[26]:


mercedes = Mercedes()


# In[27]:


mercedes.maxSpeed()


# # Özel Methodlar

# In[48]:


class Fruit():
    
    def __init__(self, name, calories):
        self.name =  name
        self.calories = calories
    
    def __str__(self):
        return f"{self.name}: {self.calories} calories"
    
    def __len__(self):
        return self.calories


# In[49]:


myFruit = Fruit("Banana", 150)


# In[50]:


myFruit.calories


# In[51]:


myFruit.name


# In[52]:


print(myFruit)


# In[53]:


len(myFruit)


# In[54]:


#https://www.informit.com/articles/article.aspx?p=453682&seqNum=6 - Özel Method

