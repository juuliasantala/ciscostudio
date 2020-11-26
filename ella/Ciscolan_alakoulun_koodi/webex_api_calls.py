import requests


API_URL = "https://webexapis.com/v1/"

def jwt_login(jwt_token):
    print("Guest log in...")
    headers = {"authorization":"Bearer {}".format(jwt_token)}
    url = API_URL + "jwt/login"
    response = requests.post(url, headers=headers).json()
    print("Guest logged in!")
    return response["token"]

def get_guest_info(guest_token):
    print("Getting guest info...")
    headers = {"authorization":"Bearer {}".format(guest_token)}
    url = API_URL + "people/me"
    response = requests.get(url, headers=headers).json()
    print("guest info retrieved!")
    return response["id"]

def add_to_room(token, room_id, guest_id):
    print("Adding guest to the room...")
    headers = {"authorization":"Bearer {}".format(token), "Content-Type":"application/json"}
    url = API_URL + "memberships"
    payload = {"roomId":room_id, "personId":guest_id}
    response = requests.post(url, headers=headers, json=payload)
    print("Guest added to the room!")