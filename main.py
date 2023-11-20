import streamlit as st

from api import get_title, get_explanation, get_copy

st.title("Astronomy picture of the day ")

title = get_title()
st.text(title)

st.image("image.jpg")
copy = get_copy()
st.text(copy)

description = get_explanation()
st.write(description)
