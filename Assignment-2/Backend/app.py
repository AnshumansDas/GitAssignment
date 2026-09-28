# import the Flask class and request object from the flask module
from flask import Flask,request,jsonify
from dotenv import load_dotenv
import os
import pymongo


load_dotenv()#load the environment variables from the .env file
mongo_uri = os.getenv("MONGO_URI")#get the MongoDB connection string from the environment variable
client = pymongo.MongoClient(mongo_uri)#create a MongoDB client using the connection string
db = client.test#Create the DB and connect to the test database
collection = db['flask_tutorials']#create a collection named flask_tutorials in the test database

app=Flask(__name__)#create the instance of the flask app
#define a route for the home page

@app.route('/submit' , methods=['POST'])
def signup():
    try:
        form_data = dict(request.json)#changed to json from form
        collection.insert_one(form_data)
        return "Data submitted successfully!"
    except(json.JSONDecodeError, OSError):
        return {OSError}

@app.route('/view', methods=['GET'])
def view_data():
    data = list(collection.find({}, {'_id': 0}))  # Exclude the '_id' field from the results and convert to List
    data = [dict(item) for item in data]  # Convert each document to a dictionary
    data={'data':data}
    #return render_template('view.html', data=data)  # Render the view.html template with the retrieved data
    return  (jsonify(data))  # Render the view.html template with the retrieved data

@app.route('/submittodoitem',methods=['POST'])
def save_Item():
    collection = db['item_list']#create a collection named item_list in the test database
    try:
        form_data = dict(request.json)#changed to json from form
        collection.insert_one(form_data)
        return "Data submitted successfully!"
    except(json.JSONDecodeError, OSError):
        return {OSError}

#run the app
if __name__ == '__main__':
    #app.run(debug=True)#run the app in debug mode with default port 5000
    app.run(host='0.0.0.0',port=9000,debug=True)