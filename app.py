import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from utils.image_utils import preprocess_image, predict_deficiency
from utils.translator import translate_text

CLASS_NAMES = ["Iron Deficiency", "Vitamin B12 Deficiency", "Omega-3 Deficiency", "Protein Deficiency", "Normal"]
DIET_TIPS = {
    "Iron Deficiency": "Eat spinach, jaggery, lentils, red meat.",
    "Vitamin B12 Deficiency": "Include eggs, dairy, fish, fortified cereals.",
    "Omega-3 Deficiency": "Consume flaxseeds, walnuts, fatty fish.",
    "Protein Deficiency": "Add pulses, dairy, soybeans, nuts.",
    "Normal": "You appear healthy. Maintain a balanced diet!"
}

st.set_page_config(page_title="Nutrient Deficiency Detector", layout="centered")
st.title("🔍 Nutrient Deficiency Detector")

lang_option = st.selectbox("🌐 Choose Language", ["English", "Hindi", "Marathi"])
lang_map = {"English": "en", "Hindi": "hi", "Marathi": "mr"}
selected_lang = lang_map[lang_option]

model = load_model("models/nutrient_model.h5")

uploaded_file = st.file_uploader("📤 Upload a clear face image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_column_width=True)
    img, arr = preprocess_image(image)

    if model:
        prediction, confidence = predict_deficiency(model, arr, CLASS_NAMES)
        result = f"Detected: {prediction} ({confidence*100:.1f}%)"
        tip = DIET_TIPS[prediction]
        st.subheader(translate_text(result, selected_lang))
        st.success(translate_text(tip, selected_lang))

st.markdown("---")
st.caption("📌 Note: This is an AI-based assistive tool. Always consult a doctor for serious concerns.")
