import streamlit as st
from PIL import Image
from summa import summarizer
import pytesseract

# Add title on the page
st.title("Text summarization from Image")

# Ask user for uploaded image
uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# Check if an image is uploaded
if uploaded_image is not None:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

    # Perform OCR using Tesseract on the uploaded image
    image_data = Image.open(uploaded_image)
    extracted_text = pytesseract.image_to_string(image_data)

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.write(extracted_text)

    # Summarization ratio slider
    ratio = st.slider("Summarization fraction", min_value=0.0, max_value=1.0, value=0.2, step=0.01)

    # Perform text summarization
    summarized_text = summarizer.summarize(extracted_text, ratio=ratio, language="english", split=True, scores=True)

    # Display the summarized text
    st.subheader("Summarized Text:")
    for sentence, score in summarized_text:
        st.write(sentence)
