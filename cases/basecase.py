import yaml
from pages.mainpage import MainPage


class BaseCase:

    datas= []

    def setup_class(self):
        self.main = MainPage()

    with open("../testdata/test_data.yml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)

