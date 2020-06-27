import pytest

from Base.driver import Driver
from Base.page import Page


# 定义页面搜索测试类
class TestSearch:

    def teardown_class(self):
        """退出driver"""
        Driver.quit_app_driver()

    # 因为只需要运行一次 并且是依赖方法，所以使用fixture工厂函数
    @pytest.fixture(scope="class", autouse=True)
    def click_search_btn(self):
        """点击搜索按钮 并且 点击一次"""
        # 搜索页面--点击搜索按钮
        Page.get_search_page().click_search_btn()

    @pytest.mark.parametrize("search_data, exp_data", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_search_text(self, search_data, exp_data):
        """
        搜索测试方法
        :param search_data: 输入内容
        :param exp_data: 预期结果
        :return:
        """
        # 搜索页面--输入搜索内容
        # 输入框输入内容
        Page.get_search_page().search_text(search_data)
        # 断言
        assert exp_data in Page.get_search_page().get_search_result()
