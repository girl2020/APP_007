from selenium.webdriver.support.wait import WebDriverWait
from Base.driver import Driver


# 定义基类
class Base:

    def __init__(self):
        """实例化驱动对象那个"""  # 已经在driver.py中声明了app的驱动对象，这里直接调用，然后实例化
        self.driver = Driver.get_app_driver()

    # 定义公用的单个元素的方法
    def search_ele(self, loc, timeout=5, poll=1):
        """
        定位单个元素
        :param loc: 元组 (By.ID,属性值) (By.CLASS_NAME,属性值) (By.XPATH,属性值)...
        :param timeout: 搜索元素超时间
        :param poll: 搜索元素间隔
        :return: 定位对象
        """
        # 因为有时候在定位元素的时候会出现由于网络原因，定位不到的情况，这里可以使用现显示等待来定位等待元素，需要返回
        # loc代表解包，因为元素可以看做成一个元组例如(BY.ID, "元素")
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    # 定位公用的多个元素的方法，返回的是元组，然后可以利用列表推导式来遍历取值
    def search_eles(self, loc, timeout=5, poll=1):
        """
        定位多个元素
        :param loc: 元组 (By.ID,属性值) (By.CLASS_NAME,属性值) (By.XPATH,属性值)...
        :param timeout: 搜索元素超时间
        :param poll: 搜索元素间隔
        :return: 定位对象列表
        """
        # 同单个元素
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    # 定义公用的单个点击的方法
    def click_ele(self, loc, timeout=5, poll=1):
        """
        点击元素
        :param loc: 元组 (By.ID,属性值) (By.CLASS_NAME,属性值) (By.XPATH,属性值)...
        :param timeout: 搜索元素超时间
        :param poll: 搜索元素间隔
        :return:
        """
        self.search_ele(loc, timeout, poll).click()

    # 定义公用的输入文本内容的方法
    def send_ele(self, loc, text, timeout=5, poll=1):
        """
        输入方法
        :param loc: 元组 (By.ID,属性值) (By.CLASS_NAME,属性值) (By.XPATH,属性值)...
        :param text: 输入的文本内容
        :param timeout: 搜索元素超时间
        :param poll: 搜索元素间隔
        :return:
        """
        # 定位文本输入框元素
        input_text = self.search_ele(loc, timeout, poll)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)
