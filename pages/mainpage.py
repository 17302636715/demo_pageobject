
from selenium.webdriver.common.by import By

from pages.base_page import BasePages
from pages.contactpage import ContactPage


class MainPage(BasePages):

    span_contact_loc = (By.XPATH,"//*[@id='menu_contacts']/span")

    def goto_contact(self):
        self.find_element(*self.span_contact_loc).click()
        return ContactPage(self.driver)




