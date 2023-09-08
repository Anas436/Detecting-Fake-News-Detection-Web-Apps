import streamlit as st

st.title('Detecting Fake news using AI', anchor=None)
st.header(' ', divider='rainbow')

st.subheader('Project Background', divider='rainbow')
st.write('Fake news poses a severe threat to the integrity of information dissemination in Liberia. With the increasing availability of social media platforms and the rapid sharing of information, distinguishing between authentic news and fake news has become increasingly challenging for the general public.')
st.write('Liberia, like many other countries in West Africa, has faced detrimental effects of misinformation and disinformation, which have led to social unrest, political instability, and public mistrust. Given that the nation is preparing for its national elections in October 2023, there will likely be a surge of misinformation from politicians in the media. This has the potential to disrupt Liberia’s democracy and plunge the nation into a crisis similar to the one it suffered 33 years ago.')
st.write('To combat this problem, there is a need to leverage the power of artificial intelligence (AI), which can be a transformative solution by using AI algorithms and machine learning techniques.')
st.write('Consequently, misinformation can spread rapidly, causing confusion, divisiveness, and even harm to individuals and communities as seen in the case of the 2020 senatorial election.         The need for an AI-powered solution arises to alleviate the burden on individuals to manually fact-check and verify news articles by harnessing the capabilities of machine learning and AI.')

st.subheader('Project goals', divider='rainbow')
st.write('The primary objective of the Fake News Detection project in Liberia is to develop an automated system that can analyze news content, identify patterns, and assess the credibility of information, thereby enabling citizens to make more informed decisions. These are a few of the goals of this project:')

st.markdown(
"""
- **Dataset Collection:**
    - Gather a diverse and representative dataset consisting of both legitimate news articles and examples of fake news prevalent in Liberia. This dataset will serve as the foundation for training and evaluating the AI models.
- **Model Development:**
    - Employ various machine learning techniques, such as natural language processing (NLP) to design and train models capable of distinguishing between authentic and fake news articles. The models will learn from the patterns and features present in the dataset to make accurate predictions.
- **Evaluation and Optimization:**
    - Evaluate the performance of the developed models using appropriate metrics such as precision, recall, and accuracy. Continuously refine and optimize the models to enhance their accuracy and effectiveness in detecting fake news.
- **User-Friendly Interface:**
    - We created word clouds to visually represent the most frequently occurring words in the textual data. This visualization technique provides an intuitive understanding of the dataset's content.
- **Date Analysis:**
    - Create an intuitive and user-friendly interface that allows users to input news articles and receive real-time feedback on the credibility of the information. The interface should provide clear indicators and explanations regarding the factors contributing to the classification of an article as authentic or fake.
"""
)



