import requests
import config


class CourseAPI:
    def __init__(self):
        self.url_add_course = config.BASE_URL + '/api/clues/course'
        self.url_select_course = config.BASE_URL + '/api/clues/course/list'

    def course(self, course_data, token):
        return requests.post(url=self.url_add_course, json=course_data, headers={'Authorization': token})

    def select_course(self, test_data, token):
        return requests.get(url=self.url_select_course + f"/{test_data}", headers={'Authorization': token})