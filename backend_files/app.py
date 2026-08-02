
from flask import Flask, Blueprint, request, jsonify
import joblib
import pandas as pd

# Initialize Flask application
app = Flask(__name__)

# Create API blueprint with base path
api = Blueprint("api", __name__, url_prefix="/superkart-backend/v1")

# Load the serialized model
model = joblib.load("superkart_model.joblib")


@app.route("/")
def home():
    return "Sales Prediction API is Running!"


@app.route("/predict", methods=["POST"])
def predict():

    # Read JSON data
    data = request.get_json()

    # Convert JSON into DataFrame
    df = pd.DataFrame([data])

    # Make prediction
    prediction = model.predict(df)

    # Return prediction
    return jsonify({
        "Predicted_Product_Store_Sales_Total": round(float(prediction[0]), 2)
    })

#defining host and port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)
