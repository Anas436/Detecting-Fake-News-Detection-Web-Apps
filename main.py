import streamlit as st
import base64

st.set_page_config(page_title='Title',
                   page_icon=':globe_with_meridians:',
                   layout='centered')

st.header('Fake News Classification.', anchor=False)

text_user = st.text_area(label='text_label',
                         value='Insert a news title here.',
                         disabled=False,
                         label_visibility='hidden')


run_button = st.button('Classify')
if run_button:
    st.text('True: 0.6')
    st.text('False: 0.4')
else:
    st.text('Classification results.')



@st.cache(allow_output_mutation=True)
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

