#!/usr/bin/env python
# coding: utf-8

# # Polymorphism

# In[1]:


class Banana():
    
    def __init__(self, name):
        self.name = name
        
    def info(self):
        return f"100 calories {self.name}"
    
class Apple():
    
    def __init__(self, name):
        self.name = name
        
    def info(self):
        return f"150 calories {self.name}"


# In[2]:


banana = Banana("banana")


# In[3]:


apple = Apple("Apple")


# In[4]:


banana.info()


# In[5]:


apple.info()


# In[6]:


fruitList = [banana, apple]


# In[7]:


for fruit in fruitList:
    print(fruit.info())


# In[ ]:




