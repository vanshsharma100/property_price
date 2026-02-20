# 🏠 Property Price Prediction System

An end-to-end Machine Learning project that predicts property prices using advanced regression techniques.  
The project includes model training, FastAPI backend, and Streamlit frontend deployment.

---

## 📌 Project Overview

This project uses historical property data to build a predictive model that estimates real estate prices based on:

- Area (sq ft)
- Location
- Number of Bedrooms
- Number of Bathrooms
- Amenities
- City Tier

The model is trained using advanced ensemble techniques and deployed as a REST API using FastAPI.

---

## 🧠 Machine Learning Pipeline

- Data Cleaning & Preprocessing
- Feature Engineering
- Handling Missing Values
- Encoding Categorical Variables
- Scaling Numerical Features
- Model Training (Stacking Regressor)
- Model Evaluation (R² Score, MAE, RMSE)
- Model Saving using Joblib

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Pydantic
- Streamlit
- Uvicorn
- Joblib


---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/property-price-prediction.git
cd property-price-prediction


2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate



3️⃣ Install Dependencies
pip install -r requirements.txt



▶️ Run FastAPI Server
uvicorn app:app --reload
Open:
http://127.0.0.1:8000/docs

🎨 Run Streamlit App
streamlit run streamlit_app.py


click the generated link
