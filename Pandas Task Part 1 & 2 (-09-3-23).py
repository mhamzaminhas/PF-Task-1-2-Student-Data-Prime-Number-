#!/usr/bin/env python
# coding: utf-8

# ## Task 1 - Part #1

# In[9]:


from tensorflow import keras


# In[10]:


import pandas as pd
dataset = keras.datasets.mnist.load_data()


# In[15]:


train_df = pd.DataFrame(list(zip(dataset[0][0], dataset[0][1])), columns =['image', 'label'])
test_df = pd.DataFrame(list(zip(dataset[1][0], dataset[1][1])), columns =['image', 'label'])
train_df.to_csv('File1.csv')


# In[14]:


test_df.to_csv('file2.csv')


# ## Task 1 - Part #2

# In[16]:


train_df =pd.read_csv('File1.csv')


# In[17]:


test_df =pd.read_csv('File2.csv')


# In[18]:


train_df


# In[38]:


train_data=train_df.loc[:,'image']
train_data
train_data_img=train_data.to_numpy
train_data_img


# In[37]:


train_data=train_df.loc[:,'label']
train_data
tr_data_lb=train_data.to_numpy
tr_data_lb


# In[36]:


test_data=test_df.loc[:,'image']
test_data
tst_data_img=test_data.to_numpy
tst_data_img


# In[35]:


lb_test_data=test_df.loc[:,'label']
lb_test_data
tst_data_lb=lb_test_data.to_numpy
tst_data_lb


# In[39]:


final_output=((train_data_img,tr_data_lb), (tst_data_img,tst_data_lb))
print(final_output)

