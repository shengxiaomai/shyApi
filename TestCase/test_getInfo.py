import pytest

from api.getInfo import getInfo

import allure




class TestGetInfo:


    @allure.severity('blocker')
    @allure.story("测试获取用户信息")
    @pytest.mark.parametrize("mibole", ["18682115996"])
    def test_getUserInfo(self,mibole):
        a=getInfo.getUserInfo(mibole)
        assert a["body"]["mobile"]!=None

    def test_getYxtoken(self):
        a=getInfo.getYxtoken()
        assert a["body"]!=None