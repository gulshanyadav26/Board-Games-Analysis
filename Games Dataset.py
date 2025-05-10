#!/usr/bin/env python
# coding: utf-8

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read games.csv as a dataframe called games.**

# In[2]:


games = pd.read_csv('games.csv')


# ** Check the head of the DataFrame. **

# In[3]:


games.head()


# ** Use .info() method to find out total number of entries in dataset**

# In[4]:


games.info() # 81312 Entries in total


# **What is the mean playin time for all games put together ?**

# In[5]:


games['playingtime'].mean()


# ** What is the highest number of comments received for a game? **

# In[6]:


games['total_comments'].max()


# ** What is the name of the game with id 1500?  **

# In[7]:


games[games['id']==1500]['name']


# ** And which year was it published? **

# In[8]:


games[games['id']==1500]['yearpublished']


# ** Which game has received highest number of comments? **

# In[9]:


games[games['total_comments']== games['total_comments'].max()]


# ** Which games have received least number of comments? **

# In[10]:


games[games['total_comments']== games['total_comments'].min()]


# ** What was the average minage of all games per game "type"? (boardgame & boardgameexpansion)**

# In[11]:


games.groupby('type')['minage'].mean()


# ** How many unique games are there in the dataset? **

# In[12]:


games['id'].nunique()  # Note - Business sense dictates us to look at unique ID values rather than names which might have clerical errors!


# ** How many boardgames and boardgameexpansions are there in the dataset?  **

# In[13]:


games['type'].value_counts()


# ** Is there a correlation between playing time and total comments for the games? - Use the .corr() function **

# In[14]:


games[['playingtime','total_comments']].corr() # No correlation.


# ## Part 2 
# 
# ## Data Visualization using Seaborn

# ### Import the seaborn library and set color codes as true

# In[15]:


import seaborn as sns
sns.set(color_codes=True)


# ### Drop na values for negating issues during visualization

# In[16]:


games.dropna(inplace=True)


# ### View the distance plot for minage

# In[17]:


sns.histplot(games['average_rating'])


# ### Is there a linear relationship between Minage & average_rating?

# In[18]:


sns.jointplot(x='minage', y='average_rating', data=games)


# ### Compare the relationship between playingtime , minage and average rating using pairplot

# In[19]:


import matplotlib.pyplot as plt
sns.pairplot(games[['playingtime', 'minage', 'average_rating']])
plt.show()


# ### Compare type of game and playingtime using a stripplot

# In[20]:


sns.stripplot(x='type', y='playingtime', data=games, jitter=True)


# ### Analyze the linear trend between playing time(less than 500 mins) and average_rating received for the same

# In[ ]:


sns.regplot(x="playingtime", y="average_rating", data=games[games['playingtime'] < 500])

