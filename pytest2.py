import compute as myfunc  #将导入的文件视为myfunc
import pytest


@pytest.mark.parametrize("test_input,expected_output",[[(5,3),10],[(3,2),6]])
def test_calc_multiply(test_input,expected_output):
    area = myfunc.multiply(test_input[0],test_input[1])
    assert area == expected_output


#pytest输入参数化：pytest.mark.parametrize()