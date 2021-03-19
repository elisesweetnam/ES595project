# see https://pythonbasics.org/flask-rest-api/
# this is a flask server 
# server no.2

from flask import render_template, Flask, request, jsonify
import json

# our modules
from retrieve_db import retrieve_dt

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "Seizure monitor"
    return render_template('index.html', message=message)

@app.route("/live")
def live():
    return render_template('live.html')

# a RESTful API route. For any pair of date-time values query the DB and return
@app.route('/retrieve', methods=['GET'])
def query_dt():
    start_dt = request.args.get('start_dt')
    end_dt = request.args.get('end_dt')
    print(start_dt,end_dt)
    data = retrieve_dt(start_dt, end_dt) # call our imported function
    data_json = json.dumps(data) # convert the data into json
    return data_json # json is a popular format for passing data over http

# run the application
if __name__ == "__main__":
    app.run(debug=True)