from flask import Flask, render_template, request
import pickle
import numpy as np

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = 'Model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    # return "Hello World"
    pred_value = 0
    if request.method == 'POST':
        Gender = request.form['Gender']
        ApplicantSalary = request.form['ApplicantSalary']
        Married = request.form['Married']
        Dependents = request.form['Dependents']
        CoapplicantIncome = request.form['CoapplicantIncome']
        TotalIncome = request.form['TotalIncome']
        Property_Area = request.form['Property_Area']
        
        feature_list = []

        feature_list.append(int(ApplicantSalary))
        feature_list.append(float(CoapplicantIncome))
        feature_list.append(float(TotalIncome))


        Gender_list = ["Male","Female"]
        Married_list = ["Yes","No"]
        Dependents_list = ["0","1","2","3+"]
        Property_Area_list = ["Semiurban","Urban","Rural"]

        # for item in company_list:
        #     if item == company:
        #         feature_list.append(1)
        #     else:
        #         feature_list.append(0)

        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        traverse_list(Gender_list, Gender)
        traverse_list(Married_list, Married)
        traverse_list(Dependents_list, Dependents)
        traverse_list(Property_Area_list, Property_Area)

        pred_value = prediction(feature_list)
        pred_value = np.round(pred_value[0],2)*300

    return render_template('index.html', pred_value=pred_value)


if __name__ == '__main__':
    app.run(debug=True)


