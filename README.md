#  House Price Prediction – End-to-End Machine Learning Project

##  Overview

This repository contains a complete end-to-end Machine Learning pipeline for predicting house prices using selected structural and location-based features from the **House Price India dataset**.

The project demonstrates real-world ML workflow including:

* Data cleaning
* Feature selection
* Exploratory Data Analysis (EDA)
* Feature engineering
* Training multiple regression algorithms
* Model evaluation & comparison
* Model serialization (.pkl under 25MB)
* Streamlit deployment

---

##  Dataset

**Dataset Used:** House Price India
**Selected Features:**

* `bedrooms`
* `postal code`
* `built year`
* `price` (target variable)

Unnecessary columns were removed to optimize model performance and reduce complexity.

---

##  Exploratory Data Analysis (EDA)

The project includes:

* Correlation heatmap
* Target distribution analysis
* Bedrooms vs Price relationship
* Statistical summary
* Outlier detection using IQR method

EDA helps understand feature impact and data distribution before modeling.

---

##  Feature Engineering

* Created `house_age = current_year - built_year`
* Removed duplicates and outliers
* Handled missing values using median imputation
* Standardized features using `StandardScaler`

---

##  Models Trained

The following regression algorithms were trained and evaluated:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* Support Vector Regressor (SVR)
* K-Nearest Neighbors Regressor

Evaluation Metrics:

* R² Score
* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)

The best-performing model was automatically selected and saved.

---

##  Model Optimization

* Reduced feature space
* Used compressed joblib serialization
* Ensured final `.pkl` size < 25MB

This makes the model suitable for deployment.

---

##  Streamlit Deployment

An interactive Streamlit web application allows users to predict house prices using sliders for:

* Bedrooms
* Postal Code
* Built Year
* Price (reference input)

Run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

##  Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

---

##  Project Structure

```
├── train.py
├── app.py
├── house_price_model.pkl
├── requirements.txt
├── README.md
```
