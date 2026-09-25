from flask import Flask,render_template,request,jsonify
import json
from datetime import datetime
import os
#create the instance of the flask app
app=Flask(__name__)
#define a route for the home page
filename = "data.txt"

def read_data():
    if not os.path.exists(filename):
        return {"data": []}

    try:
        files = open(filename,"r") #Open the file in read and write mode
        return json.load(files)

    except (json.JSONDecodeError, OSError):
        return {"data": []}

def save_data(data):    
    files = open(filename,"w") #Open the file in write mode
    json.dump(data, files, indent=4)

@app.route('/')
#define a function name home
def home():
    #return "Welcome to the Home Page!"#return a response for the home page
    current_time = datetime.now().strftime('%H:%M:%S')#get the current time
    print(current_time)#print the current time to the console
    return render_template('index.html', current_time=current_time)#render the home.html template with the day of the week and current time

#save to the file
@app.route('/submit' , methods=['POST'])
def signup():
    form_data = dict(request.form)
    
    json_data = read_data()
    # Get existing data array
    items = json_data.get("data", [])
    # Check current item length
    current_length = len(items)

    # append to the item list
    items.append(form_data)
    # Update JSON object
    json_data["data"] = items
    # Write back to file
    save_data(json_data)

    #Read the content of the file
    file_content = read_data()    
    return 'Data Submitted Successfully'

#read from file
@app.route('/viewdata')
def viewdata():
    #Read the content of the file
    file_content = read_data()    
    return file_content

#reaad from the file through /api in the address route
@app.route('/api')
def info():
    files = open(filename,"r") 
    file_content = files.read()
    files.close()
    return file_content
#run the app
if __name__ == '__main__':
    app.run(debug=True)#run the app in debug mode