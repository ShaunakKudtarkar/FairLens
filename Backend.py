"""
FairLens Backend using FastAPI

Run:
pip install fastapi uvicorn pandas scikit-learn python-multipart
uvicorn main:app --reload

Docs:
http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
app = FastAPI(title="FairLens API")
dataset = None
model = None
@app.get("/")
def health():
return {"status": "running", "service": "FairLens FastAPI"}
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
global dataset

```
try:
    dataset = pd.read_csv(file.file)
    return {
        "message": "Dataset uploaded",
        "rows": len(dataset),
        "columns": list(dataset.columns)
    }
except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
```
@app.post("/audit")
def audit():
global dataset

```
if dataset is None:
    raise HTTPException(status_code=400, detail="Upload dataset first")

return {
    "total_rows": len(dataset),
    "missing_values": int(dataset.isnull().sum().sum()),
    "columns": list(dataset.columns)
}
```
@app.post("/bias")
def bias():
global dataset

```
if dataset is None:
    raise HTTPException(status_code=400, detail="Upload dataset first")

if "gender" not in dataset.columns or "approved" not in dataset.columns:
    raise HTTPException(
        status_code=400,
        detail="Dataset must contain 'gender' and 'approved'"
    )

male_rate = dataset[dataset["gender"] == "M"]["approved"].mean()
female_rate = dataset[dataset["gender"] == "F"]["approved"].mean()

return {
    "male_rate": float(male_rate),
    "female_rate": float(female_rate),
    "bias_difference": abs(float(male_rate - female_rate))
}
```
@app.post("/mitigate")
def mitigate():
return {
"message": "Bias mitigation applied (demo)",
"method": "reweighing (simulated)"
}
@app.post("/train")
def train():
global dataset, model

```
if dataset is None:
    raise HTTPException(status_code=400, detail="Upload dataset first")

try:
    X = dataset.drop("approved", axis=1).select_dtypes(include=["number"])
    y = dataset["approved"]

    if X.empty:
        raise HTTPException(status_code=400, detail="No numeric features found")

    model = RandomForestClassifier()
    model.fit(X, y)

    return {
        "message": "Model trained",
        "features_used": list(X.columns)
    }

except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
```
@app.post("/predict")
def predict(data: dict):
global model

```
if model is None:
    raise HTTPException(status_code=400, detail="Train model first")

try:
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]

    return {
        "input": data,
        "prediction": int(prediction)
    }

except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
```
@app.post("/explain")
def explain():
global model

```
if model is None:
    raise HTTPException(status_code=400, detail="Train model first")

return {
    "message": "Explainability generated (SHAP/LIME placeholder)"
}
```

