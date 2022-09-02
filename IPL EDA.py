#!/usr/bin/env python
# coding: utf-8

# # IPL -  Exploratory Data Analysis

# importing required libraries

# In[3]:


import pandas as pd


# In[4]:


import numpy as np


# In[5]:


from matplotlib import pyplot as plt


# In[6]:


import seaborn as sns


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')

Reading the Dataset
# In[8]:


df = pd.read_csv("C:\\Users\\himan\\Downloads\\matches.csv")


# In[9]:


df.head()              ## to display first five records


# In[10]:


df.columns             ## it will give the name of all columns


# In[11]:


df.shape     ## it will give no. of rows * no.of columns

Check Null Values
# In[12]:


df.isnull().sum()       ## we can also use isna in place of isnull

Remove unwanted data
-umpire3 column has lots of NaN data, so drop that column
# In[13]:


df.drop(columns=["umpire3"],inplace=True)


# In[14]:


df.head()

Rearrange Data
- city , umpire1, umpire2 data will be replaced by "-" for easier processing
- Many teams has changed their names over the years so we consider those as same team (depending on the city)
# In[15]:


df.city = df.city.fillna("-")
df.umpire1 = df.umpire1.fillna("-")
df.umpire2 = df.umpire2.fillna("-")


# In[16]:


df = df.replace('Rising Pune Supergiants','Rising Pune Supergiant')
df = df.replace('Pune Warriors','Rising Pune Supergiant')
df = df.replace('Deccan Chargers','Sunrisers Hyderabad')
df = df.replace('Delhi Daredevils','Delhi Capitals')

Remove records which does not have valid information.So, we can remove data based on results(no result)
# In[17]:


is_NaN = df.isnull()


# In[18]:


row_has_NaN = is_NaN.any(axis=1)


# In[19]:


rows_with_NaN = df[row_has_NaN]
rows_with_NaN


# In[20]:


df.dropna(inplace=True)
df.isnull().sum()


# In[21]:


df.duplicated().sum()


# In[22]:


df.info()


# In[23]:


df.describe()


# Visualization

# ### Number of matches played in each year

# In[24]:


plt.figure(figsize=(15,7))
sns.countplot(x='Season',
              data=df,
              order = df['Season'].value_counts().index.sort_values()    # to sort the data series, we use order
              )
plt.xlabel('Season',fontsize=12)
plt.ylabel('No: of matches',fontsize=12)
plt.title('Number of matches played in each IPL season',fontsize=16)

Most number of matches were played in IPL-2013 Season
# ### Top 10 Player of the match winners over the time

# In[25]:


player_of_match = df["player_of_match"].value_counts()[:10]
player_of_match


# In[26]:


plt.figure(figsize=(15,7))
sns.barplot(player_of_match.index,
            player_of_match.values,
            palette='cividis')          # to make the chart more attractive by using diff. colors, we uses palette

plt.title("Player of the Match",fontsize=15)
plt.xlabel('Player',fontsize=12)
plt.ylabel('Count',fontsize=12)

Chris Gayle won most Man of the Match Awards
# ### Who won the most number of matches

# In[27]:


match_winner = df['winner'].value_counts()
match_winner


# In[28]:


plt.figure(figsize = (11,9))
sns.countplot(y = 'winner',
              data = df,
              order= df['winner'].value_counts().index,
              palette = 'copper' )
plt.xlabel('No: of Wins',fontsize=12)
plt.ylabel('Team',fontsize=12)
plt.title('Matches won by the Teams',fontsize=16)

Mumbai Indians won most number of matches followed by Chennai Super Kings
# ### No of matches played in stadium, Top 10

# In[29]:


plt.figure(figsize = (12,8))
sns.countplot(y = 'venue',
              data = df,
              order = df['venue'].value_counts().iloc[:10].index,
              palette='gist_heat')
plt.xlabel('No: of matches',fontsize=12)
plt.ylabel('Venue',fontsize=12)
plt.title('Number of matches played in each Stadium',fontsize=16)

Most number of IPL matches were played in Eden Gardens Stadium, Kolkata
# ### After winning the toss,what decision is taken bat or field

# In[30]:


plt.figure(figsize=(6,6))
sizes = df.toss_decision.value_counts()
labels = df.toss_decision.value_counts().index
plt.pie(sizes,colors = ['#ff9999','#66b3ff'],
         labels=labels,
         autopct='%1.1f%%',
         startangle=90,
         pctdistance=0.75,
         explode = (0.025,0.025))

In more than 61% of matches, teams chose to field after winning the toss.
# In[31]:


plt.figure(figsize=(15,7))
sns.countplot(x='Season',
              hue='toss_decision',
              data=df,
              order = df['Season'].value_counts().index.sort_values(),
              palette='deep')
plt.xlabel('Season',fontsize=12)
plt.ylabel('Count',fontsize=12)
plt.title('Decision to field or bat in each IPL season', fontsize=16)

We can see a trend that, decisions to field are more from IPL-2016 Season
# ### Which team won most number of matches with the margin of more than 5 wickets.

# In[32]:


df.loc[df.win_by_wickets > 5, "winner"].value_counts().plot(kind="barh")

Kolkata Knight Riders won maximum no. of matches with the margin of more than 5 wickets
# ### Toss winner won the match? which team did the best?

# In[33]:


df.loc[df.toss_winner == df.winner, "winner"].value_counts().plot(kind='barh')
print(df.loc[df.toss_winner == df.winner, "winner"].value_counts())

Chennai Super Kings comes out to be in choosing right decision after toss
# ### Pie chart to show, which team has highest percentage of wins.

# In[34]:


df.loc[(df["team1"] == "Chennai Super Kings") & (df["team2"] == "Mumbai Indians"), "winner"].value_counts().plot(kind="pie")

Mumbai Indians have high percentage of wins vs chennai Super Kings 
# In[35]:


sns.heatmap(df.corr())


# In[38]:


sns.boxplot(x = 'win_by_runs', data=df)


# In[ ]:




