import pytest

from cases.basecase import BaseCase


class TestAddDept(BaseCase):

    @pytest.mark.parametrize('dept_name',BaseCase.datas['test_adddept']['datas'])
    def test_adddept(self,dept_name):
        text_list = self.main.goto_contact().goto_adddept().adddept(dept_name).get_dept_list()
        assert dept_name in text_list




