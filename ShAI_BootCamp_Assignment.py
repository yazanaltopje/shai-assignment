#!/usr/bin/env python
# coding: utf-8

# #About Dataset
# salaries dataset generally provides information about the employees of an organization in relation to their compensation. It typically includes details such as how much each employee is paid (their salary), their job titles, the departments they work in, and possibly additional information like their level of experience, education, and employment history within the organization.

# # Features
# - 'Id'
# - 'EmployeeName'
# - 'JobTitle'
# - 'BasePay'
# - 'OvertimePay'
# - 'OtherPay'
# - 'Benefits'
# - 'TotalPay' -> salary
# - 'TotalPayBenefits'
# - 'Year'
# - 'Notes'
# - 'Agency'
# - 'Status'
# 

# # Tasks
# 
# 1. **Basic Data Exploration**: Identify the number of rows and columns in the dataset, determine the data types of each column, and check for missing values in each column.
# 
# 2. **Descriptive Statistics**: Calculate basic statistics mean, median, mode, minimum, and maximum salary, determine the range of salaries, and find the standard deviation.
# 
# 3. **Data Cleaning**: Handle missing data by suitable method with explain why you use it.
# 
# 4. **Basic Data Visualization**: Create histograms or bar charts to visualize the distribution of salaries, and use pie charts to represent the proportion of employees in different departments.
# 
# 5. **Grouped Analysis**: Group the data by one or more columns and calculate summary statistics for each group, and compare the average salaries across different groups.
# 
# 6. **Simple Correlation Analysis**: Identify any correlation between salary and another numerical column, and plot a scatter plot to visualize the relationship.
# 
# 8. **Summary of Insights**: Write a brief report summarizing the findings and insights from the analyses.

# # Very Important Note
# There is no fixed or singular solution for this assignment, so if anything is not clear, please do what you understand and provide an explanation.

# In[1]:


import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt



# In[2]:


# Reading data from the CSV file
df = pd.read_csv('Salaries.csv')


# In[3]:


#  Data Exploration
print(df.shape)
print(df.dtypes)


# In[4]:


# Descriptive Statistics
statistics= df['TotalPay'].describe()
print(statistics)


# In[5]:


#check for missing values in each column.
# as we see we have missing data  
plt.figure(figsize=[10,4])
sns.heatmap(df.isnull(),cmap='Blues')


# In[6]:


'''as we see we have missing data Handle missing data by suitable method with explain why you use it
There are several ways to handle missing data. One of the most common methods is to drop
the column that contains the missing data. However,
this is not a good decision in some cases, as it may lead to the loss of important information or to bias in the results.
Another way to handle missing data is to calculate the mean of the data that does not contain missing values. 
Then, this mean is used to replace the missing values.

The choice of the right method to handle missing data depends on several factors, 
including the percentage of missing data, the type of data, and the nature of the task being performed.'''

df = df.drop('Notes', axis=1)
df = df.drop('Status', axis=1)
df['Benefits'] = df['Benefits'].fillna(df['Benefits'].mean())
df['BasePay'] = df['BasePay'].fillna(df['BasePay'].mean())
plt.figure(figsize=[10,4])
sns.heatmap(df.isnull(), cmap='Blues') 


# In[7]:


plt.figure(figsize=(5, 4))
plt.hist(df['TotalPay'],  color='red')
plt.title('Salary Distribution')


# In[8]:


department_counts = df['JobTitle'].value_counts()
plt.figure(figsize=[100,100])
plt.pie(department_counts, labels=department_counts.index)
plt.show()


# In[9]:


# Grouped Analysis
average = df.groupby('JobTitle')['TotalPay'].mean().sort_values(ascending=False)
print(average)



# In[10]:


correlation = df['BasePay'].corr(df['TotalPay'])
print(f"Correlation between BasePay and TotalPay: {correlation}")


# In[11]:


plt.figure(figsize=(5, 3))
plt.scatter(df['BasePay'], df['TotalPay'])
plt.title('Scatter Plot: BasePay vs TotalPay')
plt.xlabel('BasePay')
plt.ylabel('TotalPay')
plt.show()


# In[ ]:





# # Good Luck!
