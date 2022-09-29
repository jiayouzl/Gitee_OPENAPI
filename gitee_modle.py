# -*- coding: UTF-8 -*-

import json
import requests


class giteeCodeSnippet(object):
    APIHOST = 'https://gitee.com/api/v5/gists/'

    def __init__(self, token, gists_id=''):
        self.token = token
        self.id = gists_id
        self.url = f'{self.APIHOST}{self.id}'
        self.headers = {
            'Content-Type': 'application/json;charset=UTF-8',
        }
        self.params = {
            'access_token': self.token,
        }
        self.params_all = {
            'access_token': self.token,
            'page': '1',
            'per_page': '100',
        }

    def addNewGists(self, description: str):
        # yapf: disable
        json_data = {
            'access_token': self.token,
            'description': description,
            'public': False,
            'files': {
                'placeholder.txt': {
                    'content': 'placeholder',
                }
            }
        }
        # yapf: enable
        r = requests.post(self.url.replace(self.id, ''), data=json.dumps(json_data), headers=self.headers)
        if 'forks_url' in r.text:
            self.id = r.json()['id']
            self.url = f'{self.APIHOST}{self.id}'
            return self.id
        else:
            return '初始化失败检查token是否正确'

    def getAllGistsID(self):
        r = requests.get(self.url.replace(self.id, ''), params=self.params_all, headers=self.headers)
        if '"message"' in r.text:
            return 'token错误'
        result = json.loads(r.text)
        dict_ = {}
        for i in result:
            dict_.update({i['description']: i['id']})
        return dict_

    def getGists(self):
        if self.id == '':
            return 'gists_id不可为空'
        r = requests.get(self.url, params=self.params, headers=self.headers)
        if '"message"' in r.text:
            return 'token或gists_id错误'
        return r.json()['files']

    def setGists(self, description: str, files: dict):
        if self.id == '':
            return 'gists_id不可为空'
        # yapf: disable
        json_data = {
            'access_token': self.token,
            'description': description,
            'files': files
        }
        # yapf: enable
        r = requests.patch(self.url, data=json.dumps(json_data), headers=self.headers)
        if '"message"' in r.text:
            return 'token或gists_id错误'
        return r.json()['files']

    def delGists(self):
        if self.id == '':
            return 'gists_id不可为空'
        r = requests.delete(self.url, params=self.params, headers=self.headers)
        return r.json()
