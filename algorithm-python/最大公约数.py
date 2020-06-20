# coding=utf-8
# 输入两个整数的最大公约数，辗转相除法
num01 = int(input("请输入第一个整数："))
num02 = int(input("请输入第二个整数："))
# 排序，大的在前
if num01 < num02:
    t = num01
    print(t, num01, num02)
    num01 = num02
    print(t, num01, num02)
    num02 = t
    print(t, num01, num02)

while num02 != 0:
    t = num01 % num02
    print("第0次", t, num01, num02)
    num01 = num02
    num02 = t
    print("第1次", t, num01, num02)
print("最大公约数：", num01)
