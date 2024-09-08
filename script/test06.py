from api.login import LoginAPI
from api.course import CourseAPI


class TestAddCourse:
    token = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()

        res_v = self.login_api.get_verify_code()
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": res_v.json().get("uuid")
        }
        res_l = self.login_api.login(login_data)
        TestAddCourse.token = res_l.json().get("token")

    def teardown_method(self):
        pass

    def test01_success(self):
        course_data = {
            "name": "English",
            "subject": "6",
            "price": "899",
            "applicablePerson": "2",
            "info": "语言类"
        }
        response = self.course_api.course(course_data=course_data, token=TestAddCourse.token)
        print(response.json())

        assert 200 == response.status_code
        assert "成功" in response.text
        assert 200 == response.json().get("code")

    def test02_fail(self):
        course_data = {
            "name": "Eng",
            "subject": "6",
            "price": "899",
            "applicablePerson": "2",
            "info": "语言类"
        }
        response = self.course_api.course(course_data=course_data, token="xxx")
        print(response.json())

        assert 200 == response.status_code
        assert "失败" in response.text
        assert 401 == response.json().get("code")

