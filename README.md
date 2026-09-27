# 🌾 AgriYield – Smart Crop Yield Prediction


## 🚀 Live Application - 

You can access the deployed Streamlit application here:  
https://cropyieldpredictionapp-2tmqqj575w9a2etdym9hpz.streamlit.app/

## 📌 Project Overview

**AgriYield** is a Machine Learning project that analyzes historical agricultural data and predicts crop yield based on important agricultural factors.

The project uses **Linear Regression** and is deployed as an interactive **Streamlit web application**.

## 🎯 Objectives

- Analyze historical agricultural data
- Understand factors affecting crop yield
- Preprocess and prepare the dataset
- Apply Machine Learning using Linear Regression
- Evaluate the model using R² and MAE
- Develop an interactive Streamlit application
- Predict crop yield based on user inputs

## 📊 Dataset

The dataset contains information about agricultural production, including:

- 🌾 Crop Type
- 🌍 Geographical Area
- 📅 Year
- 🌧️ Average Rainfall
- 🧪 Pesticide Usage
- 🌡️ Average Temperature
- 📈 Crop Yield (`hg/ha_yield`)

The target variable is **`hg/ha_yield`**, which represents crop yield measured in hectograms per hectare.

## 🤖 Machine Learning Model

The project uses **Linear Regression** for crop yield prediction.

### Model Workflow

1. Load the agricultural dataset
2. Inspect and clean the data
3. Remove duplicate records
4. Separate features and target variable
5. Apply one-hot encoding to categorical variables
6. Split the data into training and testing sets
7. Train the Linear Regression model
8. Evaluate the model
9. Save the trained model
10. Use the model in the Streamlit application

## 📈 Model Performance

| Metric | Value |
|---|---:|
| R² Score | 0.7599 |
| MAE | 29,491.16 hg/ha |

The model achieved an R² score of approximately **0.76** on the test data.

## 🖥️ Streamlit Application

The project includes an interactive Streamlit application where users can enter:

- Area
- Crop Type
- Year
- Average Rainfall
- Average Temperature
- Pesticide Usage

The application then provides an **estimated crop yield**.

### Application Sections

- 🏠 **Home** – Project introduction and model information
- 📖 **About / How It Works** – Project workflow
- 🤖 **Model / Prediction** – Enter values and predict crop yield
- 📊 **Insights** – Dataset analysis and visualizations

## 📊 Data Visualizations

The project includes visualizations such as:

- Crop yield distribution
- Crop yield by crop type
- Average crop yield over years
- Rainfall vs crop yield
- Correlation heatmap
- Actual vs predicted crop yield

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Linear Regression
- Streamlit
- Jupyter Notebook
- GitHub

## 📁 Project Structure

```text
AgriYield/
│
├── CROP_DATASET.xlsx
├── crop_app.py
├── crop_yield_model.pkl
├── feature_columns.pkl
├── requirements.txt
└── README.md
```

## 🔮 Future Enhancements
Try additional Machine Learning algorithms
Include soil-related parameters
Include more detailed weather information
Add geographical analysis
Use newer agricultural datasets
Add more interactive visualizations
Improve prediction explanations

## ⚠️ Limitations
Predictions depend on the quality and coverage of the dataset.
Linear Regression may not capture all complex relationships in agricultural data.
Real-world factors such as soil quality, irrigation, and fertilizer usage are not fully represented.
Predictions are estimates and are not guaranteed outcomes.

## 👥 Team Members
- Norah Grace
- Malavika C U
- Shreya Godson
- Ananya J
- Sreya Parvathy

## 📌 Conclusion

AgriYield demonstrates an end-to-end Machine Learning workflow, from data preprocessing and exploratory analysis to model training, evaluation, model saving, and deployment through Streamlit.

The project provides an interactive way to explore agricultural data and generate crop yield predictions based on selected input factors.
