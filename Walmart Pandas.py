#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd 
df = pd.read_csv("Downloads/WalmartSalesData.csv.csv")
df.head(5)


# In[9]:


#Read Headers of dataframe
print(df.columns)


# In[10]:


#print certain columns of each dataframe
print(df[['Invoice ID', 'Customer type','Product line']].head(5))


# In[11]:


#read the 1st -5th row of the dataframe 
print(df.iloc[1:6])


# In[12]:


#print a certain location 
print(df.iloc[7,4])


# Drop the total column from the copy of the original dataframe
# 

# # Find any invoice ID that starts with the 730

# In[13]:


df.loc[df["Invoice ID"].str.contains("730")]



# ### Doing conditional changes , if person wasted more than 600 dollars . change the customer type to Elite

# In[14]:


#df2= df.loc[(df["Gender"]=="Female") & (df['Customer type']=="Normal") & (df["Product line"]=="Sports and travel")].copy
#print(df2)


# In[15]:


# Assuming df is your original DataFrame
df2 = df.loc[(df["Gender"] == "Female") & (df['Customer type'] == "Normal") & (df["Product line"] == "Sports and travel")].copy()
df2

# Convert "Total" column to numeric type
#df2.loc[:, "Total"] = pd.to_numeric(df2["Total"], errors="coerce")

# Update "Customer type" for rows where "Total" > 600
#df2.loc[df2["Total"] > 600, "Customer type"] = "Elite"

# Print the resulting DataFrame
#print(df2)


# In[16]:


df2.loc[:, "Total"] = pd.to_numeric(df2["Total"], errors="coerce")
df2



# In[17]:


# Update "Customer type" for rows where "Total" > 600
df2.loc[df2["Total"] > 300, "Customer type"] = "Elite"
df2


# In[18]:


df2.reset_index(drop= True, inplace= True)
df2



# In[19]:


df2.head(5)


# ## Stripping any unecssary texts in the product line column such as dots or / 

# In[25]:


df2["Product line"]= df2["Product line"].str.strip("..._/")
df2["Product line"].head(4)


# ##Eiminate N/a or N values in the dataframe and leave it blank 

# In[32]:


#df2 = df2.replace('N/A',',')
#code below will blank any value that has "NaN"
df2 = df2.fillna(',')
df2


# # #Provide a  list of customers who purchased more than 7 quantities and have a tax higher than 30 dolllars

# In[33]:


for x in df2.index:
    if df2.loc[x, "Quantity"] <= 7:
        df2.drop(x , inplace= True)

df2


# In[34]:


for x in df2.index:
    if df2.loc[x,"Tax 5%"] <= 30:
        df2.drop(x , inplace= True)
df2


# In[42]:


#reset the index to make the dataframe look better
df2.reset_index(drop=True, inplace= True)
df2


# In[41]:


#List finalized 
df2


# In[ ]:




