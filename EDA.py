#!/usr/bin/env python
# coding: utf-8

# ***Task 3***
# 
# perform EDA on dataset 'SampleSuperstore'

# In[1]:


#import libraries:
import pandas as pd
import numpy as np
import warnings as wg
wg.filterwarnings('ignore')
import matplotlib.pyplot as plt


# ***IMPORT DATASET***

# In[2]:


#import dataset:
dataset=pd.read_csv(' SampleSuperstore.csv')

#view top observations:
dataset.head()


# ***DATA PREPROCESSING***

# In[3]:


#view information:
dataset.info()


# In[4]:


#view insights from the dataset:
dataset.describe()


# In[5]:


#view the shape:
dataset.shape


# In[6]:


#view column names:
dataset.columns


# In[7]:


#check for missing values:
dataset.isnull().sum()


# In[8]:


#check for duplicate values:
dataset.duplicated().sum()


# In[9]:


#drop dumplicate:
dataset.drop_duplicates()

#view the modfied dataset:
dataset.head()


# In[10]:


#removing some uneccesory columns:
dataset=dataset.drop(['Postal Code'],axis=1)

##view the modfied dataset:
dataset.head()


# ***EDA***

# In[11]:


#visualizing the dataset as a whole using the pair plot:
import seaborn as sns
sns.pairplot(dataset)


# In[12]:


#see the pairwise corelation between the column:

get_ipython().run_line_magic('matplotlib', 'inline')

dataset.corr()
plt.figure(figsize=(10,5))
sns.heatmap(dataset.corr(),annot=True)


# In[13]:


plt.figure(figsize=(10,16))
dataset.groupby('Category')['Profit','Sales'].agg(['sum']).plot.bar()
plt.ylabel('Profit')


# In[22]:


#computing top categories in sales:
top_category_s=dataset.groupby('Category').Sales.sum().nlargest(n=100)
#computing top categories in profit:
top_category_p=dataset.groupby('Category').Profit.sum().nlargest(n=100)
#visuallizing:
plt.style.use('seaborn')
top_category_s.plot(kind='bar',figsize=(10,5),fontsize=14)
top_category_p.plot(kind='bar',figsize=(10,5),fontsize=14,color='red')
plt.xlabel('Category',fontsize=15)
plt.ylabel('Total Profit/sales',fontsize=15)
plt.title('Top category sales vs profit',fontsize=15)
plt.show()
                                                                 


# In[24]:


#computing top sub-categories:
top_subcategory_s=dataset.groupby('Sub-Category').Sales.sum().nlargest(n=100)
#top subcategories in profit:
top_subcategory_p=dataset.groupby('Sub-Category').Profit.sum().nlargest(n=100)

#visuallize:
plt.style.use('seaborn')
top_subcategory_s.plot(kind='bar',figsize=(10,5),fontsize=14)
top_subcategory_p.plot(kind='bar',figsize=(10,5),fontsize=14,color='red')
plt.xlabel('sub-Category',fontsize=15)
plt.ylabel('Total Profit/sales',fontsize=15)
plt.title('Top sub-category sales vs profit',fontsize=15)
plt.show()


# In[25]:


#a more detailed view:
plt.figure(figsize=(14,12))
statewise=dataset.groupby(['Sub-Category'])['Profit'].sum().nlargest(50)
statewise.plot.barh()


# In[26]:


plt.figure(figsize=(8,7))
sns.lineplot(dataset['Discount'],dataset['Profit'],data=dataset)


# In[30]:


#computing top states in terms of sales from first 10 observations
top_states_s=dataset.groupby('State').Sales.sum().nlargest(n=10)
#computing top states in profit:
top_states_p=dataset.groupby('State').Profit.sum().nlargest(n=10)
#visuallize:
plt.style.use('seaborn')
top_states_s.plot(kind='bar',figsize=(10,5),fontsize=14)
top_states_p.plot(kind='bar',figsize=(10,5),fontsize=14,color='red')
plt.xlabel('States',fontsize=15)
plt.ylabel('Total sales',fontsize=15)
plt.title('Top 10 states sales vs profit',fontsize=15)
plt.show()


# In[32]:


plt.style.use('seaborn')
dataset.plot(kind='scatter',figsize=(10,5),x='Sales',y='Profit',c='Discount',s=20,fontsize=16)


# ***CONCLUSION***
1.The sub-categories sales of tables should be minimized.
2.Increase sales more in the east as the profit is more.
3.States like 'New York','California' can give more profit.