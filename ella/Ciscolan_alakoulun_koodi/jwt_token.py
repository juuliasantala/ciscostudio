import jwt, base64

def jwt_token(userUniqueId, userName, issuerId, issuerSecret):
    payload = {
    "sub": userUniqueId,
    "name": userName,
    "iss": issuerId
    }
    secret = base64.b64decode(issuerSecret)
    encoded_jwt = jwt.encode(payload, secret)
    if type(encoded_jwt) == bytes:
        encoded_jwt = encoded_jwt.decode("utf-8")
    return encoded_jwt
