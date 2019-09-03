
# coding: utf-8

# # Data visualization in Python

# ## importing the data

# pandas provides excellent data reading and querying module,dataframe, which allows you to import structured data and perform SQL-like queries.
# 
# Here we imported some house price records from Trulia. For more about extracting data from Trulia, please check my previous tutorial.

# In[1]:


import pandas
df = pandas.read_excel('house_price.xlsx')
df[:10]


# In[2]:


df.describe()


# In[3]:


df.hist(figsize=(20,20))


# In[4]:


from  pandas.plotting import scatter_matrix
scatter_matrix(df,figsize=(20, 20), diagonal='kde')


# In[5]:


df.groupby('house_type').count()


# In[6]:


df.groupby('house_type').mean()


# In[7]:


df.groupby('house_type').hist(figsize=(12,4),column=['price','views'])


# In[8]:


df.plot.scatter(x='built_in',y='price')


# In[9]:


df['unit_price']=df['price']/df['area']


# In[10]:


mean_price =df.groupby('built_in').mean()


# In[11]:


mean_price.plot.line(y='unit_price')

