import sys
import compute as myfunc  #将导入的文件视为myfunc
import pytest
sys.path.append('C:\\Users\\ds\\Desktop') #注意转义，将\都要写成\\

@pytest.mark.parametrize("input1,input2,expected_output",[(5,3,10),(3,2,6)])
def test_calc_multiply(input1,input2,expected_output):
    area = myfunc.multiply(input1,input2)
    assert area == expected_output



#pytest输入参数化：pytest.mark.parametrize(),有多少个输入，直接写出来