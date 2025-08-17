from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # або ["http://localhost:5173"] для безпеки
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sizes = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]

class PenisSize(BaseModel):
    length: int
    rirth: int  # girth/обхват

    def count_size(self):
        width = self.rirth / 2
        if width in (47, 48, 49):
            return sizes[0]
        elif width in (50, 51):
            return sizes[1]
        elif width in (52, 53, 54):
            return sizes[2]
        elif width in (55, 56, 57):
            return sizes[3]
        elif width in (58, 59, 60):
            return sizes[4]
        elif width in (61, 62, 63, 64):
            return sizes[5]
        elif width in (65, 66, 67, 68):
            return sizes[6]
        else:
            return "Нема розміру"
        
@app.get("/")
def test():
    return "It works"

@app.post("/count")
def index(data: PenisSize):
    return {
        "length": data.length,
        "rirth": data.rirth,
        "size": data.count_size()
    }
