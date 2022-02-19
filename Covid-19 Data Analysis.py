#!/usr/bin/env python
# coding: utf-8

# # Task: Covid-19 Data Analysis
# ### This notebook is used to understand the comprehension of Data Analysis techniques using Pandas library.

# 

# ### Import the necessary libraries

# In[198]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Question 1

# #### Read the dataset

# In[199]:


path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2021.csv'
df = pd.read_csv(path)
df.info()
df.head()


# #### Display the top 5 rows in the data

# In[216]:


pd.DataFrame(np.random.rand(5))


# #### Show the information of the dataset

# In[201]:


df.info()


# #### Show the sum of missing values of features in the dataset

# In[202]:


df.isnull().sum()


# ### Question 2

# #### Show the number of Confirmed cases by Country

# In[203]:


world = df.groupby("Country_Region")['Confirmed'].sum().reset_index()
world.head()


# #### Show the number of Deaths by Country

# In[204]:


world = df.groupby("Country_Region")['Deaths'].sum().reset_index()
world.head()


# #### Show the number of Recovered cases by Country

# In[205]:


world = df.groupby("Country_Region")['Recovered'].sum().reset_index()
world.head()


# #### Show the number of Active Cases by Country

# In[206]:


world = df.groupby("Country_Region")['Active'].sum().reset_index()
world.head()


# #### Show the latest number of Confirmed, Deaths, Recovered and Active cases Country-wise

# In[218]:


world = df.groupby("Country_Region")['Confirmed','Deaths','Recovered','Active'].sum().reset_index()
world.head()


# ### Question 3

# ### Show the countries with no recovered cases

# In[208]:


world = df.groupby('Country_Region')['Recovered'].sum().reset_index()
result = df[df['Recovered']==0][['Country_Region','Recovered']]
print(result)


# #### Show the countries with no confirmed cases

# In[209]:


world = df.groupby('Country_Region')['Confirmed'].sum().reset_index()
result = df[df['Confirmed']==0][['Country_Region','Confirmed']]
print(result)


# #### Show the countries with no deaths

# In[215]:


world = df.groupby('Country_Region')['Deaths'].sum().reset_index()
result = df[df['Deaths']==0][['Country_Region','Deaths']]
print(result)


# ### Question 4

# #### Show the Top 10 countries with Confirmed cases

# In[210]:


world = df.groupby("Country_Region")['Confirmed'].sum().reset_index()
world.head(10)


# #### Show the Top 10 Countries with Active cases

# In[211]:


world = df.groupby("Country_Region")['Active'].sum().reset_index()
world.head(10)


# ### Question 5

# #### Plot Country-wise Total deaths, confirmed, recovered and active casaes where total deaths have exceeded 50,000

# In[212]:


df = df.groupby(["Country_Region"])["Deaths", "Confirmed", "Recovered", "Active"].sum().reset_index()
df = df.sort_values(by='Deaths', ascending=False)
df = df[df['Deaths']>50]
plt.figure(figsize=(15, 5))
plt.plot(df['Country_Region'], df['Deaths'],color='red')
plt.plot(df['Country_Region'], df['Confirmed'],color='green')
plt.plot(df['Country_Region'], df['Recovered'], color='blue')
plt.plot(df['Country_Region'], df['Active'], color='black')
 
plt.title('Total Deaths(>50000), Confirmed, Recovered and Active Cases by Country')
plt.show()


# ### Question 6

# ### Plot Province/State wise Deaths in USA

# In[226]:


import plotly.express as px
import plotly.io as pio


# In[242]:


df = df[df['Country_Region']=='US'].drop(df.columns['Country_Region','Lat', 'Long_'],axis=1)
df = df[df.sum(axis = 1) > 0]
df = df.groupby(['Province/State'])['Deaths'].sum().reset_index()
df_death = df[df['Deaths'] > 0]
state_fig = px.bar(df_death, x='Province/State', y='Deaths', title='State wise deaths reported of COVID-19 in USA', text='Deaths')
state_fig.show()


# In[ ]:


covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-09-2021.csv')


# In[ ]:


covid_data.columns


# In[ ]:





# ### Question 7

# ### Plot Province/State Wise Active Cases in USA

# In[ ]:





# ### Question 8

# ### Plot Province/State Wise Confirmed cases in USA

# In[ ]:





# ### Question 9

# ### Plot Worldwide Confirmed Cases over time

# In[222]:


import plotly.express as px
import plotly.io as pio


# In[225]:


import plotly.express as px


# In[ ]:




