"""
Cisco DNA Center API examples

Created by Juulia Santala, Cisco Systems, 2020

Prototype, not to be used in production environment!

"""

import requests
from requests.auth import HTTPBasicAuth

# To not show Insecure warnings when communicating with DNAC
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#Credentials, these are Cisco Sandbox credentials, try out with the
#sandbox or update to your own devices!
ADDRESS = "sandboxdnac.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

BASE_URL = "https://{}/dna/intent/api/v1/".format(ADDRESS)

def token(address, username, password):
    """
    Function for creating the authorization token.
    """
    url = "https://{}/api/system/v1/auth/token".format(address)
    header = {"content-type": "application/json"}
    auth = HTTPBasicAuth(username=username,password=password)

    try:
        #SSL certification is turned off, but should be active in production environments
        response = requests.post(url,auth=auth, headers=header, verify=False)
        print("service ticket status: ", response.status_code)
        token = response.json()["Token"]
        return token
    except:
        print( "Error!")
        return 0

def get_devices(token):
    """
    Function to get all the current devices from DNA Center.
    """
    url = "{}network-device".format(BASE_URL)
    header = {
        "X-Auth-Token": token,
        "content-type" : "application/json"
        }

    try:
        #SSL certification is turned off, but should be active in production environments
        response = requests.get(url, headers=header, verify=False)
        return response.json()["response"]

    except:
        print( "Error!")
        return 0

def main():
    my_token = token(ADDRESS, USERNAME, PASSWORD)
    my_devices = get_devices(my_token)
    for device in my_devices:
        print("Model: {}, Hostname: {}".format(device["platformId"], device["hostname"]))

if __name__ == "__main__":
    main()
