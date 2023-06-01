#!/usr/bin/env python
# coding: utf-8

# # Method vs Function

# In[1]:


myName = "Doğukan"


# In[2]:


def hello():
    print("Hello")
    print("Python")


# In[3]:


hello()


# In[1]:


def hello_name(name):
    print("hello")
    print(name)


# In[6]:


hello_name("Doğukan")


# In[7]:


def sumExample(num1, num2):
    print(num1 + num2)


# In[8]:


sumExample(12, 14)


# In[1]:


def summation(n1, n2, n3):
    print(n1+n2+n3)


# In[2]:


summation(10, 23, 11)


# In[3]:


x = summation(10, 23, 11)


# In[4]:


x


# In[5]:


print(x)


# In[6]:


type(x)


# In[10]:


def returnSummation(n1, n2, n3):
    return n1+n2+n3 


# In[11]:


x = returnSummation(10, 23, 11)


# In[12]:


x


# In[13]:


def controlString(s):
    if s[0] == "a":
        print("A")


# In[14]:


controlString("atlas")


# In[15]:


controlString("James")


# # Args, Kwargs (Arguments, Key Word Arguments)

# In[16]:


def argsSum(*args):
    return sum(args)


# In[17]:


argsSum(10, 20, 30, 40, 50, 60)


# In[20]:


def argsExample(*args):
    print(args)


# In[21]:


argsExample(123, 12312310, 343, 123, 34)


# In[22]:


def kwargsExample(**kwargs):
    print(kwargs)


# In[23]:


kwargsExample(apple = 100, banana = 150, melon = 200)


# In[24]:


def kwargsExample2(**kwargs):
    if "apple" in kwargs:
        print("Apple")
    else:
        print("Wrong!")


# In[25]:


kwargsExample2(apple = 10, banana = 15)


# In[26]:


kwargsExample2(banana = 15)


# In[ ]:




