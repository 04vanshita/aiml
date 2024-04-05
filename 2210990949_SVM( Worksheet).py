#!/usr/bin/env python
# coding: utf-8

# ### INTRODUCTION

# In[ ]:


#Used SVM to build and train a model using human cell records, and classify cells to whether the samples are benign (mild state) or malignant (evil state).
#SVM works by mapping data to a high-dimensional feature space so that data points can be categorized, even when the data are not otherwise linearly separable (This gets done by kernel function of SVM classifier). A separator between the categories is found, then the data is transformed in such a way that the separator could be drawn as a hyperplane.


# ### 2. Necessary imports

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# ### Load Data From CSV File

# In[2]:


import pandas as pd

data=pd.read_csv("cell_samples.csv")
data


# ### SHAPE OF OUR DATASET

# In[3]:


print("Number of Rows",data.shape[0])
print("Number of Columns",data.shape[1])


# ### Count

# In[4]:


data.count()


# In[5]:


data['Class'].value_counts()


# ### Distribution of the classes

# In[6]:


benign_data=data[data['Class']==2][0:200]
malignant_data=data[data['Class']==4][0:200]

axes=benign_data.plot(kind='scatter',x='Clump' , y='UnifSize' , color='blue',label='Beningn')
malignant_data.plot(kind='scatter',x='Clump' , y='UnifSize' , color='red',label='malignant_df',ax=axes)
#help(benign_df.plot())


# ### Selection of unwanted columns
# 

# In[7]:


data.dtypes

data=data[pd.to_numeric(data['BareNuc'],errors='coerce').notnull()]
data['BareNuc']=data['BareNuc'].astype('int')
data.dtypes


# ### Remove unwanted columns

# In[8]:


data.columns
['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize',
       'BareNuc', 'BlandChrom', 'NormNucl', 'Mit']

feature_set=data[['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize',
       'BareNuc', 'BlandChrom', 'NormNucl', 'Mit']]

#df 100 rows and 11 coloumns
#picked 9 colomns out of 11

#Independent varibles
X=np.asarray(feature_set)

#dependent varible y
y=np.asarray(data['Class'])

X[0:5]

y[0:5]


# ### Divide the data as Train/Test dataset

# In[9]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=4)


# ### Modeling (SVM with Scikit-learn)

# In[12]:


from sklearn import svm
classifier=svm.SVC(kernel='linear', gamma='auto', C=2)
classifier.fit(X_train,y_train)

y_predit=classifier.predict(X_test)


# ### Evaluation (Results)

# In[11]:


from sklearn.metrics import classification_report
print(classification_report(y_test,y_predit))


# In[ ]:




