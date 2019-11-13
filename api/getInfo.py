import requests
from api import login
from api.BaseApi import BaseApi


class getInfo(BaseApi):

    info_url="https://radio-api-demo.zlzgy.org.cn/api/live/app/getUserInfo"
    yx_url="https://radio-api-demo.zlzgy.org.cn/api/live/app/getYxToken"

    headers = {"authorization": login.Login.login(),"content - type": "application / json;charset = UTF - 8"}
    @classmethod
    def getUserInfo(self,mobile):
        self.json_data= requests.post(self.info_url,headers=self.headers,verify = False,json={"mobile":mobile}).json()
        self.verbose(self.json_data)

        return self.json_data

    @classmethod
    def getYxtoken(self):
        r=requests.get(self.yx_url,headers = self.headers,verify =False).json()
        return r


