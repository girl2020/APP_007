"""
设置页面
设置 -显示 -字体大小
 由大 修改为 普通
建议：
 元素以页面为准，每个页面包含元素统一放在一起
 以页面为单位，定义每一个页面类
"""

# 导包
from Base.driver import Driver
from Base.page import Page


# 定义测试设置字体大小的类
class TestSetFront:

    def teardown_class(self):
        # 退出driver
        Driver.quit_app_driver()

    # 定义设置字体大小方法
    def test_set_font_size(self):
        # 设置页面 -点击显示
        Page.get_setting_page().click_show_btn()
        # 显示页面 -选择字体
        Page.get_show_page().choice_front()
        # 显示页面 -获取描述信息-断言
        assert "普通" in Page.get_show_page().get_summary_list()

