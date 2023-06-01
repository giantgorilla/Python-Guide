#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x = 5
y = 2


# In[2]:


x > y


# In[3]:


x < y


# In[4]:


y < x


# In[5]:


y = 5


# In[6]:


x >= y


# In[7]:


x <= y 


# In[8]:


x = 10 
y = 8


# In[9]:


x == y


# In[10]:


x != y


# In[11]:


"""
> = Büyüktür
< = Küçüktür
>= Büyük Eşittir
<= Küçük Eşittir
== Eşittir
!= Eşit Değildir
"""


# In[12]:


2 > 1 and 3 > 2 #and olduğu için iki koşulunda doğru olması gerekir.


# In[13]:


2 > 1 or 3 < 2 #or olduğu için iki koşulunda doğru olmasına gerek yoktur.


# In[14]:


not 1 == 1


# In[15]:


10 in [10, 20, 30] #Listenin içerisinde 10 var mı ? 


# In[16]:


5 not in [10, 20, 30] #List


# In[17]:


5 in [10, 20, 30]


# In[18]:


10 in {10, 20, 30} #Set


# In[20]:


my_dictionary = {"a": 10, "b": 20, "c": 30}
10 in my_dictionary.values()


# In[21]:


10 in my_dictionary.values() #Dictionary


# In[23]:


"b" in my_dictionary


# In[24]:


10 in (10, 20, 30) #Tuple


# In[25]:


mySuperHero = "Batman"


# In[28]:


if mySuperHero == "Batman":
    print("My Super Hero is Batman")


# In[35]:


mySuperHero = input("Enter Your Super Hero: ")


# In[36]:


if mySuperHero == "Superman":
    print("Your Super Hero is Superman")

elif mySuperHero == "Batman":
    print("Wrong Super Hero")
    
else:
    print("Undefined")


# In[40]:


age = int(input("Enter Your Age: "))


# In[41]:


if age > 18:
    print("You are come of age")
elif age >= 18:
    print("You are come of age")
else:
    print("You are underage")


# In[44]:


mySuperHero = input("Enter Your Super Hero: ")


# In[45]:


mySuperHeroList = ["Spider Man", "Iron Man", "Thor", "Black Widow"]


# In[46]:


if mySuperHero in mySuperHeroList:
    print("Yes, he/she here!")
else:
    print("Sorry, he/she not here")


# In[ ]:




