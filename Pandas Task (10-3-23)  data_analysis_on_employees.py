#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[12]:


import numpy as np


# In[28]:


data_f=pd.read_csv('demo.csv')
print(data_f)


# In[42]:


def max_joinings_month(data_f):
    data_f['Date of Joining'] = pd.to_Datetime(data_f['Date of Joining'])
    data_f['Date of joining'] = data_f['Date of joining'].dt.month_name()    
    joining_counts = data_f['Date of Joining'].value_counts()
    
    max_month = joining_counts.idxmax()
    
    # Return the name of the month with the highest joinings
    return max_month


# In[49]:


print("demo.csv",max_joinings_month(data_f))


# ### What is the mean salary is the state KS

# In[38]:


def mean_ks_salary(data_f):
    KS_data_f = data_f[data_f['State'] == 'KS'] # filterING the dataframe
    salary = KS_data_f['Salary'] # calculate the mean salary of KS state
    mean_salary=salary.mean()
    return mean_salary


# In[39]:


print("demo.csv",mean_ks_salary(data_f))


# ### Which Region has highest mean salary
# 

# In[43]:


def max_mean_salary_region(data_f):
    mean_salary_by_region = data_f.groupby('Region')['Salary'].mean()
    max_mean_salary = mean_salary_by_region.max()
    region_with_max_mean_salary = mean_salary_by_region[mean_salary_by_region == max_mean_salary].index[0]
    return region_with_max_mean_salary


# In[44]:


print("demo.csv",max_mean_salary_region(data_f))


# ### Which region has lowest mean salary
# 

# In[45]:


def min_mean_salary_region(data_f):
    mean_salary_by_region = data_f.groupby('Region')['Salary'].mean()
    min_mean_salary = mean_salary_by_region.min()
    region_with_min_mean_salary = mean_salary_by_region[mean_salary_by_region == min_mean_salary].index[0]
    return region_with_min_mean_salary


# In[46]:


print("demo.csv",min_mean_salary_region(data_f))


# ### Which City has highest mean weight
# 

# In[47]:


def max_mean_weight_city(data_f):
    # Calculate the mean weight for each city
    mean_weights = data_f.groupby('City')['Weight in Kgs.'].mean()

    # Find the city with the highest mean weight
    max_mean_weight_city = mean_weights.idxmax()

    return max_mean_weight_city


# In[48]:


print("on demo.csv",max_mean_weight_city(data_f))


# ### What is the difference between mean salary of Doctors and Professors
# 

# In[50]:


def dr_prof_mean_salary_diff(data_f):    
    dr_salary = data_f[data_f["Name Prefix"].str.contains('Dr')]['Salary'].mean()
    mean_professors_salary = data_f[data_f["Name Prefix"].str.contains('Prof')]["Salary"].mean()
    final= mean_professors_salary - dr_salary
    return final


# In[53]:


print("demo.csv",dr_prof_mean_salary_diff(data_f))


# ### How many female use yahoo
# 

# In[55]:


def females_with_yahoo(data_f):
    yahoo_mask = data_f['E Mail'].str.contains('@yahoo')
    female_mask = data_f['Gender'] == 'F'
    filtered_data_f = data_f[yahoo_mask & female_mask]
    return len(filtered_data_f)


# In[54]:


print("demo.csv",females_with_yahoo(data_f))


# ### How many Doctors use gmail
# 

# In[56]:


def doctors_with_gmail(data_f):
    gmail_mask = data_f['E Mail'].str.contains('@gmail')
    dr_mask = data_f['Name Prefix'] == 'Dr.'
    drs_mask = data_f['Name Prefix'] == 'Drs.'
    total_drs=dr_mask+drs_mask
    filtered_data_f = data_f[gmail_mask & total_drs]
    return len(filtered_data_f)


# In[60]:


print("demo.csv",doctors_with_gmail(data_f))


# ### What is the password of the youngest male
# 

# In[58]:


def youngest_male_password(data_f):
    males = data_f[data_f['Gender'] == 'M']
    youngest_male = males.loc[males['Age in Yrs.'].idxmin()]
#     return youngest_male
    return youngest_male['Password']


# In[59]:


print("demo.csv",youngest_male_password(data_f))


# In[ ]:




