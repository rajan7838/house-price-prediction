# House Price Prediction (ML + Streamlit)

## Project Overview
This project predicts house prices using Machine Learning models.
The best-performing model (Random Forest Regressor) was selected using GridSearchCV
and deployed using Streamlit.

## ML Models Used
- Linear Regression
- Ridge
- Lasso
- ElasticNet
- Random Forest Regressor (Best Model)

## Tech Stack
- Python
- Scikit-learn
- Pandas, NumPy
- Streamlit
- Joblib

##  How to Run Locally
```bash
conda activate ml_env
pip install -r requirements.txt
streamlit run app.py
“This is an end-to-end Machine Learning project that predicts house prices based on real property features. I started by exploring and preprocessing the dataset, handling both numerical and categorical features. I trained multiple regression models — including Linear Regression, Ridge Regression, ElasticNet, and Random Forest Regressor — and selected the best performing model using hyperparameter tuning with GridSearchCV. The final model was deployed as an interactive web app using Streamlit, allowing users to input house details and get price predictions. The project demonstrates a complete pipeline from data processing to model training to deployment.”
