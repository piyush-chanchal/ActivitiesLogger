#!/usr/bin/env python
# coding: utf-8

# In[160]:


import pandas as pd
import numpy as np


# In[161]:


df = pd.read_csv("/Users/piyush/Desktop/ProjectsGitHub/ActivitiesLoggerV1/Data/20201203.csv")
df.tail()


# In[162]:


df_new = df[['TotalMinutes','ActivityDoneTimeNumeric','Category','Sub Category 1']]


# In[163]:


df_new


# In[164]:


inputs = df_new.drop('Category',axis='columns')


# In[165]:


inputs = inputs.drop('Sub Category 1',axis='columns')


# In[166]:


target = df_new[['Category','Sub Category 1']]


# In[167]:


target


# In[168]:


from sklearn.preprocessing import LabelEncoder


# In[169]:


le_category = LabelEncoder()


# In[170]:


target


# In[171]:


target.tail()


# In[172]:


target['Category_n'] = le_category.fit_transform(target['Category'])


# In[173]:


target.drop('Category_n',axis='columns')


# In[174]:


target['Category_n'] = le_category.fit_transform(target['Category'])


# In[175]:


target


# In[176]:


target = target.drop('Category_n',axis='columns')


# In[177]:


target


# In[178]:


target


# In[179]:


target = target.drop('Category',axis="columns")


# In[180]:


target


# In[181]:


target = target.drop('Sub Category 1',axis="columns")


# In[182]:


target


# In[183]:


from sklearn import tree


# In[184]:


model = tree.DecisionTreeClassifier()


# In[185]:


model.fit(inputs,target)


# In[ ]:


df.tail()


# In[ ]:


model.predict([[721,16.67]])


# In[ ]:


model.predict([[241,16.67]])


# In[ ]:


model.predict([[2701,16]])


# In[ ]:


df


# In[186]:


print(pd)


# In[187]:


print("pd")


# In[188]:


print(pd)


# In[189]:


pd


# In[190]:


df


# In[191]:


print(df)


# In[192]:


df1 = pd.read_csv("/Users/piyush/Desktop/ProjectsGitHub/ActivitiesLoggerV1/catData/mainCat.csv")


# In[193]:


df1


# In[ ]:




