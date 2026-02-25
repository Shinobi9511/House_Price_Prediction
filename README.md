# 🏠 House Price Prediction – India (Streamlit App)

A Machine Learning powered web application that predicts **house prices in India** based on basic property features.

The application loads a pre-trained model and scaler from a serialized `.pkl` file and performs real-time predictions through an interactive Streamlit interface.

---

## 🚀 Project Overview

This project:

* Loads a trained regression model (`house_price_model.pkl`)
* Extracts:

  * `model`
  * `scaler`
* Accepts user inputs via sidebar sliders
* Computes house age dynamically
* Scales input features
* Displays predicted house price in ₹

---

## 🛠 Tech Stack

* Python 3.9+
* Streamlit
* NumPy
* Scikit-learn
* Joblib

---

## 📂 Project Structure

```bash
├── app.py
├── house_price_model.pkl
├── requirements.txt
└── README.md
```

---

## 📊 Input Features

The model expects the following features in this exact order:

1. Bedrooms
2. Postal Code
3. Built Year
4. House Age (calculated inside app)

### Derived Feature

```python
house_age = 2026 - built_year
```

This ensures the model incorporates property age into prediction.

---

## ⚙️ How It Works

### 1️⃣ Model Loading

The application loads a dictionary object:

```python
model_dict = joblib.load("house_price_model.pkl")
```

Which contains:

* `model` → trained regression model
* `scaler` → fitted preprocessing scaler

---

### 2️⃣ Input Processing

User inputs are collected from sidebar sliders and converted into a NumPy array:

```python
input_data = np.array([[bedrooms, postal_code, built_year, house_age]])
```

The data is then scaled using:

```python
input_scaled = scaler.transform(input_data)
```

---

### 3️⃣ Prediction

When the user clicks **Predict Price**, the model outputs:

```python
prediction = model.predict(input_scaled)
```

Displayed as formatted Indian currency:

```
₹ 12,34,567
```

---

### UI Components

✔ Bedrooms slider (1–10)
✔ Postal Code slider (100000–999999)
✔ Built Year slider (1950–2025)
✔ Predict Price button
✔ Formatted currency output

---

## ▶️ Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/house-price-india.git
cd house-price-india
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit App

```bash
streamlit run app.py
```

App will open at:

```
http://localhost:8501
```

---

## 📦 Example requirements.txt

```
streamlit
numpy
scikit-learn
joblib
```

---

## ☁️ Streamlit Cloud Deployment

To deploy:

1. Push repository to GitHub
2. Go to Streamlit Cloud
3. Select repository
4. Choose `app.py`
5. Deploy

Ensure:

* `house_price_model.pkl` is inside repository
* Dependencies are correctly listed
* Model file size is within deployment limits

---

## 🧠 Model Assumptions

* Postal code impacts pricing significantly
* House age affects depreciation
* Bedrooms correlate with property value
* Inputs are scaled before prediction

---

## ⚠️ Limitations

* No EDA dashboard
* No feature importance visualization
* No confidence interval provided
* No validation metrics displayed
* Year is hardcoded as 2026 for age calculation

---

## 👨‍💻 Author

Aanjney Kumawat
Machine Learning & Data Science Enthusiast
Experienced in ML deployment, Python, SQL, and analytics

---
