#!/usr/bin/env python
# coding: utf-8

# In[42]:


#1) Aşağıdaki kodun çıktısı ne olacaktır?


# In[43]:


def toplama(a,b):
    print(a,b)


# In[44]:


x = toplama(3,4)
print(x)


# In[5]:


#2) Aşağıdaki kodun çıktısı ne olacaktır?


# In[6]:


def usselIslem(x=5,y=3):
    print(x ** y)


# In[45]:


usselIslem(2,4)


# In[8]:


#3) Aynı fonksiyonu aşağıdaki gibi çağırırsak çıktı ne olur?


# In[46]:


usselIslem()


# In[10]:


#4) Aşağıdaki kodun çıktısı ne olacaktır?


# In[47]:


def myLoop(*args):
    for element in args:
        print(element / 2)


# In[48]:


myLoop(3,2,1,5,3,4)


# In[13]:


#5) Aşağıdaki dizide belirtilen rakamları, myFunction fonksiyonuna tabi tutup, yeni bir dizi oluşturunuz


# In[14]:


def myFunc(num):
    return num ** 3


# In[15]:


myList = [2,3,4,5,6]


# In[50]:


list(map(myFunc, myList))


# In[18]:


#6) Aşağıdaki string dizisinde, içinde sadece XYZ geçen barkodları gösterecek yeni bir liste oluşturunuz


# In[19]:


barkodDizisi = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]


# In[52]:


list(filter(lambda string : "XYZ" in string, barkodDizisi))


# In[22]:


#7) Aşağıdaki kodu okursanız, ornekFonksiyon çalıştırıldığında en altta yazdırılan print size neyi yazdıracaktır?


# In[53]:


myVar = "Atil Samancioglu"

def ornekFonksiyon():
    myVar = "Atil"
    
    def digerFonksiyon():
        print(myVar)
    
    digerFonksiyon()


# In[54]:


ornekFonksiyon()


# In[26]:


#8) Aşağıda yazdırılan sınıfı incelediğinizde kedim.yasiCarp() kodunun çıktısı ne olacaktır?


# In[55]:


class Kedi():
        
    def __init__(self,isim,yas=5):
        self.isim = isim
        self.yas = yas
        
    def yasiCarp(self):
        return self.yas * 3


# In[56]:


kedim = Kedi("Tonton")


# In[57]:


kedim.yasiCarp()


# In[31]:


#9) Aşağıdaki kodun çıktısı ne olacaktır?


# In[58]:


class Ogrenci():
    
    def __init__(self,isim,sinavNotu):
        self.isim = isim
        self.__sinavNotu = sinavNotu
    
    def notuGoster(self):
        print(f"{self.isim} sınav notu: {self.__sinavNotu}")


# In[59]:


ogrenci = Ogrenci("Mehmet",85)


# In[60]:


ogrenci.__sinavNotu = 75


# In[61]:


ogrenci.notuGoster()


# In[37]:


#10) Soyut sınıflar ve methodlar oluşturmamıza olanak tanıyan, kodlarımızı daha planlı şekilde yazmamızı mümkün kılan


# In[38]:


# aynı zamanda büyük projelerde bize yapısal olarak fayda sağlayabilecek OOP prensibinin adı nedir?


# In[39]:


#Abstraction

