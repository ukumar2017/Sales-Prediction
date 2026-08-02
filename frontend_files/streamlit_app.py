
import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Sales Prediction App")

st.title("Product Store Sales Prediction")

st.write("Enter the product and store details below.")

# User Inputs
product_weight = st.number_input("Product Weight", value=10.0)

product_sugar_content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

product_allocated_area = st.number_input(
    "Product Allocated Area",
    value=0.02,
    format="%.3f"
)

product_type = st.selectbox(
    "Product Type",
    [
        "Dairy",
        "Snack Foods",
        "Household",
        "Frozen Foods",
        "Soft Drinks",
        "Fruits and Vegetables",
        "Baking Goods",
        "Health and Hygiene"
    ]
)

product_mrp = st.number_input("Product MRP", value=250.0)

store_id = st.selectbox(
    "Store ID",
    [
        "OUT010",
        "OUT013",
        "OUT017",
        "OUT018",
        "OUT019",
        "OUT027",
        "OUT035",
        "OUT045",
        "OUT046",
        "OUT049"
    ]
)

store_establishment_year = st.number_input(
    "Store Establishment Year",
    value=1999
)

store_size = st.selectbox(
    "Store Size",
    ["Small", "Medium", "High"]
)

store_location = st.selectbox(
    "Store Location Type",
    ["Tier 1", "Tier 2", "Tier 3"]
)

store_type = st.selectbox(
    "Store Type",
    [
        "Supermarket Type1",
        "Supermarket Type2",
        "Supermarket Type3",
        "Grocery Store"
    ]
)

if st.button("Predict Sales"):

    data = {
        "Product_Weight": product_weight,
        "Product_Sugar_Content": product_sugar_content,
        "Product_Allocated_Area": product_allocated_area,
        "Product_Type": product_type,
        "Product_MRP": product_mrp,
        "Store_Id": store_id,
        "Store_Establishment_Year": store_establishment_year,
        "Store_Size": store_size,
        "Store_Location_City_Type": store_location,
        "Store_Type": store_type
    }

    API_URL = "http://localhost:9090/v1/predict"

    response = requests.post(API_URL, json=data)

    if response.status_code == 200:
        prediction = response.json()

        st.success(
            f"Predicted Sales: ₹ {prediction['Predicted_Product_Store_Sales_Total']:.2f}"
        )
    else:
        st.error("Unable to get prediction from backend API.")
