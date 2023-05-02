import streamlit as st
from PIL import Image

st.title('にもアプリ')
st.caption('これはにものテストアプリ')

image = Image.open('./data/図1.jpg')
st.image(image, width=200)