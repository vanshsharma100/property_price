from fastapi import FastAPI,HTTPException
from pydantic import Field,BaseModel,computed_field,EmailStr,field_validator
from typing import Annotated,List,Optional,Literal
from fastapi.responses import JSONResponse
import json
from model.predict import predict_output


from schema.user_input import userinput

app= FastAPI()


@app.get("/")
def home():
    return {"message" : "property price prediction system"}

@app.get("/health")
def status():
    return {"status " : "OK"}


@app.post("/predict")
def predict_price(data:userinput):
    user_input={
        'area_sqft':data.area_sqft,
        "property_category":data.property_category,
        "property_type":data.property_type,
        "distance_hospital_km":data.distance_hospital_km,
        "distance_airport_km":data.distance_airport_km,
        "zone":data.zone,
        'tier_city':data.tier_city
    }

    try:
        prediction=predict_output(user_input)
        return JSONResponse(status_code=200,content={"approximate price of your property is":prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))