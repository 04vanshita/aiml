+#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)
print(df)


# In[2]:


# convert lowercase column use str.lower()
df['Courses'] = df['Courses'].str.lower()
df


# In[18]:


# convert lowercase column use apply()
import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)


df['Courses'] = df['Courses'].apply(str.lower)
df


# In[20]:


# Use apply() & lambda function

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)


df['Courses'] = df['Courses'].apply(lambda x:x.lower())
df


# In[21]:


# Convert pandas column to lowercase use map()

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].map(str.lower)
df


# In[22]:


# Convert column to uppercase

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.upper()
df


# In[23]:


# Find length

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.len()
df


# In[24]:


# Strip Method --> Removing any leading or trailing whitespaces

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.strip()
df


# In[26]:


# lstrip method  --> Removes Leading Whitespaces

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.lstrip()
df


# In[27]:


# rstrip method  --> Removes Trailing Whitespaces

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.rstrip()
df


# In[32]:


# Split Method --> Spits each string based on specified delimeter

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.split()
df


# In[33]:


# Contains Method --> Used to check if a specified substring or pattern is present

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.contains('PA')
df


# In[35]:


# Replace Method :- Replace specified value with another value

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.replace('HADOOP' , 'VANSH')
df


# In[36]:


# Startswith Method :- Used to check if a string startswith a pattern or a substring

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.startswith('S')
df


# In[37]:


# Endswith Method :- Used to check if a string endswith a pattern or a substring

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.endswith('OP')
df


# In[39]:


# Cat Method :- Used for concatenating strings. "sep" --> seperator

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.cat(df['Discount'], sep="-")
df


# In[41]:


# Get Method :- used to get the element at a specified position in each string of a string column.

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.get(0)
df


# In[45]:


# Slice Method :- Extract a substring from each element     start = 0, end = 5

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.slice(stop=3)
df


# In[46]:


# Find Method :- Used to find element     Returns index where found, if not found, retunrs -1

import pandas as pd
import numpy as np
technologies= ({
    'Courses':["SPARK","PYSPARK","HADOOP","PANDAS"],
    'Fee' :['22000','25000','24000','26000'],
    'Duration':['30days','50days','40days','60days'],
    'Discount':['1000','2300','2500','1400']
              })
df=pd.DataFrame(technologies)

df['Courses'] = df['Courses'].str.find('PARK')
df

