#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[2]:


name = "Doğukan"


# In[3]:


type(name)


# In[7]:


print("Hello" +name)


# In[ ]:


#İlk örnekte görüldüğü gibi arada boşluk yok. Boşluk koymak için;


# In[8]:


print("Hello", "" +name) #Ekstra bir string oluşturulur lâkin boş bırakılır.


# In[9]:


"""
name. yazıp tab tuşuna basarak gerçekleştirilebilecek işlemleri görebilirsiniz.
Daha önce yukarıda tanımlanmış olan bir değeri print fonksiyonuna +degisken
yazarak printout alabilirsiniz.
"""


# In[10]:


name.capitalize() #Değişkenin ilk harfini büyük yapar. 


# In[11]:


help(name.count) #Count hakkında bilgi verir. 


# In[12]:


name.count("a") #Name değişkeni içerisinde kaç adet a harfi olduğunu sayar.


# In[13]:


name.count("b") #Name değişkeni içerisinde kaç adet b harfi olduğunu sayar.


# In[14]:


name.upper() #Name değişkeninin tüm harflerini büyük harf yapar.


# In[15]:


len(name) #lenght = değişkenin uzunluğunu, karakter sayısını verir.


# In[16]:


print("Hello \n" +name) # \n -> New Line = Alt satıra geç anlamına gelir.


# In[37]:


name = "Doğukan"


# In[38]:


surname = "Bostancı"


# In[39]:


fullName = name + " " + surname


# In[40]:


fullName


# # Index

# In[17]:


myString = "Doğukan Bostancı"


# In[18]:


myString[4] #Index değeri '0'dan başlar ve her karakter (boşluk dahil) sayılır.


# In[19]:


len(myString)


# In[20]:


len(myString) - 1 #Son değeri verir.


# In[21]:


myName = "James Hetfield"


# In[22]:


len(myName) - 1 


# In[23]:


myName[13]


# In[33]:


myName[-1] #Indexi tersten döndürmeye başlar.


# In[34]:


barcode = "ABCDE123123982"


# In[41]:


barcode[0] + barcode[1] + barcode[2]


# In[ ]:


#Slicing, starting index, stopping index, stepping size


# In[42]:


barcode[0:3:1] 


# In[43]:


barcode[3::]


# In[44]:


barcode[::-1]


# In[48]:


myString.index("k")


# In[49]:


myString.split()


# In[ ]:




