import streamlit as st
import pandas as pd

st.title('Book Search App')

# Load data from JSON file
data = pd.read_json('data/books.json')

# Display the data in a table
st.write(data)

# Optional: Checkbox to show raw data
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(data)
