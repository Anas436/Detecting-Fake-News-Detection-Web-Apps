import streamlit as st
from PIL import Image
from pathlib import Path

image = Image.open('./pictures/workflow.PNG')

st.image(image, caption='Sunrise by the mountains')
   