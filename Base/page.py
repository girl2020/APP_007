"""集中管理所有页面类对象"""
from pages.searchPage import SearchPage
from pages.settingPage import SettingPage
from pages.showPage import ShowPage


class Page:
    """返回所有页面实例化对象"""

    @classmethod
    def get_setting_page(cls):
        """返回设置页面类实例化对象"""
        return SettingPage()

    @classmethod
    def get_show_page(cls):
        """返回显示页面类实例化对象"""
        return ShowPage()

    @classmethod
    def get_search_page(cls):
        """返回搜索页面类实例化对象"""
        return SearchPage()
