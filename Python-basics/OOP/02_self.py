"""
案例：self关键字介绍

self介绍：
    概述：
        它是python内置的关键字，用于表示本类当前对象的引用
    作用：
        1个类是可以有多个对象的，这多个对象都可以通过对象名. 的方式访问类中的行为（函数）
        函数默认有self属性，函数通过self来区分到底是哪个对象调用的该函数
    谁调用函数，self就代表谁
    
"""

#需求：定义汽车类，创建多个该类的对象，看看打印结果

#1.定义汽车类
class Car:
    def run(self):
        print("Car can run")
        print(f"I am run function,self is {self}")

#2.创建汽车类的对象
car = Car()
print(f"car1对象：{car}")
print(f"c1对象的地址值：{id(car)}")
#通过 对象名. 的形式，调用Car#run()
car.run()
print('-'*34)

#3.继续创建汽车类的对象
car2 = Car()
print(f"car2对象：{car2}")
print(f"c2对象的地址值：{id(car2)}")
#通过 对象名. 的形式，调用Car#run()
car2.run()
print('-'*34)