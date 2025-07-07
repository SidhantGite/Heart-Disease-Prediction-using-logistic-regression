# Heart-Disease-Prediction-using-logistic-regression

Heart Disease Prediction is a machine learning web application built using Flask and Logistic Regression. It uses the Framingham Heart Study dataset to predict the likelihood of a person developing heart disease based on key health metrics.

## Features

- Logistic Regression model for binary classification
- Web interface using Flask and HTML templates
- User inputs common health data like age, cholesterol, BP, etc.
- Model returns prediction of heart disease risk (Yes/No)

## Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas, NumPy
- HTML/CSS (Jinja2 Templates)

---

## Getting Started

1. Clone the Repository


git clone https://github.com/yourusername/heartdisease-main.git
cd heartdisease-main/heartdisease-main

2. Create and Activate Virtual Environment (optional but recommended)
python -m venv venv
.\venv\Scripts\activate      # Windows

# source venv/bin/activate  # Mac/Linux
3. Install Dependencies
pip install -r requirements.txt

4. Run the App
python app.py
Go to your browser and open:
http://127.0.0.1:5000

### Files Overview
app.py: Main Flask application

model.pkl: Pretrained logistic regression model

framingham.csv: Dataset used for training

templates/index.html: HTML frontend form

requirements.txt: List of Python dependencies

ML___Heart_Disease_Prediction_Using_Logistic_Regression.ipynb: Notebook used for training and saving the model

