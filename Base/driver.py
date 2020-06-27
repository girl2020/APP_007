from appium import webdriver


class Driver:
    """声明web 或者 app的驱动对象"""
    # 定义app驱动对象
    app_driver = None

    @classmethod  # 类方法，不需要实例化类 也可以调用方法
    def get_app_driver(cls):
        """声明手机驱动对象"""
        if cls.app_driver is None:  # 如果app_driver为None, 则需要创建驱动对象driver
            # server 启动参数
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings'
            }
            # 声明我们的driver对象
            cls.app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            # 返回驱动对象
            return cls.app_driver
        else:  # app_driver已经声明过（如果有必须返回使用）
            return cls.app_driver

    @classmethod
    def quit_app_driver(cls):
        """退出手机驱动对象"""
        if cls.app_driver:  # app_driver有值
            # 退出
            cls.app_driver.quit()
            # 重新将app_driver置为None
            cls.app_driver = None
