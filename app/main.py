from fastapi import FastAPI, File, UploadFile
from fastai.vision.all import *
from utils import read_image, predict_hotdog

app = FastAPI()

@app.post("/predict/")
async def predict(myfile: UploadFile = File(...)):
    image = read_image(await myfile.read())

    return predict_hotdog(image)