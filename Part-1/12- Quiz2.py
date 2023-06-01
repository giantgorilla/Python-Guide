#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1) Aşağıdaki kodun çıktısı ne olacaktır?


# In[1]:


x = 5
y = 3
z = 6


# In[3]:


x > y and z > x


# In[4]:


# 2) Aynı değerlerle kod şu şekilde değiştilirse çıktı ne olacaktır?


# In[4]:


x < y or z > y


# In[5]:


# cevap


# In[6]:


# 3) Aşağıdaki kodun çıktısı ne olacaktır?


# In[5]:



yas = 20

if yas < 18:
    print("18 yaşından küçüksünüz")
elif yas >= 18 and yas < 30:
    print("18 ile 30 yaş arasında bir gençsiniz")
elif yas >= 30 and yas < 40:
    print("30 ve 40 arasına gelmişsiniz")
else:
    print("40 yaşından daha büyüksünüz")


# In[9]:


#4) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız


# In[8]:


my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}


# In[16]:


if "c" in my_dictionary.values():
    print("evet")


# In[13]:


#5) Aşağıdaki sözlükte, anahtarlar içinde a harfinin geçip geçmediğini gösteren bir if koşulu yazınız


# In[17]:


my_other_dictionary = {"b":203,"c":"a","a":400,"d":"f"}


# In[19]:


if "a" in my_other_dictionary.keys():
    print("evet")


# In[17]:


#6) Aşağıdaki listedeki sayılardan sadece çift sayı olanları yazdıran bir kod yazınız.


# In[10]:


my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]


# In[15]:


for num in my_numbers:
    if num %2 == 0:
        print(num)


# In[22]:


#7) Aşağıdaki listedeki sayılar bir dairenin yarı çapını vermektedir. 


# In[23]:


#Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.


# In[22]:


r_list = [3,2,5,8,4,6,9,12]


# In[23]:


pi = 3.14


# In[25]:


cevreList = []

for r in r_list:
    cevreList.append(2 * r * pi)


# In[26]:


cevreList


# In[28]:


#8) Aşağıdaki listede isim - yaş eşleşmelerinin bulunduğu yapılar mevcuttur.


# In[29]:


# Sadece yaşların olduğu yeni ve ayrı bir liste oluşturunuz.


# In[28]:


age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]


# In[29]:


yas_listesi = []

for(isim, yas) in age_name_list:
    yas_listesi.append(yas)


# In[30]:


yas_listesi


# In[34]:


#9) Aşağıdaki müzik gruplarından birini rastgele yazdıran bir kod yazınız


# In[33]:


metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]


# In[34]:


from random import randint


# In[35]:


metal_list[randint(0, len(metal_list)-1)]


# In[39]:


#10) Aşağıdaki kodun çıktısı ne olacaktır?


# In[36]:


number_list = [5,7,18,21,20,10,405,24]


# In[37]:


[num % 2 == 0 for num in number_list]


# In[ ]:




