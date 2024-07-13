# from service import login

class Response:
    def __init__(self, data: str, status_code: int):
        self.data = data
        self.status_code = status_code


def hash_password(raw_password):
    password = raw_password.encode('utf-8')
    return password

def match_password(raw_password, encoded_password):
    if raw_password.encode('utf-8') == encoded_password:
        return True
    else:
        return False