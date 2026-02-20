import streamlit as st
import requests

url="http://127.0.0.1:8000/predict"


st.set_page_config(page_title="property prices", layout="wide")
st.title('property prices')
st.markdown("Enter your requirments")


area_sqft = st.number_input("Area(sq ft)", min_value=0, step=1, value=0)
location=st.selectbox("location",['Noida', 'Dwarka', 'Faridabad', 'Saket', 'Gurgaon', 'Ghaziabad',
       'Vasant Kunj', 'Greater Noida', 'Rohini'])
property_category=st.selectbox("property category",['Apartment', 'Farmhouse', 'Residential'])
property_type=st.selectbox("property type",['3BHK', 'Commercial', 'Villa', '1BHK', '2BHK'])
distance_hospital_km=st.number_input("distance from hospital (at least)",min_value=0, step=1, value=0)
distance_airport_km=st.number_input("distance form airport(at least)",min_value=0,step=1,value=0)
zone=st.selectbox("Zone",['Urban', 'Semi-Urban'])

if st.button("predict price"):
    input_data={
        "area_sqft":area_sqft,
        "location":location,
        "property_category":property_category,
        "property_type":property_type,
        "distance_hospital_km":distance_hospital_km,
        "distance_airport_km":distance_airport_km,
        "zone":zone
        }
    try:
        response=requests.post(url,json=input_data)
        if response.status_code==200:
            result=response.json()
            price = result["approximate price of your property is"]

            st.success(f"Approximate price of your requirements is ₹ {price:,.2f} lakh")
           
        else:
            st.error(f"API error {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("could not connect with server")
        
    


