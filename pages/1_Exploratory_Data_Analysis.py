import streamlit as st

st.title('Exploratory Data Analysis (EDA)', anchor=None)
st.header(' ', divider='rainbow')
st.write('In the initial stages of our project, we conducted an extensive Exploratory Data Analysis (EDA) to gain insights into the dataset. This critical phase allowed us to better understand our data, identify patterns, and make informed decisions for subsequent project steps. Below is a concise summary of our EDA process:')


st.markdown(
"""
The following list won't indent no matter what I try:
- **Data Overview:**
    - Our dataset consists of a total of 33,673 entries and 605 columns, with data types including datetime, float, and object.
    - Several columns contained a significant number of missing values.
- **Data Cleaning:**
    - We removed columns with entirely missing data and applied different strategies to handle missing values in other columns, ensuring data integrity.
    - Prior to data cleaning, our dataset consisted of 33,673 entries, with a mixture of fake and real news articles.
    - The "Label" column indicated that we had 6,115 fake news articles and 27,557 real news articles.
    - After thorough data cleaning, which involved handling missing values and text preprocessing, our dataset remained robust and ready for analysis.
    - The "Label" column revealed that we had 5,646 fake news articles and 26,927 real news articles.
    - The data cleaning process resulted in a decrease in the number of fake news articles. This reduction is attributed to the removal of rows with significant missing data and other cleaning strategies applied to improve data quality.
- **Text Preprocessing:**
    - We employed several text preprocessing techniques, including:
        - Removing punctuation and special characters.
        - Converting text to lowercase.
        - Tokenization: Splitting text into individual words.
        - Removing stopwords: Common words like "the," "and," and "is" that do not contribute significantly to analysis.
        - Lemmatization: Reducing words to their base or root form.
- **Word Cloud Visualization:**
    - We created word clouds to visually represent the most frequently occurring words in the textual data. This visualization technique provides an intuitive understanding of the dataset's content.
- **Date Analysis:**
    - We extracted and analyzed date-related information from the dataset. This included identifying the minimum and maximum years present in the data, which were 2011 and 2023, respectively.
    - Furthermore, we examined the dataset for patterns related to fake news generation:
        - Fake news articles exhibited temporal patterns, with March and April being the months with the highest number of publications.
        - In terms of days, the 2nd and 3rd of the month were the most common days for fake news articles to be generated.
- **Insights on Publisher:**
    - Most fake news articles were published by the "poynter" publisher.
    - "poynter" significantly outpaced other publishers in terms of publishing fake news articles.
"""
)

st.subheader('Conclusion:', anchor=None)
st.write("The EDA phase was instrumental in understanding our dataset's structure and content. We successfully cleaned the data, preprocessed text, and derived valuable insights. These insights will guide our subsequent project steps, including feature engineering, model building, and evaluation.")
st.write('Our commitment to thorough EDA ensures that we approach the project with a solid foundation, setting the stage for accurate analysis and meaningful results.')
