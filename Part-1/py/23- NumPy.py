#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#conda install numpy - NumPy'ı kurmak için kullanılır.


# In[2]:


import numpy as np #NumPy'ı import etmek için kullanılır.


# In[2]:


my_list = [10, 20, 30, 40]


# In[3]:


type(my_list)


# In[4]:


np.array(my_list)


# In[5]:


my_numpy_array = np.array(my_list)


# In[6]:


type(my_numpy_array)


# In[7]:


my_numpy_array


# In[8]:


my_numpy_array[0] #Index Etc


# In[9]:


my_numpy_array[-1]


# In[10]:


my_numpy_array[0] = 100 #Index Variable Changing


# In[11]:


my_numpy_array


# In[12]:


my_numpy_array.max() #Max Değer


# In[14]:


my_numpy_array.min() #Min Değer


# In[16]:


my_numpy_array.mean() #Ortalama Değer


# In[17]:


matrix_list = [[1,0,0], [0,1,0], [0,0,1], [0,0,0]]


# In[18]:


type(matrix_list)


# In[19]:


matrix_list[0][0]


# In[23]:


np.array(matrix_list)


# In[25]:


numpy_matrix_list = np.array(matrix_list)


# In[26]:


numpy_matrix_list.shape #Boyut Bilgisini Verir.


# In[27]:


#Arange


# In[28]:


range(0, 10)


# In[29]:


list(range(0,10))


# In[30]:


np.arange(0,10)


# In[31]:


np.arange(0, 30, 2) #0'dan 30'a kadar 2'şer 2'şer ilerler.


# In[33]:


np.zeros((3,4))


# In[34]:


np.ones((3,4))


# In[35]:


#Linspace


# In[36]:


np.linspace(0, 10, 5) #1. parametre = Start, 2. parametre = Stop 3. parametre= Index Values


# In[37]:


#Random


# In[40]:


np.random.randint(1, 10, 3) #1. parametre = Start, 2. parametre = Stop 3. parametre = Values - Counts


# # Numpy Arrays Methods

# In[41]:


my_numpy_list = np.arange(0,20)


# In[42]:


my_numpy_list


# In[43]:


my_numpy_list[4]


# In[44]:


my_numpy_list[4:9]


# In[45]:


my_numpy_list[4:9:2]


# In[46]:


my_list = list(range(0, 20))


# In[47]:


my_list[4:9:2]


# In[48]:


my_list[4:9] 


# In[53]:


#my_list[4:9] = -10


# In[ ]:


#List ile Numpy List arasındaki fark:


# In[54]:


my_numpy_list[4:9] = -10


# In[55]:


my_numpy_list


# # NumPy Operations with NumPy Arrays

# In[6]:


new_array = np.random.randint(1, 150, 25)


# In[7]:


new_array


# In[8]:


new_array > 50 #50'den büyük değerleri True olarak döndürür.


# In[9]:


result_array = new_array > 50


# In[10]:


result_array


# In[11]:


new_array[result_array] #True olan değerlerin sayısal değerlerini verir.


# In[13]:


last_array = np.arange(0, 30)


# In[14]:


last_array


# In[15]:


last_array + last_array


# In[16]:


last_array * last_array


# In[17]:


last_array - last_array


# In[18]:


last_array / last_array


# In[19]:


last_array.max()


# In[20]:


np.max(last_array)


# In[21]:


np.sqrt(last_array)


# In[ ]:




