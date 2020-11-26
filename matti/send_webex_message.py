"""
Cisco Webex API example
Created by Juulia Santala, Cisco Systems, 2020
Prototype, not to be used in production environment!
"""

import requests

API_URL = "https://webexapis.com/v1/"
#FILL YOUR OWN DETAILS FOR TOKEN AND ROOM_ID!
TOKEN = ""
ROOM_ID = ""

def post_message(token, room_id, message):
    '''
    Function to post a message in a Webex room
    '''

    headers = {
        "authorization":"Bearer {}".format(token),
        "Content-Type":"application/json"
        }
    url = API_URL + "messages"
    payload = {"roomId":room_id, "text":message}
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(response)
    except:
        print( "Error!")

def main():
    my_message = "Tämän viestin haluan lähettää huoneeseen :)"
    post_message(TOKEN, ROOM_ID, my_message)

if __name__ == "__main__":
    main()
