"""
继承：指子类继承父类的属性和方法-->指的是类的继承，不是对象的继承

案例：继承入门

继承介绍：
    概述：
        子类继承父类的属性和方法
    写法：
        class 子类名（父类名）：
            pass
    例如：
        class A(B):
            pass
    好处：
        提高代码的复用性
    弊端：
        耦合性增强了，父类不好的内容，子类想没有都不行
    扩展：开发原则
        高内聚，低耦合
        内聚：指的是类自己独立处理问题的能力
        耦合：指的是类与类之间的关系
"""
#需求：定义父类（男，散步），定义子类（继承父类）
class Father:
    def __init__(self):
        self.gender = 'male'
    def work(self):
        print("喜欢work")
    def __str__(self):
        return f'这是一个{self.gender}'
    
class Son(Father):
    pass

#测试
if __name__ == '__main__':
    c1=Son()
    c1.work()
    print(c1)