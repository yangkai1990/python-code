a = input("请输入一个数字 ")
b = input("请输入另一个 ")

try:
    c = int(a) / int(b)

except Exception as err:
    print("error")
    c = Nones
print("a/b的结果是",c)

