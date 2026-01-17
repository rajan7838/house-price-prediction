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
