from flask import Flask, request, render_template
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect input values from the form
    try:
        features = [
            float(request.form['age']),
            float(request.form['Sex_male']),
            float(request.form['cigsPerDay']),
            float(request.form['totChol']),
            float(request.form['sysBP']),
            float(request.form['glucose'])
        ]
        features = np.array(features).reshape(1, -1)
        
        # Predict using the model
        prediction = model.predict(features)[0]
        output = 'Heart Disease' if prediction == 1 else 'No Heart Disease'

    except Exception as e:
        output = f'Error in prediction: {str(e)}'

    return render_template('index.html', prediction_text=f'Result: {output}')

if __name__ == "__main__":
    app.run(debug=True)
