from common_imports import Session, ProtonError

class ProtonAuth():
    def __init__(self, username, password):
        self.UserName = username
        self.Password = password