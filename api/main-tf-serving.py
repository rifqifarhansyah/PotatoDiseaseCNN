from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from PIL import Image

import uvicorn
import numpy as np
import tensorflow as tf
import requests

app = FastAPI()

endpoint = "https://localhost:8502/v1/models/potatoes_model:predict"

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    return np.array(Image.open(BytesIO(data)))

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    image_batch = np.expand_dims(image, 0)
    
    json_data = {
        "instances": image_batch.tolist()
    }
    
    response = requests.post(endpoint, json=json_data)
    prediction = np.array(response.json()["predictions"][0])
    
    predicted_class = CLASS_NAMES[np.argmax(prediction)]    
    confidence = np.max(prediction)
    return{
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)