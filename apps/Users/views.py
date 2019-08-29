

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        "msg": "success",
        "status": 200,
        "data": [{
            'token': token,
            'username': user.username
        }]
    }