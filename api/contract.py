import requests
import config


class ContractAPI(object):
    def __init__(self):
        # self.url_upload = 'http://kdtx-test.itheima.net/api/common/upload'
        self.url_upload = config.BASE_URL + '/api/common/upload'
        # self.url_add_contract = 'http://kdtx-test.itheima.net/api/contract'
        self.url_add_contract = config.BASE_URL + '/api/contract'

    def upload_contract(self, upload_file, token):
        return requests.post(url=self.url_upload, headers={'Authorization': token}, files={"file": upload_file})

    def add_contract(self, add_data, token):
        return requests.post(url=self.url_add_contract, headers={'Authorization': token}, json=add_data)
