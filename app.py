import streamlit as st
from PIL import Image, ImageOps

from predict import predict

# Sidebar sample images
side_image_fresh_l = Image.open('data/optional_data/sample_fresh_leaf.jpg')
side_image_dis_l = Image.open('data/optional_data/sample_dis_leaf.jpg')
side_image_fresh_p = Image.open('data/optional_data/sample_fresh_plant.jpg')
side_image_dis_p = Image.open('data/optional_data/sample_dis_plant.jpg')
# Main Template image
template_image = Image.open('data/optional_data/agri_drone1.jpg')

# Add sidebar title text and images
st.sidebar.title('Sample images')
st.sidebar.markdown('*Fresh leaf:*')
st.sidebar.image(side_image_fresh_l, use_column_width=True)
st.sidebar.markdown('*Diseased leaf:*')
st.sidebar.image(side_image_dis_l, use_column_width=True)
st.sidebar.markdown('*Fresh plant:*')
st.sidebar.image(side_image_fresh_p, use_column_width=True)
st.sidebar.markdown('*Diseased plant:*')
st.sidebar.image(side_image_dis_p, use_column_width=True)

# Add streamlit title, add descriptions and load the main template image
st.title('Cotton Disease Prediction')
st.markdown('*This model identifies whether cotton disease is present based on plant & leaf pictures.*')
st.image(template_image, use_column_width=True)
st.write('')
st.markdown('**Upload a Cotton Plant or Leaf picture ...**')

# Upload image through file uploader
uploaded_image = st.file_uploader('Upload Image', type="jpg")
if uploaded_image is not None:
    u_image = Image.open(uploaded_image)
    st.image(u_image, caption='Uploaded Image', use_column_width=True)
    st.write('')
    st.markdown('**Prediction:**')
    # Label prediction
    prediction = predict(u_image)
    st.write(prediction)