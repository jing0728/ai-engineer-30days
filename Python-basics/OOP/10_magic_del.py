"""
案例：演示str魔法方法的 用法

魔法方法：
    概述/特点：
        python内置函数，在特定的场景下，会被 自动调用，一般用于给该类对象 的属性进行初始化
    常用魔法方法
        init()  在（每次）创建对象的时候，会自动触发该类的 init() 函数。
        str()   当用 print() 函数打印对象的时候，会自动调用该对象（所在类）的 str 魔法方法。
                该魔法方法默认打印的是对象的地址值，无意义，一般都会重写，改为打印对象的各个属性值。
        del()   当 .py文件执行结束，或者 手动del释放对象自由，会自动调用该函数
"""
#1.定义汽车类，属性：品牌 行为：run() 通过del魔法方法删除该类的对象
class Car():
    def __init__(self,brand):
        self.brand=brand
    def __str__(self):
        return f'品牌：{self.brand}'
    #c重写del魔法方法，删除对象时给出提示
    def __del__(self):
        print(f"{self} 对象被删除了")
c1=Car('小米')
print(c1)

#手动删除c1
# del c1
# print c1 #报错

print("end")