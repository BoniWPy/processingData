#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import pandas as pd


# In[2]:


df = pd.read_csv(r"Dataset-training.csv",header=None)
df.head()


# In[3]:


df.describe()


# In[4]:


df.columns = ["NIP", "Staf-Proses", "Kategori"]


# In[5]:


df.head()


# In[6]:


df = df.drop(["NIP"],1)


# In[7]:


df.head()


# In[8]:


Y = df["Kategori"]


# In[9]:


X = df[["Staf-Proses"]]


# In[10]:


X.head()


# In[11]:


Y.head()


# In[12]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)


# In[13]:


clf = neighbors.KNeighborsClassifier()


# In[14]:


clf.fit(X_train, Y_train)


# In[15]:


accuracy = clf.score(X_test, Y_test)
print(accuracy)

