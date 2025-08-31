# Predict Loan Approval

Using Logistic Regression, Python Flask Server and streamlit. I was able to build a robust machine learning project, that aqcuire relaibe back-end server and intuitive streamlit UI

## Project Overview
the project include a machine learning model that can predict wheather someone's Loan demand Approved or Rejected based on some features
the project can be described in 3 main parts:
- Machine learning model - a trained model that predicts the loan approval based on entered data.
- Flask server -  an intermediate layer that act between the trained machine Learning model and the Streamlit UI.
- Streamlit User Interface - a simple UI where user can enter data to get the prediction of Loan Approval.

## Deliverables
- `loan_data.csv` Original raw dataset
- `Modeling.ipynb` jupyter notebook including the data preprocessing, model training and model serialization
- `requirements.txt` Python packages used in the project
- `model.pkl` Serialized saved trained machine leaning model
- `Flask_server_app.py` Flask local server that have dedicated endpoint for prediciting new data points
- `streamlit_app.py` Sreamlit application that represents the user interface to enter the new data points to be predicted

## Project Setup Instructions
1. Clone the Repo
```bash
git clone https://github.com/ShehabMagdy101/Predict-Loan-Approval.git
cd Predict-Loan-Approval
```

2. Install Python Packages

```bash
pip install -r requirements.txt
```

3. Run the server

```bash
python Flask_server_app.py
```

4. Run the Streamlit application

```bash
streamlit run streamlit_app.py
```

## Project Structure

```
predict-loan-approval/
├── Modeling.ipynb              # Preprocessing and Model training
├── streamlit_app.py            # Streamlit web app
├── Flask_server_app.py         # Flask API server
├── loan_data.csv               # Raw dataset
├── model.pkl                   # Trained mode
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview and setup
```

## Requirements

- Python 3.12.10
- Packages Listed in (`requirements.txt`)
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `joblib`
  - `Flask`
  - `streamlit`
  - `requests`
 
## App

<img width="774" height="729" alt="image" src="https://github.com/user-attachments/assets/373ce484-0275-45fe-9bc7-8c40ddd6beea" />

