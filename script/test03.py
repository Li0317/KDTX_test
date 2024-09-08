from api.login import LoginAPI
from api.course import CourseAPI
from api.contract import ContractAPI
import config


class TestContract:
    token = None
    fileName = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        self.contract_api = ContractAPI()

    def teardown_method(self):
        pass

    def test01_login_success(self):
        res_verify = self.login_api.get_verify_code()
        print(res_verify.status_code)
        print(res_verify.json())

        uuid = res_verify.json().get('uuid')
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": uuid
        }
        res_login = self.login_api.login(test_data=login_data)
        print(res_login.status_code)
        print(res_login.json())
        TestContract.token = res_login.json().get('token')
        print(TestContract.token)

    def test02_add_course(self):
        course_data = {
            "name": "English",
            "subject": "6",
            "price": "899",
            "applicablePerson": "2",
            "info": "语言类"
        }
        res_add_course = self.course_api.course(course_data, TestContract.token)
        print(res_add_course.status_code)
        print(res_add_course.json())

    def test03_upload_contract(self):
        f = open(config.BASE_PATH + "/data/新建文本文档.txt", "rb")
        res_upload = self.contract_api.upload_contract(upload_file=f, token=TestContract.token)
        print(res_upload.json())
        TestContract.fileName = res_upload.json().get('fileName')

    def test04_add_contract(self):
        add_data = {
            "name": "测试1",
            "phone": "20250202231",
            "contractNo": "HT20251122",
            "subject": "6",
            "courseId": "74",
            "channel": "0",
            "activityId": "6",
            "fileName": TestContract.fileName
        }
        res_add_contract = self.contract_api.add_contract(add_data=add_data, token=TestContract.token)
        print(res_add_contract.json())