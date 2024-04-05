#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv(r'C:\Users\vansh\OneDrive\Desktop\Ecommerce Purchases.unknown')
df


# In[4]:


#Display Top 10 Rows

df.head(10)


# In[5]:


#Display Last 10 rows

df.tail(10)


# In[6]:


# Check Datatype of Each column


# In[11]:


df.info()


# In[12]:


# CHeck null values in the dataset
df.isnull()


# In[13]:


# How many rows and columns in dataset
print ("Number of Rows" , df.shape[0])
print ("Number of Columns" , df.shape[1])


# In[16]:


# Highest and lowest purchase price in dataset
print(df['Purchase Price'].max())
print(df['Purchase Price'].min())


# In[17]:


# Average Purchase Price
print(df['Purchase Price'].mean())


# In[22]:


# How many people have french 'fr' as their language
print(df[df['Language'] == 'fr'].shape[0])


# In[25]:


# Job title contains engineer

df[df['Job'].str.contains('engineer')].shape[0]

