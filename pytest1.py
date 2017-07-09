import compute #导入module或者其他函数
import pytest

@pytest.mark.skip("i dont wanna run this function right now") #skip下面的测试项目
def test_compute_add():
    total = compute.add(4,3)
    assert total == 6

def test_compute_multiply():
    total = compute.multiply(4,3)
    assert total == 12



