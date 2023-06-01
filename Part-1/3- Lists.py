#!/usr/bin/env python
# coding: utf-8

# In[2]:


myString = ("Hello Python")


# In[3]:


myString.split()


# In[4]:


type(myString.split())


# In[5]:


#Immutable - Immutability


# # List

# In[6]:


myList = [10, 20, 30]


# In[7]:


type(myList)


# In[12]:


x = 10 
y = 20 
z = 30


# In[13]:


myList = [x, y, z]


# In[14]:


myList


# In[15]:


myList = [10, 20, 30, 40, 50, 60, 70]


# In[16]:


myList[0]


# In[17]:


type(myList)


# In[18]:


type(myList[0])


# In[19]:


myList[0] = 100


# In[20]:


myList #Mutable - Mutability


# In[21]:


len(myList)


# In[22]:


myList.append(80) #Append = Listeye veri eklemek için kullanılır.


# In[23]:


myList


# In[24]:


myList.count(20)


# In[25]:


myList2 = [15, 25, 35, 45, 55, 65, 75]


# In[26]:


myList.extend(myList2) #Extend = İki listeyi birleştirmek için kullanılır.


# In[27]:


myList


# In[28]:


myList.insert(10, 4) #10.indexe 4 değerini yerleştirir.


# In[29]:


myList


# In[30]:


"""
Append ve Insert arasındaki fark: Append özelliğiyle birlikte eklemek istenilen
değer listenin sonuna eklenirken Insert özelliğiyle ilk parametre index değeri
ni, ikinci parametre ise belirtilen indexe hangi değerin ekleneceği yazılır.
"""


# In[31]:


myList.pop() #Pop = Son elemanı listeden çıkartır.


# In[32]:


myList


# In[33]:


myList.remove(4) #Remove = Belirtilen değeri listeden siler.


# In[34]:


myList


# In[35]:


myList.reverse() #Reverse = Listeyi tersine çevirir.


# In[36]:


myList


# In[37]:


myList.sort() #A'dan Z'ye ya da küçükten büyüğe sıralar.


# In[38]:


myList


# In[41]:


x = input("Enter X:") #Inputtan gelen her bilgi string olarak algılanır.


# In[42]:


y = input("Enter Y:")


# In[43]:


z = input("Enter Z:")


# In[51]:


inputList = []


# In[52]:


inputList


# In[53]:


inputList.append(x)
inputList.append(y)
inputList.append(z)


# In[54]:


inputList


# In[55]:


inputList[1] * 2 


# In[56]:


type(inputList[1])


# In[57]:


#Değer string olarak tutulduğu için matematiksel işlem gerçekleşmedi.


# In[58]:


myInteger = 50


# In[59]:


str(myInteger)


# In[61]:


myString = "40"


# In[62]:


int(myString)


# In[63]:


int(inputList[1]) * 2


# In[64]:


mixedList = ["Doğukan", 100, 3.14]


# In[65]:


type(mixedList)


# In[66]:


list1 = [10, 20, 30]
list2 = [40, 50, 60]


# In[67]:


list1 + list2


# In[68]:


list1 * 2 #List1'i 2 kez yazdırır.


# # Nested List - İç İçe Liste

# In[69]:


myNestedList = [10, 20, 3.14, "Doğukan", [1, 2, 3]]


# In[70]:


myNestedList[0]


# In[71]:


myNestedList[1]


# In[72]:


myNestedList[2]


# In[73]:


myNestedList[3]


# In[74]:


myNestedList[4]


# In[75]:


x = myNestedList[0]


# In[76]:


x


# In[77]:


list2 = myNestedList[4]


# In[78]:


list2


# In[79]:


myNestedList


# In[81]:


list2 


# In[82]:


myNestedList[4][1] #4.indexte olan iç içe listenin 1. indexini verir.


# In[83]:


lastList = ["a", "b", ["c", "d", "e"], "f"]


# In[84]:


len(lastList)


# In[85]:


lastList[2][1]


# In[ ]:




