from fastapi import FastAPI, File, UploadFile
from fastai.vision.all import *
from utils import read_image, predict_hotdog
from json_models.response import Response

app = FastAPI()

@app.post("/predict/", response_model=Response)
async def predict(myfile: UploadFile = File(...)):
    image = read_image(await myfile.read())

    return predict_hotdog(image)