import streamlit as st
from PIL import Image

st.title('Project Workflow', anchor=None)

image = Image.open('./pictures/workflow.png')

st.image(image, caption='Project Workflow')
   