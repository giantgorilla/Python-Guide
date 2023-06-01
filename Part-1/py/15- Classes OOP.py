#!/usr/bin/env python
# coding: utf-8

# In[1]:


dogukanName = "Doğukan"


# In[3]:


dogukanAge = 21


# In[4]:


dogukanGender = "Male"


# In[5]:


atlasName = "Atlas"


# In[6]:


atlasAge = 14


# In[7]:


atlasGender = "Male"


# In[58]:


class Person():
    #Property
    #name = ""
    #age = 0
    #gender = ""
    
    #Initializer Method  
    def __init__(self, name, age, gender): #Initializer
        self.name = name
        self.age = age
        self.gender = gender
        
    #method
    def printName(self):
        print(self.name)


# In[59]:


dogukan = Person("Doğukan", 21, "Male")


# In[60]:


type(dogukan)


# In[61]:


dogukan.name


# In[62]:


dogukan.age


# In[63]:


dogukan.gender


# In[65]:


dogukan.printName()


# In[82]:


class Dog():
    
    year = 7
    
    def __init__(self, age):
    	self.age = age
        
    def humanAge(self):
        return self.age * self.year #Dog.year -> self.year   


# In[83]:


myDog = Dog(3)


# In[84]:


myDog.age


# In[85]:


myDog.humanAge()


# In[ ]:




