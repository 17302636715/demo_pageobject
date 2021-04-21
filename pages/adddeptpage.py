

from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePages


class AddDept(BasePages):

    ipt_dept_loc = (By.XPATH,"//*[@name='name']")
    a_parentpart_selector_loc = (By.CSS_SELECTOR,".qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list")
    a_parentpart_loc = (By.CSS_SELECTOR,".qui_dialog_body.ww_dialog_body [id='1688850249789292_anchor']")
    btn_submit_loc = (By.XPATH,"//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]")

    def adddept(self,dept_name,):
        self.find_element(*self.ipt_dept_loc).send_keys(dept_name)
        self.find_element(*self.a_parentpart_selector_loc).click()
        self.find_element(*self.a_parentpart_loc).click()
        self.find_element(*self.btn_submit_loc).click()
        sleep(3)
        from pages.contactpage import ContactPage
        return ContactPage(self.driver)






