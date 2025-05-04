from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

#Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "Model API is running"

@app.route('/predict',methods = ['POST'])
def predict():
    try:
        data = request.get_json()

        features = np.array([data['features']])
        prediction = model.predict(features)
        if prediction == 0:
            result = "Approved"
        else:
            result = "Rejected"

        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)
