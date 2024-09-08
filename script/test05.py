from api.login import LoginAPI
import pytest
import json
import config

# test_data = [
#     ("admin", "HM_2023_test", 200, "成功", 200),
#     ("", "HM_2023_test", 200, "错误", 500),
#     ("ad", "HM_2023_test", 200, "错误", 500)
# ]


def build_data(json_file):
    test_data = []
    with open(json_file, 'r', encoding='UTF-8') as f:
        json_data = json.load(f)
        for case_data in json_data:
            username = case_data.get('username')
            password = case_data.get('password')
            status = case_data.get('status')
            message = case_data.get('message')
            code = case_data.get('code')
            test_data.append((username, password, status, message, code))
    return test_data


class TestLoginAPI:
    uuid = None

    def setup_method(self):
        self.login_api = LoginAPI()
        response = self.login_api.get_verify_code()
        print(response.json())
        TestLoginAPI.uuid = response.json().get('uuid')
        print(TestLoginAPI.uuid)

    def teardown_method(self):
        pass

    @pytest.mark.parametrize("username, password, status, message, code", build_data(json_file=config.BASE_PATH + "/data/login.json"))
    def test01_success(self, username, password, status, message, code):
        login_data = {
            "username": username,
            "password": password,
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(login_data)
        print(response.json())

        assert status == response.status_code
        assert message in response.text
        assert code == response.json().get('code')

