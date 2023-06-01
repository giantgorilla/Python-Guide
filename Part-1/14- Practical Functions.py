#!/usr/bin/env python
# coding: utf-8

# In[1]:


def divideNumber(number):
    return number / 2


# In[2]:


divideNumber(15)


# In[3]:


myList = [10, 20, 30, 16, 18, 22, 39, 41, 57, 59]


# In[6]:


myResultList = []

for num in myList:
    myResultList.append(divideNumber(num))
print(myResultList)


# # Map Function

# In[8]:


list(map(divideNumber, myList))


# In[9]:


def controlString(string):
    return "Doğukan" in string


# In[10]:


controlString("Doğukan Bostancı")


# In[11]:


controlString("Bostancı")


# In[13]:


myStringList = ["Doğukan", "Doğukan Bostancı", "Bostancı"]


# In[14]:


list(map(controlString, myStringList))


# # Filter

# In[15]:


list(filter(controlString, myStringList))


# # Lambda

# In[22]:


multiplyLambda = lambda num : num * 3


# In[23]:


type(multiplyLambda)


# In[24]:


multiplyLambda(20)


# In[27]:


numList = [10, 20, 30, 40, 50]


# In[29]:


list(map(lambda num: num /4 ,numList))


# # Scope - Kapsam

# In[30]:


x = 20

def multiply(num):
    x = 5 
    return num * x


# In[31]:


multiply(10)


# In[2]:


x = 20

def multiply(num):
    return num * x


# In[3]:


multiply(10)


# # LEGB - L = Local, E = Enclosing, G = Global, B = Built- In

# In[16]:


#Global
myString = "Doğukan"

def myFunction():
    #Enclosing
    myString = "Doğukan 2"
    print(myString)
    
    def myFunction2():
        #Local
        myString = "Doğukan 3"
        print(myString)
        
    myFunction2()


# In[17]:


myString


# In[18]:


myFunction()


# In[19]:


myString


# In[20]:


def test1():
    myVariable = 10
    print(myVariable * 2)
    
def test2():
    print(myVariable * 3)


# In[21]:


test1()


# In[23]:


#test2()


# In[24]:


y = 10

def changeY():
    global y
    y = 5
    print(y)


# In[25]:


changeY()


# In[26]:


y


# In[ ]:




