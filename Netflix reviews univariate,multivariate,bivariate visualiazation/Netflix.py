import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('NETFLIX_REVIEWS.csv', nrows=2000)

data_cleaned = data.dropna()

st.write("Information about Cleaned Data:")
st.write(data_cleaned.info())

sns.set_theme()

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Interactive Data Visualization with Streamlit')

# Sidebar for selecting visualization type
selected_visualization = st.sidebar.selectbox("Select Visualization Type", ["Univariate", "Bivariate", "Multivariate"])

# Univariate Visualization
if selected_visualization == "Univariate":
    st.subheader('Univariate Visualization')
    st.subheader("1. Histogram of Review Rating")
    sns.histplot(data_cleaned['review_rating'], kde=True, color='skyblue', edgecolor='black', linewidth=0.5)
    st.pyplot()

    st.subheader('2. Boxplot of Review Likes')
    sns.boxplot(x='review_likes', data=data_cleaned, palette='pastel')
    st.pyplot()

# Bivariate Visualization
elif selected_visualization == "Bivariate":
    st.subheader('Bivariate Visualization')
    st.subheader("1. Scatter Plot of Review Rating vs Review Likes")
    plt.scatter(data_cleaned['review_rating'], data_cleaned['review_likes'], c='coral', alpha=0.6)
    st.pyplot()

    st.subheader("2. Pair Plot of Review Rating and Review Likes")
    sns.pairplot(data_cleaned[['review_rating', 'review_likes']], palette='viridis')
    st.pyplot()

elif selected_visualization == "Multivariate":
    st.subheader('Multivariate Visualization')
    st.subheader("1. Heatmap of Review Rating and Review Likes")

    heatmap_data = data_cleaned[['review_rating', 'review_likes']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(heatmap_data, annot=True, cmap='magma', cbar_kws={'label': 'Correlation'})
    st.pyplot()

    st.subheader('2. lmplot for Review Rating and Review Likes')
    sns.lmplot(x='review_rating', y='review_likes',
               data=data_cleaned,
               fit_reg=False, scatter_kws={'marker': ['o', 'x', '*']})
    plt.xlabel('Review Rating')
    plt.ylabel('Review Likes')
    plt.title('lmplot for Review Rating and Review Likes')
    st.pyplot()
