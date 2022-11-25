#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template,request
import pickle

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "LM-mZCwYDKxaN4Kla8MIGWT84fA-tna3Jt7t-9xUJzqK"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


app=Flask(__name__)
model=pickle.load(open('RFregression.pkl','rb'))

@app.route('/')
def start():
    return render_template(r'D:\ibm\index.html')

@app.route('/model',methods=["GET","POST"])
def result():
    no_of_clynder=request.form["no_of_cylinders"]
    displacement=request.form["displacement"]
    horsepower=request.form["horsepower"]
    weight=request.form["weight"]
    acceleration=request.form["acceleration"]
    model_year=request.form["model_year"]
    origin=request.form["origin"]

    t1=[[int(no_of_clynder),float(displacement),int(horsepower),int(weight),float(acceleration),int(model_year),int(origin)]]
    output=model.predict(t1)
    return render_template(r"D:\ibm\index.html",y="The predicted MPG of the vehicle is ", z=str(output[0]))

if __name__ == "__main__":
    app.run(debug=False)


# In[ ]:




