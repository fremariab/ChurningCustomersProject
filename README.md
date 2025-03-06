# Customer Churn Prediction System

## Overview
Customer retention is crucial for businesses, and understanding why customers leave (churn) can help companies take proactive measures. This project uses **machine learning** to predict customer churn, allowing businesses to **identify at-risk customers** and implement retention strategies before they leave.

## Impact
- **Reduces Revenue Loss:** Identifies customers who are likely to churn, helping businesses take preventive actions.
- **Optimizes Marketing Efforts:** Enables targeted marketing campaigns to retain high-risk customers.
- **Enhances Customer Experience:** Businesses can improve services based on churn patterns.
- **Data-Driven Decision Making:** Uses ML models to analyze behavioral trends and retention patterns.

## Features
- **Machine Learning Model** – A trained model to predict churn based on customer data.
- **Web Application** – A Flask-based UI for uploading customer details and receiving churn predictions.
- **Pre-trained Model** – Uses a pre-optimized `joblib` model for fast predictions.
- **Scalable Design** – Can be adapted for different industries (e.g., telecom, banking, SaaS, etc.).
- **User-Friendly Interface** – Simple input fields and prediction visualization.

## Project Structure
```
📦 Churning_Customers
 ┣ 📂 static                # CSS files for styling
 ┣ 📂 templates             # HTML templates for UI
 ┣ 📜 06532025_Churning_Customers.ipynb  # Jupyter Notebook for data analysis
 ┣ 📜 06532025_churning_customers.py     # Python script for processing churn data
 ┣ 📜 app.py                 # Flask application for churn prediction
 ┣ 📜 best_optimized_model.joblib  # Pre-trained churn prediction model
 ┣ 📜 fitted_scaler.joblib   # Data scaler for model input
 ┣ 📜 README.txt             # Existing documentation (to be replaced)
```

## Installation & Setup
### 1. Clone the Repository
```sh
git clone <repository-url>
cd Churning_Customers
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Run the Web App
```sh
python app.py
```
Access the application at **http://127.0.0.1:5000/**

## Usage
1. Open the web application.
2. Enter customer details (e.g., tenure, usage, payment history).
3. Click **Predict Churn** to see the likelihood of customer churn.
4. Take necessary actions based on the prediction results.

## Future Enhancements
- **Improved Model Accuracy** – Incorporate deep learning techniques for better predictions.
- **Integration with Business Dashboards** – Provide real-time insights on customer retention.
- **Automated Alerts** – Notify businesses when a customer is at risk of churning.

## Author
Developed by **Freda-Marie Beecham**

---
