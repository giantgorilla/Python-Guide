#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'test 1\ntest 2\ntest 3')


# In[2]:


myFile = open("myfile.txt")


# In[3]:


type(myFile)


# In[4]:


myFile.read()


# In[5]:


myFile.read()


# In[ ]:


myFile.seek(0) #Cursor'u en başa döndürmek için kullanılır. Manuel


# In[7]:


myFile.read()


# In[8]:


myFile.close()


# In[9]:


with open("myfile.txt") as myFile:
    myContent = myFile.read()


# In[10]:


myContent


# In[11]:


with open("myfile.txt", mode = "w") as myNewFile:
    myNewFile.write("test 4")


# In[12]:


with open("myfile.txt", mode = "r") as myFile2:
    myContent = myFile2.read()


# In[13]:


myContent


# In[ ]:


#w -> write, r -> read, a -> append

