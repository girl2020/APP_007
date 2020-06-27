"""设置页面
设置 -显示 -字体大小
 由小 修改为 普通
建议：
 元素以页面为准，每个页面包含元素统一放在一起
 以页面为单位，定义每一个页面类
"""
# 导包
from Base.base import Base
from pages.pageElements import PageElements


class SettingPage(Base):

    def __init__(self):
        super().__init__()

    def click_show_btn(self):
        """点击显示按钮"""
        self.click_ele(PageElements.show_btn_xpath)

