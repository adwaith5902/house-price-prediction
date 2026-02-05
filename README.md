# 🏠 House Price Prediction Web App

A machine learning web application that predicts house prices based on property features such as area, number of bedrooms, bathrooms, parking, and amenities.  
The app is built using **Gradient Boosting Regressor** and deployed using **Streamlit Cloud**.

🔗 **Live App**: https://uvh4zl3ebs6htdraxx2npb.streamlit.app/

---

## 📌 Project Overview

Accurately estimating house prices is a common real-world regression problem.  
In this project, multiple machine learning models were evaluated, and **Gradient Boosting** was selected as the final model due to its superior performance in capturing non-linear patterns.

The trained model is deployed as an interactive web app where users can input property details and receive real-time price predictions.

---

## 📊 Models Evaluated

The following models were trained and compared:

| Model | RMSE | R² Score |
|-----|------|----------|
| Linear Regression | ~1.32M | 0.65 |
| Ridge Regression | ~1.32M | 0.65 |
| Random Forest (tuned) | ~1.39M | 0.62 |
| **Gradient Boosting (Final)** | **~1.29M** | **0.67** |

👉 **Gradient Boosting Regressor** achieved the best generalization performance and was selected as the final model.

---

## ⚙️ Features Used

- Area (sq ft)
- Bedrooms
- Bathrooms
- Stories
- Parking
- Main road access
- Guest room
- Basement
- Hot water heating
- Air conditioning
- Preferred area
- Furnishing status

Categorical features were encoded using **one-hot encoding**.

---

## 🧠 Machine Learning Workflow

1. Data Cleaning & Exploratory Data Analysis (EDA)
2. Feature Engineering & Encoding
3. Train–Test Split
4. Model Training & Evaluation
5. Hyperparameter Tuning
6. Final Model Selection
7. Model Persistence using `joblib`
8. Web App Deployment with Streamlit

---

## 🖥️ Tech Stack

- **Python**
- **scikit-learn**
- **pandas / numpy**
- **Streamlit**
- **GitHub**
- **Streamlit Cloud**

---

## 🚀 Running the App Locally

Clone the repository:

```bash
git clone https://github.com/adwaith5902/house-price-prediction.git
cd house-price-prediction
