# import the Flask class and request object from the flask module
from flask import Flask,render_template,request #flask request
# from datetime import datetime
import requests #form Request

BACKEND_URL = 'http://0.0.0.0:9000'
msg = ""
app=Flask(__name__)#create the instance of the flask app
#define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')#render the home.html template with the day of the week and current time
@app.route('/submit' , methods=['POST'])
def signup():
    form_data = dict(request.form)
    try:
        if form_data is not None:
            requests.post(BACKEND_URL+'/submit',json=form_data)#changed the form data to Json
            return "Data submitted successfully!"
        else:
            return "Error Occured in submitting the value Tray Again !"

    except Exception as e:
        print(form_data)
        return render_template('index.html',msg = f"Unable to save data : {str(e)}")
        #raise Exception(f"Unable to save data : {str(e)}")
    

@app.route('/getdata')
def get_data():
    try:
        response = requests.get(BACKEND_URL+'/view')
        return  response.json()
    except Exception as e:
        raise Exception(f"Unable to read data file: {str(e)}")

@app.route('/saveitem',methods=['POST'])
def saveitem():
    form_data = dict(request.form)
    try:
        if form_data is not None:
            request.post(BACKEND_URL+'/submittodoitem',json=form_data)
            return "Data Submitted Successfully!"
        else:
            return "Error Occured in submitting the value Tray Again !"

    except Exception as e:
        print(form_data)
        return render_template('todo.html',msg = f"Unable to save data : {str(e)}")
        #raise Exception(f"Unable to save data : {str(e)}")

#run the app
if __name__ == '__main__':
    #app.run(debug=True)#run the app in debug mode
    app.run(host='0.0.0.0',port=8000,debug=True)