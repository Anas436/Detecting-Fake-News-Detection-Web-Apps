import streamlit as st
from PIL import Image

st.set_page_config(page_title='News Classification',
                   page_icon=':globe_with_meridians:',
                   layout='centered')

st.title('Project Workflow', anchor=None)
st.header(' ', divider='rainbow')

image = Image.open('./pictures/workflow.png')

st.image(image, caption='Project Workflow')
   