from typing import Dict
from io import BytesIO
import numpy as np
from PIL import Image
from fastai.vision.all import *

def read_image(file: bytes) -> PILImage:
    img = Image.open(BytesIO(file))
    fastimg = PILImage.create(np.array(img.convert('RGB')))

    return fastimg

def is_hotdog(x):
    return "frankfurter" in x or "hotdog" in x or "chili-dog" in x

def predict_hotdog(image) -> Dict:
    path = Path()
    inference_model = load_learner(path/'models/model.pkl')
    is_hotdog, _ , probs = inference_model.predict(image)
    if probs[1] > 0.5:
        return {
            "prediction": "hotdog",
            "probability": probs[1].item()
        }
    
    return {
        "prediction": "not hotdog",
        "probability": probs[0].item()
    }
