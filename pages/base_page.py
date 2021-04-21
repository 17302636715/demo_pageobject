from selenium import webdriver


class BasePages:

    def __init__(self, driver: webdriver = None):

        if driver is not None:
            self.driver = driver
        else:
            chrom_arg = webdriver.ChromeOptions()
            chrom_arg.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=chrom_arg)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            self.driver.implicitly_wait(3)


    def find_element(self, locator, value):
        try:
            element = self.driver.find_element(locator, value)
        except:
            print('not find element')
        return element


    def find_elements(self,locator,value):
        try:
            elementlist = self.driver.find_elements(locator, value)
        except:
            print('not find element')
        return elementlist
