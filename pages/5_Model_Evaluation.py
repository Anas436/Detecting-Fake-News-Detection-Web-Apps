import streamlit as st
import pandas as pd

st.set_page_config(page_title='Title',
                   page_icon=':globe_with_meridians:',
                   layout='centered')

st.title('Model Evaluation', anchor=None)
st.write('The culmination of our model development efforts led to an impressive performance in the evaluation phase. The final evaluation of the model yielded the following results:')
st.markdown(
"""
- Final Model Accuracy on test set:  0.99
- Final Model Precision on test set:  1.00
- Final Model Recall on test set:       0.99
- Final Model F1-Score on test set:  0.99

"""
)


st.write("These metrics highlight the exceptional capabilities of our model in distinguishing between genuine and fake news articles. It showcases a remarkable accuracy rate of 99%, underlining the model's ability to make correct predictions. Additionally, a precision score of 1.00 signifies the identification of fake news, with very few false positives. The recall score of 0.99 underscores the model's proficiency in capturing almost all instances of fake news within the dataset. The F1-score, which balances precision and recall, solidifies the overall robustness of our model.")
st.subheader('Classification Report')
st.write("To further dissect the model's performance, we provide a comprehensive classification report:")

# initialize data of lists.
data = {'precision ': ['0.98', '1.00', ' ', '0.99', '0.99'],
        'recall ': ['0.98', '0.99', ' ', '0.99', '0.99'],
        'f1-score': ['0.98', '0.99', '0.99', '0.99', '0.99'],
        'support': ['1129', '5350', '6479', '6479', '6479']
        }
  
# Create DataFrame
df = pd.DataFrame(data, index=['class 0 (Fake)','class 1 (Real)', 'accuracy', 'macro avg', 'weighted avg'])
st.write(df)

st.write("This classification report provides a more detailed breakdown of our model's performance for each class. For class 0 (representing genuine news), the model exhibits a precision and recall of 0.98, resulting in a balanced F1-score of 0.98. Class 1 (representing fake news) displays exemplary precision, recall, and F1-score values, all at 1.00. These metrics affirm the model's exceptional ability to accurately classify both genuine and fake news articles.")
st.write('While these numbers can mean that the model overfitting the data. In order to ensure the model’s consistency I tried to use the same model with the same technique and train it on a different dataset from kaggle competition Fake News. You can check the results. For Public Score is 0.98012, and for Private Score is 0.97609 which is very consistent on different test sets as well as with the same 0.98 accuracy I got while testing the model before submission.')
st.write('In conclusion, the model evaluation phase solidifies the efficacy of our fake news detection model, demonstrating its accuracy, precision, recall, and overall robustness.')