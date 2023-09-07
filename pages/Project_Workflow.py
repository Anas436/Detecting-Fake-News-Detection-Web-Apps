import streamlit as st
from PIL import Image

image = Image.open('../pictures/workflow.PNG')

st.image(image, caption='Sunrise by the mountains')
   