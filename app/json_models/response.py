from pydantic import BaseModel

class Response(BaseModel):
    prediction: str
    probability: float