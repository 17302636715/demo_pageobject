from abc import ABC

from selenium.webdriver.common.by import By

from pages.base_page import BasePages


class ContactPage(BasePages):

    add_btn_loc = (By.CSS_SELECTOR, ".member_colLeft_top_addBtnWrap.js_create_dropdown")
    dpt_btn_loc = (By.CSS_SELECTOR, ".js_create_party")
    apt_top_loc = (By.ID,"//*[@id='1688850249789292']/a[1]")
    apt_list_loc = (By.CSS_SELECTOR,("[role=group] a"))


    def goto_adddept(self):
        self.find_element(*self.add_btn_loc).click()
        self.find_element(*self.dpt_btn_loc).click()
        from pages.adddeptpage import AddDept
        return AddDept(self.driver)

    def get_dept_list(self):
        text_list = []
        element_list = self.find_elements(*self.apt_list_loc)
        for i in element_list:
            text_list.append(i.text)

        return text_list


