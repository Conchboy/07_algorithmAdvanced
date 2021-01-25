def demo1():
    # 定义一个局部变量
    num = 11
    # 1. 出生： 执行了下方代码之后，才会被创建
    # 2. 死亡： 函数执行完成之后
    print("我是一个局部变量%d " % num)


def demo2():
    # 定义一个局部变量
    num = 88
    print("这个demo2的局部变量是 %d " % num)
    pass


demo1()
demo2()

# print(num)