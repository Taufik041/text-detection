import io
import pandas as pd
import streamlit as st
from google.cloud import vision_v1
from google.cloud.vision_v1 import types



client = vision_v1.ImageAnnotatorClient()



# To use images from a folder

# content1 = io.open('./images/example.png','rb')
# content = content1.read()
# image = vision_v1.types.Image(content=content)
# response  = client.text_detection(image=image)


uploaded_file = st.camera_input(label='Input Image')

if uploaded_file is not None:
    content = uploaded_file.getvalue()
    image = vision_v1.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    st.write(texts[0].description)
