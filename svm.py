#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import pandas as pd


# In[3]:


df = pd.read_csv(r"Dataset-training.csv",header=None)
df.head()


# In[4]:


df.describe()


# In[5]:


df.columns = ["NIP", "Staf-Proses", "Kategori"]


# In[6]:


df.head()


# In[7]:


df = df.drop(["NIP"],1)


# In[8]:


df.head()


# In[9]:


Y = df["Kategori"]


# In[10]:


X = df[["Staf-Proses"]]


# In[11]:


X.head()


# In[12]:


Y.head()


# In[13]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)


# In[14]:


clf = neighbors.KNeighborsClassifier()


# In[15]:


clf.fit(X_train, Y_train)


# In[16]:


accuracy = clf.score(X_test, Y_test)
accuracy


# In[17]:


sample_measure = np.array([5])
print(sample_measure)


# In[18]:


sample_measure = sample_measure.reshape(1,-1)


# In[19]:


predict = clf.predict(sample_measure)


# In[20]:


predict
print(predict)


# In[ ]:




