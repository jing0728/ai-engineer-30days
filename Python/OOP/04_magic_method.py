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

"""
案例：演示init魔法方法有参版的 用法

魔法方法：
    概述/特点：
        python内置函数，在特定的场景下，会被 自动调用，一般用于给该类对象 的属性进行初始化
"""

#1.定义汽车类，创建该类对象，赋予颜色 和 轮胎数两个属性，并在类内访问该属性
class Car:
    #属性
    #在魔法__init__()中，初始化：属性：
    def __init__(self,color,number):
            """
            :param color:car color
            :param number:car wheel's number
            """
            self.color=color
            self.number =number
    #定义函数show()，实现 在类内访问 汽车对象的属性
    def show(self):
        print(f'我是show函数，对象的颜色：{self.color},轮胎数是{self.number}')
#2.创建汽车类的对象
c1 = Car('red',6) #调用了init()函数，但是该函数有参数所以必须传参

c1.show()

"""
案例：演示str魔法方法的 用法

魔法方法：
    概述/特点：
        python内置函数，在特定的场景下，会被 自动调用，一般用于给该类对象 的属性进行初始化
    常用魔法方法
        init()  在（每次）创建对象的时候，会自动触发该类的 init() 函数。
        str()   当用 print() 函数打印对象的时候，会自动调用该对象（所在类）的 str 魔法方法。
                该魔法方法默认打印的是对象的地址值，无意义，一般都会重写，改为打印对象的各个属性值。
        del()

del()
"""
#1.定义汽车类，创建该类对象，赋予颜色 和 轮胎数两个属性，并在类内访问该属性
class Car:
    #属性
    #在魔法__init__()中，初始化：属性：
    def __init__(self,color,number):
            """
            :param color:car color
            :param number:car wheel's number
            """
            self.color=color
            self.number =number
    #定义函数show()，实现 在类内访问 汽车对象的属性
    def __str__(self):
        return f'我是show函数，对象的颜色：{self.color},轮胎数是{self.number}'
#2.创建汽车类的对象
c1 = Car('red',6) #调用了init()函数，但是该函数有参数所以必须传参
print(c1)  #输出语句打印对象，默认调用了该对象 所在类的 str魔法方法

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