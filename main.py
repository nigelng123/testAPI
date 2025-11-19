from fastapi import FastAPI

app = FastAPI()

@app.get("/predict")
def predict(id: str):
    score = sum([ord(c) for c in id]) % 100
    return {
        "id": id,
        "prediction" : score,
        "message":"API is working!"
    }

@app.get("/")
def root():
    return {"status": "ok", "message": "Hello from Render test API!"}