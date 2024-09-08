import requests
import config


class LoginAPI():
    def __init__(self):
        self.url_verify_code = config.BASE_URL + '/api/captchaImage'
        self.url_login = config.BASE_URL + '/api/login'

    def get_verify_code(self):
        return requests.get(url=self.url_verify_code)

    def login(self, test_data):
        return requests.post(url=self.url_login, json=test_data)

