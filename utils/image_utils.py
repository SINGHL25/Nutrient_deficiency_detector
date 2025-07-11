import numpy as np
from PIL import Image
import tensorflow as tf

# Load the trained Keras model (place this path correctly in app.py too)
model = tf.keras.models.load_model("models/nutrient_model.h5")

# List of nutrient classes (you can customize these based on your training)
NUTRIENT_CLASSES = [
    "Healthy",
    "Iron Deficiency",
    "Vitamin B12 Deficiency",
    "Vitamin D Deficiency",
    "Protein Deficiency"
]

def process_image_and_predict(uploaded_image):
    """Takes a PIL Image, processes it, and returns the prediction label"""
    img = uploaded_image.resize((224, 224))  # Match your model input size
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    prediction = model.predict(img_array)[0]
    predicted_index = np.argmax(prediction)
    confidence = round(float(np.max(prediction)) * 100, 2)

    return NUTRIENT_CLASSES[predicted_index], confidence

