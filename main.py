from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is working"}

@app.get("/predict")
def predict(id: int):
    return {"received_id": id}
