from api.login import LoginAPI


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

    def test01_success(self):
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(login_data)
        print(response.json())

        assert 200 == response.status_code
        assert '成功' in response.text
        assert 200 == response.json().get('code')

    def test02_without_username(self):
        login_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(login_data)
        print(response.json())

        assert 200 == response.status_code
        assert '错误' in response.text
        assert 500 == response.json().get('code')

    def test03_without_user(self):
        login_data = {
            "username": "jack666",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(login_data)
        print(response.json())

        assert 200 == response.status_code
        assert '错误' in response.text
        assert 500 == response.json().get('code')