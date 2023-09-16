#!/usr/bin/env python
# coding: utf-8

# In[113]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[114]:


df=pd.read_csv("Data_cleaned_file.csv")


# In[115]:


df


# 

# In[116]:


df.columns


# In[117]:


df.describe()


# In[118]:


df.Founded.hist()


# In[119]:


df.Rating.hist()


# In[120]:


df.boxplot(column=['age','avg_salary','same_state','Rating'])


# In[121]:


df[['age','avg_salary','Rating']].corr()


# In[122]:


sns.heatmap(df[['age','avg_salary','Rating','num_comp']].corr(),vmax=3,square=True, cmap="crest")


# In[91]:


df.columns


# In[123]:


df_cat= df[['Location', 'Headquarters','Size','Type of ownership','Industry','Sector','Revenue','spark_xx','aws_xx','excel','job_simp','seniority']]


# In[124]:


for i in df_cat.columns:
    cat_num= df_cat[i].value_counts()
    chart= sns.barplot(x=cat_num.index, y=cat_num)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    plt.show()
    


# In[125]:


pd.pivot_table(df, index= 'job_simp', values= 'avg_salary')


# In[126]:


pd.pivot_table(df, index= ['job_simp', 'seniority'], values= 'avg_salary')


# In[127]:


pd.pivot_table(df, index= 'job_simp', values= 'avg_salary').sort_values('avg_salary', ascending= False)


# In[100]:


df.columns


# 

# In[128]:


df_pivots= df[['Rating', 'Industry', 'Sector', 'Revenue', 'num_comp', 'hourly','employer_provided','Python_xx', 'r_studio', 'spark_xx', 'excel', 'aws_xx', 'job_simp', 'seniority',
       'job_desc_len', 'avg_salary']]


# In[129]:


for i in df_pivots.columns:
    print(i)
    print(pd.pivot_table(df_pivots, index = i, values="avg_salary").sort_values('avg_salary', ascending= False))


# In[130]:


df.head()


# In[131]:


df.describe()

