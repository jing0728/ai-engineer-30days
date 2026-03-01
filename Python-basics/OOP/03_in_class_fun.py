"""
案例：演示通过self关键字实现在类内访问其他函数

self关键字：
    概述：
        代表本类当前对象的引用，谁（哪个对象）调用，self就代表谁
    作用：
        用于实现函数区分不同的对象
总结：
    在 类外 访问类中的行为，需要通过 对象名. 的方式访问
    在 类内 访问类中的行为，需要通过 self.  的方式访问
"""

#需求：定义汽车类，类内有run()函数，并在work()函数中调用run()函数，创建该类对象，调用上述的函数

#1.定义汽车类
class Car():
    #定义run()函数
    def run(self):
        print(f"{self}Car can run")
    #定义work()函数，在其内部调用run()
    def work(self):
        print(f"我是work函数，我的self值是{self}")
        self.run() #self =本类当前对象的引用

#2.在类外访问Car类的行为（函数）
c1 = Car()
print(f"c1对象：{c1}")
c1.run()
print('-'*54)
c1.work()
print('+'*54)

#3.再次创建对象
c2 = Car()
print(f"c1对象：{c2}")
c2.run()
print('-'*54)
c2.work()
print('+'*54)