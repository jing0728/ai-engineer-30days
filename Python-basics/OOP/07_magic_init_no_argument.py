"""
案例：演示init魔法方法的 用法

魔法方法：
    概述/特点：
        python内置函数，在特定的场景下，会被 自动调用
"""
#1.定义汽车类，创建该类对象，赋予颜色 和 轮胎数两个属性，并在类内访问该属性
class Car:
    #属性
    #在魔法__init__()中，初始化：属性：
    def __init__(self):
            print('我是 无参init魔法方法')
        #在init中，初始化属性，则：该类所有的对象，一创建，就要这个属性了
            self.color='blue'
            self.number =4
    #定义函数show()，实现 在类内访问 汽车对象的属性
    def show(self):
        print(f'我是show函数，对象的颜色：{self.color},轮胎数是{self.number}')
#2.创建汽车类的对象
c1 = Car()
#修改c1的属性值
c1.color = 'red'
c1.number =3
print(c1.color,c1.number)
c1.show()

