"""显示页面"""
# 导包
from Base.base import Base
from pages.pageElements import PageElements


# 定义显示页面类
class ShowPage(Base):

    def __init__(self):
        super().__init__()

    def choice_front(self):
        """选择字体"""
        # 点击字体大小
        self.click_ele(PageElements.front_size_btn_xpath)
        # 点击普通
        self.click_ele(PageElements.common_btn_xpath)

    def get_summary_list(self):
        """获取页面所有描述信息"""
        # 获取所有描述信息
        results = self.search_eles(PageElements.front_size_results_ids)
        return [i.text for i in results]


