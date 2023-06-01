#!/usr/bin/env python
# coding: utf-8

# In[1]:


#for loop, while loop


# In[2]:


#for loop


# In[10]:


myList = [10, 20, 30, 40, 50, 60, 70]


# In[11]:


myList[0] / 5 * 2


# In[12]:


for number in myList:
    print(number / 5 * 2)


# In[14]:


print("For Loop Started")
for x in myList:
    new_number = x / 5 * 2
    print(new_number)
print("For Loop Ended")


# In[17]:


for number in myList:
    if number %6 == 0:
        print("The number is divided without a remainder..")
    else:
        print("The number does not divide without a remainder..")
        
        #Yazılı Printout


# In[18]:


for number in myList:
    if number %6 == 0:
        print(number)
        
        #Sayılı Printout


# In[20]:


numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[21]:


for number in numberList:
    if number %2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


# In[22]:


for number in numberList:
    if number %2 == 0:
        print(number)


# In[29]:


myTuple = (10, 20, 30, 40, 50, 60, 70)


# In[30]:


for number in myTuple:
    print(number / 5 * 2)


# In[31]:


myNewList = [("a", "b"), ("c", "d"), ("e", "f"), ("g", "h")]


# In[32]:


len(myNewList)


# In[33]:


myNewList[0]


# In[35]:


for element in myNewList:
    print(element)


# In[36]:


#Tuple Unpacking


# In[37]:


for (x, y) in myNewList:
    print(x)


# In[38]:


myTupleList = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]


# In[39]:


len(myTupleList)


# In[41]:


for (x, y, z) in myTupleList:
    print(x, y)


# In[42]:


mySet = {1, 2, 3, 4, 5}


# In[43]:


mySet


# In[44]:


len(mySet)


# In[45]:


for number in mySet:
    print(number)


# In[46]:


myDictionary = {"k1": 100, "k2": 200, "k3": 300}


# In[47]:


for element in myDictionary:
    print(element)


# In[48]:


myDictionary.items()


# In[49]:


for (key, value) in myDictionary.items():
    print(value)


# # Continue - Break - Pass

# In[50]:


myList = [10, 20, 30, 40, 50, 60, 70]


# In[51]:


print("For Loop Started")
for number in myList:
    print(number)
print("For Loop Ended")


# In[54]:


#40'ı bulunca duran kod bloğunu yazınız.

for number in myList:
    print(number)
    if number == 40:
        print("Yes!")
        break


# In[55]:


for number in myList:
    print(number)
    if number == 40:
        print("Yes!")
        continue


# In[56]:


for number in myList:
    pass


# # While 

# In[4]:


x = 0


# In[5]:


print("While Loop Started")
while x < 10:
    print(x)
    
    x = x + 1
    
print("While Loop Ended")


# In[8]:


lastList = [10, 20, 30, 40, 50]


# In[9]:


while 20 in lastList:
    print("20 in lastList")
    lastList.pop()


# In[14]:


p = 0
while p < 20:
    print(f"Value Of P: {p}")
    
    p += 1


# In[ ]:




