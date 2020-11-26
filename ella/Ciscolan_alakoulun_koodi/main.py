"""
Webex widget + Guest user example

Created by Juulia Santala, Cisco Systems, 2020

Prototype, not to be used in production environment!
"""


from flask import Flask, render_template, request, redirect, url_for
import random
import credentials as C
import webex_api_calls as W
import jwt_token as J


APP = Flask(__name__)
STUDENT = {"name":"", "token": "", "id":""}
HOMEWORKS = [
    "Matematiikka: sivut 20-21, tehtävät 1,2,3 ja 4.",
    "Äidinkieli: sivu 25, tehtävät 1, 2 ja 3"
    ]

def addStudentToRoom (name):
    '''
    Function to add the student to the room, using the name that they 
    define when starting the program.
    Student is added as a guest, so they don't need to have a webex account

    To be able to add the guest to the room, we need to:
    1. Create the guest. For this we need uniqueId, the name of the guest, and
    a Guest Issuer, that is created in developer.webex.com.
    2. log the guest in: this way we will get a token for the guest
    3. Get the guest ID: we need this to add the guest to the room where we want to
    include them.
    4. Add the guest to the room that is going to be embedded on the site. You can use
    bot to do this, and need the guest ID to identify who you are adding to the room.
    '''

    STUDENT["name"] = name

    # I used random number in the unique ID to make sure it is unique
    userUniqueId = "unique-" + str(random.uniform(1,100000))  
    encodedJWT = J.jwt_token(userUniqueId, STUDENT["name"], C.issuerId, C.issuerSecret)
    STUDENT["token"] = W.jwt_login(encodedJWT)
    STUDENT["id"] = W.get_guest_info(STUDENT["token"])

    W.add_to_room(C.botToken, C.roomId, STUDENT["id"])


@APP.route('/')
def credentials():
    '''
    Open GUI where you ask for the name of the student
    '''
    return render_template("index.html")

@APP.route('/login', methods=["POST", "GET"])
def login():
    '''
    The action to take the name that the student has provided, and use that
    to add the student in the Webex room
    '''
    studentName = request.form["studentName"]
    addStudentToRoom(studentName)
    return redirect('/dashboard')

@APP.route('/dashboard')
def main():
    '''
    The main dashboard, which is available after the student has given their
    name and has been added as a guest to the room.

    If you try to go directly to dashboard without first giving the name for
    the student and starting the functions to add that name to the room,
    redirect the user back to beginning ("/").
    '''

    if STUDENT["name"] == "": #Student has not given name yet
        return redirect('/')
    else:
        return render_template('dashboard.html', token=STUDENT["token"], room=C.roomId, username=STUDENT["name"], homework=HOMEWORKS)

@APP.route('/call')
def call():
    '''
    To make the call to teacher. This is a 1:1 call.
    '''
    return render_template('call.html', token=STUDENT["token"], teacher=C.teacher, username=STUDENT["name"])