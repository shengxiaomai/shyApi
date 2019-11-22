import requests
from api import login
from api.BaseApi import BaseApi
import time
import calendar

class courseApi(BaseApi):
    url="https://radio-api-demo.zlzgy.org.cn/api/course/newapp/course/getHeadlineList?t="+str(int(time.time()))

    headers = {"authorization": login.Login.login(), "content - type": "application / json;charset = UTF - 8"}
    @classmethod
    def GetHeadlineLis(self):
        self.json_data = requests.get(self.url,headers = self.headers,verify = False).json()
        self.verbose(self.json_data)
        return self.json_data

    @classmethod
    def getCourseListByRootId(self,catalogueId):
        payload = {'catalogueId': catalogueId, 'key2': str(int(time.time()))}
        self.json_data =requests.get("https://radio-api-demo.zlzgy.org.cn/api/course/newapp/course/getCourseListByRootId",params=payload,headers = self.headers,verify = False).json()
        self.verbose(self.json_data)
        return self.json_data