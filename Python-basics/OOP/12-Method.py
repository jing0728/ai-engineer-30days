"""
类方法（class method）：操作类
    属于类的方法，可以通过 类名. 还可以通过 对象名. 的方式来调用
    定义类方法的时候，必须使用装饰器@classmethod，并且第一个参数必须表示 类对象
静态方法（static method）：工具函数，和类没强关系
    属于该类下说要对象所共享的方法，可以通过 类名，还可以通过 对象名. 的方式调用
    定义静态方法的时候，必须使用装饰器@staticmethod,并且参数传不传都可以
区别：
    1.类方法的第一个参数必须是 类对象，静态方法并无特殊要求
    2.如果函数中要用 类对象，就定义成类方法，否则定义成 静态方法，除此之外，并无任何区别
"""
#定义学生类
class Student():
    #定义类属性
    school = '黑马程序员'
    #定义类方法
    @classmethod
    def show1(cls):
        print(f"cls:{cls}")#cls:<class '__main__.Student'>
        print("我是类方法")
    
    #定义静态方法
    @staticmethod
    def show2():
        print("我是静态方法")

#测试
if __name__ == "__main__":
    s1=Student()
    s1.show1()
    print('*'*50)
    s1.show2()