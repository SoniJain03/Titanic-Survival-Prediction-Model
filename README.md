# Titanic-Survival-Prediction-Model

A simple and interactive Streamlit web application that predicts whether a passenger would have survived the Titanic disaster, based on key features like class, age, gender, fare etc.

# About the Project

This project uses a pre-trained **Decision Tree Classifier** (trained using the Titanic dataset) to predict survival outcomes. 
It's is loaded using `joblib`, and the interface is built with `Streamlit`.

# Features

- Takes user input for:
  - Passenger class (`Pclass`)
  - Gender('sex')
  - Age
  - Number of siblings/spouses aboard (`SibSp`)
  - Number of parents/children aboard (`Parch`)
  - Fare
- Predicts whether the passenger would survive
- Displays result in a user-friendly format (success or error message)

# Tech Stack

- **Python**
- **pandas** (for handling input features)
- **scikit-learn** (for the machine learning model)
- **joblib** (for model serialization)
- **Streamlit** (for the web UI)


## Note: 
All dependencies required to run this app are listed in requirements.txt. You can install them using pip install -r requirements.txt
## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/titanic-streamlit-app.git
   cd titanic-streamlit-app
