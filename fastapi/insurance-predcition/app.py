from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from functools import lru_cache
import json

app = FastAPI()


# Load Patient Data
@lru_cache()
def load_patient_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data


patient_data = load_patient_data()


@app.get("/")
def home():
    return {"Message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"Message": "This is a FastAPI Demo on Patients Data"}


@app.get("/view")
def get_patient_data():
    return patient_data


@app.get("/view_patient/{patient_id}")
def view_patient(
    patient_id: str = Path(..., description="ID of the Patient", example="P001"),
):
    if patient_id in patient_data:
        return patient_data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")













