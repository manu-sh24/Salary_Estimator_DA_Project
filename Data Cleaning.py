#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df= pd.read_csv("glassdoor_jobs.csv")


# In[4]:


df.info()


# In[5]:


df['hourly']= df['Salary Estimate'].apply(lambda x: 1 if "per hour" in x.lower() else 0)
df['employer_provided']=df['Salary Estimate'].apply(lambda x: 1 if "employer provided salary" in x.lower() else 0)


# In[6]:


df=df[df["Salary Estimate"]!= '-1']
df['Salary Estimate'] = df["Salary Estimate"].apply(lambda x: x.split('(')[0])
df['Salary Estimate']= df['Salary Estimate'].apply(lambda x: x.lower().replace("k",'').replace('$',''))


# In[7]:


df['Salary Estimate']= df['Salary Estimate'].apply(lambda x:x.lower().replace("per hour",'').replace("employer provided salary",''))


# In[8]:


df['Salary Estimate']= df['Salary Estimate'].apply(lambda x:x.lower().replace(':',''))


# In[9]:


pd.set_option('display.max_rows', None)
print(df['Salary Estimate'])


# In[10]:


#int wali problem puuchni h billu se


# In[11]:


df['min_salary']=df['Salary Estimate'].apply(lambda x: x.split("-")[0])


# In[12]:


df['max_salary']=df['Salary Estimate'].apply(lambda x: x.split("-")[1])


# In[13]:


df["min_salary"] = pd.to_numeric(df["min_salary"], errors="coerce")
df["max_salary"] = pd.to_numeric(df["max_salary"], errors="coerce")


# In[14]:


df["avg_salary"]=(df.min_salary+df.max_salary)/2
df


# In[15]:


#company name text only
df['company_text']=df.apply(lambda x:x["Company Name"] if x["Rating"]<0 else x["Company Name"][:-4], axis=1)


# In[16]:


#state field
df['job_state']=df["Location"].apply(lambda x: x.split(',')[1])
                                   


# In[17]:


df['same_state']= df.apply(lambda x: 1 if x.Location==x.Headquarters else 0, axis=1)


# In[18]:


#age  of the company
df["age"]=df['Founded'].apply(lambda x: x if x<1 else 2023-x)


# In[19]:


#parsing the job description
df["Python_xx"]=df['Job Description'].apply(lambda x: 1 if "python" in x.lower() else 0)
df.Python_xx.value_counts()


# In[20]:


df["r_studio"]=df['Job Description'].apply(lambda x: 1 if "r_studio" in x.lower() else 0)
df.r_studio.value_counts()


# In[21]:


df["spark_xx"]=df['Job Description'].apply(lambda x: 1 if "spark" in x.lower() else 0)
df.spark_xx.value_counts()


# In[22]:


df["excel"]=df['Job Description'].apply(lambda x: 1 if "excel" in x.lower() else 0)
df.excel.value_counts()


# In[23]:


df["aws_xx"]=df['Job Description'].apply(lambda x: 1 if "aws" in x.lower() else 0)
df.aws_xx.value_counts()


# 

# In[24]:


df.columns


# In[25]:





# In[26]:


def title_simplifier(title):
    if "data scientist" in title.lower():
        return "data scientist"
    elif "data engineer" in title.lower():
        return "data engineer"
    elif "analyst" in title.lower():
        return "analyst"
    elif "machine learning" in title.lower():
        return "machine learning"
    elif "manager" in title.lower():
        return "manager"
    elif "director" in title.lower():
        return "director"
    else:
        return 'na'


# In[27]:


def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
        return "senior"
    elif 'jr' in title.lower() or 'jr.' in title.lower():
        return 'jr'
    else:
        return 'na'


# In[28]:


df['job_simp']=df['Job Title'].apply(title_simplifier)
df.job_simp.value_counts()


# In[29]:


df['seniority']=df['Job Title'].apply(seniority)
df.seniority.value_counts()


# In[30]:


df.job_state.value_counts()


# In[31]:


df['job_state']=df.job_state.apply(lambda x:x.strip() if x.strip().lower() !='los angeles' else 'CA')


# In[32]:


df.job_state.value_counts()


# In[33]:


df['job_desc_len']= df['Job Description'].apply(lambda x: len(x))
df.job_desc_len


# In[34]:


df['num_comp'] = df['Competitors'].apply(lambda x: len(str(x).split(',')) if str(x) != '-1' else 0)


# In[35]:


df['num_comp']


# In[36]:


df['Competitors']


# In[37]:


#couldn't get this how this hourly is converted to annual just by multiplying by 2, have to ask from billu
df['min_salary']=df.apply(lambda x:x.min_salary*2 if x.hourly==1 else x.min_salary,axis=1)
df['max_salary']=df.apply(lambda x:x.max_salary*2 if x.hourly==1 else x.max_salary,axis=1)


# In[38]:


df[df.hourly==1][['hourly','min_salary','max_salary']] 


# In[43]:


df_out=df.drop(['Unnamed: 0'],axis=1)


# In[44]:


df_out.to_csv("Data_cleaned_file.csv", index=False)


# In[45]:


pd.read_csv("Data_cleaned_file.csv")

