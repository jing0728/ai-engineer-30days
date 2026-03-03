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

"""
案例：定义手机类，能开机，关机，拍照
回顾：
    定义类的格式
        class 类名：
            #属性
            #行为
    访问 类中成员 的格式：
        类外：对象名. 的方式
        类外：self. 的方式
"""
class Cell:
    def on(self):
        print(f"{self}Open")
    def off(self):
        print(f"{self}Off")
    def pic(self):
        print(f"{self}pic")

c1 = Cell()
print(f"c1 object{c1}")
c1.on()
c1.off()
c1.pic()