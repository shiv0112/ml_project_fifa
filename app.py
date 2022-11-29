from flask import Flask, render_template, request, jsonify
from flask_cors import CORS,cross_origin
import numpy as np
import joblib

app=Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def index():
    try:
            #  reading the inputs given by the user
            potential=float(request.form['potential'])
            finishing = float(request.form['finishing'])
            heading_accuracy = float(request.form['heading_accuracy'])
            dribbling = float(request.form['dribbling'])
            ball_control = float(request.form['ball_control'])
            reactions = float(request.form['reactions'])
            shot_power = float(request.form['shot_power'])
            strength = float(request.form['strength'])
            aggression = float(request.form['aggression'])
            marking = float(request.form['marking'])
            gk_diving = float(request.form['gk_diving'])
            gk_kicking = float(request.form['gk_kicking'])
            gk_positioning = float(request.form['gk_positioning'])

            x_input=[potential,finishing,heading_accuracy,dribbling,ball_control,reactions,shot_power,strength,aggression,marking,gk_diving,gk_kicking,gk_positioning]
            
            loaded_model = joblib.load("model.joblib")# loading the model file
            # predictions using the loaded model file
            
            prediction=loaded_model.predict([x_input])[0]

            # showing the prediction results in a UI
            return render_template('results.html',prediction=np.ceil(prediction))
    except Exception as e:
            print('The Exception message is: ',e)
            return 'Something went wrong'

if __name__ == "__main__":
    app.run(debug=True)
