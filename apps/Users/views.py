


def jwt_response_payload_handler(token, user=None, request=None):
    """
    设置jwt登陆返回的格式
    :param token:
    :param user:
    :param request:
    :return:
    """
    return {
        "msg": "success",
        "status": 200,
        "data": [{
            'token': token,
            'username': user.username
        }]
    }

def jwt_response_payload_error_handler(serializer, request = None):
    return {
        "msg": "用户名或者密码错误",
        "status": 400,
        "detail": serializer.errors
    }

