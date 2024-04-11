import streamlit as st
from tokeniser import tokeniser

st.title("Agent Messaging Arch")
st.markdown("# List Your Product")

image_file = st.file_uploader("Upload your picture:",
                              type=['png','jpg','jpeg'])
if image_file is not None:
    image_file.seek(0)
    st.image(image_file, caption='Uploaded Image', use_column_width=True)

data1 = st.text_input("Data 1:")
data2 = st.text_input("Data 2:")
data3 = st.text_input("Data 3:")
data4 = st.text_input("Data 4:")
data5 = st.text_input("Data 5:")

if st.button('Submit'):
    if image_file is not None:
        tokeniser(image_file, data1, data2, data3, data4, data5)
        st.success("Data added successfully to the Excel file.")
    else:
        st.error("Please upload an image.")