import sys
import compute as myfunc  #将导入的文件视为myfunc
from readcsv import a,b,func
import pytest
sys.path.append('C:\\Users\\ds\\Desktop') #注意转义，将\都要写成\\

func() #运行一次函数，得到a，b的值
length = len(a)
num = 0
while num < length:
        @pytest.mark.parametrize("input1,input2,expected_output",[(int(a[num]),int(b[num]),6)])
        def test_calc_multiply(input1,input2,expected_output):
            area = myfunc.multiply(input1,input2)
            try:
                assert area == expected_output,"结果不对"#结果不对是说明的理由
            except AssertionError:
                print("error")
        num = num+1 #注意缩进，缩进影响变量作用范围
else:
    print("done!")

#pytest输入参数化：pytest.mark.parametrize(),有多少个输入，直接写出来

if __name__ == "__main__":
    print(length)
    pytest.main() #直接在本程序中运行即可，若没有，则需要到console里面py.test运行