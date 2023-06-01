#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1) Asagidaki string'in 5. harfini bir degiskene atayiniz


# In[3]:


my_string = "Python Ogreniyorum"


# In[78]:


x = my_string[4]


# In[79]:


x 


# In[5]:


# 2) Asagidaki String'in 5. ve 8. karakteri arasindaki tum harflerini yazdiriniz (5 ve 8 dahil)


# In[6]:


my_new_string = "ProgramlamayaMerhabaDedik"


# In[80]:


x = my_new_string[4:8]


# In[81]:


x


# In[9]:


# 3) Asagidaki String'i kod ile tersten yazin


# In[9]:


my_last_string = "Afyonkarahisarlilastiramadiklarimizdanmisiniz"


# In[18]:


len(my_last_string) - 1


# In[28]:


my_last_string[::-1]


# In[13]:


# 4) Asagidaki islemin sonucu hangi veri tipinde olacaktir?


# 4 + 12.2 + 48

# In[29]:


x = 4 + 12.2 + 48


# In[30]:


type(x)


# In[16]:


# 5) Asagidaki islemin sonucu kactir?


# 5 + 7 * 12

# In[31]:


x = 5 + 7 * 12


# In[32]:


x


# In[19]:


# 6) Bu listeyi en az 2 farkli yoldan olusturunuz: [1,3,"a"]


# In[43]:


my_list1 = [1, 3, "a"]


# In[44]:


my_list1.append(1)
my_list1.append(3)
my_list1.append("a")


# In[45]:


my_list


# In[46]:


# 7) Asagidaki "b"'yi tek satirda aliniz:


# In[47]:


my_list = [3.14,4,[2,3,"b"],True]


# In[49]:


my_list[2][2]


# In[26]:


#cevap


# In[27]:


#cevap


# In[28]:


# 8) Asagidaki "a"'yi tek satirda aliniz:


# In[54]:


my_dictionary = {"key1":20.25, "kk2":[40,{"k21":"a"}]}


# In[84]:


my_dictionary["kk2"][1]["k21"]


# In[52]:


#cevap


# In[32]:


# 9) Asagidaki liste set'e cevirilince hangi degerler icinde kalacaktir?


# In[66]:


my_list_to_be_set = [3,4,9,3,21,22,4,3,9,10,21,22]


# In[70]:


mySet = set(my_list_to_be_set)


# In[71]:


mySet


# In[36]:


# 10) Asagidaki ifadenin sonucu ne olacaktir?


# In[74]:


x = 30 * 5 + 3


# In[73]:


y = 108 - 2 * 4


# x > y

# In[75]:


x


# In[76]:


y


# In[77]:


x > y


# In[ ]:




