import pytest

from api.course import courseApi

import allure




class TestCourseApi:

    @allure.severity('blocker')
    @allure.story("课程模块 获取每日速递列表")
    def test_GetHeadlineLis(self):
        a=courseApi.GetHeadlineLis()
        assert a["msg"]=="success"

    @allure.severity('blocker')
    @allure.story("课程模块 根据根目录查询所有二级目录下的所有课程")
    @pytest.mark.parametrize("catalogueId", [487377109979759325])
    def test_GetCourseListByRootId(self,catalogueId):
        a = courseApi.getCourseListByRootId(catalogueId)
        assert a["msg"] == "success"

