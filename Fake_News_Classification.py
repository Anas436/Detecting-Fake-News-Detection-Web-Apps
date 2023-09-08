import streamlit as st
import base64
import sklearn
import pickle
import clean

st.set_page_config(page_title='Title',
                   page_icon=':globe_with_meridians:',
                   layout='centered')
                   

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('pictures/background.jpg')


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


xgb_model_loaded = pickle.load(open('models/Best_LGBMClassifier_Final_model_X1.pkl', "rb"))
tf_idf = pickle.load(open('models/Best_tfidf_vectorizer_Final_model_X1.pkl', "rb"))

st.header('Fake News Classification.', anchor=False)

text_input = st.text_area(label='text_label',
                         value='Paste news text here.',
                         disabled=False,
                         height=400,
                         label_visibility='hidden')


run_button = st.button('Classify')

clean_text = clean.pipline_cleaning_step(text_input)
text_tf_idf = tf_idf.transform([clean_text])
pred = xgb_model_loaded.predict_proba(text_tf_idf)
label_0 = "{0:0.4f}".format(pred[0][0])
label_1 = "{0:0.4f}".format(pred[0][1])
if run_button:
    st.write('True: ', label_1)
    st.write('Fake: ', label_0)    
else:
    st.text('Classification results.')


