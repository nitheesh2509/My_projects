#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv('NETFLIX_REVIEWS.csv')
data.head()


# In[38]:


data.shape


# In[42]:


sns.set(style="white")


# In[43]:


palette = sns.color_palette("viridis", as_cmap=True)
sns.histplot(data=data, x='review_rating', kde=True, hue='review_rating', palette=palette)
plt.title('Histogram of Review Ratings.')
plt.show()


# In[20]:


sns.boxplot(x='review_likes', data=data)
plt.title('Box Plot of Review Likes')
plt.show()


# In[37]:


for rating_category in data['review_rating'].unique():
    subset = data[data['review_rating'] == rating_category]
    plt.scatter(subset['review_rating'], subset['review_likes'], label=f"Rating {rating_category}")

plt.xlabel('Review Rating')
plt.ylabel('Review Likes')
plt.title('Scatter Plot: Rating vs Likes')
plt.legend()
plt.show()


# In[33]:


plt.figure(figsize=(12,16))
sns.pairplot(data[['review_rating', 'review_likes']])
plt.show()


# In[45]:


correlation_matrix = data[['review_rating', 'review_likes']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# In[51]:


import matplotlib.dates as mdates


# In[58]:


data['review_timestamp'] = pd.to_numeric(data['review_timestamp'], errors='coerce')


fig = plt.figure(figsize=(10,12))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['review_rating'], data['review_likes'], data['review_timestamp'])
ax.set_xlabel('Review Rating')
ax.set_ylabel('Review Likes')
ax.set_zlabel('Review Timestamp')
plt.title('3D Scatter Plot')
plt.show()


# In[67]:


st.title('Interactive Data Visualization with Streamlit')

# Univariate Visualization
st.subheader('Univariate Visualization')
sns.histplot(data['review_rating'], kde=True)
st.pyplot()
sns.boxplot(x='review_likes', data=data)
st.pyplot()

# Bivariate Visualization
st.subheader('Bivariate Visualization')
plt.scatter(data['review_rating'], data['review_likes'])
st.pyplot()
sns.pairplot(data[['review_rating', 'review_likes']])
st.pyplot()

# Multivariate Visualization
st.subheader('Multivariate Visualization')
data['review_timestamp'] = pd.to_numeric(data['review_timestamp'], errors='coerce')
# Create a heatmap of correlation matrix
heatmap_data = data[['review_rating', 'review_likes']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', cbar_kws={'label': 'Correlation'})
st.pyplot()

# 3D Scatter Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['review_rating'], data['review_likes'], data['review_timestamp'])
ax.set_xlabel('Review Rating')
ax.set_ylabel('Review Likes')
ax.set_zlabel('Review Timestamp')
plt.title('3D Scatter Plot')
st.pyplot()


# In[ ]:




