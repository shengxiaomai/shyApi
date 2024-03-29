import requests
from api import login
from api.BaseApi import BaseApi
import time
import calendar

class courseApi(BaseApi):
    HeadlineList="api/course/newapp/course/getHeadlineList?t="+str(int(time.time()))
    CourseListByRootId="api/course/newapp/course/getCourseListByRootId"
    headers = {"authorization": login.Login.login(), "content - type": "application / json;charset = UTF - 8"}
    @classmethod
    def GetHeadlineLis(self):#课程模块 获取每日速递列表
        self.json_data = requests.get(self.url+self.HeadlineList,headers = self.headers,verify = False).json()
        self.verbose(self.json_data)
        return self.json_data

    @classmethod
    def getCourseListByRootId(self,catalogueId):#课程模块 根据根目录查询所有二级目录下的所有课程
        payload = {'catalogueId': catalogueId, 'key2': str(int(time.time()))}
        self.json_data =requests.get(self.url+self.CourseListByRootId,params=payload,headers = self.headers,verify = False).json()
        self.verbose(self.json_data)
        return self.json_data

