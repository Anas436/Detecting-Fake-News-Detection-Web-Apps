import streamlit as st

st.set_page_config(page_title='Title',
                   page_icon=':globe_with_meridians:',
                   layout='centered')
                   
st.title('Introduction', anchor=None)
st.header(' ', divider='rainbow')
st.write("The data collection phase is a crucial step in the development of any machine learning model, especially in the context of fake news detection. In this report, we outline the data collection process and sources used for our Fake News Detection Project. This report provides an overview of the sources, methods, and outcomes.")
st.subheader("Data Sources")
st.write("Our data collection effort focused on two categories of sources:")
st.markdown(
"""
- **Reliable News Sources:**
    - The New Dawn Liberia
    - GNN Liberia
    - The Bush Chicken
"""
)
st.write("These sources primarily contain true and real news data. They served as the basis for collecting genuine articles.")
st.markdown(
"""
- **Fact-Checking Websites:**
    - GhanaFact
    - The International Center for Investigative Reporting (ICIR) Nigeria
    - Fact Check Hub
    - AFP Fact Check
"""
)
st.write("Fact-checking websites typically focus on debunking fake news, but they may also contain instances of true information. We used these sources to collect fake news articles.")
st.subheader("Data Collection Methodology")
st.write("To gather data from the selected sources, we employed a Python-based web scraping approach using the Scrapy library. Our data collection process involved the following steps:")
st.markdown(
"""
- Website Scraping: We scraped almost all the articles from each selected website. The key data points collected included titles, authors, article content, publication dates, article links, and labels indicating whether the article was true or false.
- Data Organization: The scraped data was organized and structured, and we ensured that each article was associated with its corresponding source.
"""
)
st.subheader("Outcome")
st.write("Through our data collection efforts, we were able to compile a substantial dataset for our Fake News Detection Project. The dataset consists of approximately:")
st.markdown(
"""
- 27,000 Real Articles: These articles were collected from reliable news sources and represent authentic news stories.
- 6,000 Fake Articles: These articles were collected from fact-checking websites and include instances of both fake and true information. This diversity is essential for training and evaluating our fake news detection model.
"""
)
st.subheader("Conclusion")
st.write("The success of our Fake News Detection Project heavily relies on the quality and diversity of the dataset. Our data collection process resulted in a comprehensive dataset containing both genuine and fake news articles. This dataset will serve as the foundation for training, validating, and testing our machine learning model.")
st.write("As we move forward with the project, the next steps will involve exploratory data analysis, data preprocessing, model development, evaluation, integration and deployment. The robustness of our model will be trained and tested against this dataset to identify and classify fake news articles accurately.")
st.write("This data collection effort represents a critical milestone in our project, and we are well-prepared to proceed with the model development phase.")