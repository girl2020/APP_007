"""把所有页面元素定义一个类，统一管理"""
# 导包
from selenium.webdriver.common.by import By


# 定义页面元素类
class PageElements:
    """管理所有页面元素"""

    # ----搜索页面元素----
    # 搜索按钮
    search_btn_id = (By.ID, "com.android.settings:id/search")
    # 搜索输入框
    search_input_id = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result_ids = (By.ID, "com.android.settings:id/title")

    # -----设置页面元素----
    # ‘显示’按钮
    show_btn_xpath = (By.XPATH, "//*[contains(@text,'显示')]")

    # -----显示页面元素
    # ‘字体大小’按钮
    front_size_btn_xpath = (By.XPATH, "//*[contains(@text,'字体大小')]")
    # 单选‘普通’按钮
    common_btn_xpath = (By.XPATH, "//*[contains(@text,'普通')]")
    # 定位所有元素信息
    front_size_results_ids = (By.ID, "android:id/summary")
