from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LinearRegression

app = FastAPI(
    title="W12D1 MLOps ML API",
    version="1.0.0",
    description="Containerised machine learning prediction API",
)


# Small deterministic training dataset for demonstration.
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

model = LinearRegression()
model.fit(X, y)


class PredictionRequest(BaseModel):
    feature: float


@app.get("/")
def root():
    return {
        "message": "W12D1 MLOps ML API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": "LinearRegression",
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    prediction = model.predict([[request.feature]])[0]

    return {
        "feature": request.feature,
        "prediction": round(float(prediction), 4),
    }