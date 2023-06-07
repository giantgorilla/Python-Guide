#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# # Series 

# In[2]:


my_dict = {"James": 50, "Lars": 60, "Kirk": 55, "Rob": 65}


# In[3]:


pd.Series(my_dict)


# In[4]:


age_list = [50, 60, 55, 65]
name_list = ["James", "Lars", "Kirk", "Rob"]


# In[5]:


pd.Series(name_list, age_list)


# In[9]:


pd.Series(data = age_list, index = name_list)


# In[10]:


numpy_array = np.arange(0, 8)


# In[11]:


numpy_array


# In[12]:


pd.Series(numpy_array)


# In[13]:


new_numpy_array = np.array([10, 20, 30, 40])


# In[14]:


pd.Series(new_numpy_array)


# In[15]:


new_numpy_array


# In[16]:


name_list


# In[17]:


pd.Series(data = new_numpy_array, index = name_list)


# In[18]:


my_series = pd.Series(data = new_numpy_array, index = name_list)


# In[19]:


my_series


# In[20]:


type(my_series)


# In[21]:


my_series["Kirk"]


# In[22]:


my_series["Kirk"] = 60


# In[23]:


my_series


# In[26]:


quiz_results1 = pd.Series(data = [70, 60, 100], index = ["A", "B", "C"])


# In[27]:


quiz_results2 = pd.Series(data = [80, 30, 50], index = ["A", "B", "C"])


# In[28]:


quiz_results1


# In[29]:


quiz_results2


# In[31]:


quiz_results1 + quiz_results2


# In[32]:


exam_results1 = pd.Series(data = [70, 60, 100], index = ["A", "B", "C"])


# In[33]:


exam_results2 = pd.Series(data = [80, 30, 50], index = ["A", "D", "C"])


# In[34]:


exam_results1 + exam_results2


# # DataFrame Pandas

# In[35]:


my_data = np.array([[10, 20, 30], [20, 30, 40], [20, 50, 10], [10, 15, 20]])


# In[36]:


my_data


# In[37]:


my_names = ["James", "Lars", "Kirk", "Rob"]


# In[38]:


my_columns = ["Jan", "Feb", "March"]


# In[39]:


my_data_frame = pd.DataFrame(my_data)


# In[41]:


my_data_frame


# In[42]:


type(my_data_frame)


# In[43]:


my_data_frame[0]


# In[45]:


new_data_frame = pd.DataFrame(my_data, index = my_names, columns = my_columns)


# In[46]:


new_data_frame


# In[48]:


type(new_data_frame["Feb"])


# In[49]:


feb_series = new_data_frame["Feb"]


# In[51]:


feb_series.mean()


# In[52]:


feb_series.Lars


# In[53]:


new_data_frame[["Jan", "Feb"]] #Sadece Ocak ve Şubat aylarını gmsterir.


# In[54]:


new_data_frame.loc["Lars"]


# In[58]:


new_data_frame.loc["Rob"].mean()


# In[59]:


new_data_frame.iloc[3]


# In[61]:


new_data_frame["Apr"] = new_data_frame["March"] * 2


# In[63]:


new_data_frame #Mart ayında kazanılan paranın iki katına çıkartılıp yazdırılması.


# In[65]:


new_data_frame.drop("Rob", axis = 0) #axis = 0 satır axis = 1 sütün


# In[66]:


new_data_frame.drop("Rob", axis = 0, inplace = True) #inplace = Kalıcı silme


# In[73]:


new_data_frame


# In[74]:


boolean_frame = new_data_frame > 25


# In[75]:


boolean_frame


# In[76]:


new_data_frame[boolean_frame]


# In[78]:


new_data_frame[new_data_frame > 30]


# In[79]:


new_data_frame[new_data_frame["March"] > 25]


# In[80]:


new_data_frame.reset_index()


# In[81]:


new_data_frame["NewIndex"] = ["Jam", "Lar", "Kir"]


# In[82]:


new_data_frame


# In[83]:


new_data_frame.set_index("NewIndex") #Yeni indexi başa alır.


# # DataFrame Operations

# In[84]:


my_dict = {"James": [40, 30, np.nan],  "Kirk": [20, np.nan, 50], "Lars" : [30, 40, 50]}


# In[85]:


my_data_frame = pd.DataFrame(my_dict)


# In[86]:


my_data_frame


# In[87]:


my_data_frame.dropna()


# In[88]:


my_data_frame.dropna(axis = 1) #axis = 1, satır anlamına denk gelir.


# In[89]:


my_new_dict = {"James": [40, 30, np.nan],  "Kirk": [20, np.nan, 50], "Lars" : [30, 40, 50], "Rpb": [45, np.nan, np.nan]}


# In[90]:


my_new_data_frame = pd.DataFrame(my_new_dict)


# In[91]:


my_new_data_frame


# In[92]:


my_new_data_frame.dropna(axis = 1, thresh = 2) #Thresh = minimum gereksinim


# In[93]:


my_new_data_frame.fillna(20) #Boş değerleri doldurma.


# # GroupBY

# In[97]:


salary_dict = {"Programming Language" : ["Python", "Python", "Python", "Java", "Java", "Swift"], "Name": ["A", "B", "C", "D","E", "F"], "Salary": [100,90, 80, 70, 60, 50]}


# In[98]:


salary_frame = pd.DataFrame(salary_dict)


# In[99]:


salary_frame


# In[101]:


group_object = salary_frame.groupby("Programming Language")


# In[102]:


group_object.count()


# In[103]:


group_object.mean()


# In[104]:


group_object.min("Salary")


# In[105]:


group_object.max("Salary")


# In[106]:


group_object.describe()


# In[107]:


my_dict1 = {"Name": ["A", "B", "C", "D"],
            "Sports": ["Basketball", "Football", "Tennis", "Running"],
            "Calories": [100, 200, 300, 400]}


# In[120]:


my_frame1 = pd.DataFrame(my_dict1, index = [1, 2, 3, 4])


# In[121]:


my_frame1


# In[122]:


my_dict2 = {"Name": ["E", "F", "G", "H"],
            "Sports": ["Basketball", "Football", "Tennis", "Running"],
            "Calories": [200, 50, 330, 440]}


# In[123]:


my_frame2 = pd.DataFrame(my_dict2, index = [5, 6, 7, 8])


# In[124]:


my_frame2 


# In[125]:


my_dict3 = {"Name": ["I", "J", "K", "L"],
            "Sports": ["Basketball", "Football", "Tennis", "Running"],
            "Calories": [300, 150, 320, 410]}


# In[126]:


my_frame3 = pd.DataFrame(my_dict3, index = [9, 10, 11, 12])


# In[127]:


my_frame3


# # Concat - Concatenation

# In[128]:


pd.concat([my_frame1, my_frame2, my_frame3])


# # Merge

# In[129]:


my_frame1


# In[130]:


my_frame2


# In[131]:


my_frame3


# In[132]:


pd.merge(my_frame1, my_frame2, on = "Sports") #Spora göre birleştirme işlemi.


# In[141]:


new_salary_frame = pd.DataFrame({"Name" : ["James", "Kirk", "Lars"], "Salary" : [10, 20, 30], "Age": [60, 65, 70]})


# In[142]:


new_salary_frame


# In[143]:


new_salary_frame["Name"].unique()


# In[144]:


new_salary_frame["Name"].nunique() #Number of Unique


# In[145]:


def grosstoNet(salaray):
    return  salaray * 0.65


# In[148]:


new_salary_frame["Salary"].apply(grosstoNet)


# In[ ]:




