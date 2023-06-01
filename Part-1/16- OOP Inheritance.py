#!/usr/bin/env python
# coding: utf-8

# # Inheritance - Kalıtım

# In[14]:


class Musician():
    
    def __init__(self, name):
        self.name = name
        print("Musician Class")
        
    def test1(self):
        print("Test 1")
        
    def test2(self):
        print("Test 2")


# In[15]:


dogukan = Musician("Dogukan")


# In[16]:


class MusicianPlus(Musician):
    
    def __init__(self, name):
        Musician.__init__(self, name)
        print("Musician Plus")
    


# In[18]:


atlas = MusicianPlus("Atlas")


# In[ ]:




