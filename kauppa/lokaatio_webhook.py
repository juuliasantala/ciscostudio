from flask import Flask, json, request

# init a flash web app
app = Flask(__name__)

# validate web server from meraki
@app.route('/', methods=['GET'])
def get_validator():
    return "<Your validator from meraki dashboard>"

# receive location data
@app.route('/', methods=['POST'])
def get_location():
    # Get the JSON that Meraki sends!
    data = request.json
    #Print the data and validate, which part of the
    # data you want to use for your use case
    print(data)
    return "Location POST Received"
