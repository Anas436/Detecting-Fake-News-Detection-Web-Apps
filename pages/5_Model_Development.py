import streamlit as st

st.set_page_config(page_title='News Classification',
                   page_icon=':globe_with_meridians:',
                   layout='centered')
                   
st.title('Model Development', anchor=None)
st.header(' ', divider='rainbow')

st.write('In the pursuit of creating an effective fake news detection model, I began by conducting comprehensive research to gain insight into the state of the art within the field. It quickly became evident that transfer learning methods were at the forefront, with the BERT model standing out as the most popular and promising choice. Motivated by this discovery, I made the decision to use the pretrained transfer learning BERT model for our project. But after facing the following challenges I had to change that decision.')
st.subheader('Computational Challenges')
st.write("As I delved into the model development process, I encountered a significant computational challenge. Due to the amount of data we were working with, surpassing 33,000 records, it was imperative to maintain uninterrupted training sessions that extended beyond the standard 12-hour runtime limitations on the platform I used to work on which is Kaggle. While initially working on Google Colab and Kaggle, I found that the BERT model's training process exceeded the allotted 12-hour window, largely owing to the sheer volume of content within each article. This issue forced me to look for other than the optimal solution.")
st.subheader('Switch to Article Titles')
st.write("To address this computational challenge, I tried to stick with the BERT model, so I considered a shift in approach. I tried using only titles as inputs to the model. However, I quickly realized that this approach had limitations. Titles, being concise and limited in content, lacked the necessary depth in information to produce an efficient fake news classification model. A significant concern was the potential for overfitting to the titles data, rendering the model less effective when presented with novel test data.")
st.subheader("Exploring Classification Models")
st.write("Given the aforementioned challenges, I decided to pivot towards machine learning classification models. The abundance of data—33,000 records—made this transition feasible. I experimented with several classifiers, including Passive Aggressive, XGBoost, and LightGBM, meticulously testing and evaluating their performance.")
st.subheader("Model Selection")
st.write("Ultimately, these classifiers yielded results that were quite similar in terms of performance metrics. To make a decision, I opted for the model that struck a balance between false and true recall scores while demonstrating robustness. This choice was pivotal in ensuring that our model effectively identified fake news without neglecting genuine articles.")
st.subheader("Training and Fine-Tuning")
st.write("With the selected classifier in hand, I embarked on the training process using both article content and titles together as inputs. Fine-tuning was carried out using Gridsearch to optimize model hyperparameters and enhance its overall performance. Rigorous testing, performed multiple times, validated the model's effectiveness. To mitigate overfitting concerns, I implemented a train-validation-test split methodology.")
st.subheader("Handling Data Imbalance")
st.write("Additionally, our dataset exhibited a significant class imbalance, with a True/Fake news ratio of 4:1. To tackle this issue, I employed the Balanced Weights method, one of the widely used methods for imbalanced classification models. It modifies the class weights of the majority and minority classes during the model training process to achieve better model results. Unlike the oversampling and under-sampling methods, the balanced weights methods do not modify the minority and majority class ratio. Instead, it penalizes the wrong predictions on the minority class by giving more weight to the loss function, ensuring that the model did not favor the majority class during training, thus enhancing its ability to handle imbalanced data effectively.")
