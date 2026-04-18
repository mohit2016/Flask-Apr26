from flask import Flask, request
import pickle

app = Flask(__name__)

with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route("/", methods=['GET'])
def home():
    return "<h1>Welcome to the Loan API V2!</h1>"

@app.route("/predict", methods=['GET'])
def predict():
    data = """
    Please send a POST request with the required data.<br>
    Endpoint:
    http://127.0.0.1:5000/predict <br>
    Sample JSON
    data required:
    ```{
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 5000,
        "LoanAmount": 200,
        "CreditHistory": 1
    }```
    
    """
    return data

@app.route("/predict", methods=['POST'])
def make_predict():
    # get the inputs data from the request (you can use request.get_json() to get JSON data)

    data = request.get_json()
    # print(data)

    if data['Gender'] == "Male":
        gender = 0
    else:
        gender = 1
    if data['Married'] == "No":
        married = 0
    else:
        married = 1
    
    input_features = [[gender, married, data['ApplicantIncome'], data['LoanAmount'], data['Credit_History']]]
    print(input_features)

    result = model.predict(input_features)
    if result[0] == 0:
        result = "Rejected"
    else:
        result = "Approved"

    return {'loan_approval_status': result}


if __name__ == "__main__":
    app.run(debug=True) # all changes will be reflected immediately, no need to restart the server.