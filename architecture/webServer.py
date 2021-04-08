# see https://pythonbasics.org/flask-rest-api/
# this is a flask server 
# server no.2
from datetime import datetime, timedelta
from flask import render_template, Flask, request, jsonify
import json
# if the serve is going to send emails, wee need the email utility
from email_util import handleEmail

# our modules
from db.retrieve_db import retrieve_dt

def handleServer():
    # creates a Flask application, named app
    app = Flask(__name__)
    # read in the current email address to be used
    try:
        with open('emailAddress.txt','rt') as fin: # fin for 'file in', rt for 'read text'
            currentEmail = fin.readline()
    except: # if we fail to read the text file, just set a default
        currentEmail = 'es595recipient@gmail.com'
    # print(currentEmail)

    # a route where we will display a welcome message via an HTML template
    # @ allows html to run 
    @app.route("/")
    def hello():
        message = "Seizure monitor"
        return render_template('index.html', message=message)

    @app.route("/live")
    def live():
        return render_template('live.html')

    @app.route("/alert")
    def alert():
        start_dt = request.args.get('start_dt')
        end_dt = request.args.get('end_dt')
        area_under = request.args.get('area_under')
        
        # check we have valid start and end points
        if start_dt == '0':
            start_dt = datetime.now() - timedelta(seconds=30) # default to 30 seconds ago
        if end_dt == '1':
            end_dt = datetime.now()
        if area_under == '0':
            area_under = 'no value'
        # print(start_dt,end_dt)
        data = retrieve_dt(start_dt, end_dt) # call our imported function
        data_json = json.dumps(data) # convert the data into json
        return render_template('alert.html', data=data_json, area_under=area_under, start_dt=start_dt, end_dt=end_dt)

    @app.route("/samples")
    def samples():
        return render_template('samples.html')

    # a RESTful API route. For any pair of date-time values query the DB and return
    @app.route('/retrieve', methods=['GET'])
    def query_dt():
        start_dt = request.args.get('start_dt')
        end_dt = request.args.get('end_dt')
        # print(start_dt,end_dt)
        data = retrieve_dt(start_dt, end_dt) # call our imported function
        data_json = json.dumps(data) # convert the data into json
        return data_json # json is a popular format for passing data over http

    @app.route('/send_email', methods=['GET'])
    def sendEmail():
        newMessage = request.args.get('message')
        start_dt = request.args.get('start_dt')
        end_dt = request.args.get('end_dt')
        area_under = request.args.get('area_under')
        # write this message to an email
        handleEmail(newMessage, start_dt, end_dt, area_under)
    
    @app.route('/set_email', methods=['GET'])
    def setEmail():
        newEmail = request.args.get('userEmail')
        # write this email to a text file
        with open('emailAddress.txt', 'wt') as fout: # fout for 'file out', wt for '(over)write text'
            fout.write(newEmail)
            # also, set the email to use from here on
            currentEmail = newEmail
            print(currentEmail)
        return '200 ok'

    # run the application
    app.run(debug=True)

if __name__ == "__main__":
    handleServer()
