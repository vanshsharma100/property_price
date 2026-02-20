import joblib
import pandas as pd

model=joblib.load("model/prop_model.joblib")

def predict_output(user_input:dict):
    input_df=pd.DataFrame([user_input])
    output=float(model.predict(input_df)[0])
    return output