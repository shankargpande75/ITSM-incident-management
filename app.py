from flask import Flask,render_template,request
import pickle
import sklearn
import pickle
import numpy as np

app=Flask(__name__)

with open('prioritymodel.pkl','rb') as file:
    model=pickle.load(file)

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
      # Convert form input data to appropriate data types
        # CI_cat = int(request.form.get('CI_cat'))
        CI_Subcat = int(request.form.get('CI_Subcat'))
        Impact = int(request.form.get('Impact'))
        Category = int(request.form.get('Category'))
        priority = int(request.form.get('priority'))
        No_of_Reassignments = float(request.form.get('No_of_Reassignments'))
        No_of_Related_Interactions = int(request.form.get('No_of_Related_Interactions'))
        Closure_Code = int(request.form.get('Closure_Code'))
        No_of_Related_Changes = int(request.form.get('No_of_Related_Changes'))
        
        input_data = [
            CI_Subcat, Impact, Category, priority, No_of_Reassignments,
            No_of_Related_Interactions, Closure_Code, No_of_Related_Changes
        ]

        # Make the prediction using your model
        prediction_result = model.predict([input_data])  # Assuming 'model' is defined and loaded

        # Render the same HTML template with the prediction result
        return render_template('home.html', prediction_result=prediction_result)

    # If the request method is GET (initial page load), render the form template without prediction result
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

    
