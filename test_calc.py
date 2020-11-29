import pytest
import yaml
import allure_pytest

from test_calculator_pytest.conftest import comment_calc
from test_calculator_pytest.Calculator import Calculator

"""
文件名：test_*或*_test
类：Test*
case:test_*
"""
def get_datas(type):
    with open('calc.yml') as f:
        mydatas=yaml.safe_load(f)
        if type=='add':
            datas = mydatas['add']['datas']
            ids = mydatas['add']['myids']
        elif type=='sub':
            datas,ids=mydatas['sub']['datas'],mydatas['sub']['myids']
        elif type=='mul':
            datas,ids=mydatas['mul']['datas'],mydatas['mul']['myids']
        elif type=='div':
            datas,ids=mydatas['div']['datas'],mydatas['div']['myids']
        return [datas, ids]



@pytest.mark.usefixtures('comment_calc')
class TestCalc():
    comment_calc
    calc = Calculator()


    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect_value',get_datas('add')[0],ids=get_datas('add')[1])
    def test_add(self,a,b,expect_value):
        result=self.calc.add(a,b)
        assert result==expect_value

    @pytest.mark.sub
    @pytest.mark.parametrize('a,b,expect_value',get_datas('sub')[0],ids=get_datas('sub')[1])
    def test_sub(self,a,b,expect_value):
        result=self.calc.sub(a,b)
        assert result==expect_value

    @pytest.mark.mul
    @pytest.mark.parametrize('a,b,expect_value',get_datas('mul')[0],ids=get_datas('mul')[1])
    def test_mul(self,a,b,expect_value):
        result=self.calc.mul(a,b)
        assert result==expect_value

    @pytest.mark.div
    @pytest.mark.parametrize('a,b,expect_value',get_datas('div')[0],ids=get_datas('div')[1])
    def test_div(self,a,b,expect_value):
        result=round(self.calc.div(a,b),1)
        assert result==expect_value