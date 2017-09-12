# 闭包——>装饰器
#不改变原来函数的调用方式，执行内容等；为了自己的目的添加一些额外功能
#扩展原有函数的功能

import time
def cal_time_cost(func):
    def wrapper():
        start_time = time.clock()
        func()
        end_time = time.clock()
        time_cost = end_time - start_time
        print(time_cost)
    return wrapper   #只返回了内层函数对象，并没有执行


@cal_time_cost   #等价于cal = cal_time_cost(cal)
def cal():
    sum = 0
    for i in (j**2 for j in range(10)):
        sum = sum + i
    print(sum)

if __name__ == "__main__":
    cal()       #没有改变原函数cal()的调用方式，并且添加了时间计算功能