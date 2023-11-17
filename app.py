from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

# Initialize Flask application
app = Flask(__name__)

# Load the trained model from the specified file
model_path = "best_optimized_model.joblib"
best_optimized_model = joblib.load(model_path)

# Load the fitted scaler from the specified file
scaler_path = "fitted_scaler.joblib"
scaler = joblib.load(scaler_path)

# Selected features used in the input form
selected_features = [
    "MonthlyCharges",
    "TotalCharges",
    "tenure",
    "gender",
    "Partner",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
]


# Define the route for the home page
@app.route("/")
def home():
    # Render the home page and pass the selected features to the template
    return render_template("index.html", selected_features=selected_features)


# Define the route for handling predictions
@app.route("/predict", methods=["POST"])
def predict():
    # Check if the request method is POST
    if request.method == "POST":
        # Retrieve input values from the form and convert to float or int as needed
        values = []
        for feature in selected_features:
            if feature == "TotalCharges" or feature == "MonthlyCharges":
                values.append(float(request.form[feature]))
            elif feature == "tenure":
                values.append(int(request.form[feature]))
            else:
                values.append(request.form[feature])

        # Create a DataFrame from user input
        user_data = pd.DataFrame([values], columns=selected_features)

        # Scale the user input using the fitted scaler
        scaled_data = pd.DataFrame(
            scaler.transform(user_data), columns=user_data.columns
        )

        # Make predictions using the loaded model
        prediction = best_optimized_model.predict(scaled_data)

        prediction_class = "No"

        if prediction >= 0.5:
            prediction_class = "Yes"

        # Display the result on the prediction.html page
        # return render_template("prediction.html", prediction_class=prediction[0])
        return render_template("prediction.html", prediction_class=prediction_class)


# Run the Flask application if this script is the main module
if __name__ == "__main__":
    app.run(debug=True)
