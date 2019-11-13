#完成所有功能类的初始化
from utils.Utils import Utils

class BaseApi:

    json_data=None

    @classmethod
    def verbose(self,json_object):
        print(Utils.format(json_object))

    @classmethod
    def jsonpath(self,expr):
        return Utils.jsonpath(self.json_data,expr)

